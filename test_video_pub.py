import cv2
import zmq
import numpy as np
from utils.core import *  # Импорт всего из utils


# Инициализация камеры
cap = cv2.VideoCapture(0)  # 0 - индекс камеры по умолчанию

adrr = "tcp://*:5556"
context, socket = create_pub_socket(adrr)

try:
    print("Сервер видеопотока запущен...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        send_frame_pub(socket, frame)
        
        # Для отладки: показ FPS
        cv2.imshow('Publisher', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
except KeyboardInterrupt:
    print("Сервер остановлен")
finally:
    cap.release()
    cv2.destroyAllWindows()
    socket.close()
    context.term()