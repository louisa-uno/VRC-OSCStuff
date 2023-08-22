import threading
import time

from pythonosc.udp_client import SimpleUDPClient

from misc import get_vrchat_port

CLIENT = SimpleUDPClient("127.0.0.1", get_vrchat_port())

textprint = input("Enter initial text to use in the chatbox: ")
print("Press Ctrl+C to stop the script.")
while True:
	if len(textprint) < 144:
		textprint = "\v" + textprint
	else:
		break


def listen_for_input():
	global textprint
	while True:
		try:
			textprint = input("Enter new text: ")
			while True:
				if len(textprint) < 144:
					textprint = "\v" + textprint
				else:
					break
		except EOFError:
			print("Input thread terminated.")
			break


input_thread = threading.Thread(target=listen_for_input)
input_thread.daemon = True
input_thread.start()

try:
	while True:
		CLIENT.send_message("/chatbox/input", (textprint, True, False))
		time.sleep(1.5)
except KeyboardInterrupt:
	print("KeyboardInterrupt has been caught.")
	time.sleep(1.5)
	CLIENT.send_message("/chatbox/input", ("", True, False))
