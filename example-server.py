import zmq
import random
import sys
import time as tm
import json
import datetime as dt


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:1234")


while True:
    
    print("Sending...")
    #
    # Time string
    #
    time = dt.datetime.now(dt.timezone.utc)
    time_string = time.strftime("%Y%m%d_%H%M%S")

    #
    # Trigger Message
    #
    message = {
        "message_type": "trigger",
        "time": time_string
    }

    message = json.dumps(message, indent=4, sort_keys=True, default=str)
    socket.send_string(message)


    #
    # Simulate Delay
    #
    tm.sleep(1)