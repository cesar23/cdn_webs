#!/usr/bin/env bash
export LC_ALL="es_ES.UTF-8"
DATE_HOUR_GIT="`date +%Y`-`date +%m`-`date +%d`_`date +%H`:`date +%M`:`date +%S`"
CURRENT_USER=$(id -un)
CURRENT_PC_NAME=$(exec /usr/bin/hostname)
MY_INFO="${CURRENT_USER}@${CURRENT_PC_NAME}"
PATH_SCRIPT=`readlink -f "${BASH_SOURCE:-$0}"`
CURRENT_DIR=`dirname $PATH_SCRIPT`
NAME_DIR=$(basename $CURRENT_DIR) # nombre del Directorio actual

scriptPathDir=$(dirname $0)
scriptPathFile=$(realpath $0)
scriptPathFileName="$(basename "$(test -L "$0" && readlink "$0" || echo "$0")")"
# echo "scriptPathDir: $scriptPathDir"
# echo "scriptPathFile: $scriptPathFile"
# echo "scriptPathFileName: $scriptPathFileName"
# -------------- version 01
function upgit() {
	git pull
    git add -A
    git commit -m "cmder se actualizo :${DATE_HOUR_GIT}"
    git push -u origin master
}

function gitup() {
    git pull
	  git add -A
    git commit -m "cmder se actualizo :${DATE_HOUR_GIT}"
    git push -u origin master
}

function gitup2() {
    git pull
	  git add -A
    git commit -m "cmder se actualizo :${DATE_HOUR_GIT}"
    git push
}

function compilar() {
   cd $scriptPathDir
    python listar_img_webp.py
}


clear

echo "###############################################"
echo "############# Compilar Imagenes ###############"
echo "###############################################"
echo ""
sleep 2
compilar
gitup

echo ""
echo "  ██████  ██   ██                ██████ ███████ ███████  █████  ██████  "
echo " ██    ██ ██  ██                ██      ██      ██      ██   ██ ██   ██ "
echo " ██    ██ █████       █████     ██      █████   ███████ ███████ ██████  "
echo " ██    ██ ██  ██                ██      ██           ██ ██   ██ ██   ██ "
echo "  ██████  ██   ██                ██████ ███████ ███████ ██   ██ ██   ██ "
echo ""
echo ""
sleep 4
python -m webbrowser https://cesar23.github.io/cdn_webs/index.html?date=$DATE_HOUR_GIT