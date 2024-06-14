import zmq
import json

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, "")

print("Connecting...")
socket.connect ("tcp://localhost:1234")

while True:
    print("Waiting for Message...")
    msg = socket.recv_string()

    json_msg = json.loads(msg)

    print(json_msg)