import cv2
import datetime

dt_now = datetime.datetime.now()
dataTime = str(dt_now.strftime('%Y-%m%d-%H%M'))

device_id = 0
cap = cv2.VideoCapture(device_id)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(str(dataTime) + '.avi',fourcc, 30.0, (640,480))

"""
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # ファイル形式(ここではmp4)
out = cv2.VideoWriter(str(dataTime) + '.mp4', fourcc, 30.0, (640,480)) # ライター作成
"""

while True:
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    if not ret:
        break  # 映像取得に失敗
    
    # write the flipped frame
    out.write(frame)
    
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # q キーを押したら終了する。

out.release()
cap.release()
cv2.destroyAllWindows()