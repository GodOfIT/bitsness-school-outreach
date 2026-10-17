# -*- coding: utf-8 -*-
"""[Claude] Mô hình tài chính bảng giá ngoại ngữ – có thể chạy lại để kiểm chứng.

Chạy:   python analysis/pricing_model_2026-10-17.py            (in bảng ra màn hình)
        python analysis/pricing_model_2026-10-17.py --md out.md (ghi thêm file Markdown)

QUAN TRỌNG
- Đơn vị tiền: TRIỆU ĐỒNG. Giá chào (100k/TK/tháng, 350/330/320, 5tr/tháng, 54tr/năm) lấy từ
  đề bài của Minmin (17/10/2026) – là GIẢ THUYẾT KINH DOANH, chưa phê duyệt.
- Mọi CHI PHÍ (hạ tầng của trường, giá vốn của bên cung cấp) dưới đây là GIẢ ĐỊNH MINH HỌA
  để phân tích độ nhạy. KHÔNG phải chi phí thực tế, KHÔNG được dùng làm giá vốn.
- Không tính VAT (phần mềm có thể không chịu thuế GTGT theo khoản 21 Điều 5 Luật 48/2024/QH15 –
  cần kế toán xác nhận cho từng cấu phần).
- Chi phí giảng viên KHÔNG đưa vào so sánh TCO vì mọi phương án đều cần người dạy (GV trường hoặc GV thuê).
"""
import math
import sys

# ----------------------------- GIÁ CHÀO (đề bài) -----------------------------
P_G1 = 0.1          # triệu / tài khoản / tháng
P_G2 = 350.0        # mua học liệu + LMS + đào tạo GV nguồn
P_G3 = 330.0        # mua học liệu + LMS, thuê GV (phí dạy tính riêng)
P_G4 = 320.0        # như G3, cam kết quy mô lớn
OPS_MONTH = 5.0     # vận hành LMS thuê ngoài, theo tháng
OPS_YEAR = 54.0     # vận hành LMS thuê ngoài, theo năm
HANDOVER_MONTHS = 3 # 3 tháng chuyển giao – không bán vận hành trùng thời gian này

# ------------------ GIẢ ĐỊNH MINH HỌA phía NHÀ TRƯỜNG (sửa được) ------------------
def hosting_per_year(n):
    """Chi phí máy chủ/năm do TRƯỜNG trả, theo số học viên hoạt động. MINH HỌA."""
    if n <= 300:
        return 18.0
    if n <= 1000:
        return 36.0
    return 72.0

IT_INTERNAL_PER_YEAR = 0.0   # chi phí nhân sự CNTT nội bộ khi tự vận hành; mặc định 0 (để lộ rõ đây là giả định thiếu)

# ------------- GIẢ ĐỊNH MINH HỌA phía BÊN CUNG CẤP (KHÔNG phải giá vốn thật) -------------
SUPPLIER_SCEN = {
    #            hosting/TK/tháng, hỗ trợ/trường/năm (G1), triển khai G2, đào tạo GV nguồn, bảo hành/năm, vận hành/năm (chi phí)
    "thấp":   dict(c_host=0.005, c_sup=12.0, c_deploy=40.0, c_tot=15.0, c_warr=10.0, c_ops=30.0),
    "cơ sở":  dict(c_host=0.010, c_sup=24.0, c_deploy=60.0, c_tot=25.0, c_warr=15.0, c_ops=40.0),
    "cao":    dict(c_host=0.020, c_sup=36.0, c_deploy=90.0, c_tot=35.0, c_warr=25.0, c_ops=55.0),
}

NS = [100, 300, 500, 1000, 3000]
MS = [6, 9, 12]
TS = [1, 3, 5]


def ops_cost_school(T):
    """Phí vận hành trường trả trong T năm, bắt đầu sau 3 tháng chuyển giao.
    Năm 1: 9 tháng × 5tr (rẻ hơn 54tr/năm). Năm 2..T: 54tr/năm."""
    if T <= 0:
        return 0.0
    first = min(OPS_MONTH * (12 - HANDOVER_MONTHS), OPS_YEAR)
    return first + OPS_YEAR * (T - 1)


def tco(pkg, n, m, T, ops=False):
    """Tổng chi phí sở hữu của TRƯỜNG (triệu), chưa gồm giảng viên, chưa VAT."""
    if pkg == "G1":
        return P_G1 * n * m * T
    base = {"G2": P_G2, "G3": P_G3, "G4": P_G4}[pkg]
    cost = base + hosting_per_year(n) * T + IT_INTERNAL_PER_YEAR * T
    if ops:
        cost += ops_cost_school(T)
    return cost


def breakeven_n(pkg, m, T, ops=False, nmax=20000):
    """Số học viên/năm nhỏ nhất để G1 đắt hơn gói mua (tính lặp vì hosting theo bậc)."""
    for n in range(1, nmax + 1):
        if tco("G1", n, m, T) >= tco(pkg, n, m, T, ops):
            return n
    return None


def supplier_g1(n, m, T, s):
    rev = P_G1 * n * m * T
    cost = s["c_host"] * n * m * T + s["c_sup"] * T
    return rev, cost, rev - cost


def supplier_g2(T, s, ops=False, with_tot=True, price=P_G2):
    rev = price + (ops_cost_school(T) if ops else 0.0)
    cost = s["c_deploy"] + (s["c_tot"] if with_tot else 0) + s["c_warr"] * min(T, 3)
    if ops:
        # chi phí vận hành bắt đầu sau 3 tháng, quy đổi theo tỷ lệ thời gian
        cost += s["c_ops"] * (T - HANDOVER_MONTHS / 12)
    return rev, cost, rev - cost


def option_c(n, T, F=150.0, p=0.25):
    """Phương án C (THAY THẾ – chờ duyệt): phí chuyển giao F + phí học liệu p triệu/học viên/năm (on-prem)."""
    return F + p * n * T


def cashflow_g2(price=P_G2, terms=(0.30, 0.60, 0.10)):
    """Dòng tiền thu theo đợt: tạm ứng khi ký / nghiệm thu (tháng 3) / sau 3 tháng vận hành ổn định (tháng 6)."""
    return [round(price * t, 1) for t in terms]


# ------------------------------ IN KẾT QUẢ ------------------------------
out = []


def p(line=""):
    out.append(line)


def fmt(x, d=1):
    if x is None:
        return "–"
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def fi(n):
    return f"{n:,}".replace(",", ".")


p("## M1. Tổng chi phí sở hữu (TCO) của NHÀ TRƯỜNG – triệu đồng, chưa gồm giảng viên, chưa VAT")
p("Giả định minh họa máy chủ trường trả/năm: ≤300 HV: 18; ≤1.000 HV: 36; >1.000 HV: 72. Nhân sự CNTT nội bộ = 0 (thiếu, cần bổ sung).")
p()
for T in TS:
    p(f"**Thời hạn {T} năm**")
    p()
    p("| Học viên/năm | G1 6 th | G1 9 th | G1 12 th | G2 tự vận hành | G2 + thuê vận hành | G3/G4 tự vận hành (chưa gồm phí dạy) |")
    p("|---:|---:|---:|---:|---:|---:|---:|")
    for n in NS:
        p(f"| {fi(n)} | {fmt(tco('G1', n, 6, T))} | {fmt(tco('G1', n, 9, T))} | {fmt(tco('G1', n, 12, T))} | "
          f"{fmt(tco('G2', n, 0, T))} | {fmt(tco('G2', n, 0, T, ops=True))} | {fmt(tco('G3', n, 0, T))} / {fmt(tco('G4', n, 0, T))} |")
    p()

p("## M2. Điểm ngang giá G1 ↔ G2 (số học viên trả phí/năm để thuê tài khoản bắt đầu ĐẮT hơn mua)")
p()
p("| Thời hạn | Tháng dùng/năm | G2 tự vận hành | G2 + thuê vận hành |")
p("|---:|---:|---:|---:|")
for T in TS:
    for m in MS:
        p(f"| {T} năm | {m} | {breakeven_n('G2', m, T)} | {breakeven_n('G2', m, T, ops=True)} |")
p()

p("## M3. Đơn giá ngầm định trên mỗi học viên-năm (triệu đồng) – để thấy độ vênh giữa gói thuê và gói mua")
p()
p("| Học viên/năm | G1 (9 tháng) | G2 trong 3 năm | G2 trong 5 năm | G1 / G2(5 năm) |")
p("|---:|---:|---:|---:|---:|")
for n in NS:
    g1 = P_G1 * 9
    g2_3 = P_G2 / (n * 3)
    g2_5 = P_G2 / (n * 5)
    p(f"| {fi(n)} | {fmt(g1, 3)} | {fmt(g2_3, 3)} | {fmt(g2_5, 3)} | {fmt(g1/g2_5)}× |")
p()

p("## M4. Bên cung cấp – DOANH THU, CHI PHÍ GIẢ ĐỊNH, LỢI NHUẬN GỘP (triệu đồng, 3 năm, 9 tháng/năm)")
p("Chi phí là GIẢ ĐỊNH MINH HỌA 3 kịch bản, KHÔNG phải giá vốn thực tế.")
p()
p("| Kịch bản chi phí | Học viên | G1: DT / CP / LNG | G2 (gồm đào tạo GV): DT / CP / LNG | G2 + vận hành: DT / CP / LNG | PA C (150 + 0,25/HV/năm): DT |")
p("|---|---:|---|---|---|---:|")
for sname, s in SUPPLIER_SCEN.items():
    for n in (100, 300, 1000, 3000):
        a = supplier_g1(n, 9, 3, s)
        b = supplier_g2(3, s)
        c = supplier_g2(3, s, ops=True)
        p(f"| {sname} | {fi(n)} | {fmt(a[0])} / {fmt(a[1])} / {fmt(a[2])} | {fmt(b[0])} / {fmt(b[1])} / {fmt(b[2])} | "
          f"{fmt(c[0])} / {fmt(c[1])} / {fmt(c[2])} | {fmt(option_c(n, 3))} |")
p()

p("## M5. Dòng tiền thu G2 nếu áp điều kiện thanh toán đề xuất 30% / 60% / 10%")
p()
cf = cashflow_g2()
p(f"Ký hợp đồng: {fmt(cf[0])} · Nghiệm thu (≈ tháng 3): {fmt(cf[1])} · Sau 3 tháng vận hành ổn định (≈ tháng 6): {fmt(cf[2])}. "
  "Chi phí triển khai phát sinh chủ yếu trong tháng 0–3, chi phí bảo hành trải 36 tháng sau nghiệm thu → doanh thu đến trước, nghĩa vụ kéo dài 3 năm.")
p()

p("## M6. Phí vận hành 5 triệu/tháng mua được bao nhiêu giờ công? (độ nhạy theo đơn giá giờ công GIẢ ĐỊNH)")
p()
p("| Đơn giá giờ công giả định (triệu/giờ) | Giờ/tháng với 5 tr | Giờ/tháng với 54 tr/năm (4,5 tr/tháng) |")
p("|---:|---:|---:|")
for r in (0.3, 0.5, 0.8):
    p(f"| {fmt(r)} | {fmt(OPS_MONTH / r)} | {fmt(OPS_YEAR / 12 / r)} |")
p()

p("## M7. Chi phí G1 cho MỘT học viên đi từ con số 0 đến B1 (độ nhạy)")
p("Cambridge English ước tính khoảng 350–400 giờ học có hướng dẫn (cộng dồn từ người mới bắt đầu) để đạt B1; đây là con số tham khảo, không phải cam kết.")
p()
p("| Giờ học/tuần | Số tháng ước tính cho 375 giờ | Chi phí G1/học viên (triệu) |")
p("|---:|---:|---:|")
for h in (4, 6, 8, 10):
    months = math.ceil(375 / (h * 52 / 12))
    p(f"| {h} | {months} | {fmt(months * P_G1)} |")
p()

p("## M8. So sánh 3 cấu trúc trong 5 năm (9 tháng/năm, trường tự vận hành) – THAY THẾ, CHỜ DUYỆT")
p("B+ = bản quyền 330 (+20 đào tạo GV nguồn tùy chọn) có HẠN MỨC 500 HV hoạt động/năm; mỗi 500 HV/năm vượt hạn mức: +80 (một lần);"
  " từ năm 4 có gói cập nhật & bảo trì TÙY CHỌN 15%/năm của phí bản quyền. C = phí chuyển giao 150 + 0,25/HV/năm."
  " Mọi con số mới (500, 80, 15%, 150, 0,25) là GIẢ ĐỊNH MINH HỌA để so sánh cấu trúc, không phải giá đề xuất chính thức.")
p()
p("| Học viên/năm | G1: TCO trường = DT bên CC | G2 hiện tại: TCO / DT | B+ (mua bảo trì năm 4–5): TCO / DT | C: TCO / DT |")
p("|---:|---:|---:|---:|---:|")
for n in (100, 300, 500, 1000, 3000):
    T = 5
    h = hosting_per_year(n) * T
    g1 = P_G1 * n * 9 * T
    g2 = P_G2
    blocks = max(0, math.ceil((n - 500) / 500))
    bplus = P_G3 + 20 + 80 * blocks + 0.15 * (P_G3 + 20) * 2
    c = option_c(n, T)
    p(f"| {fi(n)} | {fmt(g1)} | {fmt(g2 + h)} / {fmt(g2)} | {fmt(bplus + h)} / {fmt(bplus)} | {fmt(c + h)} / {fmt(c)} |")
p()
p("Đọc bảng: TCO trường đã cộng máy chủ giả định; DT = doanh thu bên cung cấp (chưa trừ chi phí, KHÔNG phải lợi nhuận).")
p()

text = "\n".join(out)
print(text)
if "--md" in sys.argv:
    path = sys.argv[sys.argv.index("--md") + 1]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("# [Claude] Kết quả mô hình tài chính – sinh tự động từ analysis/pricing_model_2026-10-17.py\n\n")
        fh.write("> Giá chào là giả thuyết của Minmin (chưa duyệt). Mọi chi phí là GIẢ ĐỊNH MINH HỌA, không phải giá vốn thực tế.\n\n")
        fh.write(text + "\n")
