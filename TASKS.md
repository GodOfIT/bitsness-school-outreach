# Danh sách việc (backlog)

Trạng thái: `MỞ` → `ĐANG LÀM (tên)` → `CHỜ MINMIN DUYỆT` → `XONG`.
Nhận việc: đổi trạng thái, ghi tên và ngày. Tiến độ và kết quả ghi ngay dưới mục của việc, theo mẫu `- [Tên] YYYY-MM-DD: …`.
Đề xuất sửa dữ liệu: dùng bảng mẫu ở mục 4 của [`AGENTS.md`](AGENTS.md).

---

## T1 – Điền C8 (mức quan hệ) cho 97 trường
- **Ai làm:** Minmin · **Ưu tiên:** cao nhất · **Trạng thái:** MỞ
- **Mục tiêu:** cho điểm 1–5 mức quan hệ với từng trường (1 = chưa quen ai, 3 = quen gián tiếp, 5 = quen trực tiếp BGH/Trưởng phòng Đào tạo).
- **Cách làm:** điền cột C8 trong sheet "Chấm điểm" của file Excel, hoặc ghi danh sách `tên trường – điểm – quen ai` vào đây để AI cập nhật vào `scripts/data.py`.
- **Tiến độ:**

## T2 – Xác minh 16 trường Đợt 1
- **Ai làm:** AI (ChatGPT/Claude) + Minmin · **Ưu tiên:** cao · **Trạng thái:** MỞ
- **Mục tiêu:** với mỗi trường Đợt 1, xác minh có nguồn:
  - tên đúng hiện nay, chủ quản, địa chỉ cơ sở gần Hà Đông nhất;
  - quy mô (HSSV, số ngành);
  - LMS/e-learning thực tế (URL hệ thống nếu có);
  - người phụ trách đào tạo/CNTT (chỉ chức danh, tên nếu công khai);
  - sự kiện gần đây (sáp nhập, dự án CĐS, kiểm định).
- **Đầu ra:** bảng đề xuất sửa điểm C1, C5, C6, C7, C10 kèm nguồn; cập nhật cột `do_tin_cay_du_lieu`.
- **Danh sách:** xem `data/schools_scored.csv`, lọc `dot_de_xuat = Đợt 1`.
- **Tiến độ:**

## T3 – Thay điểm ước lượng của 30 trường đại học
- **Ai làm:** AI · **Ưu tiên:** cao · **Trạng thái:** MỞ
- **Mục tiêu:**
  - xác minh LMS hiện có, quy mô, cơ chế tự chủ, chuẩn đầu ra ngoại ngữ của 30 trường ĐH;
  - đề xuất có nên thêm tiêu chí "chu kỳ bán dự kiến", hoặc tăng trọng số C6, để phản ánh đúng việc bán cho ĐH công lập lớn lâu hơn.
- **Tiến độ:**

## T4 – Kiểm tra khả năng tích hợp SCORM/xAPI/LTI
- **Ai làm:** Minmin + kỹ thuật Bitsness · **Ưu tiên:** cao · **Trạng thái:** MỞ
- **Vì sao:** khoảng 1/4 danh sách đã có LMS mạnh (CĐ Công nghệ cao, HCEM, FPT, HaUI…). Muốn bán nội dung cho họ thì học liệu và khóa mô phỏng phải chạy được trên LMS của trường.
- **Cần trả lời:** LMS Bitsness có xuất/nhập SCORM 1.2/2004, xAPI, LTI 1.3 không? Khóa mô phỏng đóng gói được không?
- **Tiến độ:**

## T5 – Bộ chào hàng cho 7 phân khúc
- **Ai làm:** AI · **Ưu tiên:** trung bình · **Trạng thái:** MỞ
- **Đầu ra cho mỗi phân khúc** (xem mục 10 của BRIEF):
  - 1 trang giới thiệu;
  - 1 đề xuất pilot mẫu (phạm vi, thời gian 1 học kỳ, chỉ số thành công);
  - 1 email + 1 tin nhắn Zalo mở đầu.
- **Phụ thuộc:** cần Minmin cung cấp thông tin sản phẩm (tính năng LMS, danh mục khóa học có sẵn, khung giá).
- **Tiến độ:**

## T6 – Đề xuất cấp cụm cho Sở GD&ĐT Hà Nội (14 TT GDNN-GDTX)
- **Ai làm:** AI + Minmin · **Ưu tiên:** trung bình · **Trạng thái:** MỞ
- **Mục tiêu:**
  - xác định phòng ban phụ trách GDNN-GDTX của Sở GD&ĐT;
  - xác định tên mới của 14 TT (nếu đã công bố);
  - soạn đề xuất "một nền tảng + phòng thí nghiệm ảo cho cả cụm", kèm pilot tại 1 TT.
- **Tiến độ:**

## T7 – Phân tích đối thủ và quy định mua sắm
- **Ai làm:** AI · **Ưu tiên:** trung bình · **Trạng thái:** MỞ
- **Mục tiêu:**
  - các nhà cung cấp LMS/học liệu số đang làm cho trường nghề và ĐH ở Hà Nội;
  - nền tảng học liệu dùng chung của Bộ;
  - văn bản đấu thầu/mua sắm/thuê dịch vụ CNTT **còn hiệu lực** áp dụng cho đơn vị sự nghiệp công lập (ngưỡng chỉ định thầu) → gợi ý cách chia gói pilot.
- **Tiến độ:**

## T8 – Mở rộng danh sách: trung cấp tư thục và trường tỉnh (Đợt 4)
- **Ai làm:** AI · **Ưu tiên:** thấp · **Trạng thái:** MỞ
- **Mục tiêu:** bổ sung trung cấp tư thục, trường của bộ ngành tại Hà Nội còn thiếu; lập danh sách trường ở Bắc Ninh, Hưng Yên, Phú Thọ, Ninh Bình; chấm bằng cùng khung (thay C9 bằng thời gian di chuyển).
- **Tiến độ:**
