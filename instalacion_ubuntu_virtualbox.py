# En la clase anterior instalamos VirtualBox. El siguiente paso es crear una máquina virtual, pero antes de eso necesitamos descargar el sistema operativo que deseamos virtualizar, en nuestro caso será Ubuntu. Podemos descargarlo directamente de su página oficial. La versión que descargamos será la de Ubuntu Desktop.

# Lo que te descargara la página será una imagen ISO. Este es un tipo de archivo que almacena un sistema de archivos de manera idéntica, en este caso un sistema operativo completo. Este archivo es el que necesitamos darle a VirtualBox para crear nuestra máquina virtual.

# En nuestra ventana principal de VirtualBox le damos al icono de “nueva” y aparecerá la siguiente pestaña. Dentro de ella en la sección de nombre colocaremos “Ubuntu” y VirtualBox automáticamente detectará que tipo de máquina virtual queremos crear. Una vez haga esto da click en siguiente.

# Lo siguiente es configurar los recursos que tendrá nuestra máquina como la memoria RAM, el espacio en disco y el procesador. Esas opciones aparecerán en diferentes ventanas. En mi caso solo usaré 4 GB de memoria RAM y los 10 GB de espacio en disco que se recomiendan al crear una máquina virtual. También se debe seleccionar la opción de que el disco crezca dinámicamente para que no ocupe tanto espacio inicialmente.

# Al final solo damos en la última ventana en “crear” y así tendremos nuestra máquina lista para instalar Ubuntu como sistema operativo. Estas opciones son muy sencillas de configurar y la mayoría por defecto funcionan para nuestra máquina virtual.

# Para que nuestra máquina virtual pueda instalar el sistema operativo se necesita “insertar” la imagen ISO de Ubuntu en nuestra máquina virtual. Para ello vamos a configuración > almacenamiento > controlador IDE > Unidad óptica y seleccionar un archivo de disco.

# El archivo que debemos seleccionar es la imagen ISO de Ubuntu.

# La última configuración que debemos realizar es cambiar el adaptador de video de la máquina virtual, para ello en pantalla < controlador gráfico selecciona “vBoxSVGA”.

# Con esto ya podemos iniciar nuestra máquina virtual y empezar el proceso de instalación. Debemos seleccionar el idioma en el que queremos Ubuntu, crear nuestro usuario y terminando la instalación nos pedirá reiniciar nuestra máquina virtual. En vez de reiniciar debemos apagarla haciendo click en archivo < cerrar.

# Antes de volver a iniciar nuestro sistema con Ubuntu ya instalado debemos remover la imagen de instalación que previamente habíamos seleccionado. Esto se hace en la sección de almacenamiento con la máquina ya apagada.

# ¡Al volver a iniciar la máquina ya tendrás Ubuntu completamente instalado!