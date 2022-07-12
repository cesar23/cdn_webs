    sudo apt install -y screen
    screen --version

## opciones
```
    Ctrl-a ?          Ayuda de Screen
    Ctrl-a c          Crear una nueva ventana virtual.
    Ctrl-a ”          Lista navegable de ventanas abiertas
    Ctrl-a Ctrl-n Cambiar a la venana Siguiente o Anterior
    Ctrl-a Ctrl-N Cambiar a la Ventana N (de 0-9)
    Ctrl-a x          Bloquear todas las terminales con una clave
    Ctrl-a d          Hacer un Detach. Sales de la ventana pero la deja activa.
    exit              Con esto cierras la ventana virtual de definitivamente.
    Ctrl-a S          Divide la ventana horizontalmente
    Ctrl-a tab        Salta a la siguiente zona
    Ctrl-a X          Cerrar la zona actual
    Ctrl-a Q          Cerrar todas las zonas excepto la actual
    Copiar en Screen
    Ctrl-a + [      Entrar en modo copia/scroll.
    Enter           Comenzar la selección de texto / Finalizar la selección
                    de texto, copiar y salir modo copia/scroll.
    Cursor          Desplazamiento del cursor selecciona el texto a
                    copiar (si estamos en modo copia/scroll).
    ESC             Salir del modo copia/scroll sin copiar nada.
    Ctrl-a + ]      Pegar el texto copiado.




```




## 1. Crear Screen 
Para iniciar una sesión de pantalla, simplemente escriba screenen su consola:
```
--- para crear cada  ventana usaremos
> screen
--- para  crear un screen con nombre
> screen -S ssh-session
```
![](https://i.imgur.com/YRyHbib.png) 
presionar enter  para seguir y  ejecutaremos  cualquier  otro   comando


### 2. Ahora  ya  esta  ejecutandose screem  ahora probaremos con
```
htop
```

### 2.1 para  minimizar o enviar a  background la  venta  presionamos
```
Ctrl+a+d
```
![](https://i.imgur.com/u7OdArx.png) 


### 3. Para  restaurar -r screens :
```
screen -r
```
![](https://i.imgur.com/nWtzRBm.png) 

### 3.2 Para listar screens :
```
 screen -list
```



### 4. Para  recuperar un screen pir id

```
screen -r 21021.pts-0.server-local
```
![](https://i.imgur.com/MVt5UCX.png) 
>


### 5. para  cerrar un screen determinado
```
screen -S 21021.pts-0.server-local -X quit
```

### 5.2 para  restaurar una session en : attached (adjuntada)
```
screen -D 25028.samba-session 
#--  ahora  ya  podemos  entrar
screen -r 25028.samba-session 
```
![](https://i.imgur.com/I5eygXs.png) 

### 6. Eliminar session
```
screen -S '25028.samba-session' -X quit
screen -X -S 25028.samba-session quit
```
### 6.2 Eliminar todas
```

#- no funcionan
screen -ls | grep '(Detached)' | awk 'BEGIN  {system("screen -S " $1 "  -X quit ")}'
screen -ls | grep '(Detached)' | awk 'sys {screen -S $1 -X quit}'

o
pkill screen
killall screen

```
