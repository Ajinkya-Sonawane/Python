# Run this script as Administrator
import time 
from datetime import datetime as dt 

hostsFilePath = "C:\\Windows\\System32\\drivers\\etc\\hosts"
# localhost's IP Address 
redirect_IP = "127.0.0.1"

# Websites that you want to block 
website_list =["www.facebook.com","facebook.com", 
		"www.gmail.com","gmail.com"] 

while True: 
	# time of your work 
	if dt(dt.now().year, dt.now().month, dt.now().day,8) \
	< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,21): 
		with open(hostsFilePath, 'r+') as file: 
			content = file.read() 
			for website in website_list: 
				if website in content: 
					pass
				else: 
					# Mapping hostnames to be blocked to your localhost IP address 
					file.write(redirect_IP + " " + website + "\n") 
					print("Access Denied...") 
	else: 
		with open(hostsFilePath, 'r+') as file: 
			content=file.readlines() 
			file.seek(0) 
			for line in content: 
				if not any(website in line for website in website_list): 
					file.write(line) 
			# Removing hostnmes from hosts file 
			file.truncate() 
		print("Access Granted...") 
	time.sleep(5) 

