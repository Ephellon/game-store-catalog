#!/usr/bin/env python3
"""Clean game names in the store JSON files, in place.

Passes, applied to every object in every <store>/*.json:
  1. Keys:  strip surrounding whitespace from object keys ("name " -> "name")
  2. Names: strip surrounding whitespace from "name" values
  3. Names: drop trailing junk, repeated until nothing changes:
         INPUT  -> "name": "([^"]+)(?:[&: ]+|\\([&+: ]*\\)|\\[[&+: ]*\\])"
         OUTPUT -> "name": "$1"
     i.e. trailing runs of & : or spaces, and empty () / [] holding only & + : or spaces.

Files are only rewritten when something changed.
"""
import argparse, json, re, sys
from pathlib import Path

JUNK = re.compile(r"(?:[&: ]+|\([&+: ]*\)|\[[&+: ]*\])$")

def clean_name(name):
    name = name.strip()
    while True:
        cut = JUNK.sub("", name).rstrip()
        if cut == name or not cut:
            return name
        name = cut

def clean(obj, stats):
    if isinstance(obj, list):
        return [clean(x, stats) for x in obj]
    if not isinstance(obj, dict):
        return obj
    out = {}
    for k, v in obj.items():
        key = k.strip() if isinstance(k, str) else k
        if key != k:
            stats["keys"] += 1
        v = clean(v, stats)
        if key == "name" and isinstance(v, str):
            new = clean_name(v)
            if new != v:
                stats["names"] += 1
                v = new
        out[key] = v
    return out

def dump(data, newline):
    return json.dumps(data, indent=4, ensure_ascii=False).replace("\n", newline)

def main():
    ap = argparse.ArgumentParser(description="Clean keys and trailing junk from game names in store JSON files")
    ap.add_argument("-r", "--root", default=Path(__file__).resolve().parent, type=Path,
                    help="Catalog folder containing the store folders (default: this script's folder)")
    ap.add_argument("-n", "--dry-run", action="store_true", help="Report changes without writing")
    args = ap.parse_args()

    files = sorted(p for p in args.root.glob("*/*.json")
                   if not p.parent.name.startswith(".") and p.name != "$.json")
    total = {"files": 0, "keys": 0, "names": 0}
    for f in files:
        raw = f.read_text(encoding="utf-8")
        newline = "\r\n" if "\r\n" in raw else "\n"
        trailing = raw[len(raw.rstrip("\r\n")):]
        data = json.loads(raw)
        stats = {"keys": 0, "names": 0}
        cleaned = clean(data, stats)
        if not (stats["keys"] or stats["names"]):
            continue
        # Refuse to rewrite a file whose formatting this script can't reproduce
        if dump(data, newline) + trailing != raw:
            print(f"\tSkipping {f.parent.name}/{f.name}: formatting would change", file=sys.stderr)
            continue
        total["files"] += 1
        total["keys"] += stats["keys"]
        total["names"] += stats["names"]
        if not args.dry_run:
            f.write_text(dump(cleaned, newline) + trailing, encoding="utf-8", newline="")

    verb = "Would clean" if args.dry_run else "Cleaned"
    print(f"\t{verb} {total['names']} names and {total['keys']} keys in {total['files']} of {len(files)} files")
    return 0

if __name__ == "__main__":
    sys.exit(main())
