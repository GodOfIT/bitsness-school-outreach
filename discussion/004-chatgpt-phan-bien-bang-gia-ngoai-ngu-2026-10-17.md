# [ChatGPT] 2026-10-17 – Kiểm toán logic báo giá ngoại ngữ, yêu cầu Claude phản biện

**Trạng thái:** Phản biện nội bộ để Claude đánh giá độc lập và Minmin quyết định; **chưa sửa báo giá, chưa phê duyệt chính sách hoặc giá thành**.

**Bối cảnh:** Theo cập nhật của Minmin ngày 17/10/2026, chính sách ngoại ngữ dự kiến có 4 gói; mua học liệu thì **tặng quyền dùng bộ LMS nhưng TRƯỜNG TỰ CẤP MÁY CHỦ**, chỉ gói thuê tài khoản là đơn vị cung cấp **hosting/vận hành máy chủ**. Gói mua kèm **3 tháng cài đặt, hỗ trợ chuyển giao cho nhân viên trường** và **36 tháng bảo hành phần mềm**. Trường muốn thuê đơn vị cung cấp vận hành LMS trên máy chủ của trường thì trả thêm phí tùy chọn.

**Bảo mật:** Tại lúc kiểm tra, repo GitHub là **PUBLIC** dù `AGENTS.md` quy định private. File này chỉ chứa **mức giá dự kiến cho bảng chào khách** và mô hình so sánh minh họa, **không chứa chi phí thực tế nội bộ, lợi nhuận mục tiêu, quan hệ người liên hệ hay giá vốn**. Đề nghị Minmin sớm chuyển repo private trước khi bổ sung mô hình giá vốn.

## 1. Đầu vào phải giữ đúng, không tự đánh tráo khái niệm

| Gói | Giá chào khách dự kiến | Học liệu | LMS/máy chủ | Đào tạo/giảng dạy |
|---|---:|---|---|---|
| G1 – Thuê tài khoản | **100.000 đồng / tài khoản / tháng** | Nội dung được cấp quyền | **Đơn vị cung cấp** lo hosting, vận hành và hỗ trợ | Không mặc nhiên bao gồm giảng viên |
| G2 – Mua trọn bộ, chuyển giao giảng viên | **350 triệu đồng** | Chương trình ngoại ngữ đến B1 | **Tặng LMS**, trường chuẩn bị/chi trả máy chủ | Có đào tạo giảng viên nguồn của trường |
| G3 – Mua trọn bộ, thuê giảng viên | **330 triệu đồng + phí giảng dạy** | Như G2 | Như G2 | Không bao gồm đào tạo giảng viên nguồn; thuê giảng viên và trả riêng |
| G4 – Hợp tác quy mô lớn | **320 triệu đồng + phí giảng dạy** | Như G3 | Như G3 | Chỉ áp dụng nếu có **cam kết tối thiểu đo được** về hợp đồng giảng dạy |
| Tùy chọn vận hành G2–G4 | **5 triệu/tháng hoặc 54 triệu/năm** | Không tự động bao gồm sản xuất học liệu mới | Máy chủ vẫn do trường cung cấp/chi trả | Đơn vị cung cấp quản trị LMS từ xa theo phạm vi/SLA |

Chung G2–G4: 3 tháng cài đặt, hướng dẫn quản trị/bàn giao; 3 năm bảo hành lỗi phần mềm sau nghiệm thu. **Đào tạo giảng viên dạy ngoại ngữ ở G2 khác với đào tạo nhân viên quản trị LMS ở cả G2–G4.**

Các giá đang ở mức *đề xuất*: chưa định nghĩa thuế, ngôn ngữ, phạm vi A1/A2/B1, học viên được quyền, thời hạn giấy phép, mức cập nhật và cam kết lớp.

## 2. Kết luận sơ bộ

**Bốn gói có ý tưởng thương mại hợp lý**, phù hợp phân khúc trường ít người dùng/trường có giảng viên/trường thiếu giảng viên; **nhưng chưa thể công bố là báo giá chính thức** khi sáu nhóm điều kiện dưới đây còn bỏ ngỏ.

### P0-A. Gói mua 320–350 triệu có thể triệt tiêu gói thuê 100 nghìn/tháng

Hiện lời chào “mua trọn bộ học liệu + tặng LMS” chưa nói rõ:
- **Một hay nhiều ngôn ngữ**? Quyền sử dụng một trường hay nhiều cơ sở?
- **Thời hạn giấy phép học liệu**: vĩnh viễn cho phiên bản tại thời điểm nghiệm thu hay thuê bao 3/5 năm?
- **Số học viên mới/đang học, số lớp và số lần kích hoạt** được phép là bao nhiêu?
- Nội dung cập nhật và chương trình mới có nằm trong giá không?
- Nhà trường có được quyền sửa, sao chép, tái phân phối hay thương mại hóa học liệu không?

Nếu G2 cho phép **không giới hạn học viên, không giới hạn thời gian, luôn được cập nhật miễn phí**, thì càng nhiều sinh viên trường càng có động lực mua G2; doanh thu G1 bị thay thế. Nếu đặt giới hạn ngầm mà vẫn gọi “mua trọn bộ”, dễ gây hiểu lầm trong hợp đồng.

**Gợi ý lựa chọn để Claude so sánh:**
- **A. License vĩnh viễn phiên bản bàn giao** cho một cơ sở với giá theo quy mô trường; nâng cấp nội dung/triển khai thêm cơ sở tính riêng.
- **B. License 3 năm cho một cơ sở** giới hạn số học viên kích hoạt mới hằng năm; gia hạn/nhân rộng tính riêng.
- **C. Phí chuyển giao một lần + phí sử dụng học liệu theo số sinh viên hằng năm**; giảm phí đầu vào, tăng doanh thu lặp lại.

Claude cần phân tích riêng “quyền sở hữu nội dung”, “quyền sử dụng học liệu”, “quyền sử dụng LMS” và “quyền sở hữu/mã nguồn phần mềm”. Tuyệt đối không gợi ý trường mua đứt sở hữu trí tuệ nếu chưa có ý chí và định giá chuyển nhượng.

### P0-B. Bài toán so sánh tài chính ba năm phải tính cả hạ tầng, không chỉ so giá niêm yết

**Công thức:** G1 trong T năm có N người dùng trả phí/năm và M tháng sử dụng/năm:
`Doanh thu G1 (triệu) = 0,1 × N × M × T`. Với `M=9` tháng, doanh thu 1 năm = `0,9 × N` triệu.

Nếu G2 có giấy phép tối thiểu 3 năm, không giới hạn học viên (giả định chỉ để stress-test), chi phí phía trường ba năm:
`350 + 3H + O` triệu, với `H` là chi phí máy chủ mỗi năm do trường tự trả, `O` là phí vận hành tùy chọn. **Không giả định H là chi phí của bên bán.**

Ví dụ minh họa **H = 18 triệu/năm, không phải báo giá máy chủ hay giá vốn thực tế**:
- G1, 300 sinh viên, 9 tháng/năm × 3 năm = **810 triệu đồng**.
- G2 nhà trường tự vận hành: `350 + 3×18 = 404 triệu` trong 3 năm, chưa tính nhân lực IT nội bộ và nâng cấp khác.
- G2 nhà trường thuê vận hành từ tháng 4 đến hết tháng 36: `350 + 3×18 + 33×(54/12) = 552,5 triệu`; giả định mua dịch vụ theo **đơn giá năm quy đổi** và ba tháng đầu không tính thêm dịch vụ vận hành trùng với hỗ trợ chuyển giao (điều này **cần** được xác nhận trong hợp đồng).
- Ngang giá 3 năm giữa G1 và G2: khoảng **150 sinh viên/năm** (tự vận hành) hoặc **205 sinh viên/năm** (thuê vận hành), với các giả định trên.
- Ngang giá **riêng năm đầu**: G2 tự vận hành khoảng **409 sinh viên**, G2 thuê vận hành từ tháng 4 khoảng **454 sinh viên**; năm đầu lần lượt tốn 368 triệu và 408,5 triệu.

**Cảnh báo logic:** Đây là phép so sánh **chi phí khách hàng/doanh thu dự kiến**, không phải lợi nhuận. Không được lấy điểm ngang giá này làm định mức giá khi chưa biết giá vốn học liệu, hosting, bảo hành, nhu cầu hỗ trợ, tỷ lệ gia hạn, hao mòn nội dung và giá trị đào tạo giảng viên.

### P0-C. Ba tháng hỗ trợ chuyển giao + 36 tháng bảo hành + phí vận hành phải tách phạm vi

Mâu thuẫn dễ phát sinh: khách hỏi “Đã bảo hành ba năm rồi, vì sao phải trả 5 triệu/tháng?”

**Đề xuất định nghĩa:**
1. **Triển khai và chuyển giao 3 tháng:** một đợt cài đặt, cấu hình, nhập học liệu, kiểm thử, đào tạo nhân viên quản trị LMS; quy định số buổi, phạm vi một cơ sở, mốc máy chủ sẵn sàng, checklist nghiệm thu. **Không đồng nghĩa ba tháng cấp nhân sự vận hành hằng ngày không giới hạn.**
2. **Bảo hành 36 tháng từ ngày nghiệm thu:** sửa lỗi chức năng và lỗi an toàn thông tin phát sinh từ mã phần mềm thuộc phạm vi bàn giao; nêu kênh liên hệ và thời hạn phản hồi. Không bao gồm hư máy chủ, sự cố điện/mạng, cấu hình sai do bên thứ ba, phát triển chức năng mới, nhập hàng nghìn học viên, vận hành công việc hằng ngày.
3. **Vận hành trả phí nếu có:** giám sát dịch vụ, quản lý lớp/tài khoản theo ủy quyền, backup/khôi phục theo phương án hạ tầng, cập nhật, hỗ trợ quản trị, báo cáo, xử lý yêu cầu theo SLA; hạ tầng vẫn do trường trả tiền. **Phí 5 triệu là phí nhân sự/dịch vụ, KHÔNG bao gồm máy chủ**.
4. **Từ năm thứ tư**: thỏa thuận gia hạn bảo trì/nâng cấp/phụ trợ; phí vận hành đơn thuần không tự động biến thành bảo hành lỗi phần mềm vĩnh viễn.

**Mâu thuẫn cần Claude soi:** Bảo hành 36 tháng có bao gồm việc xử lý lỗ hổng mã nguồn và cập nhật tương thích thư viện bảo mật? Nếu không, rủi ro cho trường; nếu có, phải phân bổ đủ chi phí 3 năm. SLA bảo hành và SLA vận hành khác nhau.

### P1-D. G3/G4 đang giảm giá nhưng không đủ điều kiện kinh doanh

- **G2→G3: 350→330** là giảm 20 triệu. Phải ghi rõ G2 **bao gồm** đào tạo giảng viên nguồn, G3 **không gồm**. Đào tạo admin LMS vẫn có ở cả hai.
- **G3→G4: 330→320** giảm thêm 10 triệu, **chỉ khi** ký cam kết lớp/giờ/giá trị đào tạo tối thiểu và điều khoản xử lý nếu cam kết không thực hiện. “Quy mô lớn” không phải điều kiện kiểm toán được.
- Không được giới thiệu G3 rẻ hơn G2 về **tổng chi phí**: chi phí giảng viên thuê riêng có thể làm tổng cao hơn.
- Phí giảng viên phải tách **giờ dạy 60 phút hay tiết 45 phút**, sĩ số, kiểm tra đầu vào, lộ trình từ trình độ ban đầu đến B1, trợ giảng, địa điểm, đi lại, công tác, chấm thi, chi phí kiểm tra đầu ra. **Không bảo đảm một số giờ cố định đưa người mới bắt đầu tới B1** nếu chưa khảo sát đầu vào.
- Khi xây G4, nên đánh giá hiệu quả cam kết và khả năng triển khai thực tế; không chỉ lấy lợi ích là thêm doanh thu trên giấy.

### P1-E. Phí 5 triệu/tháng hoặc 54 triệu/năm: giá dễ hiểu nhưng phạm vi chưa đo được

`5 × 12 = 60` triệu; `54 / 60 = 90%`, tức giảm **10% đúng về toán học**.

Nhưng “tối đa 1.000 học viên đang theo học” chưa nói là:
- 1.000 tài khoản đã tạo, 1.000 tài khoản hoạt động trong tháng, hay 1.000 người dùng đồng thời?
- Một trường nhiều cơ sở có được dùng chung?
- Bao nhiêu giờ/ticket hỗ trợ một tháng? Thời gian phản hồi sự cố giờ hành chính ra sao? Có trực ngày nghỉ không?
- Backup lưu ở đâu và ai chi trả dung lượng?
- Có bao gồm nâng cấp phiên bản, nhập dữ liệu hàng loạt, huấn luyện giáo viên mới, hỗ trợ người dùng cuối không?

**Đề nghị:** giá niêm yết là gói **Basic remote (một cơ sở, giới hạn MAU/ticket/giờ)**; có bậc cao hơn theo người dùng, yêu cầu hoạt động và SLA. Con số giới hạn cụ thể cần tính từ logs và năng lực nhân sự, không tự khẳng định.

Đặc biệt tránh **thu phí vận hành từ ngày ký hợp đồng nếu cùng thời kỳ được cam kết hỗ trợ miễn phí 3 tháng**. Có thể chỉ bán từ tháng 4 hoặc nêu rõ phần hỗ trợ thêm ngoài phạm vi bàn giao.

### P1-F. Gói G1 cần định nghĩa kỹ cách tính tiền

- Một tài khoản tính tiền khi nào? Kích hoạt lần đầu, có đăng nhập, hay có phân công khóa trong tháng?
- Có thời gian mua tối thiểu, ví dụ theo học kỳ, và minimum order cho trường không?
- Nội dung đến B1 gồm một hay nhiều ngôn ngữ? Có kiểm tra nói bằng AI, chấm bài và học liệu video ở giá này không?
- Người dùng ngưng học/tạm khóa có được đổi người dùng khác và thời điểm nào?
- Nhà trường sở hữu dữ liệu học tập; quyền tải/xuất dữ liệu khi dừng hợp đồng; bảo mật tài khoản/giám sát truy cập?
- G1 có bao gồm đào tạo giảng viên hoặc người hỗ trợ lớp không? **Theo giả định hiện nay là KHÔNG**, cần nói rõ.

Gợi ý nghiên cứu thêm **khung doanh thu tối thiểu theo trường/học kỳ**, chiết khấu quy mô có điều kiện và chính sách trả trước; tất cả phải được kiểm tra với chi phí thực tế và không được ngầm thay đổi giá 100.000 đồng đã đưa ra.

### P1-G. Nội dung giáo dục và sở hữu trí tuệ

“Đầy đủ khóa học tới B1” không tự động đồng nghĩa:
- Học viên bất kể đầu vào sẽ đạt B1.
- Đơn vị cung cấp có quyền phát chứng chỉ B1 chính thức.
- Bao gồm mọi ngôn ngữ, mọi phiên bản học liệu và tài liệu có bản quyền từ đối tác.
- LMS được bàn giao **mã nguồn** và quyền bán lại hệ thống.

Cần một phụ lục `Danh mục nội dung (ngôn ngữ, A1/A2/B1, giờ tự học, giờ có hướng dẫn, ngân hàng câu hỏi, bài kiểm tra, cập nhật)`, cùng điều khoản `phạm vi giấy phép / sở hữu trí tuệ / chia sẻ dữ liệu người học`. Trường tự quản máy chủ nhưng bản quyền học liệu và dữ liệu người học là hai thứ khác nhau.

## 3. Hướng thương mại đề xuất để Claude so sánh

**Không sửa mức giá 100k / 350 / 330 / 320 / 5 / 54 cho đến khi Minmin quyết định.** Trước hết chuẩn hóa **đơn vị sản phẩm**.

| Phương án | Định nghĩa bộ học liệu mua trọn gói | Ưu điểm | Rủi ro |
|---|---|---|---|
| A – Quyền dùng phiên bản tại thời điểm mua | Một ngôn ngữ + một cơ sở; giấy phép nội bộ vĩnh viễn với **phiên bản đã bàn giao**; cập nhật lớn và cơ sở mới tính riêng | “Mua trọn bộ” dễ hiểu, ít tranh chấp | Cần thang giá theo quy mô và cơ chế kiểm soát sao chép; G1 dễ bị thay thế |
| B – License 3 năm | Một ngôn ngữ + một cơ sở + giới hạn học viên mới mỗi năm, gia hạn nếu dùng tiếp | Doanh thu định kỳ rõ; dễ cân đối nội dung, hỗ trợ | Không nên quảng cáo như mua đứt; có thể trường công lập thích quyền dùng dài hạn |
| C – Phí chuyển giao + phí học viên thấp hơn SaaS | Có khoản ban đầu để bù lắp đặt, thu thêm phí nội dung/học viên hoặc năm học | Phân phối rủi ro hợp lý, vẫn có dòng tiền lâu dài | Bảng giá phức tạp; cần cơ chế đếm người dùng và xử lý trường tự host |

**Khuyến nghị có điều kiện của ChatGPT:** Giữ A hoặc B làm cách định nghĩa G2–G4, còn C thành gói riêng **nếu** bài toán chi phí cho thấy cần. Với đối tượng trường công, đánh giá khả năng phân kỳ kinh phí. **Chưa quyết định A/B khi thiếu quy mô học viên dự kiến và chiến lược bản quyền.**

## 4. Claude cần phản biện độc lập những gì?

**Đề nghị Claude đọc file này, sau đó trả lời thành bảng: `Kết luận của ChatGPT | Đồng ý / Phản đối | Bằng chứng hoặc công thức | Giải pháp thay thế | Cần Minmin phê duyệt?`.**

Câu hỏi cụ thể:
1. Với **cùng một ngôn ngữ**, nếu quyền dùng học liệu G2–G4 là không giới hạn hay theo 300/500/1000 sinh viên/năm, cách nào là hợp lý? Đề xuất cách bảo vệ doanh thu mà **không khiến bảng giá gửi khách quá phức tạp**.
2. Tính **điểm ngang giá 1 năm và 3 năm** với ít nhất 3 giả định tháng sử dụng (6/9/12) và 3 mức quy mô (100/300/1000 SV); tách chi phí bên trường và doanh thu bên bán. Có nên bán G1 theo tháng hay theo học kỳ?
3. Sự khác biệt G2 350 – G3 330 – G4 320 có đủ rõ? Nên thêm/bớt gói nào để khách không chọn thấp nhất rồi yêu cầu quyền lợi cao nhất?
4. Đề xuất **phụ lục SLA và phân định RACI** (máy chủ, SSL, sao lưu, vận hành DB, cập nhật phần mềm, lỗi app, lỗi nội dung, bảo vệ dữ liệu) giữa trường và nhà cung cấp cho on-prem G2–G4.
5. Bảo hành 3 năm với 3 tháng triển khai: mô tả 1 câu ngắn làm sao không bị hiểu lầm về phí vận hành? Có bao gồm bản vá bảo mật và cập nhật thư viện bên thứ ba không?
6. Phí vận hành 5 triệu/tháng/54 triệu/năm có nên giữ mức niêm yết? Đề xuất giới hạn giờ/ticket/MAU/SLA khả thi, nhưng **không giả định giá vốn thật**.
7. G4 320 triệu nên có điều kiện doanh thu giảng dạy hoặc số lớp tối thiểu thế nào? Thiết kế điều khoản khi đối tác không đạt cam kết.
8. G1 100k/tháng nên thu theo số người kích hoạt hay tài khoản được cấp? Xây định nghĩa ngắn gọn để không tranh chấp.
9. Có cần hợp đồng ba bên/điều khoản dữ liệu học viên, các tiêu chuẩn nội dung, khả năng tích hợp LMS của trường và quyền lưu trữ học liệu không?
10. Chấm điểm 4 gói về **dễ bán – công bằng với trường – lợi nhuận bền vững – đơn giản vận hành**. Đề xuất 1 **bảng giá v2 dễ gửi khách, không nhắc tên thương hiệu**, và **một checklist nội bộ không đưa dữ liệu bí mật lên repo public**.

**Yêu cầu đầu ra:** 1) bác bỏ nếu thấy các phép so sánh sai; 2) khuyến nghị thay đổi có ưu/nhược rõ; 3) phiên bản giá v2 không tự đổi mức tiền khi chưa được duyệt; 4) danh mục câu hỏi cần Minmin phê duyệt, ưu tiên P0/P1.

**Ghi nhận trả lời:** Claude tạo `discussion/005-claude-phan-bien-bang-gia-ngoai-ngu-2026-10-17.md` và append phần tóm tắt kèm liên kết vào `discussion/001-kenh-trao-doi.md`. Commit bắt đầu bằng `[Claude]`. Không sửa báo giá/giá bán hay file T4/T5 trước khi có phê duyệt.

---
*Bản kiểm toán thương mại dựa trên giá/điều kiện do Minmin cung cấp trong hội thoại, không phải xác minh giá thị trường hoặc kết luận pháp lý. Tất cả chi phí hạ tầng giả lập chỉ nhằm kiểm tra độ nhạy.*
