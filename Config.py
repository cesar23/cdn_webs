import sys, os,re
import time,os
import datetime
from datetime import datetime
def getCurrentNameDir():
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    return  os.path.basename(dirname)


SERVER='https://cesar23.github.io'
SERVER_PATH_URL=SERVER+"/"+ getCurrentNameDir()


# current date and time
now = datetime.now()
timestamp = datetime.timestamp(now)

tiemp = now.strftime("%Y-%m-%d_%H-%M-%S")


CONFIG = {
    'server': SERVER,
    'dirRoot': getCurrentNameDir(),
    'directorios':["camicv","pcbyte"],
    'links':{
        "carpeta -> index":SERVER_PATH_URL+"/index.html"+"?aletorio="+str(tiemp),
        "carpeta -> camicv":SERVER_PATH_URL+"/camicv/index.html"+"?aletorio="+str(tiemp),
        "carpeta -> pcbyte":SERVER_PATH_URL+"/pcbyte/index.html"+"?aletorio="+str(tiemp),
        "carpeta -> webcursos":SERVER_PATH_URL+"/webcursos/index.html"+"?aletorio="+str(tiemp),
    },

    'plantillaGlobal' : """
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
    <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="#">Navegador</a>
    <button class="navbar-toggler position-absolute d-md-none collapsed" type="button" data-bs-toggle="collapse"
            data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false"
            aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
 
   
</header>

<div class="container-fluid">
    <div class="row">
        <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
            <div class="position-sticky pt-3">
                <ul class="nav flex-column">
                   
                    {{%LINKS%}}

                </ul>

               
                </ul>
            </div>
        </nav>

        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
            <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
                <h1 class="h2">Drirectorio: {{%CURRENT_DIR%}}</h1>

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
   if ('loading' in HTMLImageElement.prototype) {
    const images = document.querySelectorAll('*[loading="lazy"]');
    images.forEach(img => {
        data_src=img.getAttribute('data-src')
        img.src = data_src;
    });
    console.log('nativo')
} else {
    console.log('lazysizes')
    // Dynamically import the LazySizes library
    const script = document.createElement('script');
    script.src =
        'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.1.2/lazysizes.min.js';
    document.body.appendChild(script);
}


  function copiarAlPortapapeles2(obj) {
        elemento=obj;
        link=elemento.parentElement.querySelector('a').innerHTML;
        var aux = document.createElement("input");
        aux.setAttribute("value",link);
        document.body.appendChild(aux);
        aux.select();
        document.execCommand("copy");
        document.body.removeChild(aux);
    }
</script>
</body>
</html>

"""
}