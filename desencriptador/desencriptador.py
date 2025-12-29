from cryptography.fernet import fernet
import os

def retornar_key():
    return open("key.key", 'rb').read()

def desencriptador(items, key):
    i = fernet(key)
    for item in items:
        with open(item,'rb') as file:
            file_data = file.read()
        data =i.desencriptador(file_data)

        with open(item, 'wb') as file:
            file.write(data)

if __name__ == '__main__':
    path = "C:\\User\\JuanPerezMaldonado\\Downloads"
    os.remove(path+"\\"+"readme.txt")
    items  = os.listdir(path)
    archivos = [path+"\\"+x for x in items]

key = retornar_key()
desencriptador(archivos, key)