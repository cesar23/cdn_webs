"""

primero poner el  cwebp.exe en windows

uso de script:
ejecutar desde la consola

# cmd> python cwebp_compressor_dir.py folder-name 80

"""

import sys,os
import time
from subprocess import call
from glob import glob

from  Config.constantes import *

print(DATABASE_CONFIG['db_host'])
exit(0)

plantilla ="""
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Dashboard Template · Bootstrap v5.0</title>
    <!-- Bootstrap core CSS -->
    <link href="https://getbootstrap.com/docs/5.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }

        @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
        }
    </style>
    <script>
        const SITE = ''
    </script>

    <!-- Custom styles for this template -->
    <link href="https://getbootstrap.com/docs/5.0/examples/dashboard/dashboard.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"
            integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
            crossorigin="anonymous"></script>
</head>
<body>

<header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
    <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="#">Company name</a>
    <button class="navbar-toggler position-absolute d-md-none collapsed" type="button" data-bs-toggle="collapse"
            data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false"
            aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <input class="form-control form-control-dark w-100" type="text" placeholder="Search" aria-label="Search">
    <ul class="navbar-nav px-3">
        <li class="nav-item text-nowrap">
            <a class="nav-link" href="#">Sign out</a>
        </li>
    </ul>
</header>

<div class="container-fluid">
    <div class="row">
        <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
            <div class="position-sticky pt-3">
                <ul class="nav flex-column">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">
                            <span data-feather="home"></span>
                            Inicio
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">
                            <span data-feather="file"></span>
                            Orders
                        </a>
                    </li>

                </ul>

               
                </ul>
            </div>
        </nav>

        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
            <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
                <h1 class="h2">Raiz</h1>

            </div>

            <div class="row">
                {{%LISTADO%}}

            </div>


        </main>
    </div>
</div>


<script src="https://getbootstrap.com/docs/5.0/dist/js/bootstrap.bundle.min.js"></script>

<script src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/feather.min.js"></script>

<script>
    function changeUrl() {
        var site = "http://www.w3schools.com";
        document.getElementsByName('iFrameName')[0].src = site;
    }
</script>
</body>
</html>

"""




def generarIndex(path,platilla_html):
    global plantilla

    img_list = []

    for dirpath, dirnames, filenames in os.walk(path,topdown=True):
        print('\nruta       :', dirpath)
        for img_name in filenames:
            # se pueden utilizar más tipos de imágenes (bmp, tiff, gif)
            # if img_name.endswith(".jpg") or img_name.endswith(".png") or img_name.endswith(".jpeg"):
            if img_name.endswith(".webp") or img_name.endswith(".jpg") or img_name.endswith(".png")or img_name.endswith(".svg"):
                img_list.append(img_name)

    print("-------------------------------------------------------------------------")
    print("-----------------Ejecutamos el comando para Convertir---------------------")
    print("-------------------------------------------------------------------------")


    salida_html=''
    for img_name in img_list:

        url_imagen ="https://cesar23.github.io/cdn_webs/{}".format(img_name)

        min_template="""
        <div class="col-md-3">
                    <div class="card">
                        <img class="card-img-bottom img-fluid"
                             src="{url_imagen}"/>
                        <div class="card-body">
                            <h4 class="card-title">{name_imagen}</h4>
                            <p class="card-text">aqui ver link</p>
                            <a href="{url_imagen}" class="btn btn-primary">Ver</a>
                        </div>

                    </div>
                </div>
        
        """.format(url_imagen=url_imagen,name_imagen=img_name)

        #
        # str ="https://cesar23.github.io/web_cursos_geral/2020/{}".format(img_name)
        # str= '<a href="{}">{}</a> <br>'.format(str,str)
        # print(str )
        salida_html+=min_template +'\n'
        # running the above command
        # call(cmd, shell=False)
        # print(cmd)    # for debug

    platilla_nueva=platilla_html.replace('{{%LISTADO%}}',salida_html)
    with open('index.html', "w",encoding='utf-8') as file:
        file.write(platilla_nueva)









#
# for img_name in glob(path+'/*'):
#     # se pueden utilizar más tipos de imágenes (bmp, tiff, gif)
#     if img_name.endswith(".jpg") or img_name.endswith(".png") or img_name.endswith(".jpeg"):
#         # extraer el nombre de las imágenes (image_name. [jpg | png]) de la ruta completa
#         print("Nombre de la imagen a convertir:",img_name.split('\\')[-1])
#         img_list.append(img_name.split('\\')[-1])




# print(img_list)   # for debug



# salida = input("Pulsar [enter para salir]")

#folder-name
path = r"D:\repos\cdn_webs"
#quality of produced .webp images [0-100]

generarIndex(path,plantilla)

print("-------------------------------------------------------------------------")
print("-----------------Filtramos solo las imagenes [jps,png]---------------------")
print("-------------------------------------------------------------------------")
