import multiprocessing as mp
from tkinter import N
import cv2, sys

cameras = ["rtsp://user:password@ip:554",\
            "rtsp://user:password@ip:554", "rtsp://user:password@ip:554",\
                "rtsp://user:password@ip:554", "rtsp://user:password@ip:554"]

class camMp(mp.Process):

    def __init__(self, previewName, camID):
        mp.Process.__init__(self)
        self.previewName = previewName
        self.camID = camID
        
    def run(self):
        print ("Starting " + self.previewName)
        capture_frames(self.previewName, self.camID)

def capture_frames(previewName, camID):
    
    capture = cv2.VideoCapture(camID)

    while (capture.isOpened()):       
        status, frame = capture.read()
        
        if not status:
            break
        else:
            frame_rz = cv2.resize(frame, (640,480))
            cv2.imshow(previewName, frame_rz)
            
            if cv2.waitKey(1) == 27: #27 - Esc
                sys.exit()

    capture.release()
    cv2.destroyAllWindows()

def main():
    count_line = len(cameras)
    print(count_line)
    i = 0
    while i < count_line:
        capture_process = camMp(f"Camera {i}: " + cameras[i], cameras[i])
        capture_process.start()
        i = i + 1

if __name__ == '__main__':
    main()

        