# TÔ MÀU CHO ẢNH XÁM BẰNG CÔNG NGHỆ DEEP LEARNING
**Tóm tắt đề tài:** Tô màu cho ảnh xám được lựa chọn rộng rãi cho các nghiên cứu khác nhau về đồ hoạ và thị giác máy tính. Gần đây với sự thành công của mạng nơ-ron, đặc biệt là với các phương pháp học sâu, U-net rất quan trọng để tô màu cho hình ảnh thang màu xám, là kiến trúc chính cho đề tài nghiên cứu lần này. U-net là một loại mạng CNN bao gồm các phần down-sampling và up-sampling. Đầu vào của mạng này là ảnh xám với kích thước 128x128x1 và nó sẽ tạo ra ảnh màu RGB với kích thước 128x128x3. Loss function được dùng trong bài toán này là Mean Squared Error (MSE) để phân biệt chất lượng giữa ảnh dự đoán và ảnh thực.
## Dữ liệu:
Tập dữ liệu sử dụng ở đây là CelebA chứa khuôn mặt của những người nổi tiếng. Tập dữ liệu này khá lớn (202,599 ảnh) nhưng ta sẽ chỉ sử dụng 10,000 ảnh lưu trong thư mục **data_raw** để huấn luyện.

Tham khảo và tải về tập dữ liệu: https://www.kaggle.com/datasets/jessicali9530/celeba-dataset

## Xây dựng mô hình:

**Color_photo:**

	data_raw: resize ảnh thành 128x128 trước khi train
	data_resized: ảnh sau khi resize sẽ được lưu ở đây
	models: (Link tải model ở bên dưới)
		best: lưu giữ model tốt nhất sau khi train
		last: lưu giữ model sau khi train ở lần cuối
		history: lưu giữ file để đánh giá hàm loss
[Tải model ở đây](https://drive.google.com/drive/folders/1n4TGAN0KiZZ9aPNmJZzDrpd4UEKgzIOb?usp=sharing)

## Xây dựng giao diện người dùng bằng Tkinter:

**GUI:**

	gray_imgs: ảnh xám tải về được lưu ở đây
	color_imgs: ảnh sau khi được tô màu được lưu ở đây
	Tải model để test từ link ở bên dưới

[Tải model ở đây](https://drive.google.com/file/d/1iCFCXdMtK6RbF2Q4_m0IobNZVjKk7ESt/view?usp=sharing)	
