# Reprendre l'installation de R et RStudio sur mon PC de travail
## Installer r-base 
```bash
jmena01@m077-2281091:~$ sudo apt install r-base
[sudo] Mot de passe de jmena01 : 
Lecture des listes de paquets... Fait
Construction de l'arbre des dépendances... Fait
Lecture des informations d'état... Fait      
Les paquets supplémentaires suivants seront installés : 
  bzip2-doc gfortran gfortran-13 gfortran-13-x86-64-linux-gnu gfortran-x86-64-linux-gnu icu-devtools libblas-dev libbz2-dev libgfortran-13-dev libicu-dev libjpeg-dev libjpeg-turbo8-dev
  libjpeg8-dev liblapack-dev liblzma-dev libncurses-dev libpcre2-dev libpcre2-posix3 libpkgconf3 libpng-dev libpng-tools libreadline-dev libtk8.6 pkg-config pkgconf pkgconf-bin
  r-base-core r-base-dev r-base-html r-cran-boot r-cran-class r-cran-cluster r-cran-codetools r-cran-foreign r-cran-kernsmooth r-cran-lattice r-cran-mass r-cran-matrix r-cran-mgcv
  r-cran-nlme r-cran-nnet r-cran-rpart r-cran-spatial r-cran-survival r-doc-html r-recommended zlib1g-dev
Paquets suggérés :
  gfortran-multilib gfortran-doc gfortran-13-multilib gfortran-13-doc libcoarrays-dev liblapack-doc icu-doc liblzma-doc ncurses-doc readline-doc tk8.6 elpa-ess r-doc-info | r-doc-pdf
  r-mathlib texlive-base texlive-latex-base texlive-plain-generic texlive-fonts-recommended texlive-fonts-extra texlive-extra-utils texlive-latex-recommended texlive-latex-extra
  texinfo
Les NOUVEAUX paquets suivants seront installés :
  bzip2-doc gfortran gfortran-13 gfortran-13-x86-64-linux-gnu gfortran-x86-64-linux-gnu icu-devtools libblas-dev libbz2-dev libgfortran-13-dev libicu-dev libjpeg-dev libjpeg-turbo8-dev
  libjpeg8-dev liblapack-dev liblzma-dev libncurses-dev libpcre2-dev libpcre2-posix3 libpkgconf3 libpng-dev libpng-tools libreadline-dev libtk8.6 pkg-config pkgconf pkgconf-bin r-base
  r-base-core r-base-dev r-base-html r-cran-boot r-cran-class r-cran-cluster r-cran-codetools r-cran-foreign r-cran-kernsmooth r-cran-lattice r-cran-mass r-cran-matrix r-cran-mgcv
  r-cran-nlme r-cran-nnet r-cran-rpart r-cran-spatial r-cran-survival r-doc-html r-recommended zlib1g-dev
0 mis à jour, 48 nouvellement installés, 0 à enlever et 1 non mis à jour.
Il est nécessaire de prendre 82,4 Mo dans les archives.
Après cette opération, 205 Mo d'espace disque supplémentaires seront utilisés.
Souhaitez-vous continuer ? [O/n] 
```
* test
```r
jmena01@m077-2281091:~$ R

R version 4.3.3 (2024-02-29) -- "Angel Food Cake"
Copyright (C) 2024 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)

R est un logiciel libre livré sans AUCUNE GARANTIE.
Vous pouvez le redistribuer sous certaines conditions.
Tapez 'license()' ou 'licence()' pour plus de détails.

R est un projet collaboratif avec de nombreux contributeurs.
Tapez 'contributors()' pour plus d''information et
'citation()' pour la façon de le citer dans les publications.

Tapez 'demo()' pour des démonstrations, 'help()' pour l''aide
en ligne ou 'help.start()' pour obtenir l'aide au format HTML.
Tapez 'q()' pour quitter R.

> q()
Save workspace image? [y/n/c]: n
```
## Installation de R-Studio
* aller sur le [site de posit](https://posit.co/download/rstudio-desktop/#download) pour trouver le paquet debian à installer
  * Pour notre Ubuntu 24 il s'agit de [rstudio-2025.05.1-513-amd64.deb](https://download1.rstudio.org/electron/jammy/amd64/rstudio-2025.05.1-513-amd64.deb) 203MB
* obliger de faire un fix-broken-install comme pour Ubuntu 20.04
  * cf [réponse 3 de ce post Stack Exchange au sujet de la 20.04](https://askubuntu.com/questions/1337617/unable-to-install-libclang-on-20-04-lts)
```bash
jmena01@m077-2281091:~/Téléchargements$ sudo dpkg -i rstudio-2025.05.1-513-amd64.deb
Sélection du paquet rstudio précédemment désélectionné.
(Lecture de la base de données... 297649 fichiers et répertoires déjà installés.)
Préparation du dépaquetage de rstudio-2025.05.1-513-amd64.deb ...
Dépaquetage de rstudio (2025.05.1+513) ...
dpkg: des problèmes de dépendances empêchent la configuration de rstudio :
 rstudio dépend de libclang-dev; cependant :
  Le paquet libclang-dev n'est pas installé.

dpkg: erreur de traitement du paquet rstudio (--install) :
 problèmes de dépendances - laissé non configuré
Traitement des actions différées (« triggers ») pour gnome-menus (3.36.0-1.1ubuntu3) ...
Traitement des actions différées (« triggers ») pour desktop-file-utils (0.27-2build1) ...
Traitement des actions différées (« triggers ») pour hicolor-icon-theme (0.17-2) ...
Traitement des actions différées (« triggers ») pour shared-mime-info (2.4-4) ...
Des erreurs ont été rencontrées pendant l'exécution :
 rstudio
# Comme pour La Ubuntu 20 obligé de passer cette commande 
jmena01@m077-2281091:~/Téléchargements$ sudo apt --fix-broken install
Lecture des listes de paquets... Fait
Construction de l'arbre des dépendances... Fait
Lecture des informations d'état... Fait      
Correction des dépendances... Fait
Les paquets supplémentaires suivants seront installés : 
  lib32gcc-s1 lib32stdc++6 libc6-i386 libclang-18-dev libclang-common-18-dev libclang-dev libclang-rt-18-dev libobjc-13-dev libobjc4
Les NOUVEAUX paquets suivants seront installés :
  lib32gcc-s1 lib32stdc++6 libc6-i386 libclang-18-dev libclang-common-18-dev libclang-dev libclang-rt-18-dev libobjc-13-dev libobjc4
0 mis à jour, 9 nouvellement installés, 0 à enlever et 1 non mis à jour.
1 partiellement installés ou enlevés.
Il est nécessaire de prendre 37,2 Mo dans les archives.
Après cette opération, 367 Mo d''espace disque supplémentaires seront utilisés.
Souhaitez-vous continuer ? [O/n] O
Réception de :1 http://10.154.53.200/ubuntu noble-updates/universe amd64 libobjc4 amd64 14.2.0-4ubuntu2~24.04 [47,0 kB]
Réception de :2 http://10.154.53.200/ubuntu noble-updates/universe amd64 libobjc-13-dev amd64 13.3.0-6ubuntu2~24.04 [194 kB]
Réception de :3 http://10.154.53.200/ubuntu noble-updates/universe amd64 libclang-common-18-dev amd64 1:18.1.3-1ubuntu1 [736 kB]
Réception de :4 http://10.154.53.200/ubuntu noble-updates/universe amd64 libclang-18-dev amd64 1:18.1.3-1ubuntu1 [28,8 MB]
Réception de :5 http://10.154.53.200/ubuntu noble/universe amd64 libclang-dev amd64 1:18.0-59~exp2 [5 424 B]
Réception de :6 http://10.154.53.200/ubuntu noble-updates/main amd64 libc6-i386 amd64 2.39-0ubuntu8.4 [2 787 kB]
Réception de :7 http://10.154.53.200/ubuntu noble-updates/main amd64 lib32gcc-s1 amd64 14.2.0-4ubuntu2~24.04 [92,3 kB]
Réception de :8 http://10.154.53.200/ubuntu noble-updates/main amd64 lib32stdc++6 amd64 14.2.0-4ubuntu2~24.04 [814 kB]
Réception de :9 http://10.154.53.200/ubuntu noble-updates/universe amd64 libclang-rt-18-dev amd64 1:18.1.3-1ubuntu1 [3 772 kB]
37,2 Mo réceptionnés en 0s (105 Mo/s)
############### 
Traitement des actions différées (« triggers ») pour libc-bin (2.39-0ubuntu8.4) ...
needrestart is being skipped since dpkg has failed
# on relance l'installation !!!
jmena01@m077-2281091:~/Téléchargements$ sudo dpkg -i rstudio-2025.05.1-513-amd64.deb
(Lecture de la base de données... 305541 fichiers et répertoires déjà installés.)
Préparation du dépaquetage de rstudio-2025.05.1-513-amd64.deb ...
Dépaquetage de rstudio (2025.05.1+513) sur (2025.05.1+513) ...
Paramétrage de rstudio (2025.05.1+513) ...
Traitement des actions différées (« triggers ») pour gnome-menus (3.36.0-1.1ubuntu3) ...
Traitement des actions différées (« triggers ») pour desktop-file-utils (0.27-2build1) ...
Traitement des actions différées (« triggers ») pour hicolor-icon-theme (0.17-2) ...
Traitement des actions différées (« triggers ») pour shared-mime-info (2.4-4) ...
```
* Il crée tout seul le .desktop
```bash
jmena01@m077-2281091:/usr/share/applications$ cat rstudio.desktop 
[Desktop Entry]
Exec=/usr/lib/rstudio/rstudio %F
Icon=rstudio
Type=Application
Terminal=false
Name=RStudio
Categories=Development;IDE;
MimeType=text/x-r-source;text/x-r;text/x-R;text/x-r-doc;text/x-r-sweave;text/x-quarto-markdown;text/x-r-markdown;text/x-r-html;text/x-r-presentation;application/x-r-data;application/x-r-project;application/x-rdp-rsp;text/x-r-history;text/x-r-profile;text/x-tex;text/x-markdown;text/css;text/javascript;text/x-chdr;text/x-csrc;text/x-c++hdr;text/x-c++src;
```  
# Bonne explication [R and VisualStudio](https://code.visualstudio.com/docs/languages/r)
* le install.package met du temps il compile
* Il a besoin commme prérequis
```bash
jmena01@m077-2281091:~$ sudo apt install libxml2-dev
[sudo] Mot de passe de jmena01 : 
Lecture des listes de paquets... Fait
Construction de l'arbre des dépendances... Fait
Lecture des informations d'état... Fait      
Les NOUVEAUX paquets suivants seront installés :
  libxml2-dev
0 mis à jour, 1 nouvellement installés, 0 à enlever et 1 non mis à jour.
Il est nécessaire de prendre 780 ko dans les archives.
Après cette opération, 3 340 ko d'espace disque supplémentaires seront utilisés.
Réception de :1 http://10.154.53.200/ubuntu noble-updates/main amd64 libxml2-dev amd64 2.9.14+dfsg-1.3ubuntu3.2 [780 kB]
780 ko réceptionnés en 0s (27,0 Mo/s)
```
* Il faut aussi donner le proxy dans la session cf [réponse 3 de ce post StackOverflow](https://stackoverflow.com/questions/14524449/how-to-install-r-packages-via-proxy-user-password)
```r
> install.packages("languageserver")
################## Très longues compilations""
server.o reader.o search.o stack.o -L/usr/lib/R/lib -lR
installing to /home/jmena01/R/x86_64-pc-linux-gnu-library/4.3/00LOCK-languageserver/00new/languageserver/libs # les package sont installés en local sur mon compte
** R
** inst
** byte-compile and prepare package for lazy loading
** help
*** installing help indices
** building package indices
** testing if installed package can be loaded from temporary location
** checking absolute paths in shared objects and dynamic libraries
** testing if installed package can be loaded from final location
** testing if installed package keeps a record of temporary installation path
* DONE (languageserver)

Les packages source téléchargés sont dans
	‘/tmp/RtmpEuEnSi/downloaded_packages’
```
## Il ne veut pas installer la R Extension sur mon VSCODE
* l'[archive deb](https://code.visualstudio.com/) sert aussi bien pour l'installation que pour la mise à jour
```bash
jmena01@m077-2281091:~/Téléchargements$ sudo dpkg -i code_1.102.1-1752598717_amd64.deb
[sudo] Mot de passe de jmena01 : 
(Lecture de la base de données... 346050 fichiers et répertoires déjà installés.)
Préparation du dépaquetage de code_1.102.1-1752598717_amd64.deb ...
Dépaquetage de code (1.102.1-1752598717) sur (1.94.2-1728494015) ... # Il met à jour de la version fournie avec le Socle 1.94.2 vers la dernière téléchargée 1.102.1
Paramétrage de code (1.102.1-1752598717) ... # il me demande d'ajouter le apt reository Microsoft et j'ai dit oui (écran pseudo graphique)
Traitement des actions différées (« triggers ») pour gnome-menus (3.36.0-1.1ubuntu3) ...
Traitement des actions différées (« triggers ») pour desktop-file-utils (0.27-2build1) ...
Traitement des actions différées (« triggers ») pour shared-mime-info (2.4-4) ...
```
* Il a installé les extensions R et R Syntax
# une [formation officielle express à R](https://cran.r-project.org/doc/manuals/R-intro.html)
* [Avancée jusqu'au paragrphe 2.4 (exclu)](../../R/debut_2.4.R)
# Installation de R sur monPC Windows + WSL
* WSL fait tourner une Ubuntu 22.04 (todo: passer à la Ubuntu 24.04 comme au travail)
## Installation de R
```bash
jpmena@LAPTOP-E2MJK1UO:~$ sudo apt install r-base-core
[sudo] password for jpmena:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following package was automatically installed and is no longer required:
  libopengl0
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:
  bzip2-doc gfortran gfortran-11 icu-devtools libblas-dev libbz2-dev libgfortran-11-dev libicu-dev libjpeg-dev
  libjpeg-turbo8-dev libjpeg8-dev liblapack-dev liblzma-dev libncurses-dev libncurses5-dev libpcre16-3 libpcre2-32-0
  libpcre2-dev libpcre2-posix3 libpcre3-dev libpcre32-3 libpcrecpp0v5 libpng-dev libpng-tools libreadline-dev
  pkg-config r-base-dev r-cran-boot r-cran-class r-cran-cluster r-cran-codetools r-cran-foreign r-cran-kernsmooth
  r-cran-lattice r-cran-mass r-cran-matrix r-cran-mgcv r-cran-nlme r-cran-nnet r-cran-rpart r-cran-spatial
  r-cran-survival r-doc-html r-recommended
Suggested packages:
  gfortran-multilib gfortran-doc gfortran-11-multilib gfortran-11-doc libcoarrays-dev liblapack-doc icu-doc
  liblzma-doc ncurses-doc readline-doc elpa-ess r-doc-info | r-doc-pdf r-mathlib r-base-html
The following NEW packages will be installed:
  bzip2-doc gfortran gfortran-11 icu-devtools libblas-dev libbz2-dev libgfortran-11-dev libicu-dev libjpeg-dev
  libjpeg-turbo8-dev libjpeg8-dev liblapack-dev liblzma-dev libncurses-dev libncurses5-dev libpcre16-3 libpcre2-32-0
  libpcre2-dev libpcre2-posix3 libpcre3-dev libpcre32-3 libpcrecpp0v5 libpng-dev libpng-tools libreadline-dev
  pkg-config r-base-core r-base-dev r-cran-boot r-cran-class r-cran-cluster r-cran-codetools r-cran-foreign
  r-cran-kernsmooth r-cran-lattice r-cran-mass r-cran-matrix r-cran-mgcv r-cran-nlme r-cran-nnet r-cran-rpart
  r-cran-spatial r-cran-survival r-doc-html r-recommended
0 upgraded, 45 newly installed, 0 to remove and 57 not upgraded.
Need to get 80.2 MB of archives.
After this operation, 195 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
########################################
```
* test:
```R
jpmena@LAPTOP-E2MJK1UO:~$ R

R version 4.1.2 (2021-11-01) -- "Bird Hippie"
Copyright (C) 2021 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

> quit()
Save workspace image? [y/n/c]: y
```
## Installer RStudio
```bash
jpmena@LAPTOP-E2MJK1UO:~$ rstudio
Command 'rstudio' not found, but can be installed with:
sudo snap install rstudio # Il propse ce mode d'installation
jpmena@LAPTOP-E2MJK1UO:~$ sudo snap install rstudio
error: This revision of snap "rstudio" was published using classic confinement and thus may perform
       arbitrary system changes outside of the security sandbox that snaps are usually confined to,
       which may put your system at risk.

       If you understand and want to proceed repeat the command including --classic. # il propose l'option classic
jpmena@LAPTOP-E2MJK1UO:~$ sudo snap install rstudio --classic
rstudio 2025.05.1-513 from Ubuntu High-Performance Computing (ubuntuhpcbot) installed
```
* Je teste:
  * malgré les erreurs en console ci dessous il me lance l'application Graphique sur mon Windows
```bash
jpmena@LAPTOP-E2MJK1UO:~$ rstudio
/snap/rstudio/19/electron-launch: line 22: /snap/rstudio/19/usr/lib/x86_64-linux-gnu/libgtk-3-0/gtk-query-immodules-3.0: No such file or directory
ERROR: /snap/rstudio/19/usr/lib/x86_64-linux-gnu/libgtk-3-0/gtk-query-immodules-3.0 exited abnormally with status 127
[9776:0719/104648.421748:ERROR:gl_factory.cc(102)] Requested GL implementation (gl=none,angle=none) not found in allowed implementations: [(gl=egl-angle,angle=default)].

[9776:0719/104648.429411:ERROR:viz_main_impl.cc(185)] Exiting GPU process due to errors during initialization

[9908:0719/104651.430615:ERROR:gl_factory.cc(102)] Requested GL implementation (gl=none,angle=none) not found in allowed implementations: [(gl=egl-angle,angle=default)].
[9908:0719/104651.434855:ERROR:viz_main_impl.cc(185)] Exiting GPU process due to errors during initialization
[9946:0719/104651.604566:ERROR:gl_factory.cc(102)] Requested GL implementation (gl=none,angle=none) not found in allowed implementations: [(gl=egl-angle,angle=default)].
[9946:0719/104651.626368:ERROR:viz_main_impl.cc(185)] Exiting GPU process due to errors during initialization
```