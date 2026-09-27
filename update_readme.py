#!/usr/bin/env python3
import argparse, json, re, sys
from pathlib import Path

# Require @ to activate; support optional meta-flags after a pipe |sf
PAT_UNDERSCORE = re.compile(
    r"([_\*]){2}([^\1\n]*?)\1{2}\s*<!--\s*(?P<at>@{1,2})(?P<key>[A-Za-z0-9_.-]+)(?:\|(?P<flags>[A-Za-z]+))?\s*-->",
    re.M
)
PAT_BOLD = re.compile(
    r"<(b|strong)>\s*(.*?)\s*</\1>\s*<!--\s*(?P<at>@{1,2})(?P<key>[A-Za-z0-9_.-]+)(?:\|(?P<flags>[A-Za-z]+))?\s*-->",
    re.M | re.S
)

def load_values(path):
    if not path:
        return {}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    flat = {}
    def walk(prefix, obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                walk(f"{prefix}.{k}" if prefix else k, v)
        else:
            flat[prefix] = obj
    walk("", data)
    return flat

_NUM_RE = re.compile(r"""
    ^\s*
    (?P<sign>[+-]?)
    (?P<int>\d[\d_,]*)
    (?:\.(?P<frac>\d+))?
    \s*$
""", re.X)

def _as_str_no_scientific(value):
    if isinstance(value, float):
        s = f"{value:.15g}"
        try:
            if float(s).is_integer():
                return str(int(float(s)))
        except Exception:
            pass
        return s
    return str(value)

def _format_number_string(s, include_sign=False, comma_format=False):
    m = _NUM_RE.match(s.replace("\u202f", "").replace("\xa0", ""))
    if not m:
        return s
    sign = m.group("sign") or ""
    int_raw = m.group("int").replace(",", "").replace("_", "")
    frac = m.group("frac") or ""
    try:
        int_val = int(int_raw)
    except ValueError:
        return s
    int_fmt = f"{abs(int_val):,d}" if comma_format else str(abs(int_val))
    out = int_fmt + (("." + frac) if frac else "")
    is_negative = (sign == "-")
    if include_sign:
        out = ("-" if is_negative else "+") + out
    else:
        if is_negative:
            out = "-" + out
    return out

def format_value(value, include_sign=False, comma_format=False):
    s = _as_str_no_scientific(value)
    formatted = _format_number_string(s, include_sign=include_sign, comma_format=comma_format)
    if formatted is not s:
     return formatted
    return s

def _sub_with(values, warn_missing, bold=False, include_sign=False, comma_format=False):
    missing = set()
    def _sub(m):
        old_val = m.group(2)
        at = m.group("at")
        key = m.group("key")
        flags = (m.group("flags") or "").lower()

        # Per-marker flags (meta-flags) override/augment CLI flags
        local_sign = include_sign or ("s" in flags)
        local_commas = comma_format or ("f" in flags)

        if key in values:
            new_val = format_value(values[key], local_sign, local_commas)
        else:
            new_val = old_val
            missing.add(key)

        # Preserve original marker exactly (including @ count and |flags if present)
        tail = f"<!--{at}{key}{('|' + flags) if flags else ''}-->"
        return (f"<b>{new_val}</b>{tail}" if bold else f"__{new_val}__{tail}")
    _sub.missing = missing
    return _sub

def replace_text(text, values, warn, include_sign, comma_format):
    sub_unders = _sub_with(values, warn_missing=warn, bold=False,
                          include_sign=include_sign, comma_format=comma_format)
    text = PAT_UNDERSCORE.sub(sub_unders, text)

    sub_bold = _sub_with(values, warn_missing=warn, bold=True,
                                include_sign=include_sign, comma_format=comma_format)
    text = PAT_BOLD.sub(sub_bold, text)

    if warn:
        missing = (sub_unders.missing | sub_bold.missing)
        if missing:
            print("\tMissing values for:", ", ".join(sorted(missing)), file=sys.stderr)
    return text

def main():
    ap = argparse.ArgumentParser(
        description="Replace values preceding <!--@key.path[|flags]--> markers; @ required"
    )
    ap.add_argument("files", nargs="+", help="Markdown/README files to update")
    ap.add_argument("-v", "--values", help="JSON file with values (supports nested objects)")
    ap.add_argument("-i", "--in-place", action="store_true",
                   help="Write back to files (default: print to stdout if single file)")
    ap.add_argument("--warn-missing", action="store_true",
                   help="Warn about keys seen but not provided")
    ap.add_argument("-s", "--include-sign", action="store_true",
                   help="Force explicit sign (+/-) on numeric outputs")
    ap.add_argument("-f", "--format", action="store_true",
                   help="Format integer parts with thousands separators (commas)")
    args = ap.parse_args()

    values = load_values(args.values)

    for fp in args.files:
        p = Path(fp)
        text = p.read_text(encoding="utf-8")
        updated = replace_text(text, values, args.warn_missing,
                             args.include_sign, args.format)
        if args.in_place:
            if updated != text:
                p.write_text(updated, encoding="utf-8", newline="")
        else:
            sys.stdout.write(updated)

if __name__ == "__main__":
    main()
