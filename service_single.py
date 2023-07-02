import os
import paramiko
import shutil
from dotenv import load_dotenv
load_dotenv()

SERVER_BOOK_DIRECTORY = os.getenv("SERVER_BOOK_DIRECTORY")
LOCAL_DIRECTORY = os.getenv("LOCAL_DIRECTORY")
SERVER_HOST = os.getenv("SERVER_HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

def copiar_archivos_servidor_a_pc(directorio_servidor, directorio_local, servidor, usuario, contraseña):
    # Crear una instancia de cliente SSH
    cliente_ssh = paramiko.SSHClient()
    cliente_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conectarse al servidor Linux
        cliente_ssh.connect(servidor, username=usuario, password=contraseña)

        # Crear una instancia de SFTP
        sftp = cliente_ssh.open_sftp()

        # Listar los archivos en el directorio del servidor
        archivos = sftp.listdir(directorio_servidor)

        # Copiar cada archivo a la PC con Windows
        for archivo in archivos:
            archivo_servidor = os.path.join(directorio_servidor, archivo)
            archivo_local = os.path.join(directorio_local, archivo)
            sftp.get(archivo_servidor, archivo_local)

        print("Copia de archivos completada exitosamente.")

    except Exception as e:
        print(f"Error al copiar archivos: {str(e)}")

    finally:
        # Cerrar la conexión SSH y SFTP
        if sftp:
            sftp.close()
        if cliente_ssh:
            cliente_ssh.close()

copiar_archivos_servidor_a_pc(SERVER_BOOK_DIRECTORY, LOCAL_DIRECTORY, SERVER_HOST, USER, PASSWORD)
