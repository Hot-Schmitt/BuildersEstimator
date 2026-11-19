"""
Read the builder's job-cost workbook: his cost code list, and for each code
the budget, change orders and paid amount by cost type (Labor, Material, Sub).
Payee names are counted, never written out.

Usage: python3 -I read_cost_workbook.py <costs.xlsx> <out.json>
"""
import datetime
import json
import re
import sys
import warnings

import openpyxl

TYPES = {"labor": "labor", "material": "material", "sub": "subcontract"}


def read(path):
    warnings.simplefilter("ignore")
    wb = openpyxl.load_workbook(path, data_only=True)
    codes = []
    for ws in wb:
        m = re.search(r"[Dd]iv (\d+)$", ws.title)
        if not m:
            continue
        division, code, row_type = int(m.group(1)), None, None
        for r in range(3, ws.max_row + 1):
            a, b, c, d, e, f = (ws.cell(r, k).value for k in range(1, 7))
            if isinstance(a, (int, float)) and isinstance(b, str):
                code = {"code": str(int(a)), "name": b.strip(), "division": division, "types": []}
                codes.append(code)
                row_type = None
            elif code and a is None and isinstance(b, str) and not b.lower().startswith("total"):
                key = TYPES.get(b.strip().lower().split(" ")[0])
                if key:
                    row_type = {"type": key, "label": b.strip(), "budget": c or 0, "co": d or 0,
                                "adjusted": e or 0, "paid": f or 0, "payments": 0, "payees": set()}
                    code["types"].append(row_type)
            elif row_type and isinstance(a, datetime.datetime) and isinstance(c, (int, float)):
                row_type["payments"] += 1
                row_type["payees"].add(str(b).strip().lower())
    for code in codes:
        for t in code["types"]:
            t["payees"] = len(t["payees"])
    return codes


if __name__ == "__main__":
    codes = read(sys.argv[1])
    json.dump(codes, open(sys.argv[2], "w"), indent=0)
    print(len(codes), "codes")
