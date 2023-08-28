# Installation
Required: the ```webomints``` font


1. Download the installer [install-getnonfreefonts](https://tug.org/fonts/getnonfreefonts/install-getnonfreefonts) from https://www.tug.org/fonts/getnonfreefonts/ to an arbitrary directory.
2. Open Terminal and type: cd <directory containing the downloaded file here minus brackets>
3. In Terminal, type: texlua install-getnonfreefonts
4. In Terminal, type: getnonfreefonts --sys webomints. This installs the fonts system−wide, which is the best practices solution. 

See also:(https://tex.stackexchange.com/questions/284082/cant-install-webomints-package)


Manully

http://mirror.ox.ac.uk/sites/ctan.org/fonts/webomints/README

1) Copy WebOMintsGD.tfm to the directory texmf/fonts/tfm/public/misc
2) Copy WebOMintsGD.pfb to the directory texmf/fonts/type1/public/misc
3) Copy uwebo.fd to the directory texmf/tex/latex/misc
4) If you are using dvips or pdfTeX, copy webo.map and config.webo to
   the directory texmf/dvips/config.  Add the contents of webo.map
   permanently to the font map or call dvips with the option -Pwebo .



texhash

updmap --sys --enable Map webo.map


See also:(https://tex.stackexchange.com/questions/497689/installing-fonts-what-about-the-map-file)


## Compilation

latexmk (xelatex)