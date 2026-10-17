# -*- coding: utf-8 -*-
"""Build the scored school dataset (colleges from user's file + added rows)."""
import re

import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLAT = os.path.join(ROOT, 'data', 'original_flat.txt')

CRIT = [
    # code, name, weight, what it measures, 1 / 3 / 5 descriptors
    ("C1", "Khoảng trống LMS", 12, "Trường càng thiếu LMS (đặc biệt LMS cho thực hành) thì nhu cầu càng lớn và ít bị nhà cung cấp cũ chiếm chỗ",
     "Đã có hệ sinh thái LMS tự phát triển/đồng bộ", "Có Moodle/e-learning lý thuyết", "Chưa có LMS hoặc chỉ dùng Google Classroom/Drive"),
    ("C2", "Khớp mô phỏng", 10, "Số nhóm ngành khớp 4 mảng mô phỏng: điện–điện tử; cơ khí/ô tô/thiết bị; y tế–điều dưỡng; phòng thí nghiệm khoa học",
     "Không ngành nào khớp", "Khớp 1 nhóm ngành", "Khớp từ 3 nhóm, hoặc 1–2 nhóm 'rất khớp' và là thế mạnh trường"),
    ("C3", "Nhu cầu ngoại ngữ", 8, "Áp lực chuẩn đầu ra ngoại ngữ, Đề án 2371 (tiếng Anh ngôn ngữ thứ hai), ngành cần ngoại ngữ (du lịch, điều dưỡng đi làm việc nước ngoài, hợp tác Hàn/Nhật/Đức)",
     "Ngành năng khiếu, ít cần ngoại ngữ", "Ngoại ngữ là môn chung/chuẩn đầu ra", "Ngoại ngữ là năng lực nghề cốt lõi hoặc có chương trình liên kết nước ngoài"),
    ("C4", "Nhu cầu số hóa học liệu", 10, "Khối lượng giáo trình cần số hóa, ngành nặng thực hành, trường vừa gộp cần chuẩn hóa học liệu của nhiều trường cũ",
     "Đã có thư viện số/học liệu số đầy đủ", "Trường nghề thông thường, học liệu chủ yếu giấy/PDF", "Vừa sáp nhập/nâng cấp, phải hợp nhất học liệu nhiều đơn vị"),
    ("C5", "Quy mô người học", 8, "Số HSSV và số ngành; quy mô càng lớn, giá trị hợp đồng và mức lan tỏa càng cao",
     "Trường nhỏ, chuyên biệt", "Quy mô trung bình / chưa rõ", "Trường lớn, nhiều ngành, nhiều cơ sở"),
    ("C6", "Năng lực & tốc độ chi", 10, "Cơ chế tài chính và tốc độ ra quyết định: tư thục nhanh; công lập tự chủ khá; công lập phụ thuộc ngân sách chậm, qua dự toán/đấu thầu",
     "Phụ thuộc ngân sách, quy trình dài", "Công lập trực thuộc bộ/thành phố, có nguồn thu sự nghiệp", "Tư thục hoặc tự chủ tài chính, chủ trường quyết nhanh"),
    ("C7", "Sự kiện kích hoạt", 10, "Có sự kiện buộc trường phải đầu tư ngay: mới sáp nhập, lãnh đạo mới, nâng cấp lên cao đẳng, kiểm định, đề án chuyển đổi số",
     "Không có sự kiện đặc biệt", "Có động lực chính sách chung (Đề án 2371, chuyển đổi số)", "Vừa sáp nhập/nâng cấp/đổi lãnh đạo trong 6 tháng qua"),
    ("C8", "Đường tiếp cận", 12, "Bạn có người quen/giới thiệu tới người ra quyết định không. BẠN TỰ ĐIỀN (mặc định 1)",
     "Chưa có ai, tiếp cận lạnh", "Có người quen gián tiếp (cựu SV, đối tác, hội nhóm)", "Quen trực tiếp BGH/Trưởng phòng Đào tạo"),
    ("C9", "Khoảng cách", 6, "Vùng theo khoảng cách từ Hà Đông; ảnh hưởng chi phí gặp trực tiếp và hỗ trợ triển khai",
     "Ngoài Hà Nội", "Vùng 3 (11–15 km)", "Vùng 1 (≤5 km)"),
    ("C10", "Năng lực triển khai phía trường", 7, "Trường có đủ hạ tầng, nhân sự CNTT và thói quen số để dùng được sản phẩm (đối trọng của C1: trường quá sơ khai thì triển khai rủi ro)",
     "Sơ khai: dữ liệu rời rạc trên bảng tính", "Trung bình: đã có cổng tra cứu/tuyển sinh online", "Đã số hóa quản lý bài bản"),
    ("C11", "Giá trị tham chiếu", 7, "Thắng trường này có giúp bán cho trường khác không (trường đầu tàu, cùng hệ thống với nhiều trường, thương hiệu lớn)",
     "Trường lẻ, ít ảnh hưởng", "Trường trung bình trong mạng lưới", "Đầu tàu ngành/thuộc hệ thống nhiều trường cùng chủ quản"),
]
WEIGHTS = [c[2] for c in CRIT]
assert sum(WEIGHTS) == 100

VUNG_SCORE = {"1": 5, "2": 4, "3": 3, "4": 2, "Ngoài HN": 1}

# ---------- keyword heuristics ----------
K_DIEN = r"điện|mạch|vi mạch|IoT|tự động|nhúng|viễn thông|máy lạnh|tín hiệu|vi điều khiển|vi tính|robot|mạng"
K_COKHI = r"ô tô|cơ khí|CNC|đầu máy|máy xây dựng|xây dựng|cấp thoát|trắc địa|BIM|hàn|thiết bị|cầu đường|máy in|máy bơm"
K_YTE = r"y học|dược|điều dưỡng|xét nghiệm|hộ sinh|phục hồi|vật lý trị liệu|hình ảnh y|y sinh|máy y tế|lâm sàng"
K_KH = r"xét nghiệm|chế biến|nông nghiệp|thú y|chăn nuôi|môi trường|dược|hóa|sinh học|khoa học"


def fit_groups(text):
    g = []
    t = text.lower()
    if re.search(K_DIEN, t, re.I): g.append("điện–điện tử")
    if re.search(K_COKHI, t, re.I): g.append("cơ khí/ô tô/thiết bị")
    if re.search(K_YTE, t, re.I): g.append("y tế")
    if re.search(K_KH, t, re.I): g.append("lab khoa học")
    return g


def score_fit(text, strong):
    g = fit_groups(text)
    n = len(g)
    s = {0: 1, 1: 3, 2: 4}.get(n, 5)
    if strong and s < 5:
        s += 1
    return s, g


def score_lms(t):
    tl = t.lower()
    if "tự phát triển" in tl: return 1, "hệ sinh thái LMS tự phát triển"
    if "smart campus" in tl: return 1, "Smart Campus đã vận hành"
    if re.search(r"chưa có lms thực hành sâu\. mới sử dụng", tl): return 4, "chỉ có phần mềm học liệu/thi trắc nghiệm"
    if tl.startswith("chưa có"): return 5, "chưa có LMS (theo file)"
    if "google" in tl: return 4, "dùng Google Classroom/Drive"
    if re.search(r"chuyên sâu|hoàn chỉnh|lms chuẩn|đồng bộ", tl): return 2, "đã có LMS đầy đủ"
    if "moodle" in tl: return 3, "đang dùng Moodle"
    if re.search(r"cơ bản|tạm thời", tl): return 4, "LMS mức cơ bản"
    return 3, "có e-learning lý thuyết"


def score_cap(t):
    tl = t.lower()
    if "sơ khai" in tl: return 2, "quản lý sơ khai"
    if tl.startswith("cơ bản"): return 2, "số hóa quản lý cơ bản"
    if tl.startswith("trung bình - khá"): return 3, "số hóa trung bình–khá"
    if tl.startswith("trung bình"): return 3, "số hóa trung bình"
    if tl.startswith("đang"): return 3, "đang nâng cấp"
    if tl.startswith("khá"): return 4, "số hóa quản lý khá"
    return 5, "đã số hóa quản lý tốt"


# ---------- per-school metadata for the colleges in the user's file ----------
# stt: (owner, owner_score_C6, scale C5, trigger(text,score), ref C11, lang override, trust, vung override, name override, note)
SIDE = {
 1: dict(name="CĐ Y tế Hà Nội (đã hợp nhất CĐ Y tế Hà Đông)", owner="Công lập – TP Hà Nội", c6=3, c5=4,
         trig=("Hợp nhất CĐ Y tế Hà Đông + CĐ Y tế Hà Nội (QĐ 2026); BGH mới bổ nhiệm 6/10/2026", 5), c11=4, c4=5,
         trust="Đã xác minh sáp nhập; hiện trạng LMS là của CĐ Y tế Hà Đông cũ", web="cdythadong.edu.vn"),
 2: dict(owner="Tư thục", c6=5, c5=3, trust="Chưa xác minh (file gốc)"),
 3: dict(owner="Chưa rõ", c6=3, c5=3, trust="Chưa xác minh tên/chủ quản"),
 4: dict(owner="Công lập – Bộ Công Thương", c6=3, c5=3),
 5: dict(owner="Công lập – Bộ Xây dựng", c6=3, c5=3),
 6: dict(owner="Tư thục", c6=5, c5=4),
 7: dict(owner="Tư thục (cần xác minh)", c6=5, c5=3, trust="Chưa xác minh tên/cơ sở"),
 8: dict(owner="Tư thục (cần xác minh)", c6=5, c5=3, trust="Chưa xác minh tên/cơ sở"),
 9: None,  # duplicate of HHT (#16) -> merged
 10: dict(owner="Tư thục", c6=5, c5=3, vung="Ngoài HN", c11=2,
          trust="SAI VỊ TRÍ: trường đặt tại TP.HCM, không thấy cơ sở Hà Nội"),
 11: dict(owner="Chưa rõ", c6=3, c5=3, trust="Chưa xác minh chủ quản"),
 12: dict(owner="Tư thục", c6=5, c5=3),
 13: dict(owner="Tư thục", c6=5, c5=3, trust="Khoảng cách trong file có thể sai (Phạm Văn Đồng >10 km)"),
 14: dict(owner="Công lập – TP Hà Nội", c6=3, c5=4, c11=4,
          trig=("Nhận sáp nhập TC Kỹ thuật Tin học HN + TC KT-KT&CN HN; BGH mới 6/10/2026", 5), c4=5,
          trust="Đã xác minh sáp nhập"),
 15: None,  # CĐ Cộng đồng HN -> merged into HCAT (#33)
 16: dict(name="CĐ Công nghệ cao Hà Nội (CS1 Tây Mỗ + CS2 Thanh Xuân)", owner="Công lập – TP Hà Nội", c6=3, c5=4, c11=5,
          trig=("Giữ nguyên, đang tái cấu trúc; BGH bố trí lại 6/10/2026", 3), c4=2, vung="1",
          trust="Đã xác minh giữ nguyên; gộp 2 dòng #9 và #16 của file"),
 17: dict(owner="Công lập – bộ ngành (cần xác minh)", c6=3, c5=3),
 18: dict(owner="Tư thục – Tổ chức GD FPT", c6=3, c5=5, c11=3, c4=2,
          note="Quyết định ở cấp tập đoàn, tự phát triển LMS; chỉ nên chào khóa mô phỏng/học liệu"),
 19: dict(owner="Tư thục", c6=5, c5=3),
 20: dict(owner="Chưa rõ", c6=3, c5=2, trust="Chưa xác minh tên trường tồn tại"),
 21: dict(owner="Công lập – Bộ Y tế", c6=3, c5=3, c11=5),
 22: dict(owner="Chưa rõ", c6=3, c5=2, trust="Chưa xác minh"),
 23: dict(owner="Công lập – bộ ngành", c6=3, c5=4, c11=5, c4=2),
 24: dict(owner="Công lập – TP Hà Nội", c6=3, c5=4, c11=4,
          trig=("Nhận sáp nhập TC nghề số 1 HN + TC Xây dựng HN; BGH mới 6/10/2026", 5), c4=5,
          trust="Đã xác minh sáp nhập"),
 25: dict(owner="Tư thục", c6=5, c5=4),
 26: dict(owner="Công lập – Bộ Y tế", c6=3, c5=3, c11=4),
 27: dict(owner="Tư thục (cần xác minh)", c6=5, c5=3, trust="Chưa xác minh địa chỉ"),
 28: dict(owner="Tư thục", c6=5, c5=4),
 29: dict(owner="Công lập – bộ ngành", c6=3, c5=3),
 30: dict(owner="Tư thục", c6=5, c5=3),
 31: dict(owner="Công lập – Bộ VHTTDL", c6=3, c5=3),
 32: dict(owner="Công lập – Bộ GD&ĐT", c6=3, c5=3, c11=4),
 33: dict(owner="Công lập – TP Hà Nội", c6=3, c5=4, c11=4,
          trig=("Nhận sáp nhập CĐ Cộng đồng HN + TC Nấu ăn-NVDL&TT HN; BGH mới 6/10/2026", 5), c4=5,
          name="CĐ Thương mại và Du lịch Hà Nội (đã nhận CĐ Cộng đồng HN)",
          trust="Đã xác minh sáp nhập; gộp dòng #15 (CĐ Cộng đồng HN) vào đây"),
 34: dict(owner="Tư thục", c6=5, c5=4, trig=("Đang đầu tư mạnh cơ sở vật chất mới", 4)),
 35: dict(owner="Công lập – TP Hà Nội", c6=3, c5=2, trig=("Giữ nguyên, tái cấu trúc; BGH bố trí lại 6/10/2026", 3),
          trust="Đã xác minh giữ nguyên; khoảng cách trong file có thể sai"),
 36: dict(owner="Tư thục", c6=5, c5=3),
 37: dict(owner="Tư thục", c6=5, c5=3, lang=(4, "trường có thế mạnh ngoại ngữ, có thể là đối thủ ở mảng khóa ngoại ngữ")),
 38: dict(owner="Công lập – TP Hà Nội", c6=3, c5=3, c11=4,
          trig=("Giữ nguyên, đang tái cấu trúc; BGH bố trí lại 6/10/2026", 4), c4=4, trust="Đã xác minh giữ nguyên"),
 39: dict(owner="Công lập – Bộ VHTTDL", c6=3, c5=2, c4=2),
 40: dict(owner="Công lập – Đài THVN", c6=3, c5=3),
 41: dict(owner="Công lập – Bộ Xây dựng", c6=3, c5=4),
 42: dict(owner="Chưa rõ", c6=3, c5=3, trust="KHÔNG XÁC MINH ĐƯỢC tên trường; kiểm tra lại"),
 43: dict(owner="Công lập – Bộ NN&MT", c6=3, c5=3),
 44: dict(owner="Công lập – Đài TNVN", c6=3, c5=3, vung="Ngoài HN",
          trust="SAI VỊ TRÍ: trụ sở tại Phủ Lý (Hà Nam cũ)"),
 45: dict(owner="Công lập – Tổng Cty ĐSVN", c6=3, c5=3),
 46: dict(owner="Chưa rõ", c6=3, c5=3, trust="Chưa xác minh tên/chủ quản"),
 47: dict(owner="Công lập – Liên minh HTX VN", c6=3, c5=3),
 48: dict(owner="Công lập – Bộ Xây dựng", c6=3, c5=3),
 49: dict(owner="Chưa rõ", c6=3, c5=3, trust="Chưa xác minh chủ quản"),
 50: dict(owner="Doanh nghiệp – Tập đoàn Dệt May", c6=3, c5=3, trust="Chưa xác minh website (file có link nghi vấn)"),
 51: dict(owner="Chưa rõ", c6=3, c5=3, vung="Ngoài HN", trust="NGHI SAI VỊ TRÍ: nhiều khả năng ở Hưng Yên; kiểm tra lại"),
 52: dict(owner="Công lập – bộ ngành", c6=3, c5=4, vung="Ngoài HN",
          trust="SAI VỊ TRÍ: trụ sở tại Bình Xuyên, Vĩnh Phúc cũ (nay Phú Thọ)"),
}


def lang_score(text, name):
    t = (text + " " + name).lower()
    if re.search(r"du lịch|khách sạn|thương mại|hàn quốc", t):
        return 5, "ngành du lịch/thương mại/liên kết Hàn: ngoại ngữ là năng lực nghề"
    if re.search(r"điều dưỡng|hộ sinh|dược|y tế|y dược", t):
        return 4, "điều dưỡng/y tế: nhu cầu tiếng Nhật/Đức/Anh để làm việc nước ngoài"
    if re.search(r"múa|nghệ thuật|mỹ thuật", t):
        return 2, "ngành năng khiếu, ngoại ngữ ít ưu tiên"
    return 3, "ngoại ngữ là chuẩn đầu ra chung"


def parse_file():
    rows = []
    vung = None
    for line in open(FLAT, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('P: Vùng'):
            vung = re.search(r"Vùng (\d)", line).group(1)
            continue
        if not line.startswith('R: ') or line.startswith('R: STT'):
            continue
        c = [x.strip() for x in line[3:].split(' | ')]
        stt = int(c[0])
        namefield = c[1]
        name = namefield.split('•')[0].strip()
        web = namefield.split('•')[1].strip() if '•' in namefield else ''
        if 'removed' in web: web = ''
        km = re.match(r"([\d.]+)\s*km", c[2])
        rows.append(dict(stt=stt, name=name, web=web, vung=vung, km=float(km.group(1)) if km else None,
                         addr=c[2].split('(')[-1].rstrip(')') if '(' in c[2] else '',
                         nganh=c[3], lms=c[4], sis=c[5]))
    return rows


def build_rows():
    out = []
    for r in parse_file():
        side = SIDE.get(r['stt'], {})
        if side is None:
            continue
        name = side.get('name', r['name'])
        strong = bool(re.search(r"rất khớp|cực khớp", r['nganh'], re.I))
        nganh_clean = re.sub(r"^(Rất khớp|Cực khớp):\s*", "", r['nganh'])
        c1, c1r = score_lms(r['lms'])
        c2, groups = score_fit(nganh_clean + " " + name, strong)
        c3, c3r = side.get('lang', lang_score(nganh_clean, name))
        trig_txt, c7 = side.get('trig', ("Không có sự kiện riêng; chỉ có động lực chính sách chung", 2))
        if 'c4' in side:
            c4 = side['c4']
        else:
            c4 = 4
        c4r = {5: "vừa gộp trường, phải hợp nhất học liệu", 4: "trường nghề nặng thực hành, học liệu chủ yếu giấy/PDF",
               2: "đã có thư viện số/học liệu số tốt"}.get(c4, "")
        if c4 == 2 and re.search(r"múa", name, re.I):
            c4r = "đào tạo năng khiếu trực tiếp, ít học liệu số hóa được"
        vung = side.get('vung', r['vung'])
        c9 = VUNG_SCORE[vung]
        c10, c10r = score_cap(r['sis'])
        c5 = side.get('c5', 3)
        c6 = side.get('c6', 3)
        c11 = side.get('c11', 3)
        out.append(dict(
            src=f"File gốc #{r['stt']}" + (" + #9" if r['stt'] == 16 else "") + (" + #15" if r['stt'] == 33 else ""),
            name=name, loai="Cao đẳng", owner=side.get('owner', 'Chưa rõ'), vung=vung, km=r['km'], addr=r['addr'],
            nganh=nganh_clean, lms=r['lms'], sis=r['sis'], trig=trig_txt,
            trust=side.get('trust', "Chưa xác minh (file gốc)"), web=side.get('web', r['web']),
            s=[c1, c2, c3, c4, c5, c6, c7, 1, c9, c10, c11],
            why=[c1r, ("khớp: " + ", ".join(groups)) if groups else "không khớp nhóm nào", c3r, c4r,
                 {5: "rất lớn", 4: "lớn, nhiều ngành", 3: "trung bình/chưa rõ", 2: "nhỏ, chuyên biệt"}[c5],
                 side.get('owner', 'Chưa rõ'), trig_txt, "chưa có quan hệ (tự cập nhật)", f"Vùng {vung}", c10r,
                 {5: "đầu tàu ngành", 4: "thuộc hệ thống trường của TP/bộ, dễ nhân rộng", 3: "trường trong mạng lưới",
                  2: "ít giá trị tham chiếu tại HN"}[c11]],
            note=side.get('note', ''),
        ))
    return out


# ---------- additions ----------
def add(name, loai, owner, vung, nganh, s, why, trig, trust, note="", web="", addr="", lms="Cần khảo sát", sis="Cần khảo sát"):
    return dict(src="Bổ sung", name=name, loai=loai, owner=owner, vung=vung, km=None, addr=addr, nganh=nganh,
                lms=lms, sis=sis, trig=trig, trust=trust, web=web, s=s, why=why, note=note)


def additions():
    A = []
    TRIG_MERGE_TC = "Nhận sáp nhập 2 trường trung cấp (KH 292/KH-UBND); BGH mới 6/10/2026"
    A.append(add("CĐ nghề Việt Nam – Hàn Quốc TP Hà Nội", "Cao đẳng", "Công lập – TP Hà Nội", "3",
                 "Cơ khí, điện – điện tử, ô tô, CNTT (hợp tác Hàn Quốc)",
                 [4, 4, 5, 5, 4, 3, 5, 1, 3, 3, 4],
                 ["chưa rõ, giả định LMS rời rạc sau sáp nhập", "khớp: điện–điện tử, cơ khí/ô tô", "tiếng Hàn là lợi thế cốt lõi",
                  "vừa nhận 2 trường trung cấp, phải hợp nhất học liệu", "lớn sau sáp nhập", "Công lập – TP Hà Nội",
                  TRIG_MERGE_TC + " (TC nghề Cơ khí I HN + TC KT-KT Bắc Thăng Long)", "chưa có quan hệ (tự cập nhật)", "Vùng 3 (ước lượng)",
                  "chưa rõ", "thuộc hệ thống trường của TP"],
                 TRIG_MERGE_TC, "Đã xác minh sáp nhập; vị trí/LMS cần khảo sát"))
    for nm in ["Trung cấp nghề Tổng hợp Hà Nội", "Trung cấp nghề Giao thông công chính Hà Nội"]:
        A.append(add(nm, "Trung cấp", "Công lập – TP Hà Nội", "2",
                     "Nghề kỹ thuật (điện, cơ khí, ô tô…) – cần xác minh",
                     [5, 4, 3, 5, 3, 2, 5, 1, 4, 2, 3],
                     ["trường trung cấp, nhiều khả năng chưa có LMS", "khớp: điện–điện tử, cơ khí (giả định)", "chuẩn đầu ra chung",
                      "nâng cấp lên cao đẳng: phải xây chương trình/học liệu mới", "trung bình", "Công lập – ngân sách TP",
                      "Đang lập đề án nâng cấp thành cao đẳng đa ngành", "chưa có quan hệ (tự cập nhật)", "Vùng 2 (ước lượng)",
                      "giả định sơ khai", "thuộc hệ thống trường của TP"],
                     "Lập đề án nâng cấp lên CĐ đa ngành (KH 292/KH-UBND)", "Đã xác minh trong KH 292; vị trí/ngành cần khảo sát"))
    # 14 TT GDNN-GDTX after merger
    TT = [("Hà Đông – Chương Mỹ", "1"), ("Hoàng Mai – Thanh Xuân", "1"), ("Thanh Trì – Thanh Oai", "2"),
          ("Ba Đình – Cầu Giấy – Nam Từ Liêm", "2"), ("Hoàn Kiếm (Nguyễn Văn Tố) – Đống Đa – Hai Bà Trưng", "2"),
          ("Hoài Đức – Đan Phượng", "3"), ("Phú Xuyên – Thường Tín", "3"), ("Gia Lâm – Long Biên", "3"),
          ("Đông Anh – Tây Hồ", "3"), ("Thạch Thất – Quốc Oai", "4"), ("Ứng Hòa – Mỹ Đức", "4"),
          ("Sơn Tây – Phúc Thọ", "4"), ("Mê Linh – Sóc Sơn", "4"), ("Ba Vì", "4")]
    to_tht = {"Mê Linh – Sóc Sơn", "Ba Vì", "Phú Xuyên – Thường Tín", "Ứng Hòa – Mỹ Đức", "Thanh Trì – Thanh Oai"}
    for area, v in TT:
        merged = area != "Ba Vì"
        trig = ("Hợp nhất từ nhiều TT (29→14)" if merged else "Giữ nguyên") + \
               ("; dự kiến chuyển thành trường trung học nghề" if area in to_tht else "")
        c7 = 5 if (merged or area in to_tht) else 3
        A.append(add(f"TT GDNN-GDTX khu vực {area}", "TT GDNN-GDTX", "Công lập – Sở GD&ĐT Hà Nội", v,
                     "GDTX cấp THPT (Lý, Hóa, Sinh, Tiếng Anh) + nghề ngắn hạn",
                     [5, 3, 3, 5 if merged else 4, 3, 2, c7, 1, VUNG_SCORE[v], 2, 4],
                     ["giả định chưa có LMS", "khớp: lab khoa học (chương trình GDTX THPT)", "tiếng Anh bắt buộc theo chương trình phổ thông",
                      "hợp nhất học liệu các TT cũ" if merged else "học liệu chủ yếu giấy", "trung bình", "Ngân sách qua Sở GD&ĐT, quyết định chậm",
                      trig, "chưa có quan hệ (tự cập nhật)", f"Vùng {v} (ước lượng)", "giả định sơ khai",
                      "cùng chủ quản với 13 TT khác: thắng 1 dễ nhân rộng"],
                     trig, "Đã xác minh danh sách khu vực sáp nhập (KH 292); tên mới chưa công bố",
                     note="Cân nhắc tiếp cận cả cụm qua Sở GD&ĐT thay vì từng TT"))
    # Universities – curated list, LMS status unknown (needs discovery)
    U = [
        # name, owner, vung, nganh, c1, c2, c3, c4, c5, c6, c7, c10, c11, trig, note
        ("Học viện Công nghệ Bưu chính Viễn thông (PTIT)", "Công lập – tự chủ", "1", "Điện tử viễn thông, CNTT, đa phương tiện",
         2, 4, 5, 3, 5, 4, 3, 5, 4, "Đề án 2371: chuẩn đầu ra tiếng Anh", "Mạnh CNTT, có thể tự làm LMS; chào khóa ngoại ngữ + mô phỏng mạch"),
        ("Trường ĐH Phenikaa", "Tư thục", "1", "Kỹ thuật, ô tô, điện tử, y dược, điều dưỡng",
         3, 5, 5, 4, 5, 5, 3, 5, 4, "Đề án 2371: chuẩn đầu ra tiếng Anh", ""),
        ("Trường ĐH Đại Nam", "Tư thục", "1", "Y dược, điều dưỡng, CNTT, ngôn ngữ",
         3, 4, 4, 4, 4, 5, 3, 4, 3, "Đề án 2371: chuẩn đầu ra tiếng Anh", ""),
        ("Học viện Y Dược học cổ truyền Việt Nam", "Công lập – Bộ Y tế", "1", "Y học cổ truyền, dược, điều dưỡng",
         3, 4, 4, 4, 4, 3, 3, 4, 3, "Đề án 2371", ""),
        ("Trường ĐH Kiến trúc Hà Nội", "Công lập", "1", "Kiến trúc, xây dựng, cấp thoát nước, đồ họa 3D",
         3, 3, 4, 4, 4, 3, 3, 4, 3, "Đề án 2371", ""),
        ("Trường ĐH Công nghệ Giao thông vận tải (UTT)", "Công lập – Bộ Xây dựng", "1", "Ô tô, cơ khí, điện – điện tử, xây dựng",
         3, 4, 4, 4, 4, 3, 3, 4, 3, "Đề án 2371", ""),
        ("Trường ĐH Thăng Long", "Tư thục", "2", "Điều dưỡng, y tế công cộng, CNTT, ngôn ngữ",
         3, 4, 4, 4, 4, 5, 3, 4, 3, "Đề án 2371", ""),
        ("Trường ĐH Kinh tế – Kỹ thuật Công nghiệp (UNETI)", "Công lập – Bộ Công Thương", "2", "Điện, điện tử, cơ khí, dệt may, thực phẩm",
         3, 5, 4, 4, 5, 3, 3, 4, 3, "Đề án 2371", ""),
        ("Trường ĐH Thủ đô Hà Nội", "Công lập – TP Hà Nội", "2", "Sư phạm, ngôn ngữ, công nghệ, khoa học",
         3, 3, 4, 4, 4, 3, 4, 4, 4, "Giữ nguyên đầu mối, định hướng mô hình ĐH ứng dụng (KH 292); BGH bố trí lại 6/10/2026", ""),
        ("Trường ĐH Mở Hà Nội", "Công lập – Bộ GD&ĐT", "2", "Đào tạo từ xa/trực tuyến, ngôn ngữ, CNTT, điện tử",
         2, 3, 4, 5, 5, 4, 3, 5, 4, "Đề án 2371", "Mạnh đào tạo trực tuyến: vừa là khách hàng số hóa học liệu, vừa có thể là đối thủ/đối tác"),
        ("Trường ĐH Giao thông vận tải", "Công lập – tự chủ", "2", "Cơ khí, ô tô, điện – điện tử, xây dựng",
         2, 4, 4, 3, 5, 4, 3, 5, 5, "Đề án 2371", ""),
        ("Trường ĐH Thủy lợi", "Công lập – Bộ NN&MT", "2", "Xây dựng, cơ khí, điện, môi trường",
         3, 5, 4, 4, 5, 3, 3, 4, 4, "Đề án 2371", ""),
        ("Trường ĐH Xây dựng Hà Nội", "Công lập – tự chủ", "2", "Xây dựng, cơ khí, môi trường, BIM",
         3, 4, 4, 4, 5, 4, 3, 5, 4, "Đề án 2371", ""),
        ("Trường ĐH Y Hà Nội", "Công lập – Bộ Y tế", "2", "Y khoa, điều dưỡng, xét nghiệm",
         2, 4, 4, 3, 5, 4, 3, 5, 5, "Đề án 2371", "Chu kỳ bán dài; ưu tiên khi đã có case trường y khác"),
        ("Trường ĐH Sư phạm Hà Nội", "Công lập – Bộ GD&ĐT", "2", "Sư phạm, khoa học tự nhiên, ngôn ngữ",
         2, 3, 4, 4, 5, 3, 3, 5, 5, "Đề án 2371 (đào tạo giáo viên dạy bằng tiếng Anh)", ""),
        ("Trường ĐH Lao động – Xã hội", "Công lập", "2", "Kinh tế, xã hội, CNTT",
         3, 1, 4, 4, 4, 3, 3, 4, 3, "Đề án 2371", ""),
        ("Trường ĐH Hòa Bình", "Tư thục", "2", "Dược, điều dưỡng, CNTT, kiến trúc",
         4, 4, 4, 4, 3, 5, 3, 3, 2, "Đề án 2371", ""),
        ("Trường ĐH Kinh doanh và Công nghệ Hà Nội (HUBT)", "Tư thục", "2", "Y, dược, kỹ thuật, kinh tế",
         3, 4, 4, 4, 5, 5, 3, 4, 3, "Đề án 2371", ""),
        ("Trường ĐH CMC", "Tư thục", "2", "CNTT, vi mạch, ngôn ngữ",
         2, 3, 4, 3, 3, 5, 3, 5, 3, "Đề án 2371", ""),
        ("Trường ĐH Mỹ thuật Công nghiệp", "Công lập", "2", "Thiết kế, mỹ thuật, đồ họa 3D",
         4, 1, 3, 3, 3, 3, 2, 3, 2, "Không có sự kiện riêng", ""),
        ("Trường ĐH Công nghiệp Hà Nội (HaUI)", "Công lập – tự chủ", "3", "Cơ khí, điện, điện tử, ô tô, ngoại ngữ",
         2, 5, 5, 4, 5, 4, 3, 5, 5, "Đề án 2371", "Quy mô rất lớn; nhiều khả năng đã có hệ thống riêng"),
        ("Trường ĐH Điện lực", "Công lập – Bộ Công Thương", "3", "Điện, điện tử, tự động hóa, năng lượng",
         3, 4, 4, 4, 4, 3, 3, 4, 4, "Đề án 2371", ""),
        ("Trường ĐH Thành Đô", "Tư thục", "3", "Dược, điều dưỡng, ô tô, điện, ngôn ngữ",
         4, 5, 4, 4, 3, 5, 3, 3, 2, "Đề án 2371", ""),
        ("Trường ĐH Mỏ – Địa chất", "Công lập", "3", "Mỏ, địa chất, cơ điện, trắc địa, môi trường",
         3, 5, 4, 4, 4, 3, 3, 4, 3, "Đề án 2371", ""),
        ("Trường ĐH Tài nguyên và Môi trường Hà Nội", "Công lập – Bộ NN&MT", "3", "Môi trường, trắc địa, CNTT",
         3, 3, 4, 4, 4, 3, 3, 4, 3, "Đề án 2371", ""),
        ("Trường ĐH Y tế Công cộng", "Công lập – Bộ Y tế", "3", "Y tế công cộng, xét nghiệm, dinh dưỡng",
         3, 4, 4, 4, 2, 3, 3, 4, 3, "Đề án 2371", ""),
        ("Trường ĐH Dược Hà Nội", "Công lập – Bộ Y tế", "3", "Dược, hóa dược, công nghệ sinh học",
         3, 4, 4, 4, 4, 4, 3, 5, 5, "Đề án 2371", ""),
        ("Trường ĐH FPT (Hòa Lạc)", "Tư thục – Tổ chức GD FPT", "4", "CNTT, vi mạch, ngôn ngữ",
         1, 3, 4, 2, 5, 3, 3, 5, 3, "Đề án 2371", "Tự phát triển hệ thống; chỉ chào khóa mô phỏng/học liệu"),
        ("Trường ĐH Lâm nghiệp", "Công lập – Bộ NN&MT", "4", "Lâm nghiệp, cơ điện, môi trường, sinh học",
         3, 4, 4, 4, 3, 3, 3, 3, 3, "Đề án 2371", ""),
        ("Học viện Nông nghiệp Việt Nam", "Công lập – tự chủ", "4", "Nông nghiệp, cơ điện, công nghệ sinh học, thú y",
         2, 5, 4, 4, 5, 4, 3, 5, 4, "Đề án 2371", ""),
    ]
    LMS_TXT = {1: "hệ thống tự phát triển (giả định)", 2: "nhiều khả năng đã có LMS (giả định)", 3: "chưa rõ, giả định có LMS/Moodle cơ bản",
               4: "chưa rõ, giả định LMS sơ khai"}
    for (nm, owner, v, ng, c1, c2, c3, c4, c5, c6, c7, c10, c11, trig, note) in U:
        g = fit_groups(ng)
        A.append(add(nm, "Đại học", owner, v, ng, [c1, c2, c3, c4, c5, c6, c7, 1, VUNG_SCORE[v], c10, c11],
                     [LMS_TXT[c1], ("khớp: " + ", ".join(g)) if g else "không khớp nhóm nào",
                      "Đề án 2371 + chuẩn đầu ra tiếng Anh ĐH" if c3 >= 4 else "ngành năng khiếu, ngoại ngữ là môn chung",
                      {5: "khối lượng học liệu rất lớn (đào tạo từ xa)", 4: "khối lượng giáo trình lớn", 3: "đã có một phần học liệu số",
                       2: "đã có hệ thống học liệu số riêng"}[c4],
                      {5: "rất lớn", 4: "lớn", 3: "trung bình", 2: "nhỏ"}[c5], owner, trig, "chưa có quan hệ (tự cập nhật)",
                      f"Vùng {v} (ước lượng)", {5: "hạ tầng CNTT mạnh", 4: "hạ tầng khá", 3: "hạ tầng trung bình"}[c10],
                      {5: "thương hiệu đầu ngành", 4: "uy tín trong khối ngành", 3: "trường trung bình", 2: "ít giá trị tham chiếu"}[c11]],
                     trig, "Ước lượng – LMS/quy mô cần khảo sát", note=note,
                     lms="Cần khảo sát (" + LMS_TXT[c1] + ")"))
    return A


def all_rows():
    rows = build_rows() + additions()
    for r in rows:
        r['score'] = round(sum(s * w for s, w in zip(r['s'], WEIGHTS)) / (5 * 100) * 100, 1)
    return rows


if __name__ == '__main__':
    rows = all_rows()
    rows.sort(key=lambda r: -r['score'])
    import collections
    print(len(rows), collections.Counter(r['loai'] for r in rows))
    for r in rows:
        print(f"{r['score']:5.1f}  V{r['vung']:<8} {r['loai'][:6]:6}  {r['name'][:60]}")
