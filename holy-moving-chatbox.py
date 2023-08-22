import threading
import time

import misc

CLIENT = misc.load_client()

file_path = 'bible.txt'  # Replace with your desired file path
with open(file_path, 'r', encoding='utf-8') as file:
	text = file.read().replace('\n', '\v')

current_char = 0
z = 0
chatbox = input("Do you want to use chatbox osc? (y/n) ")
chatbox = True if chatbox == "y" else False
movements = input("Do you want to use movements osc? (y/n) ")
movements = True if movements == "y" else False
eyes = input("Do you want to use eyes osc? (y/n) ")
eyes = True if eyes == "y" else False

print("Press Ctrl+C to stop the script.")

try:
	while True:
		textprint = "ʜᴏʟʏ ᴍᴏᴠɪɴɢ ᴄʜᴀᴛʙᴏx\v"
		stringprint = text[current_char:current_char + 144 - len(textprint)]
		current_char += 144 - len(textprint)
		print("ʜᴏʟʏ ᴍᴏᴠɪɴɢ ᴄʜᴀᴛʙᴏx: ", stringprint)

		multiplier = 0.05
		capital_multiplier = multiplier * 2

		move_forward = stringprint.count('w') * multiplier + stringprint.count(
		    'W') * capital_multiplier
		move_backward = stringprint.count(
		    's') * multiplier + stringprint.count('S') * capital_multiplier
		move_left = stringprint.count('a') * multiplier + stringprint.count(
		    'A') * capital_multiplier
		move_right = stringprint.count('d') * multiplier + stringprint.count(
		    'D') * capital_multiplier

		sleep_time = max(move_forward, move_backward, move_left, move_right)
		sleep_time = 1.5 if sleep_time < 1.5 else sleep_time

		if chatbox:
			misc.send_to_chatbox(textprint + stringprint)
			CLIENT.send_message("/chatbox/typing", False)
		if movements:
			threading.Thread(target=misc.send_command,
			                 args=("/input/MoveForward",
			                       move_forward)).start()
			threading.Thread(target=misc.send_command,
			                 args=("/input/MoveBackward",
			                       move_backward)).start()
			threading.Thread(target=misc.send_command,
			                 args=("/input/MoveLeft", move_left)).start()
			threading.Thread(target=misc.send_command,
			                 args=("/input/MoveRight", move_right)).start()
		if eyes:
			z = misc.smooth_send_command("/tracking/eye/EyesClosedAmount",
			                             sleep_time, z)
		else:
			time.sleep(sleep_time)
except KeyboardInterrupt:
	print("KeyboardInterrupt has been caught.")
	CLIENT.send_message("/input/MoveForward", 0)
	CLIENT.send_message("/input/MoveBackward", 0)
	CLIENT.send_message("/input/MoveLeft", 0)
	CLIENT.send_message("/input/MoveRight", 0)
	time.sleep(1.5)
	misc.send_to_chatbox("")