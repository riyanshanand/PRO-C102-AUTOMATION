import cv2
def takescreenshot():
    v = cv2.VideoCapture(0) 
    result = True 
    while(result): 
        ret,frame=v.read() 
        cv2.imwrite("a.jpg",frame) 
        result = False 
    v.release() 
    cv2.destroyAllWindows()

takescreenshot()