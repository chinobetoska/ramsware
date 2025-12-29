# ramsware
Se deberan instalar las siguientes librerias para el uso correcto del los archivos 

1- Instalar las siguientes librerias  
    1- cryptography
    2- os
 Para seguridad de tus archivos de py3 se debera hacer un entorno especial para las librerias que se usan y no se corrompa las principales, el entorno se hara con los siguintes comandos en linux:
    python3 -m venv "nombre de tu entorno"
    "nombre de tu entorno"/bin/activate

 Las librerias se instalan con:
    pip install cryptography
    pip install os          (esta ya esta instalada por defecto asi que es decision tuya si la instalas o no)
 
 2- para ejecutar el archivo se requiere el usu de la terminal y se hace de la siguinte manera 
     Para activar el ramsonware:
     python "ruta donde el archivo este alojado"ramsware.py
     (este programa creara un archivo key.key si se llagara a eliminar este se volveria dificil de desenencriptar TENER EXTREMA PRECAUCION AL TRABAJAR CON EL)
     Para desifrar los archivos:
     python "ruta donde el archivo este alojado"desencriptador.py
     