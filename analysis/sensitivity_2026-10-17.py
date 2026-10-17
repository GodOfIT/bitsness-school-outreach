# -*- coding: utf-8 -*-
"""[Claude] Phân tích kiểm chứng & độ nhạy – CHỈ ĐỌC, không sửa dữ liệu/điểm/trọng số.

Chạy:  python analysis/sensitivity_2026-10-17.py
Mục đích: kiểm chứng các nhận xét kỹ thuật trong discussion/002 và các rủi ro mô hình
nêu trong discussion/003. Mọi kịch bản "what-if" chỉ tính trong bộ nhớ.
"""
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))
import data as D  # noqa: E402

W = D.WEIGHTS
T1, T2 = 70, 65


def total(s):
    return round(sum(a * b for a, b in zip(s, W)) / 5, 1)


def wave(r, sc):
    if r["vung"] == "Ngoài HN":
        return "Đ4"
    return "Đ1" if sc >= T1 else ("Đ2" if sc >= T2 else "Đ3")


rows = D.all_rows()
hn = [r for r in rows if r["vung"] != "Ngoài HN"]
print("=" * 70)
print("1) C8: phân bố và tác động")
print("   C8 values:", Counter(r["s"][7] for r in rows))
print("   +1 bậc C8 =", 12 * 1 / 5, "điểm; 1→5 =", 12 * 4 / 5, "điểm")
for bump, label in [(2, "C8 1→3"), (4, "C8 1→5")]:
    up = [r for r in hn if r["score"] < T1 <= r["score"] + 12 * bump / 5]
    print(f"   {label} (+{12*bump/5}): số trường HN đang dưới 70 sẽ vượt 70 nếu được nâng: {len(up)}/{sum(1 for r in hn if r['score']<T1)}")

print("=" * 70)
print("2) Độ mong manh quanh ngưỡng 70")
for d in (1, 2, 5):
    n = sum(1 for r in hn if abs(r["score"] - T1) <= d)
    print(f"   Trường HN trong ±{d} điểm quanh 70: {n}")
print("   Đúng 70,0:", [r["name"] for r in hn if r["score"] == 70.0])
sc = sorted((r["score"] for r in hn), reverse=True)
print("   Điểm cao nhất/thấp nhất HN:", sc[0], sc[-1], "| khoảng cách hạng 1 → hạng 16:", round(sc[0] - sc[15], 1),
      "| hạng 16 → hạng 52:", round(sc[15] - sc[51], 1))

print("=" * 70)
print("3) Đợt 1 – tỷ lệ dữ liệu đã kiểm chứng")
d1 = [r for r in hn if r["score"] >= T1]
for r in d1:
    tag = ("XÁC MINH" if r["trust"].startswith("Đã xác minh") else
           "ƯỚC LƯỢNG" if r["trust"].startswith("Ước lượng") else "CHƯA XÁC MINH")
    print(f"   {r['score']:5.1f} {tag:13} {r['loai']:9} {r['name'][:55]}")
print("   Đếm:", Counter(("XÁC MINH" if r["trust"].startswith("Đã xác minh") else
                         "ƯỚC LƯỢNG" if r["trust"].startswith("Ước lượng") else "CHƯA XÁC MINH") for r in d1))

print("=" * 70)
print("4) Regex C2 – từ khóa nào kích hoạt nhóm nào (chỉ áp dụng cho cao đẳng file gốc)")
PAT = {"điện–điện tử": D.K_DIEN, "cơ khí/ô tô/thiết bị": D.K_COKHI, "y tế": D.K_YTE, "lab khoa học": D.K_KH}
sus = []
for r in rows:
    if not r["src"].startswith("File gốc"):
        continue
    t = (r["nganh"] + " " + r["name"]).lower()
    hits = {g: sorted(set(m.group(0) for m in re.finditer(p, t, re.I))) for g, p in PAT.items()}
    hits = {g: h for g, h in hits.items() if h}
    flags = []
    if "chế biến" in hits.get("lab khoa học", []) and re.search(r"món ăn|chế biến\b(?! thực phẩm)", t):
        flags.append("'chế biến (món ăn)' → lab khoa học")
    if hits.get("cơ khí/ô tô/thiết bị") == ["thiết bị"]:
        flags.append("chỉ 'thiết bị' → nhóm cơ khí")
    if set(hits.get("điện–điện tử", [])) <= {"mạng", "vi tính"} and hits.get("điện–điện tử"):
        flags.append("chỉ 'mạng/vi tính' → nhóm điện")
    if "dược" in hits.get("lab khoa học", []) and set(hits.get("lab khoa học", [])) <= {"dược", "xét nghiệm"}:
        flags.append("'dược/xét nghiệm' đếm 2 nhóm (y tế + lab)")
    if flags:
        sus.append((r["name"], r["s"][1], hits, flags))
for name, c2, hits, flags in sus:
    print(f"   C2={c2} {name[:50]}\n        hits={hits}\n        cờ={flags}")
print("   Tổng số dòng có cờ:", len(sus))

print("=" * 70)
print("5) Đếm trùng sự kiện 'sáp nhập/nâng cấp' (C4=5 & C7=5)")
merged = [r for r in rows if r["s"][3] == 5 and r["s"][6] == 5]
print("   Số dòng C4=5 và C7=5:", len(merged), Counter(r["loai"] for r in merged))
# what-if: C4 về mức mặc định theo loại hình (4) cho các dòng này -> chỉ C7 giữ sự kiện
chg = []
for r in merged:
    s2 = list(r["s"]); s2[3] = 4
    new = total(s2)
    chg.append((r["name"], r["score"], new, wave(r, r["score"]), wave(r, new)))
for n, a, b, wa, wb in chg:
    if wa != wb or n.startswith("CĐ"):
        print(f"   {a:5.1f} → {b:5.1f}  {wa}→{wb}  {n[:55]}")

print("=" * 70)
print("6) Tương quan C1 và C10 (cao đẳng file gốc)")
pairs = [(r["s"][0], r["s"][9]) for r in rows if r["src"].startswith("File gốc")]
print("   Bảng (C1, C10):", sorted(Counter(pairs).items()))
n = len(pairs); mx = sum(a for a, _ in pairs) / n; my = sum(b for _, b in pairs) / n
cov = sum((a - mx) * (b - my) for a, b in pairs); vx = sum((a - mx) ** 2 for a, _ in pairs); vy = sum((b - my) ** 2 for _, b in pairs)
print("   Pearson r =", round(cov / (vx * vy) ** 0.5, 2))

print("=" * 70)
print("7) Dữ liệu trống")
print("   Không website:", sum(1 for r in rows if not r["web"]), "/", len(rows))
print("   Không km:", sum(1 for r in rows if r["km"] is None), "/", len(rows),
      Counter(r["loai"] for r in rows if r["km"] is None))

print("=" * 70)
print("8) Kịch bản: bỏ 30 ĐH ước lượng khỏi xếp hạng – Đợt 1 còn gì")
d1b = [r for r in hn if r["score"] >= T1 and r["loai"] != "Đại học"]
print("   Đợt 1 không tính ĐH:", len(d1b), [r["name"][:40] for r in d1b])
nxt = sorted([r for r in hn if r["loai"] != "Đại học" and r["score"] < T1], key=lambda r: -r["score"])[:8]
print("   8 cơ sở không phải ĐH kế tiếp:", [(r["name"][:40], r["score"]) for r in nxt])
