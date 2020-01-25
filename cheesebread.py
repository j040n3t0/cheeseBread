# -*- coding:utf-8 -*-

import os, time

while True:
	try:
		print("\n\n[*] Fazendo download da planilha...")
		os.system("curl -s 'https://docs.google.com/spreadsheets/d/1ccBo1KdDbjzUyx3e9zQvldEL2fUqQYqIeWuh2Z62Yh4/export?exportFormat=csv' > a.csv")
		print("[*] Atualizando os dados...")
		difference = os.popen("grep -v -f temp.csv a.csv").read()
		if difference:
			print("[*] Essa é a diferença ==> " + difference)
			print("[!] Essa diferença será enviada para o ELASTIC!!\n")
			print("[*] Atualizando o arquivo local")
			os.system("cat a.csv > temp.csv")
		else:
			print("[*] Sem dados para atualizar aqui!")
		time.sleep(15)
	except KeyboardInterrupt:
		print("\n[*] Apertou CTRL+C que eu sei! ;)\n\n")
		break

