"""Research pool store for Birch–Swinnerton-Dyer exploration loop.

Usage:
    python3 code/pool.py list [STATUS]
    python3 code/pool.py show  ID
    python3 code/pool.py add   '<json object>'
    python3 code/pool.py set   ID field=value [field=value ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

POOL = Path(__file__).resolve().parent.parent / "research" / "pool" / "candidates.json"
TERMINAL = {"REFUTED", "DUPLICATE"}
STATUSES = {"ACTIVE", "PROMISING", "PARTIAL_RESULT", "BLOCKED", "REFUTED", "DUPLICATE",
            "VERIFICATION_REQUIRED", "SUBMISSION_READY"}


def load() -> dict:
    return json.loads(POOL.read_text(encoding="utf-8"))


def save(db: dict) -> None:
    POOL.write_text(json.dumps(db, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd, args = sys.argv[1], sys.argv[2:]
    db = load()
    cands = db["candidates"]
    index = {c["id"]: c for c in cands}

    if cmd == "list":
        want = args[0].upper() if args else None
        for c in cands:
            if want and c.get("status") != want:
                continue
            print(f"{c['id']:<8} {c.get('status',''):<22} {c['claim'][:85]}")
        return 0

    if cmd == "show":
        print(json.dumps(index[args[0]], indent=2))
        return 0

    if cmd == "add":
        obj = json.loads(args[0])
        for k in ("id", "claim", "method", "status"):
            if k not in obj:
                raise SystemExit(f"missing required field: {k}")
        if obj["id"] in index:
            raise SystemExit(f"id already used: {obj['id']}")
        cands.append(obj)
        save(db)
        print(f"Added candidate {obj['id']}")
        return 0

    if cmd == "set":
        cid = args[0]
        if cid not in index:
            raise SystemExit(f"unknown id: {cid}")
        for assign in args[1:]:
            k, v = assign.split("=", 1)
            try:
                v = json.loads(v)
            except Exception:
                pass
            index[cid][k] = v
        save(db)
        print(f"Updated {cid}")
        return 0

    print(f"unknown command: {cmd}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
