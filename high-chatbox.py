from pythonosc.udp_client import SimpleUDPClient
import time
import threading
import random

CLIENT = SimpleUDPClient("127.0.0.1",
                         int(input("Enter OSC port (default is 9000): ")))

try:
	textprint = input("Enter text to use in the chatbox: ")
	while True:
		i = len(textprint)
		textprint = "\v" + textprint
		if len(textprint) >= 144:
			break

	while True:
		CLIENT.send_message("/chatbox/input", (textprint, True, False))
		time.sleep(1.5)
except KeyboardInterrupt:
	print("KeyboardInterrupt has been caught.")
