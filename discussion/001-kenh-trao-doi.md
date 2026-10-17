# 💬 Kênh trao đổi: Minmin ↔ ChatGPT ↔ Claude

> **Cách dùng file này:** ghi **nối tiếp xuống cuối** (append-only). Không sửa hay xóa bình luận của người khác. Mỗi bình luận bắt đầu bằng một tiêu đề cấp 2 theo mẫu `## [Tên] YYYY-MM-DD – chủ đề ngắn`. Trả lời một ý cụ thể thì trích dẫn (`>`) câu đang trả lời. Quy ước đầy đủ: [`AGENTS.md`](../AGENTS.md).
>
> Thảo luận chi tiết theo từng việc nằm ở [`TASKS.md`](../TASKS.md): mỗi việc có một mục, ghi tiến độ ngay dưới mục đó.

---

## [Claude] 2026-10-17 – Bàn giao dự án cho ChatGPT

Chào ChatGPT,

Mình là Claude. Mình vừa làm phần nền của dự án này cùng Minmin. Tóm tắt nhanh để bạn tiếp nhận:

**Đã làm xong**
1. Khung chấm **11 tiêu chí** (tổng trọng số 100) cho việc ưu tiên tiếp cận trường: [`data/criteria.csv`](../data/criteria.csv), giải thích ở mục 6 của [`docs/BRIEF.md`](../docs/BRIEF.md).
2. Chấm sơ bộ **97 cơ sở** ở Hà Nội: 51 CĐ, 30 ĐH, 2 TC, 14 TT GDNN-GDTX. Kết quả trong [`data/schools_scored.csv`](../data/schools_scored.csv). Cột `can_cu_cham` ghi lý do từng điểm.
3. Phân đợt: Đợt 1 = 16, Đợt 2 = 36, Đợt 3 = 41, Đợt 4 (ngoài HN) = 4.
4. Đã xác minh bối cảnh chính sách:
   - Hà Nội vừa gộp trường nghề công lập (KH 292/KH-UBND, xong trước 25/8/2026).
   - Ban Giám hiệu mới được bổ nhiệm ngày 6/10/2026.
   - QĐ 2371/QĐ-TTg về tiếng Anh ngôn ngữ thứ hai.
   - Đây là căn cứ để đưa các trường vừa sáp nhập lên đầu danh sách.
5. File Excel 7 sheet (công thức sống) ở `excel/`, và script để tạo lại ở `scripts/`.

**Điều bạn cần biết ngay**
- Điểm **còn sơ bộ**. File gốc của Minmin có nhiều dữ liệu chưa xác minh, vài chỗ sai rõ (mục 4 và 8 của BRIEF). Điểm 30 trường đại học là mình ước lượng. Tiêu chí quan hệ C8 đang = 1 cho tất cả.
- Minmin muốn **phản biện thẳng** và **lập luận từng dòng**. Đừng khen; thấy sai thì nói và đưa cách sửa.
- Mọi dữ liệu thực tế về trường phải có **nguồn URL + ngày truy cập**.

**Đề nghị việc đầu tiên cho bạn** (chọn một rồi ghi "Nhận việc" vào [`TASKS.md`](../TASKS.md)):
- **T2 – Xác minh 16 trường Đợt 1**: việc có tác động lớn nhất, vì Minmin sắp đi gặp các trường này.
- Hoặc **T3 – Thay điểm ước lượng của 30 trường ĐH** bằng dữ liệu có nguồn, và cho ý kiến có nên thêm tiêu chí "chu kỳ bán dự kiến" không.

**Câu hỏi muốn bạn phản biện ngay ở file này:**
1. 11 tiêu chí và trọng số (mục 6.2 của BRIEF) có thiếu hay thừa gì không? Mình nghi mô hình đang **đánh giá thấp độ dài chu kỳ bán** của đại học công lập lớn.
2. Ngưỡng Đợt 1 = 70 điểm cho ra 8 CĐ + 8 ĐH. Bạn có đồng ý nên đổi thành khoảng 2/3 CĐ/TC và 1/3 ĐH không?
3. Có cách nào tốt hơn để đi vào 14 TT GDNN-GDTX ngoài đề xuất cấp cụm qua Sở GD&ĐT?

— Claude

---

<!-- Bình luận tiếp theo ghi bên dưới dòng này -->
