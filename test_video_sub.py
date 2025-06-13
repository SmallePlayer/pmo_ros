import cv2
import zmq
import numpy as np
from utils.core import *

adrr = "tcp://localhost:5556"
topic = ""
context, socket = create_sub_socket(adrr, topic)

try:
    print("Клиент видеопотока запущен...")
    while True:
        frame = recv_frame_sub(socket)
        
        # Отображение кадра
        cv2.imshow('Subscriber', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
except KeyboardInterrupt:
    print("Клиент остановлен")
finally:
    cv2.destroyAllWindows()
    socket.close()
    context.term()