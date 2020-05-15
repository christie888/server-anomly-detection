import cv2
import numpy as np

def find_rect_of_target_color(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    mask = np.zeros(h.shape, dtype=np.uint8)
    mask[((h > 0) | (h < 43)) & (s > 128)] = 255
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rects = []
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)
        rects.append(np.array(rect))
    return rects
    

if __name__ == "__main__":
    capture = cv2.VideoCapture(0)
    while cv2.waitKey(30) < 0:
        ret, frame = capture.read()
        rects = find_rect_of_target_color(frame)
        if len(rects) > 0:
            rect = max(rects, key=(lambda x: x[2] * x[3]))
            cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (0, 0, 255), thickness=2)
            cv2.putText(frame, 'error', (np.array(rect)[0], np.array(rect)[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (0, 0, 255), 2)
        cv2.imshow('red', frame)
    capture.release()
    cv2.destroyAllWindows()