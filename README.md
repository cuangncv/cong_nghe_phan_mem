# cong_nghe_phan_mem
Quản Lý PT (Quản lý phòng gym)
# Hướng dẫn cài đặt và sử dụng cơ sở dữ liệu với XAMPP

Tài liệu này sẽ hướng dẫn bạn cách thiết lập môi trường máy chủ cục bộ bằng XAMPP, tạo cơ sở dữ liệu và nhập dữ liệu từ file `.sql`.

---

## 1. Cài đặt XAMPP

Nếu bạn chưa có XAMPP, hãy làm theo các bước sau:

1.  **Tải XAMPP:**
    * Truy cập trang web chính thức của XAMPP: [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html)
    * Tải xuống phiên bản XAMPP phù hợp với hệ điều hành của bạn (Windows, macOS, Linux).

2.  **Cài đặt XAMPP:**
    * Chạy file cài đặt đã tải xuống.
    * Làm theo các hướng dẫn trên màn hình. Bạn có thể giữ các tùy chọn mặc định trong quá trình cài đặt.
    * Sau khi cài đặt xong, XAMPP Control Panel sẽ tự động khởi động hoặc bạn có thể tìm và mở nó.

3.  **Khởi động Apache và MySQL:**
    * Trong XAMPP Control Panel, hãy nhấp vào nút **"Start"** bên cạnh **"Apache"** và **"MySQL"**.
    * Đảm bảo rằng cả hai dịch vụ đều chạy thành công (màu xanh lá cây).

---

## 2. Tạo cơ sở dữ liệu `congnghe_phanmem`

Sau khi Apache và MySQL đã chạy, bạn có thể tạo cơ sở dữ liệu:

1.  **Mở phpMyAdmin:**
    * Mở trình duyệt web của bạn và truy cập địa chỉ: `http://localhost/phpmyadmin/`
    * Bạn sẽ thấy giao diện quản lý cơ sở dữ liệu phpMyAdmin.

2.  **Tạo cơ sở dữ liệu mới:**
    * Ở thanh bên trái của phpMyAdmin, nhấp vào **"Mới"** (hoặc "New").
    * Trong ô "Tên cơ sở dữ liệu", nhập: `congnghe_phanmem`
    * Đối với "Đối chiếu" (Collation), bạn có thể chọn `utf8mb4_unicode_ci` để hỗ trợ đầy đủ các ký tự, hoặc để mặc định nếu không có yêu cầu đặc biệt.
    * Nhấp vào nút **"Tạo"** (hoặc "Create").

    Bây giờ bạn đã có một cơ sở dữ liệu trống có tên `congnghe_phanmem`.

---

## 3. Nhập (Import) file `pt.sql`

Tiếp theo, chúng ta sẽ nhập dữ liệu từ file `pt.sql` vào cơ sở dữ liệu `congnghe_phanmem` vừa tạo.

1.  **Chọn cơ sở dữ liệu `congnghe_phanmem`:**
    * Trong phpMyAdmin, ở thanh bên trái, nhấp vào cơ sở dữ liệu **`congnghe_phanmem`** mà bạn vừa tạo.

2.  **Chuyển đến tab "Nhập" (Import):**
    * Ở khu vực chính của phpMyAdmin, nhấp vào tab **"Nhập"** (hoặc "Import").

3.  **Chọn file `pt.sql`:**
    * Trong phần "File cần nhập", nhấp vào nút **"Chọn tệp"** (hoặc "Choose File").
    * Tìm và chọn file `pt.sql` trên máy tính của bạn.
    * **Đảm bảo rằng file `pt.sql` này đã được đặt ở một vị trí dễ tìm, ví dụ: trong cùng thư mục với file `README.md` này hoặc một thư mục con của dự án.**

4.  **Thực hiện nhập:**
    * Kéo xuống dưới cùng của trang và nhấp vào nút **"Thực hiện"** (hoặc "Go").

    Nếu quá trình nhập thành công, bạn sẽ thấy thông báo xác nhận và bảng `pt` sẽ xuất hiện trong cơ sở dữ liệu `congnghe_phanmem` ở thanh bên trái.

---

## 4. Hoàn tất

Bây giờ bạn đã có cơ sở dữ liệu `congnghe_phanmem` với bảng `pt` đã được nhập dữ liệu, sẵn sàng để sử dụng cho dự án của bạn!

Nếu bạn gặp bất kỳ vấn đề nào, hãy kiểm tra lại các bước hoặc tham khảo tài liệu của XAMPP/phpMyAdmin.
