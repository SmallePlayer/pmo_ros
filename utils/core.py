import zmq
import time
import cv2
import numpy as np

def create_pub_socket(address: str):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(address)
    time.sleep(1)
    return context, socket

def create_sub_socket(address: str, topic_filter: str = ""):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(address)
    socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)
    return context, socket

def send_message_pub(socket, topic: str, message: str):
    message = f"{topic} {message}"
    socket.send_string(message)

def recv_message_sub(socket):
    recv_message = socket.recv_string() 
    topic, message = recv_message.split()
    return message

def send_frame_pub(socket, frame):
    _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
    socket.send(buffer.tobytes())

def recv_frame_sub(socket):
    buffer = socket.recv()
    nparr = np.frombuffer(buffer, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)