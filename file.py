import re
import psutil
import platform
from time import sleep
from datetime import datetime


bat = psutil.sensors_battery()
now = datetime.now()

print(int(bat[0]), end='')
print('%', end='')

if not bat.power_plugged:
	print('' +  ' >>>', end='\n')
else:
	print(' <<< ' + '', end='\n')	
	

print(f'{now.hour}:{now.minute}', end=' ')

release = platform.release()
release = (re.findall('[a-z]+', release))
print(f'{release[0].title()} {platform.system()}', end=' ') 
print(f'{now.day}/{now.month}/{now.year}')
