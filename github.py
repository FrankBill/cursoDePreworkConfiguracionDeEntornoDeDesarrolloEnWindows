# Vincular GitHub con terminal de Ubuntu.

# 1. ssh-keygen -t rsa -b 4096 -C "email de GitHub" => Ingresar en la terminal (en el home).
# 2. Ingresar contraseña (sugerencia: la misma contraseña de Ubuntu).
# 3. eval "$(ssh-agent -s)" => Nos ayuda a gestionar nuestras claves. Se evalúa que haya un agente corriendo y que todo esté en orden. -- Agent pid 2074

# Para obtener nuestra llave SSH:
# 4. cd ~/.ssh
# 5. cat id_rsa.pub
# 6. Copiar la llave SSH obtenida en la terminal de Ubuntu.

# Acciones en GitHub:
# 7. Ir a GitHub en la sección de Settings, luego click en SSH and GPG keys.
# 8. Click en New SSH key.
# 9. Ingresar title y llave SSH.
# 10. Se agrega la llave SSH a GitHub y ya tenemos vinculado el terminal a GitHub.