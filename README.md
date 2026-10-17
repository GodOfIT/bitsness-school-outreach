# Bitsness – Ưu tiên tiếp cận trường học (Hà Nội)

Dự án xếp hạng các trường cao đẳng, đại học, trung cấp và TT GDNN-GDTX tại Hà Nội. Mục đích là quyết định **liên hệ trường nào trước** để chào dịch vụ của Bitsness: **LMS**, **khóa ngoại ngữ**, **khóa khoa học**, **khóa đào tạo mô phỏng** và **số hóa học liệu**. Hà Nội làm trước, các tỉnh làm sau.

## Bắt đầu từ đâu

| Bạn là | Đọc |
|---|---|
| Mở ChatGPT để làm tiếp | Dán prompt trong [`docs/PROMPT_CHATGPT.md`](docs/PROMPT_CHATGPT.md) |
| AI tiếp nhận (ChatGPT, Claude…) | [`docs/BRIEF.md`](docs/BRIEF.md) → [`AGENTS.md`](AGENTS.md) → [`discussion/001-kenh-trao-doi.md`](discussion/001-kenh-trao-doi.md) → [`TASKS.md`](TASKS.md) |
| Minmin | [`discussion/001-kenh-trao-doi.md`](discussion/001-kenh-trao-doi.md) và [`TASKS.md`](TASKS.md) |

## Trạng thái (17/10/2026)

- **97 cơ sở** đã được chấm sơ bộ theo **11 tiêu chí**: 51 CĐ, 30 ĐH, 2 TC, 14 TT GDNN-GDTX.
- **Đợt 1:** 16 trường. **Đợt 2:** 36. **Đợt 3:** 41. **Đợt 4 (ngoài HN):** 4.
- Điểm còn sơ bộ:
  - tiêu chí quan hệ (C8) chưa điền;
  - dữ liệu file gốc chưa xác minh;
  - điểm các trường đại học là ước lượng.

## Dữ liệu

- [`data/schools_scored.csv`](data/schools_scored.csv): điểm từng tiêu chí, tổng điểm, đợt, gói chào, căn cứ chấm, độ tin cậy.
- [`data/criteria.csv`](data/criteria.csv): khung 11 tiêu chí và trọng số.
- [`data/original_colleges_list.csv`](data/original_colleges_list.csv): danh sách 52 trường cao đẳng từ file gốc của Minmin.

## Chạy lại

```bash
pip install openpyxl
python scripts/export_csv.py   # sinh lại CSV
python scripts/build.py        # sinh file Excel 7 sheet vào output/
```
