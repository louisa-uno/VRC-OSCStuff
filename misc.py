import psutil
import random
import time
from pythonosc.udp_client import SimpleUDPClient


def get_vrchat_port():
	for proc in psutil.process_iter(attrs=['pid', 'name']):
		try:
			if proc.info['name'] == 'VRChat.exe':
				for conn in psutil.Process(proc.info['pid']).connections():
					if 9000 <= conn.laddr.port < 10000:  # Check if the port is 4 digits and starts with 9
						return conn.laddr.port
		except (psutil.NoSuchProcess, psutil.AccessDenied,
		        psutil.ZombieProcess):
			pass
	print(
	    "You don't have VRChat running or you don't have VRChat's port set to a port between 9000 and 9999."
	)
	exit()


def load_client():
	global CLIENT
	CLIENT = SimpleUDPClient("127.0.0.1", get_vrchat_port())
	return CLIENT


def lerp(a, b, t):
	return a + t * (b - a)


def smooth_send_command(command, duration, z):
	j = random.random()
	fps = 144
	steps = int(duration * fps)
	for i in range(steps):
		t = i / steps  # t varies from 0 to 1 over the duration
		value = lerp(z, j, t)
		CLIENT.send_message(command, value)
		time.sleep(1 / fps)
	return j


def send_command(command, duration):
	CLIENT.send_message(command, 1)
	time.sleep(duration)
	CLIENT.send_message(command, 0)


def send_to_chatbox(text):
	CLIENT.send_message("/chatbox/input", (text, True, False))


def return_tall_string(text):
	while True:
		if len(text) < 144:
			text = "\v" + text
		else:
			break
	return text