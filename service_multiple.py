import os
import paramiko
import stat
from dotenv import load_dotenv
load_dotenv()

SERVER_DIRECTORY = os.getenv("SERVER_DIRECTORY")
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

        # Llamada a la función recursiva para copiar los archivos
        copiar_recursivo(sftp, directorio_servidor, directorio_local)

        print("Copia de archivos completada exitosamente.")

    except Exception as e:
        print(f"Error al copiar archivos: {str(e)}")

    finally:
        # Cerrar la conexión SSH y SFTP
        if sftp:
            sftp.close()
        if cliente_ssh:
            cliente_ssh.close()

def copiar_recursivo(sftp, directorio_remoto, directorio_local):
    
    try:
        elementos_remotos = sftp.listdir(directorio_remoto)
		
        for elemento in elementos_remotos:
            ruta_remota = os.path.join(directorio_remoto, elemento)
            ruta_local = os.path.join(directorio_local, elemento)
			
            fileattr = sftp.lstat(ruta_remota)
            if stat.S_ISDIR(fileattr.st_mode):
                os.makedirs(ruta_local, exist_ok=True)

                ruta_remota = ruta_remota + "/"
                copiar_recursivo(sftp, ruta_remota, ruta_local)
				
            else:
                sftp.get(ruta_remota, ruta_local)
    except IOError:
        pass

copiar_archivos_servidor_a_pc(SERVER_DIRECTORY, LOCAL_DIRECTORY, SERVER_HOST, USER, PASSWORD)
