# -*- coding: utf-8 -*-
"""Xuất dữ liệu chấm điểm ra CSV (UTF-8) để người/AI đọc trực tiếp trên GitHub.

Chạy:  python scripts/export_csv.py
Logic tính Tổng điểm / Đợt / Gói chào giống hệt công thức trong file Excel (scripts/build.py).
"""
import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import all_rows, CRIT, parse_file, WEIGHTS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
T1, T2 = 70, 65  # ngưỡng Đợt 1 / Đợt 2 (sheet 'Trọng số' C19/C20)


def wave(r):
    if r["vung"] == "Ngoài HN":
        return "Đợt 4 – Ngoài HN"
    return "Đợt 1" if r["score"] >= T1 else ("Đợt 2" if r["score"] >= T2 else "Đợt 3")


def offer(s):
    c1, c2, c3 = s[0], s[1], s[2]
    base = "LMS + số hóa học liệu" if c1 >= 4 else ("Nâng cấp/thay LMS + số hóa học liệu" if c1 == 3
                                                      else "Số hóa học liệu, chạy trên LMS sẵn có")
    return base + (" + mô phỏng" if c2 >= 4 else "") + (" + ngoại ngữ" if c3 >= 4 else "")


def main():
    rows = sorted(all_rows(), key=lambda r: -r["score"])
    # rank (RANK() style: ties share rank)
    for r in rows:
        r["rank"] = 1 + sum(1 for x in rows if x["score"] > r["score"])

    head = (["hang", "truong", "loai_hinh", "chu_quan", "vung", "km_tu_ha_dong_file_goc", "nganh_chinh",
             "hien_trang_lms_file_goc", "so_hoa_quan_ly_file_goc", "su_kien_kich_hoat"]
            + [c[0] for c in CRIT]
            + ["tong_diem_100", "dot_de_xuat", "goi_chao_mo_cua", "do_tin_cay_du_lieu", "can_cu_cham", "ghi_chu",
               "website", "nguon_dong"])
    with open(os.path.join(DATA, "schools_scored.csv"), "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(head)
        for r in rows:
            why = " | ".join(f"{c[0]}={s}: {y}" for c, s, y in zip(CRIT, r["s"], r["why"]))
            w.writerow([r["rank"], r["name"], r["loai"], r["owner"], r["vung"], r["km"] if r["km"] is not None else "",
                        r["nganh"], r["lms"], r["sis"], r["trig"]] + r["s"] +
                       [r["score"], wave(r), offer(r["s"]), r["trust"], why, r["note"], r["web"], r["src"]])

    with open(os.path.join(DATA, "criteria.csv"), "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["ma", "tieu_chi", "trong_so_pct", "do_cai_gi", "diem_1", "diem_3", "diem_5"])
        for c in CRIT:
            w.writerow(list(c))

    with open(os.path.join(DATA, "original_colleges_list.csv"), "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["stt_file_goc", "vung", "truong", "website", "km", "dia_chi", "nganh", "hien_trang_lms", "so_hoa_quan_ly"])
        for r in parse_file():
            w.writerow([r["stt"], r["vung"], r["name"], r["web"], r["km"], r["addr"], r["nganh"], r["lms"], r["sis"]])

    from collections import Counter
    print("rows:", len(rows), Counter(wave(r) for r in rows))
    assert sum(WEIGHTS) == 100


if __name__ == "__main__":
    main()
