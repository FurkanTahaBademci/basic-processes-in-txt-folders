import cv2
from datetime import datetime

from cv2 import resize 

#cap= cv2.VideoCapture(0) # KAMERA BİLGİSİ
numara = 11000                # İLK NUMARA BAŞLANGICI


dosya_yolu = "C:\\Users\\90551\\Desktop\\plaka_veri\\trafik3\\"
video_yolu = "C:\\Users\\90551\\Desktop\\plaka_veri\\video3.mp4"

cap = cv2.VideoCapture(video_yolu)

while True:
    
    ret, frame = cap.read()   
    frame_copy = frame.copy()
    frame_copy = resize(frame_copy, (640,480))
    #frame = cv2.flip(frame,1)
    
    cv2.imshow("Webcam Live", frame_copy)    # FRAME VE İSİMİ 
    a = cv2.waitKey(30)                
 
    if a == ord("q")or a == ord("Q"):               # DÖNGÜYÜ KIR 
        break

         
    if  a == ord("s") or a == ord("S"):                                 # İF İ ÇALIŞTIR S
        tarih = datetime.now().strftime("%H__%M__%S")      # TARİH SAAT BİLGİSİ ANLIK 
        cv2.imwrite(f'{dosya_yolu}\\resim_{tarih}_{numara}.jpg', frame)

           # RESMİ KAYDETME   KONUMU    İSİMLENDIRMESİ  VE SONUNA KAYDEDECEĞİ KARE 
        
        print(f'Resim Kaydedildi{numara}')
        numara +=1
       

  
cap.release()
cv2.destroyAllWindows()