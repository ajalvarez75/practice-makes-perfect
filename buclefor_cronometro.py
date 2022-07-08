import os
import time

for hora in range(0,24):
	os.system("cls")
	for minutos in range(0,60):
		os.system("cls")
		for segundos in range(0,60):
			os.system("cls")
			print(f'{hora}:{minutos}:{segundos}')
			time.sleep(1)
			os.system("cls")