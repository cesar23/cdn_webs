#!/usr/bin/env bash
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
    git pull
	  git add -A
    python listar_img_webp.py
    python camicv/listar_interno.py
    python pcbyte/listar_interno.py
    git push
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