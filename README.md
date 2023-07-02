Certainly! Here's a basic README.md file that describes the code selected:

# Copying Files from a Remote Server to a Local Machine

This Python script uses the Paramiko library to copy files from a remote server to a local machine. The script connects to the remote server using SSH, creates an SFTP instance, and then calls a recursive function to copy the files from the remote directory to the local directory.

## Usage

To use this script, you'll need to modify the following variables:

* `directorio_servidor`: The directory on the remote server that you want to copy files from.
* `directorio_local`: The directory on the local machine that you want to copy files to.
* `servidor`: The IP address or hostname of the remote server.
* `usuario`: The username to use when connecting to the remote server.
* `contraseña`: The password to use when connecting to the remote server.

Once you've modified these variables, you can run the script using Python.

## Requirements

This script requires the following Python libraries:

* Paramiko
* DotEnv

You can install these libraries using pip:

**pip install paramiko**

pip install dotenv

## License

This script is released under the MIT License. See LICENSE for more information.
