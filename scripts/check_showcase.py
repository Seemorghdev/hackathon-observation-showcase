"""Offline documentation-package checks; does not execute the application."""
from pathlib import Path
import hashlib
import json
import re
import sys

root = Path(__file__).resolve().parent.parent
inventory = root / "SHA256SUMS.txt"
entries = {}
for line in inventory.read_text().splitlines():
    digest, name = line.split("  ", 1)
    if not re.fullmatch(r"[0-9a-f]{64}", digest) or name in entries:
        sys.exit("Invalid or duplicate checksum entry")
    entries[name] = digest
files = {str(p.relative_to(root)) for p in root.rglob("*")
         if p.is_file() and ".git" not in p.relative_to(root).parts
         and "__pycache__" not in p.parts and p != inventory}
assert files == set(entries), "Inventory differs from package files"
for name, digest in entries.items():
    path = root / name
    assert path.suffix in {".md", ".html", ".png", ".jpg", ".mp4", ".json", ".py"}, name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, name
    if path.suffix in {".md", ".html", ".json"}:
        text = path.read_text()
        assert "/Users/" not in text and "PLANNING/" not in text, name
        assert not re.search(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN .*PRIVATE KEY-----)", text), name
    if path.suffix == ".md":
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if not re.match(r"https?://|#", target):
                resolved = (path.parent / target.split("#", 1)[0]).resolve()
                assert resolved.is_relative_to(root) and resolved.exists(), (name, target)
readme = (root / "README.md").read_text()
assert "documentation-only" in readme and "not an installable application" in readme
html = (root / "assets/presentation-excerpt.html").read_text()
assert "NOT A RUNTIME SCREENSHOT" in html
assert not re.search(r"<script|(?:src|href)=[\"']https?://", html, re.I)
review = (root / "docs/interface-review.md").read_text()
assert "not a working application capture" in review
assert "Blank panes are intentional" in review
assert "LIVE label was replaced with STATIC" in review
assert "separately documented synthetic scenario" in review
capture = json.loads((root / "visuals/capture-record.json").read_text())
shell = next(c for c in capture["captures"] if c["file"] == "operator-console-static-desktop.png")
assert shell["applicationScripts"] == 0 and shell["externalResourceElements"] == 0
assert shell["allControlsDisabled"] and not shell["fixturesLoaded"] and not shell["servicesStarted"]
assert (root / "visuals/operator-console-static-desktop.png").exists()
print(f"PASS: {len(entries)} package files; checksums, links and documentation boundaries")

runtime = json.loads((root / "visuals/runtime-capture-record.json").read_text())
assert runtime["synthetic_only"] and not runtime["field_evidence_captured"]
assert runtime["recording"]["first_t"] == 0 and runtime["recording"]["last_t"] == 90
assert len(runtime["timeline_samples"]) == runtime["recording"]["samples"]
for capture in runtime["captures"]:
    assert (root / "visuals" / capture["file"]).exists()
assert (root / "visuals" / runtime["recording"]["file"]).exists()
assert "not verified judgment" in (root / "docs/runtime-architecture.md").read_text()
print("PASS: synthetic runtime capture inventory and evidence boundary")
