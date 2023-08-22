import threading
import time

import misc

CLIENT = misc.load_client()

textprint = misc.return_tall_string(
    input("Enter initial text to use in the chatbox: "))
print("Press Ctrl+C to stop the script.")


def listen_for_input():
	global textprint
	while True:
		try:
			textprint = misc.return_tall_string(input("Enter new text: "))
		except EOFError:
			print("Input thread terminated.")
			break


input_thread = threading.Thread(target=listen_for_input)
input_thread.daemon = True
input_thread.start()

try:
	while True:
		misc.send_to_chatbox(textprint)
		time.sleep(1.5)
except KeyboardInterrupt:
	print("KeyboardInterrupt has been caught.")
	time.sleep(1.5)
	misc.send_to_chatbox(textprint)
