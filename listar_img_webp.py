"""

primero poner el  cwebp.exe en windows

uso de script:
ejecutar desde la consola

# cmd> python cwebp_compressor_dir.py folder-name 80

"""

import sys, os,re
import time
from subprocess import call
from glob import glob

from Config import *

def humanbytes(B):
    'Return the given bytes as a human friendly KB, MB, GB, or TB string'
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B/KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B/MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B/GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B/TB)






plantilla = CONFIG['plantillaGlobal']



def getCurrentNameDir():
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    return  os.path.basename(dirname)

def getCurrentDir():
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    return dirname

def generarIndex(path, platilla_html):
    global plantilla

    img_list = []
    excludeDirs = ['.git', '.idea', 'Config']
    salida_html = ''
    links_navs=''

    NameDir =getCurrentDir()

    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        [dirnames.remove(d) for d in list(dirnames) if d in excludeDirs]
        # if dirpath.endswith(".git") or dirpath.endswith(".idea") or dirpath.endswith("Config")or dirpath.endswith("libs"):
        #     continue

        print('\nruta       :', dirpath)
        # NameDir = dirpath.replace(getCurrentNameDir(),'')

        print("Nombre Carpeta : " +NameDir)


        for file in filenames:
            archivo = dirpath + os.sep + file
            sizeBytesfile = os.path.getsize(archivo)
            peso_archivo=humanbytes(sizeBytesfile)
            print('path_archivo :', archivo)
            # se pueden utilizar más tipos de imágenes (bmp, tiff, gif)
            # if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            if file.endswith(".webp") or file.endswith(".jpg") or file.endswith(".png") or file.endswith(".svg"):
                img_list.append(file)
                img_name = file

                path_corto=archivo.replace(path,'')
                # path_corto=NameDir +path_corto
                path_corto=path_corto.replace('\\','/').replace('//','/').replace('///','/')

                pathServer=path_corto
                # url_imagen ="https://cesar23.github.io{}".format(pathServer)
                url_imagen =CONFIG['server']+"/"+CONFIG['dirRoot']+"{}".format(pathServer)



                # if NameDir != '':
                #     NameDir = re.sub(r'(?is):.+', '', NameDir)
                #     img_name = "{}/{}".format(NameDir, file)
                #     img_name=img_name.replace('\\','/').replace('//','/')
                #
                # pathServer ="/cdn_webs/{}".format(img_name)
                # pathServer=pathServer.replace('//','/')
                # # url_imagen ="https://cesar23.github.io{}".format(pathServer)
                # url_imagen =CONFIG['server']+"{}".format(pathServer)

                #url_imagen = "https://cesar23.github.io/{}".format(img_name)

                min_template = """
                <div class="col-md-3">
                            <div class="card">
                                <img class="card-img-bottom img-fluid"
                                    src="https://www.solodev.com/_/images/client-loader.gif" loading="lazy" data-src="{url_imagen}"/>
                                <div class="card-body">
                                    <h6 class="card-title">{name_imagen}</h6>
                                    <p class="card-text">peso de archivo es:{peso}</p>
                                    <a href="{url_imagen}" class="btn btn-primary">Ver</a>
                                </div>
        
                            </div>
                        </div>
                
                """.format(url_imagen=url_imagen, name_imagen=img_name,peso=peso_archivo)

                #
                # str ="https://cesar23.github.io/web_cursos_geral/2020/{}".format(img_name)
                # str= '<a href="{}">{}</a> <br>'.format(str,str)
                # print(str )
                salida_html += min_template + '\n'
                # running the above command
                # call(cmd, shell=False)
                # print(cmd)    # for debug


    for clave, valor in CONFIG['links'].items():
        links_navs+="""
         <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{nav_link}">
                        <span data-feather="home"></span>
                        {nav_name}
                    </a>
                </li>
        """.format(nav_name=clave,nav_link=valor)


    platilla_nueva = platilla_html.replace('{{%LISTADO%}}', salida_html)
    platilla_nueva = platilla_nueva.replace('{{%LINKS%}}', links_navs)
    platilla_nueva = platilla_nueva.replace('{{%CURRENT_DIR%}}', getCurrentNameDir())
    with open('index.html', "w", encoding='utf-8') as file:
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

# folder-name
path = r"D:\repos\cdn_webs"
# quality of produced .webp images [0-100]

currentDir = os.path.abspath(__file__)
currentDir = os.path.dirname(currentDir)

generarIndex(currentDir, plantilla)

print("-------------------------------------------------------------------------")
print("-----------------Filtramos solo las imagenes [jps,png]---------------------")
print("-------------------------------------------------------------------------")


