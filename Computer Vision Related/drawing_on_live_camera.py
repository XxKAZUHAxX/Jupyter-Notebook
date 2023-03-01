import cv2


##### CALLBACK FUNCTION FOR RECTANGLE #####
def draw_rectangle(event, x ,y ,flags,param):
    global pt1, pt2, top_left_clicked, bottom_right_clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        # RESET THE RECTANGLE (CHECKS IF RECTANGLE EXISTS)
        if top_left_clicked and bottom_right_clicked:
            pt1 = (0, 0)
            pt2 = (0, 0)
            top_left_clicked = False
            bottom_right_clicked = False

        if top_left_clicked == False:
            pt1 = (x, y)
            top_left_clicked = True

        elif bottom_right_clicked == False:
            pt2 = (x, y)
            bottom_right_clicked = True

##### GLOBAL VARIABLES #####
pt1 = (0, 0)
pt2 = (0, 0)
top_left_clicked = False
bottom_right_clicked = False

##### CONNECT TO THE CALLBACK #####
cap = cv2.VideoCapture(0)
cv2.namedWindow('Video')
cv2.setMouseCallback('Video', draw_rectangle)


while cap.isOpened():
    success, frame = cap.read()

    # DRAWING ON THE FRAME BASED OFF THE GLOBAL VARIABLES
    if top_left_clicked == True:
        cv2.circle(img=frame, center=pt1, radius=5, color=(0, 0, 255),thickness=-1)
    
    if top_left_clicked & bottom_right_clicked == True:
        cv2.rectangle(img=frame, pt1=pt1, pt2=pt2, color=(0,0,255), thickness=3)


    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
