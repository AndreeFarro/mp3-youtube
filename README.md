# mp3-youtube
Es una aplicacion web que permite la descarga de musica en formato `mp3` en la mejor calidad posible usando la libreria `youtube-dl` y con ayuda de Sockets para el manejo de procesos en paralelo.

<img src="https://github.com/AndreeFarro/mp3-youtube/blob/main/img/test.png" />

## Instalación de dependencias y run del proyecto
### Clonación del Repositorio
```shell
git clone https://github.com/AndreeFarro/mp3-youtube
```

### Creacion y activacion de un entorno virtual
Esto con la finalidad de tener el proyecto aislado, en caso no utilice estos entornos se recomienda buscar informacion al respecto.
```shell
virtualenv venv
./venv/Scripts/activate
```
### Instalación de Dependencias
`(venv)` es una referencia que estamos instalando estas dependencias en un entorno virtual aislado.
```shell
(venv) D:\Projects\Web\mp3-youtube> pip install -r requirements.txt
```

### Run 
- main
```shell
(venv) D:\Projects\Web\mp3-youtube> python main.py
```

- waitress
```shell
(venv) D:\Projects\Web\mp3-youtube> waitress-serve --listen 127.0.0.1:5000 main:app
```


## Nota:

En caso se deseé cambiar de host y puerto, debe considerar cambiar las variables de entorno en un archivo `.env`  y que se le da un ejemplo en `.example.env`.
