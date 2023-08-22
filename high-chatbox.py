import time

from pythonosc.udp_client import SimpleUDPClient

from misc import get_vrchat_port

CLIENT = SimpleUDPClient("127.0.0.1", get_vrchat_port())

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
	time.sleep(1.5)
	CLIENT.send_message("/chatbox/input", ("", True, False))