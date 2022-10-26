#!/usr/bin/env bash
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
