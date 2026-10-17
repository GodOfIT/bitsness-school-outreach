# Quy ước làm việc (cho ChatGPT, Claude và Minmin)

Repo này là nơi nhiều trợ lý AI và Minmin cùng làm một dự án. Mọi người làm theo các quy ước dưới đây để không giẫm chân nhau và không làm hỏng dữ liệu.

## 1. Đọc gì trước

1. [`docs/BRIEF.md`](docs/BRIEF.md): toàn bộ bối cảnh, quyết định, khung chấm điểm, kết quả, việc còn lại.
2. [`data/schools_scored.csv`](data/schools_scored.csv): dữ liệu hiện tại. Cột `can_cu_cham` giải thích từng điểm.
3. [`discussion/001-kenh-trao-doi.md`](discussion/001-kenh-trao-doi.md) (kênh trao đổi) và [`TASKS.md`](TASKS.md) (danh sách việc).

## 2. Nói chuyện ở đâu, như thế nào

Quyền GitHub hiện có không mở được Issue, nên **trao đổi bằng file trong repo**. Mỗi lần ghi là một commit, lịch sử nằm trong git.

- **Kênh chung:** [`discussion/001-kenh-trao-doi.md`](discussion/001-kenh-trao-doi.md). Dùng cho câu hỏi, phản biện, đề xuất đổi hướng, báo cáo tiến độ.
  - **Ghi nối tiếp xuống cuối file**, không sửa/xóa bình luận của người khác.
  - Mỗi bình luận mở đầu bằng tiêu đề: `## [ChatGPT] 2026-10-18 – chủ đề`, `## [Claude] …`, `## [Minmin] …`
  - Chủ đề lớn, dài thì mở file mới: `discussion/002-<chu-de>.md`, rồi ghi link vào kênh chung.
- **Việc cụ thể:** [`TASKS.md`](TASKS.md). Nhận việc bằng cách đổi trạng thái thành `ĐANG LÀM (tên, ngày)`. Tiến độ ghi ngay dưới mục của việc đó.
- **Cần Minmin quyết định:** ghi `**@Minmin cần quyết định:**` kèm các phương án và khuyến nghị.
- **Commit message** bắt đầu bằng tên: `[ChatGPT] Xác minh 5 trường Đợt 1`, `[Claude] …`, `[Minmin] …`
- **Nếu ChatGPT không tự commit được:** ChatGPT soạn nội dung (bình luận hoặc file sửa) theo đúng định dạng, Minmin dán vào GitHub (sửa file trên web → Commit). Claude cũng có thể áp vào khi được nhờ.
- Nếu sau này bật được Issues, có thể chuyển sang Issues; giữ file này làm lưu trữ.

## 3. Nguyên tắc nội dung

1. **Không bịa dữ liệu.** Mọi thông tin thực tế về trường (tên, chủ quản, địa chỉ, quy mô, LMS, lãnh đạo) phải có **nguồn URL + ngày truy cập**. Không có nguồn thì ghi "chưa xác minh".
2. **Cập nhật cột độ tin cậy** (`do_tin_cay_du_lieu`) mỗi khi sửa dữ liệu một trường. Dùng các nhãn: `Đã xác minh (nguồn…)`, `Chưa xác minh`, `Ước lượng`, `SAI…`/`KHÔNG XÁC MINH ĐƯỢC…`.
3. **Giải thích lập luận cho từng điểm** đã sửa. Minmin muốn thấy lý do từng dòng, không chỉ con số.
4. **Phản biện thẳng.** Thấy khung chấm, dữ liệu hay kế hoạch có vấn đề thì nói rõ, kèm cách sửa. Không cần khen.
5. Viết **tiếng Việt**, câu ngắn, rõ ràng.
6. Repo là **riêng tư**. Không chuyển sang công khai. Không đưa số điện thoại/email cá nhân của cán bộ trường vào repo khi chưa có sự đồng ý của Minmin.

## 4. Sửa dữ liệu thế nào

**Cách 1 – chạy được code (khuyến nghị):**
1. Tạo nhánh mới, ví dụ `verify-dot1`.
2. Sửa `scripts/data.py`:
   - trường cao đẳng trong file gốc → dict `SIDE` theo số thứ tự file gốc;
   - trường bổ sung → hàm `additions()`;
   - trọng số → `CRIT`.
3. Chạy `python scripts/export_csv.py` (và `python scripts/build.py` nếu cần Excel).
4. Mở Pull Request. Mô tả PR liệt kê từng thay đổi theo mẫu ở cách 2.

**Cách 2 – không chạy được code:** ghi vào mục của việc trong `TASKS.md` (hoặc kênh trao đổi) một bảng theo mẫu:

| Trường | Tiêu chí / trường dữ liệu | Cũ | Mới | Lý do | Nguồn (URL, ngày truy cập) |
|---|---|---|---|---|---|
| CĐ Y tế Hà Nội | C5 Quy mô | 4 | 5 | Sau hợp nhất có khoảng X HSSV | https://… (18/10/2026) |

Claude hoặc Minmin sẽ áp vào code.

## 5. Không được làm

- Không sửa tay `data/schools_scored.csv` mà không cập nhật `scripts/data.py`, vì lần chạy script sau sẽ ghi đè.
- Không đổi công thức tổng điểm, ngưỡng đợt hay trọng số mà chưa nêu ở kênh trao đổi và chưa được Minmin đồng ý.
- Không xóa dòng dữ liệu. Trường không còn phù hợp thì đánh dấu ở cột ghi chú/độ tin cậy.
