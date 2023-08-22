import psutil


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