import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# WINDOWS -- *'DIVX'
# MACOS & LINUX -- *'XVID'
writer = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))

while cap.isOpened():
    success, frame = cap.read()

    writer.write(frame)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows
