"""Static check: core/ must not import network libraries.

This backs the "on-device only" commitment in the README. It reads every .py
file under core/ and fails if one imports a network-capable module.

Limits (be honest about them):
- It is a static import check. It cannot prove that no network call happens
  (for example through a library that is allowed but opens connections itself).
- It looks at core/ only. api/, Procfile and render.yaml are the legacy cloud
  demo and are deliberately not scanned.
- Treat a pass as "no known network imports", not as a security audit.
"""

import ast
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
CORE_DIR = REPO_ROOT / "core"

# A module is blocked if its dotted name equals an entry or sits under it.
BANNED_MODULES = {
    # HTTP clients and LLM SDKs
    "requests",
    "httpx",
    "aiohttp",
    "urllib3",
    "httplib2",
    "pycurl",
    "openai",
    "anthropic",
    # standard library network modules (urllib.parse is harmless and allowed)
    "urllib.request",
    "urllib.error",
    "http.client",
    "http.server",
    "socket",
    "socketserver",
    "ssl",
    "ftplib",
    "smtplib",
    "poplib",
    "imaplib",
    "telnetlib",
    "xmlrpc",
    "asyncio.streams",
    "asyncio.sslproto",
    # websockets, RPC, servers, cloud SDKs
    "websocket",
    "websockets",
    "grpc",
    "paramiko",
    "boto3",
    "botocore",
    "fastapi",
    "flask",
    "starlette",
    "uvicorn",
    "gunicorn",
}


def _is_banned(module_name):
    return any(
        module_name == banned or module_name.startswith(banned + ".")
        for banned in BANNED_MODULES
    )


def find_violations(source, filename="<source>"):
    """Return a list of 'file:line: module' strings for banned imports."""
    tree = ast.parse(source, filename=filename)
    found = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if _is_banned(alias.name):
                    found.append("%s:%d: import %s" % (filename, node.lineno, alias.name))

        elif isinstance(node, ast.ImportFrom):
            if node.level > 0 or not node.module:
                continue  # relative import inside the package
            if _is_banned(node.module):
                found.append("%s:%d: from %s import ..." % (filename, node.lineno, node.module))
                continue
            # "from urllib import request" resolves to urllib.request
            for alias in node.names:
                full_name = node.module + "." + alias.name
                if _is_banned(full_name):
                    found.append("%s:%d: from %s import %s" % (filename, node.lineno, node.module, alias.name))

        elif isinstance(node, ast.Call):
            # __import__("requests") and importlib.import_module("requests")
            func = node.func
            is_dynamic = (isinstance(func, ast.Name) and func.id == "__import__") or (
                isinstance(func, ast.Attribute) and func.attr == "import_module"
            )
            if is_dynamic and node.args:
                first = node.args[0]
                if isinstance(first, ast.Constant) and isinstance(first.value, str):
                    if _is_banned(first.value):
                        found.append("%s:%d: dynamic import of %s" % (filename, node.lineno, first.value))

    return found


# ---------------------------------------------------------------- the real check


def _core_files():
    return sorted(p for p in CORE_DIR.rglob("*.py") if "__pycache__" not in p.parts)


def test_core_directory_exists_and_has_code():
    # A missing or empty core/ must fail, never pass silently.
    assert CORE_DIR.is_dir(), "core/ directory not found at %s" % CORE_DIR
    assert _core_files(), "core/ contains no .py files, so there is nothing to check"


def test_core_has_no_network_imports():
    violations = []
    for path in _core_files():
        source = path.read_text(encoding="utf-8")
        violations.extend(find_violations(source, str(path.relative_to(REPO_ROOT))))
    assert not violations, (
        "core/ must stay on-device. Network imports found:\n  " + "\n  ".join(violations)
    )


# ------------------------------------------------- self-tests (the checker works)


@pytest.mark.parametrize(
    "source",
    [
        "import requests",
        "import socket",
        "import urllib.request",
        "from urllib import request",
        "from http import client",
        "from requests import get",
        "from openai import OpenAI",
        "import aiohttp as net",
        "__import__('requests')",
        "import importlib\nimportlib.import_module('httpx')",
    ],
)
def test_checker_catches_network_imports(source):
    assert find_violations(source), "checker missed: %r" % source


@pytest.mark.parametrize(
    "source",
    [
        "import time",
        "import math",
        "import json",
        "from urllib.parse import quote",
        "from . import helpers",
        "from .timer import PauseTimer",
        "import hashlib",
    ],
)
def test_checker_allows_local_imports(source):
    assert not find_violations(source), "checker wrongly blocked: %r" % source
