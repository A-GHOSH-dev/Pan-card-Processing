import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('panimage.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img, lang ="eng+hin"))
#print(pytesseract.image_to_boxes(img, lang ="eng+hin"))
hImg,wImg,_ = img.shape 
# cong=r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img, lang ="eng+hin", config=cong)
boxes = pytesseract.image_to_boxes(img, lang ="eng+hin") 
for b in boxes.splitlines(): 
    #print(b) 
    b = b.split(' ') 
    #print(b) 
    x,y,w,h= int(b[1]), int(b[2]),int(b[3]),int(b[4]) 
    cv2.rectangle(img, (x,hImg-y), (w,hImg-h), (0,0,255), 3)
    cv2.putText(img, b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

boxes = pytesseract.image_to_data(img, lang ="eng+hin") 
for x,b in enumerate(boxes.splitlines()): 
    if x!=0: 
        b = b.split(' ') 
        #print(b) 
        if len(b)==12:
            x,y,w,h= int(b[6]), int(b[7]),int(b[8]),int(b[9]) 
            cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255), 3)
            cv2.putText(img, b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)



imgwindow = 'Result'
cv2.namedWindow(imgwindow, cv2.WINDOW_NORMAL)
#cv2.setWindowProperty(imgwindow, cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_CAP_PROP_FORMAT)
cv2.setWindowProperty(imgwindow, cv2.WINDOW_NORMAL, cv2.WND_PROP_FULLSCREEN)
cv2.imshow(imgwindow,img)
cv2.waitKey(0)
