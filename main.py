import func
from machine import lightsleep

print("\n" + "Bem vindo ao NodeMcu")
print('')

func.do_connect() #Conecta no WiFi

tag = ''
usr = func.do_arq()

print('\n')

print('Aguardando a Tag:')

while True:
	try:
		tag = func.do_read()# Chama a função que le tag

		if (tag in usr): #Checa se a tag lida esta entre as tags cadastradas
			print('Porta aberta pela tag: ' + tag)

	except KeyboardInterrupt:
		print("Stop while True")
		break

	lightsleep(1 * 1000)
