# 🎥 Motion Detection with OpenCV (Python)

## 📌 Giới thiệu

Dự án này xây dựng một hệ thống **phát hiện chuyển động (motion detection)** sử dụng webcam laptop và thư viện OpenCV trong Python.

Chương trình hoạt động bằng cách:

* So sánh **2 frame liên tiếp**
* Tìm sự khác biệt giữa các pixel
* Xác định vùng có chuyển động
* Vẽ bounding box xung quanh vùng đó

👉 Đây là kỹ thuật cơ bản trong computer vision, được dùng trong:

* Camera an ninh
* Giám sát chuyển động
* Tracking object cơ bản ([Reintech][1])

---

## 🚀 Demo chức năng

* Hiển thị camera realtime
* Highlight vùng chuyển động
* Loại bỏ nhiễu nhỏ
* Hiển thị nhiều cửa sổ debug:

  * Camera
  * Difference
  * Threshold

---

## ⚙️ Cài đặt

### 1. Clone project

```bash
git clone https://github.com/phamminhhieu122000-jpg/Hieupm16.git
cd Hieupm16
```

---

### 2. Tạo môi trường ảo (khuyến khích)

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Cài thư viện

```bash
pip install opencv-python
```

---

## ▶️ Cách chạy

```bash
python3 motion.py
```

👉 Nhấn `q` để thoát

---

## 🧠 Nguyên lý hoạt động (rất quan trọng)

### 1. Đọc video từ camera

```python
cap = cv2.VideoCapture(0)
```

---

### 2. So sánh 2 frame

```python
diff = cv2.absdiff(frame1, frame2)
```

👉 Hàm này tính độ khác biệt pixel giữa 2 ảnh ([codegenes][2])

---

### 3. Chuyển grayscale

```python
gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
```

👉 Giảm dữ liệu → xử lý nhanh hơn

---

### 4. Blur (lọc nhiễu)

```python
blur = cv2.GaussianBlur(gray, (5, 5), 0)
```

---

### 5. Threshold (nhị phân hóa)

```python
_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
```

👉 Pixel thay đổi → màu trắng
👉 Pixel không đổi → màu đen

---

### 6. Dilate (làm dày vùng chuyển động)

```python
dilated = cv2.dilate(thresh, None, iterations=3)
```

---

### 7. Tìm contour

```python
contours, _ = cv2.findContours(...)
```

👉 Contour = vùng có chuyển động ([Delft Stack][3])

---

### 8. Lọc nhiễu

```python
if cv2.contourArea(contour) < 1000:
    continue
```

👉 Loại bỏ chuyển động nhỏ (noise)

---

### 9. Vẽ bounding box

```python
cv2.rectangle(...)
```

---

## 📂 Cấu trúc project

```
Hieupm16/
│── motion.py
│── README.md
│── .gitignore
│── requirements.txt (optional)
```

---

## ⚠️ Lỗi thường gặp

### ❌ Không mở được camera

```python
cv2.VideoCapture(1)
```

---

### ❌ Bị nhiễu (detect sai)

👉 Tăng threshold:

```python
threshold = 30
```

👉 Hoặc tăng diện tích:

```python
contourArea > 2000
```

---

### ❌ Lag

👉 Resize frame:

```python
frame = cv2.resize(frame, (640, 480))
```

---

## 🔥 Nâng cấp dự án

Bạn có thể phát triển thêm:

### 1. 📸 Chụp ảnh khi có chuyển động

```python
cv2.imwrite("capture.jpg", frame)
```

---

### 2. 🔔 Cảnh báo âm thanh

---

### 3. 🎥 Ghi video khi detect

---

### 4. 🤖 Kết hợp AI (YOLO)

* Detect người
* Detect điện thoại

---

### 5. 📲 Gửi cảnh báo Telegram

---

## 🧪 Tối ưu & cải tiến

Một số vấn đề thực tế:

* ánh sáng thay đổi gây nhiễu
* camera rung
* chuyển động nhỏ bị bỏ qua

👉 Có thể cải thiện bằng:

* adaptive threshold
* background subtraction
* tracking object

---

#* Xử lý ảnh cơ bản
* Computer Vision
* Làm việc với video stream
* OpenCV pipeline

---

## 👨‍💻 Tác giả

* GitHub: https://github.com/phamminhhieu122000-jpg
