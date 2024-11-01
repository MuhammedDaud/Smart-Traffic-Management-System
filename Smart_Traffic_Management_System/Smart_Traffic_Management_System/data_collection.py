# Data Collection Script
import cv2
import time

def collect_data():
    # Initialize camera
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Save frame for later processing
        cv2.imwrite('data/frame_{}.jpg'.format(int(time.time())), frame)
        time.sleep(1)  # Adjust the delay as needed
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    collect_data()