import zmq
from utils.core import create_sub_socket, recv_message_sub

adrr = "tcp://localhost:5555"
topic = "data"

context, socket = create_sub_socket(adrr, topic)

try:
    while True:
        meassage = recv_message_sub(socket)
        print(f"Получено: {meassage}")

except KeyboardInterrupt:
    print("\nSubscriber остановлен")
    socket.close()
    context.term()