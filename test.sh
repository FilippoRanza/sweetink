#! /bin/bash

# installa solo quello che serve da texlive-full.
sudo apt update -qqq
sudo apt install $(apt-cache depends texlive-full |
                    grep Depends: |
                    awk '{print $2}' |
                    grep -v 'lang' |
                    grep -v  'doc' ) -y -qq --no-install-recommends

sudo apt install texlive-lang-italian -y -qq --no-install-recommends

# modifica tesi.tex in modo che includa un frontespizio
# alla volta quindi compila

for f in frontespizio_* ; do 
    perl -pe "s|%CHANGE_HERE|$f|" > 'tesi_temp.tex'
    pdflatex -synctex=1 -interaction=nonstopmode --shell-escape 'tesi_temp.tex'
    [[ -f 'tesi_temp.tex' ]] || exit 1
done