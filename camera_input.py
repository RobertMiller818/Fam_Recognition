import cv2

# Verify camera_index
# MAC == 1
# Raspberry Pi == ??
CAMERA_INDEX = 1

# https://opencv.org/reading-and-writing-videos-using-opencv/
# Review values for mp4v for width, heigth, size
cap = cv2.VideoCapture(CAMERA_INDEX)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)

if not cap.isOpened():
    print(f"Error: Could not access the camera at index {CAMERA_INDEX}.")
    exit()
else:
    print(f"Camera index {CAMERA_INDEX} opened successfully.")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, size)

print("Camera is now recording. Pres 'q' to stop.")


while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to read video frame.")
        # determine some additional logic
        break

    out.write(frame)

    cv2.imshow('Testing camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()

cv2.destroyAllWindows()
print("Video saved as output.mp4")