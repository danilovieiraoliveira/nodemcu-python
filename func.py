#Arquivo para colocar todas as funçoes criadas
import mfrc522

#Funcão que conecta na rede IoT
def do_connect():
	import network

	sta_if = network.WLAN(network.STA_IF)
	if not sta_if.isconnected():
		print('connecting to network...')
		sta_if.active(True)
		sta_if.connect('IoT', 'danielNaolembra123')
		while not sta_if.isconnected():
			pass

#Função que le o UID da tag
def do_read():
	uid_tag = "none"

	rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)


	(stat, tag_type) = rdr.request(rdr.REQIDL)

	if stat == rdr.OK:

		(stat, raw_uid) = rdr.anticoll()

		if stat == rdr.OK:

			uid_tag = str(raw_uid[0]) + str(raw_uid[1]) + str(raw_uid[2]) + str(raw_uid[3])

	return uid_tag

#Le o arquivo, monta a lista e a retorna
def do_arq():
	usr = []
	f = open('usr', 'r')

	for linha in f:
		usr.append(linha.replace('\n', '')) #Adiciona as tags lidas do arquivo e retira os \n no final das linhas

	f.close()

	return usr
