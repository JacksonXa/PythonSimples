import os

# Consultando funcionalidades do modulo OS

# 1 - Retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos
print(os.listdir())

# 3 - Versao do SO
os.system('ver')

# 4 - Configuracoes da maquina
os.system('systeminfo')

# 5 - Limpar a tela do terminal
os.system('cls')

# 6 - Desligar o computador
# os.system('shutdown /s')
os.system('shutdown /a') # Cancela o desligamento

def turn_off_one_hour():
    os.system('Shutdown /s /t /3600') #Desliga o PC em 1hr

def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800') #Desliga o PC em meia hr

def cancel_shutdown():
    os.system('shutdown /a') #Cancela desligamento do PC

