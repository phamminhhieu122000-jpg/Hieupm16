import cv2

# Mở camera
cap = cv2.VideoCapture(0)

# Đọc frame đầu tiên
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Tính sự khác biệt giữa 2 frame
    diff = cv2.absdiff(frame1, frame2)

    # Chuyển sang grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Làm mờ để giảm nhiễu
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Nhị phân hóa (threshold)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Làm dày vùng trắng (giúp detect tốt hơn)
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Tìm contour (vùng chuyển động)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Bỏ qua vùng nhỏ (noise)
        if cv2.contourArea(contour) < 1000:
            continue

        # Vẽ bounding box
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(frame1, "Motion Detected",
                    (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)

    # Hiển thị
    cv2.imshow("Camera", frame1)
    cv2.imshow("Diff", diff)
    cv2.imshow("Threshold", thresh)

    # Cập nhật frame
    frame1 = frame2
    ret, frame2 = cap.read()

    # Nhấn q để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
