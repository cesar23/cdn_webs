# with open('cursos.txt', 'r') as f:
#     for linea in f:
#         print(linea)

# Contetx manager anidado
# with open("cursos.txt", "r") as file_1, open("data_new.txt", "w") as file_2:
#     texto = file_1.read()
#     print(texto)
#     file_2.write(texto)
import urllib.parse

def normalize(s):
    replacements = (
        # LETRAS
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
        # SIGNOS
        (" ", "+"),
        ("Ñ", "N"),
        ("ñ", "n"),

    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s



plantlla_search_google ="https://www.google.com/search?q=%BUSQUEDA%&tbm=isch&ved=2ahUKEwjj8biKkYDtAhUXCbkGHbbMDJ4Q2-cCegQIABAA&oq=Audios+Mentalidad+Emprendedora+Euge+Oller&gs_lcp=CgNpbWcQA1CwkNADWLCQ0ANgjZ3QA2gAcAB4AIABjgGIAY4BkgEDMC4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=Kc6uX6O5NJeS5OUPtpmz8Ak&bih=937&biw=1920"

with open('cursos.txt', 'r', encoding='utf-8') as f:
    lineas = f.readlines()
    for linea in lineas:
        # video_url=normalize(linea).strip()
        video_url=urllib.parse.quote(linea)
        search_google=plantlla_search_google.replace('%BUSQUEDA%',video_url)
        print("Nombre del Video:",linea)
        print("Imagenes:",search_google)
        print("")
    # print(linea)
