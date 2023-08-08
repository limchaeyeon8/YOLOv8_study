import cv2
import imagezmq

img_hub = imagezmq.ImageHub()   # ImageHub 클래스 initialize

while True:
    yeonpi, img = img_hub.recv_image()  # while True로 계속해서 이미지를 받아옴

    cv2.imshow(yeonpi, img) # imshow를 통해 받아온 이미지 출력
    if cv2.waitKey(1) == ord('q'):
        break

    img_hub.send_reply(b'ok')   # RPi로 ok라는 응답 보냄