from cryptography.fernet import Fernet
import os
import sys

KEY_FILE = "key.key"

def retornar_key():
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def desencriptar(archivos, key):
    cipher = Fernet(key)
    for archivo in archivos:
        try:
            with open(archivo, 'rb') as f:
                datos_encriptados = f.read()
            datos = cipher.decrypt(datos_encriptados)
            with open(archivo, 'wb') as f:
                f.write(datos)
            print(f"Desencriptado: {archivo}")
        except Exception as e:
            print(f"Error al desencriptar {archivo}: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        path = input("Ingresa la ruta de la carpeta a desencriptar: ").strip()
    else:
        path = sys.argv[1]

    if not os.path.isdir(path):
        print(f"Error: la ruta '{path}' no existe o no es una carpeta.")
        sys.exit(1)

    if not os.path.exists(KEY_FILE):
        print(f"Error: no se encontró '{KEY_FILE}'. Sin la llave no es posible desencriptar.")
        sys.exit(1)

    readme_path = os.path.join(path, "readme.txt")
    if os.path.exists(readme_path):
        os.remove(readme_path)

    items = os.listdir(path)
    archivos = [os.path.join(path, x) for x in items if os.path.isfile(os.path.join(path, x))]

    key = retornar_key()
    desencriptar(archivos, key)

    print("\nDesencriptación completada.")
