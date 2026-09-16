from pathlib import Path

import cv2

image_path = Path(__file__).with_name("task3.jpg")
ksize = (5, 5)
sigmax = 0
img = cv2.imread(str(image_path))
if img is None:
    print("Error: Could not read the image.")
    exit()  
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, ksize, sigmax)
canny_edges = cv2.Canny(img_blur, 100, 200)
contours,hierarchy= cv2.findContours(canny_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
triangle_count = 0
square_count = 0
circle_count = 0
rectangle_count = 0
for contour in contours:
    arc_length = cv2.arcLength(contour, True)
    if cv2.contourArea(contour) < 400:
        continue
    approx_contour = cv2.approxPolyDP(contour, 0.035 * arc_length, True)
    vertex_count = len(approx_contour)

    if vertex_count == 3:
        shape="Triangle"
        triangle_count += 1
    elif vertex_count == 4:
        x, y, w, h = cv2.boundingRect(approx_contour)
        if 0.95 <= (w / h) <= 1.05:
            shape="Square"
            square_count += 1
        else:
            shape="Rectangle"
            rectangle_count += 1
    else:
        shape="Circle"
        circle_count += 1
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        cv2.putText(img, shape, (cx - 20, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.drawContours(img, [contour], 0, (0, 255, 0), 2)

print(f"Triangles: {triangle_count}")
print(f"Squares: {square_count}")
print(f"Rectangles: {rectangle_count}")
print(f"Circles: {circle_count}")

cv2.imshow("Detected Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
