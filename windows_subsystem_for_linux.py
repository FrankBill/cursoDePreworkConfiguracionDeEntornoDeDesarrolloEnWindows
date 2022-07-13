# Es lo que Microsoft viene desarrollando para que Windows 10 sea una plataforma competitiva para desarrollo de aplicaciones web.
# Con WSL todo se puede hacer desde una terminal de Linux dentro del SO Windows 10.
# WSL es de buen rendimiento y bastante útil.
# Si se tiene una versión anterior a Windows 10 y no se puede actualizar, se debe configurar una máquina virtual y prepararla para que sea el entorno de desarollo.

# GNU/Linux
# Es una familia de SO (distribuciones) y todas usan el kernel de Linux.
# Fedora
# Arch Linux
# Ubuntu
# El pingüino Tux es la mascota oficial de Linux, Linus Torvalds, el creador de Linux, fue mordido por un pingüino, por eso es que la mascota oficial de Linux es un pingüino.

# Configuración de Ubuntu en WSL
# 1. Seguir los pasos del manual de instalación de WSL.
# 2. Instalar Ubuntu en Microsoft Store.
# 3. Instalar Windows Terminal en Microsoft Store.
# 4. Instalar en VSC la extensión Remote - WSL.

# TIPS
# Alt + 126 => ~
# cd ~ => directorio home
# cd / => directorio raíz
# sudo mkdir xxx => Para crear un directorio con permisos de Administrador.
# mv name_directory name_directory => Para mover una carpeta dentro de otra.
# mv name_file name_directory => Para mover un archivo dentro de una carpeta.
# sudo mv carpeta1 carpeta2 => En caso salga permisos denegados al ejecutar la línea anterior.
# explorer.exe . => Para abrir el explorador de archivos en la carpeta de Ubuntu.
# man cat => Para ver el manual de uso del comando cat.
# rm nombrearchivo.nombreextension => Para eliminar un archivo.
# rm -d nombredirectorio => Para eliminar un directorio vacío.
# rm -rf nombredirectorio => Para eliminar un directorio lleno.
# RESPECTO A LO YA INSTALADO
# sudo apt-get update => Para consultarle al repositorio de dependencias (manejador de paquetes) si hay alguna novedad que pueda actualizarse.
# sudo apt-get upgrade => Para aplicar los cambios de la línea anterior.
# PARA INSTALAR NUEVAS COSAS
# sudo apt install nodejs => Para instalar nodejs.
# node -v => Para ver la versión de nodejs instalado.
# sudo apt install npm => Para instalar el manejador de paquetes npm.

# El comando para darle permisos a VS Code para crear y editar archivos es:
# sudo chown -R [tu usuario] [la carpeta que quieres que tenga permisos (ejemplo: ~/projects)]

# Activar Live Server en WSL
# To fix this issue go to Settings make sure you're under Remote[WSL:"your linux distro"] and modify the Live Server>Settings: Advance Custom Browser CMD Line click edit in settings.json it should look like this:
# "liveServer.settings.AdvanceCustomBrowserCmdLine": "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
# change the path a needed for Firefox, Edge etc.

# It seems the extension is looking within the OS for the browser as installing linux chrome also works, but under wsl its not too good so Id suggest th above fix or maybe adding chrome to the path for linux.