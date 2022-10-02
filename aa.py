import os
import datetime
import cv2
import sys
import fileinput
global_path = sys.stdin.read().rstrip() 
print (sys.argv)
def with_opencv(filename):
    data = cv2.VideoCapture(str(filename))
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = int (data.get(cv2.CAP_PROP_FPS))
    if(fps):
        duration = int (frames / fps / 60)
    else:
        duration = 0
#    duration = str (datetime.timedelta(seconds = seconds))
#    print('file length: '+ str(duration))
    return duration

time =0;
for filename in os.listdir():
    if(filename[-3:]=='mp4'):
        time = time+int(with_opencv(str(global_path)+'/'+filename))

print(str(time)+'min');
