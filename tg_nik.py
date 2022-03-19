
from telethon.sync import TelegramClient
from telethon import functions, types
import time

try:
	file = open("names.txt", 'r')
	pause = input('Введите паузу между сменой ников в секундах. Для бесконечной работы требуется пауза минимум 36 сек, т.к. в телеграме возможна смена ника только 100 раз в час.\n\nПауза - ')
	all_names = list()
	for line in file.readlines():
		all_names.extend(line.rstrip().split(' '))

	while True:
		for name in all_names:
			with TelegramClient('session', '1042789', '990edf4ef84e4b10892d9af908ba5d9e') as client:
				client(functions.account.UpdateProfileRequest(first_name=str(name)))
			print('Имя изменено на ' + name)
			time.sleep(int(pause))
except Exception as e:
	print('Ошибка -', e)
	wait = input('Нажмите ENTER для завершения:')
