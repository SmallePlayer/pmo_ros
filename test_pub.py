import zmq
import time
from utils.core import create_pub_socket, send_message_pub

adrr = "tcp://*:5555"
topic = "data"

context, socket = create_pub_socket(adrr)

counter = 0
try:
    while True:
        counter += 1
        # Отправляем сообщение с темой "data" и значением counter
        send_message_pub(socket, topic, counter)
        print(f"Отправлено: {counter}")
        time.sleep(1)  # Пауза 1 сек

except KeyboardInterrupt:
    print("\nPublisher остановлен")
    socket.close()
    context.term()