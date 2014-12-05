





Nếu bạn vào từ trình duyệt localhost:5000/signup

thì sẽ có một form cho bạn signup, ở đấy sẽ dùng js để gọi lên server để tạo một session_id

rồi sau đó sẽ gen ra file signup.html

Có một trường ẩn cert_key được tạo ra là do server truyền key xuống client.


Nếu dùng tools để signup tự động thì ghi đọc ra chỉ được file có nội dung js mà không có mã

html.

Vì thường chỉ có các browser hỗ trợ đọc js để thực hiện hàm



