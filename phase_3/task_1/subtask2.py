from pathlib import Path

import cv2
import numpy as np


class ShapeDetector:
    def __init__(self, video_path):
        self.video_path = video_path
        self.lower_red1 = np.array([0, 100, 100])
        self.upper_red1 = np.array([10, 255, 255])
        self.lower_red2 = np.array([170, 100, 100])
        self.upper_red2 = np.array([180, 255, 255])
        self.lower_blue = np.array([100, 150, 0])
        self.upper_blue = np.array([140, 255, 255])

    def video_frames_detector(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("Error: Could not open video.")
            return
        ret, frame = cap.read()
        while ret:
           
            img_blur = cv2.GaussianBlur(frame, (5, 5), 0)
            img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)
            red_mask1 = cv2.inRange(img_hsv, self.lower_red1, self.upper_red1)
            red_mask2 = cv2.inRange(img_hsv, self.lower_red2, self.upper_red2)
            red_mask = cv2.bitwise_or(red_mask1, red_mask2)
            blue_mask = cv2.inRange(img_hsv, self.lower_blue, self.upper_blue)

            self.detect_redcircles(red_mask, frame)
            self.detect_bluesquares(blue_mask, frame)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
            ret, frame = cap.read()

        cap.release()
        cv2.destroyAllWindows()

    def detect_redcircles(self, mask, frame):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            arc_length = cv2.arcLength(contour, True)
            if cv2.contourArea(contour) < 400:
                continue
            approx_contour = cv2.approxPolyDP(contour, 0.035 * arc_length, True)
            vertex_count = len(approx_contour)
            if vertex_count > 4:
                shape = "Circle"
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    cv2.putText(frame, shape, (cx - 20, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                cv2.drawContours(frame, [contour], 0, (0, 255, 0),2)

    def detect_bluesquares(self, mask, frame):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            arc_length = cv2.arcLength(contour, True)
            if cv2.contourArea(contour) < 400:
                continue
            approx_contour = cv2.approxPolyDP(contour, 0.03 * arc_length, True)
            vertex_count = len(approx_contour)
            if vertex_count == 4:
                x, y, w, h = cv2.boundingRect(approx_contour)
                if 0.95 <= (w / h) <= 1.05:
                    shape = "Square"
                    M = cv2.moments(contour)
                    if M["m00"] != 0:
                        cx = int(M["m10"] / M["m00"])
                        cy = int(M["m01"] / M["m00"])
                        cv2.putText(frame, shape, (cx - 20, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                    cv2.drawContours(frame, [contour], 0, (0, 255, 0), 2)

if __name__ == "__main__":
    video_path = Path(__file__).with_name("task2.mp4")
    shape_detector = ShapeDetector(video_path)
    shape_detector.video_frames_detector()