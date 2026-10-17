# Prompt bàn giao cho Claude – phản biện ý kiến ChatGPT (17/10/2026)

> Dùng với Claude Code hoặc Claude có quyền đọc/ghi repository GitHub `GodOfIT/bitsness-school-outreach`. Có thể dán toàn bộ đoạn bên dưới vào Claude. Đây là prompt **mời phản biện**, không phải lệnh tự động chỉnh mô hình.

---

Bạn là Claude, cộng tác cùng ChatGPT và Minmin trong dự án **Bitsness School Outreach** tại GitHub:
https://github.com/GodOfIT/bitsness-school-outreach

## 1. Đọc repo trước khi phát biểu

Đọc đúng nội dung trên nhánh `main`, ưu tiên thứ tự:
1. `docs/BRIEF.md` – bối cảnh, quyết định và giả định.
2. `AGENTS.md` – quy tắc làm việc và giới hạn thay đổi.
3. `discussion/001-kenh-trao-doi.md` – lời bàn giao và kênh trao đổi.
4. **`discussion/002-phan-bien-chatgpt-2026-10-17.md` – BẢN PHẢN BIỆN MỚI CỦA CHATGPT; PHẢI ĐỌC HẾT.**
5. `TASKS.md`, `data/criteria.csv`, `data/schools_scored.csv`.
6. Kiểm tra trực tiếp `scripts/data.py`, `scripts/export_csv.py`, `scripts/build.py` để xác minh các kết luận kỹ thuật.

## 2. Nhiệm vụ của bạn

**Không cần đồng ý với ChatGPT. Hãy phản biện có căn cứ, kể cả phản bác hoàn toàn nếu hợp lý.** Đặc biệt trả lời:

**A. Mô hình:** Có nên giữ 11 tiêu chí Fit Score và thêm một lớp Sales Readiness tách biệt? Hay nên sửa C6/thêm C12? Nêu tác động đến khả năng ký hợp đồng và nguy cơ double-count.

**B. Đợt 1:** Cách chia Quick Wins / Strategic Accounts có tốt hơn ép tỷ lệ 2/3 CĐ/TC – 1/3 ĐH không? Cho đề xuất triển khai thực tế với 16 trường, phân biệt điểm đã kiểm chứng và giả định.

**C. 14 TT GDNN-GDTX:** Đánh giá phương án pilot tại TT + đề xuất cấp cụm qua Sở + hội thảo. Những ràng buộc về thẩm quyền, ngân sách, tên pháp lý, dữ liệu người học cần xác minh trước khi ký là gì?

**D. Kiểm tra kỹ thuật:** Tự đối chiếu source với các nhận xét ChatGPT:
- C8=1 cho 97 trường; C8 tăng 1→5 làm tổng điểm tăng 9,6 có đúng không?
- Regex C2 có thể nhận diện sai chuyên ngành do từ khóa quá rộng?
- Có rủi ro nhập C8 trong Excel rồi chạy lại `scripts/build.py` làm mất thay đổi?
- Pipeline có tự cập nhật **danh sách tên trường** khi thứ hạng mới thay đổi, hay chỉ cập nhật điểm/đợt cho những tên đã có?
- 30 trường đại học ước lượng, dữ liệu website/vị trí còn trống có làm biến dạng shortlist không?

**E. Bảo mật:** Kiểm tra visibility của GitHub repo. `AGENTS.md` ghi repo riêng tư nhưng ChatGPT nhìn thấy `public`; đề nghị cách xử lý. **Không đăng tải số điện thoại/email cá nhân hay quan hệ thực tế trước khi xác nhận quyền riêng tư.**

**F. Phân công:** Gợi ý phân chia T2/T3 giữa ChatGPT và Claude, một kế hoạch tối đa 2 tuần, đầu ra có thể kiểm chứng; ghi rõ cần Minmin quyết định gì.

## 3. Định dạng câu trả lời bắt buộc

Trình bày:
1. **Điểm đồng ý với ChatGPT** – từng luận điểm + bằng chứng.
2. **Điểm không đồng ý** – vì sao sai/yếu + phương án thay thế.
3. **Điểm chưa đủ dữ liệu** – cái gì cần xác minh; không biến giả định thành sự thật.
4. **Quyết định đề nghị Minmin** – bảng: `Vấn đề | Phương án A | Phương án B | Bạn đề nghị | Lý do`.
5. **Công việc tiếp theo** – người nhận, ưu tiên, đầu ra và phạm vi chưa được phép sửa.

Với sự kiện bên ngoài (tên trường, sáp nhập, LMS, văn bản chính sách, pháp lý/mua sắm), ghi **URL nguồn và ngày truy cập**. Không bịa nguồn.

## 4. Ghi lại vào GitHub để ChatGPT đọc được

- **Append-only** bình luận mới vào cuối `discussion/001-kenh-trao-doi.md`, tiêu đề `## [Claude] 2026-10-17 – Phản biện lại ChatGPT` (hoặc ngày thực tế).
- Nếu dài, tạo `discussion/003-phan-hoi-claude.md` và thêm một bình luận ngắn chứa link đến file đó ở kênh chung.
- Commit bắt đầu bằng `[Claude]`. Không sửa/xóa bình luận của ChatGPT hoặc Minmin.
- **Chưa sửa** `scripts/data.py`, `data/schools_scored.csv`, trọng số, công thức hay ngưỡng chia đợt trước khi Minmin duyệt.
- Nếu không có quyền push, xuất **nguyên văn phần bình luận/file Markdown sẵn để dán** thay vì tuyên bố đã commit.

Mục tiêu cuối cùng là có một phương án **được hai AI phản biện và Minmin phê duyệt**, để chuyển từ danh sách xếp hạng sơ bộ sang pipeline tiếp cận trường có kiểm chứng, bán được và triển khai được.
