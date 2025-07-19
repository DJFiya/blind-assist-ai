# Camera Implementation

import cv2

def capture_frame(save_path: str = None):
    """
    Capture a single frame from the default camera.
    Returns the raw OpenCV image (numpy array).
    """
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        raise RuntimeError("Unable to open camera")

    ret, frame = cam.read()
    cam.release()

    if not ret or frame is None:
        raise RuntimeError("Failed to capture frame")

    if save_path:
        cv2.imwrite(save_path, frame)

    return frame

if __name__ == "__main__":
    # Quick test
    img = capture_frame(save_path="test_frame.jpg")
    print("Captured frame saved to test_frame.jpg")
