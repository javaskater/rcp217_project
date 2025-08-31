# installation de [Python sous Windows](https://www.python.org/downloads/)
* C'est la 3.13.15 que l'on installe (27.5. Mo)
## Virtual environments pour installer nos librairies de RCP217
* cf [le travail des Python Libs sous venv](./PYTHONLIBS.md) 
```powershell
PS C:\Users\jeanp\CONSULTANT> python -m venv env_python_for_projet_rcp217
PS C:\Users\jeanp\CONSULTANT> .\env_python_for_projet_rcp217\Scripts\activate
.\env_python_for_projet_rcp217\Scripts\activate : Impossible de charger le fichier
C:\Users\jeanp\CONSULTANT\env_python_for_projet_rcp217\Scripts\Activate.ps1, car l’exécution de scripts est désactivée
sur ce système. Pour plus d’informations, consultez about_Execution_Policies à l’adresse
https://go.microsoft.com/fwlink/?LinkID=135170.
Au caractère Ligne:1 : 1
+ .\env_python_for_projet_rcp217\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : Erreur de sécurité : (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
## problème Windows refuse par défaut l'exécution de scripts Powershell (résolu)
* [Comment autoriser les scripts powershell](https://casits.artsandsciences.fsu.edu/how-run-powershell-scripts-windows-11)
  * faire cela depuis une console d'admin [lien vers ouvrir une console d'admin (elle est sur fond bleu)](https://learn.microsoft.com/en-us/answers/questions/1338912/how-to-run-powershell-as-administrator)
  * Menu démarrer / Window Powershell / clic droit sur l'icône de la console / Run As Administrator
```powershell
PS C:\WINDOWS\system32> Set-ExecutionPolicy Unrestricted                                                                                                                                                                                        Modification de la stratégie d'exécution                                                                                La stratégie d’exécution permet de vous prémunir contre les scripts que vous jugez non fiables. En modifiant la         stratégie d’exécution, vous vous exposez aux risques de sécurité décrits dans la rubrique d’aide                        about_Execution_Policies à l'’adresse https://go.microsoft.com/fwlink/?LinkID=135170. Voulez-vous modifier la stratégie  d’'exécution ?                                                                                                           [O] Oui  [T] Oui pour tout  [N] Non  [U] Non pour tout  [S] Suspendre  [?] Aide (la valeur par défaut est « N ») : O 
``` 
* ça marche (console non admin déjà ouverte auparavant)
```powershell
PS C:\Users\jeanp\CONSULTANT> .\env_python_for_projet_rcp217\Scripts\activate
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> deactivate
PS C:\Users\jeanp\CONSULTANT> deactivate
PS C:\Users\jeanp\CONSULTANT> .\env_python_for_projet_rcp217\Scripts\activate
```
* une fois terminé passage en Restricted depuis la console bleue (admin Powershell)
```powershell
PS C:\WINDOWS\system32> Set-ExecutionPolicy Restricted                                                                                                                                                                                          Modification de la stratégie d'exécution                                                                                La stratégie d’exécution permet de vous prémunir contre les scripts que vous jugez non fiables. En modifiant la         stratégie d’exécution, vous vous exposez aux risques de sécurité décrits dans la rubrique d’aide                        about_Execution_Policies à l’adresse https://go.microsoft.com/fwlink/?LinkID=135170. Voulez-vous modifier la stratégie  d’exécution ?                                                                                                           [O] Oui  [T] Oui pour tout  [N] Non  [U] Non pour tout  [S] Suspendre  [?] Aide (la valeur par défaut est « N ») : O  
```
## Quelle version de pip dans l'environnement virtuel
```powershell
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> pip --version
pip 22.3 from C:\Users\jeanp\CONSULTANT\env_python_for_projet_rcp217\Lib\site-packages\pip (python 3.11)
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> pip3 --version
pip 22.3 from C:\Users\jeanp\CONSULTANT\env_python_for_projet_rcp217\Lib\site-packages\pip (python 3.11)
```
# Installation des [libraries de Serge Rosmoduc dans l'environnement virtuel](./PYTHONLIBS.md)
## installation de numpy
```powershell
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> pip install "numpy<2.0"
Collecting numpy<2.0
  Downloading numpy-1.26.4-cp311-cp311-win_amd64.whl (15.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.8/15.8 MB 16.8 MB/s eta 0:00:00
Installing collected packages: numpy
Successfully installed numpy-1.26.4

[notice] A new release of pip available: 22.3 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip
```
### on fait ce qu'il demande on passe de pip 22.3 à 25.2 uniquement dans notre environnement virtuel de travail
```powershell
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\jeanp\consultant\env_python_for_projet_rcp217\lib\site-packages (22.3)
Collecting pip
  Downloading pip-25.2-py3-none-any.whl (1.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 11.2 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.3
    Uninstalling pip-22.3:
      Successfully uninstalled pip-22.3
Successfully installed pip-25.2
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> pip --version n # on véridie la version de pip installé
pip 25.2 from C:\Users\jeanp\CONSULTANT\env_python_for_projet_rcp217\Lib\site-packages\pip (python 3.11) # la mise à jour de pip a affecté uniquement notre environnement virtuel (environnement de travail)
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> deactivate
PS C:\Users\jeanp\CONSULTANT> pip --version # dans l'installation générale 
pip 22.3 from C:\Python311\Lib\site-packages\pip (python 3.11) ## on est encore en version 22.3
PS C:\Users\jeanp\CONSULTANT> .\env_python_for_projet_rcp217\Scripts\activate # retour à notre environnement de travail
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT>
```
## Installation de la famille des torch (gros morceau)
```powershell
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> pip install torch=="2.2.2" torchvision=="0.17.2" torchaudio=="2.2.2"# gros morceau mais pas plus de 5 minutes
#######################################################################"
Installing collected packages: mpmath, typing-extensions, sympy, pillow, networkx, MarkupSafe, fsspec, filelock, jinja2, torch, torchvision, torchaudio
Successfully installed MarkupSafe-3.0.2 filelock-3.18.0 fsspec-2025.7.0 jinja2-3.1.6 mpmath-1.3.0 networkx-3.5 pillow-11.3.0 sympy-1.14.0 torch-2.2.2 torchaudio-2.2.2 torchvision-0.17.2 typing-extensions-4.14.1
```
## Installation de mathplotlib
```powershell
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> pip install matplotlib=="3.10.0"
################################################"
Installing collected packages: six, pyparsing, packaging, kiwisolver, fonttools, cycler, contourpy, python-dateutil, matplotlib
Successfully installed contourpy-1.3.3 cycler-0.12.1 fonttools-4.59.0 kiwisolver-1.4.8 matplotlib-3.10.0 packaging-25.0 pyparsing-3.2.3 python-dateutil-2.9.0.post0 six-1.17.0
```
## installation de scikit-learn
```powershell
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> pip install scikit-learn=="1.6.1"
###################################################""
Installing collected packages: threadpoolctl, scipy, joblib, scikit-learn
Successfully installed joblib-1.5.1 scikit-learn-1.6.1 scipy-1.16.1 threadpoolctl-3.6.0
```
## installation de ipykernel (gros morceau mais rapide)
* installe le noyau Jupyter
```powershell
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> pip install ipykernel=="6.29.5"
###################################################""
Installing collected packages: wcwidth, pywin32, pure-eval, traitlets, tornado, pyzmq, pygments, psutil, prompt_toolkit, platformdirs, parso, nest-asyncio, executing, decorator, debugpy, comm, colorama, asttokens, stack_data, matplotlib-inline, jupyter-core, jedi, ipython-pygments-lexers, jupyter-client, ipython, ipykernel
Successfully installed asttokens-3.0.0 colorama-0.4.6 comm-0.2.3 debugpy-1.8.15 decorator-5.2.1 executing-2.2.0 ipykernel-6.29.5 ipython-9.4.0 ipython-pygments-lexers-1.1.1 jedi-0.19.2 jupyter-client-8.6.3 jupyter-core-5.8.1 matplotlib-inline-0.1.7 nest-asyncio-1.6.0 parso-0.8.4 platformdirs-4.3.8 prompt_toolkit-3.0.51 psutil-7.0.0 pure-eval-0.2.3 pygments-2.19.2 pywin32-311 pyzmq-27.0.0 stack_data-0.6.3 tornado-6.5.1 traitlets-5.14.3 wcwidth-0.2.13
```
## installation des notebook Jupyter (oubli de Serge Rosmorduc)
* installe le jupyter Server et le JupyterLab
* assez rapide malgré la masse des installations car beaucoup déjà installé précédemment ...
```powershell
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> pip install notebook
####################################################################################""
Installing collected packages: webencodings, fastjsonschema, websocket-client, webcolors, urllib3, uri-template, types-python-dateutil, tinycss2, soupsieve, sniffio, send2trash, rpds-py, rfc3986-validator, rfc3339-validator, pyyaml, pywinpty, python-json-logger, pycparser, prometheus-client, pandocfilters, overrides, mistune, lark, jupyterlab-pygments, jsonpointer, json5, idna, h11, fqdn, defusedxml, charset_normalizer, certifi, bleach, babel, attrs, async-lru, terminado, rfc3987-syntax, requests, referencing, httpcore, cffi, beautifulsoup4, arrow, anyio, jupyter-server-terminals, jsonschema-specifications, isoduration, httpx, argon2-cffi-bindings, jsonschema, argon2-cffi, nbformat, nbclient, jupyter-events, nbconvert, jupyter-server, notebook-shim, jupyterlab-server, jupyter-lsp, jupyterlab, notebook
Successfully installed anyio-4.9.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 arrow-1.3.0 async-lru-2.0.5 attrs-25.3.0 babel-2.17.0 beautifulsoup4-4.13.4 bleach-6.2.0 certifi-2025.7.14 cffi-1.17.1 charset_normalizer-3.4.2 defusedxml-0.7.1 fastjsonschema-2.21.1 fqdn-1.5.1 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.10 isoduration-20.11.0 json5-0.12.0 jsonpointer-3.0.0 jsonschema-4.25.0 jsonschema-specifications-2025.4.1 jupyter-events-0.12.0 jupyter-lsp-2.2.6 jupyter-server-2.16.0 jupyter-server-terminals-0.5.3 jupyterlab-4.4.5 jupyterlab-pygments-0.3.0 jupyterlab-server-2.27.3 lark-1.2.2 mistune-3.1.3 nbclient-0.10.2 nbconvert-7.16.6 nbformat-5.10.4 notebook-7.4.4 notebook-shim-0.2.4 overrides-7.7.0 pandocfilters-1.5.1 prometheus-client-0.22.1 pycparser-2.22 python-json-logger-3.3.0 pywinpty-2.0.15 pyyaml-6.0.2 referencing-0.36.2 requests-2.32.4 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1 rfc3987-syntax-1.1.0 rpds-py-0.26.0 send2trash-1.8.3 sniffio-1.3.1 soupsieve-2.7 terminado-0.18.1 tinycss2-1.4.0 types-python-dateutil-2.9.0.20250708 uri-template-1.3.0 urllib3-2.5.0 webcolors-24.11.1 webencodings-0.5.1 websocket-client-1.8.0
```
# Tester les notebook Jupyter
```bash
.0 webcolors-24.11.1 webencodings-0.5.1 websocket-client-1.8.0
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> jupyter notebook
[I 2025-08-02 17:01:06.108 ServerApp] Extension package jupyter_server_terminals took 0.3397s to import
[I 2025-08-02 17:01:06.652 ServerApp] jupyter_lsp | extension was successfully linked.
[I 2025-08-02 17:01:06.668 ServerApp] jupyter_server_terminals | extension was successfully linked.
[I 2025-08-02 17:01:06.687 ServerApp] jupyterlab | extension was successfully linked.
[I 2025-08-02 17:01:06.700 ServerApp] notebook | extension was successfully linked.
[I 2025-08-02 17:01:06.715 ServerApp] Writing Jupyter server cookie secret to C:\Users\jeanp\AppData\Roaming\jupyter\runtime\jupyter_cookie_secret
[I 2025-08-02 17:01:08.189 ServerApp] notebook_shim | extension was successfully linked.
[I 2025-08-02 17:01:08.236 ServerApp] notebook_shim | extension was successfully loaded.
[I 2025-08-02 17:01:08.240 ServerApp] jupyter_lsp | extension was successfully loaded.
[I 2025-08-02 17:01:08.240 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2025-08-02 17:01:08.246 LabApp] JupyterLab extension loaded from C:\Users\jeanp\CONSULTANT\env_python_for_projet_rcp217\Lib\site-packages\jupyterlab
[I 2025-08-02 17:01:08.246 LabApp] JupyterLab application directory is C:\Users\jeanp\CONSULTANT\env_python_for_projet_rcp217\share\jupyter\lab
[I 2025-08-02 17:01:08.246 LabApp] Extension Manager is 'pypi'.
[I 2025-08-02 17:01:08.352 ServerApp] jupyterlab | extension was successfully loaded.
[I 2025-08-02 17:01:08.355 ServerApp] notebook | extension was successfully loaded.
[I 2025-08-02 17:01:08.371 ServerApp] Serving notebooks from local directory: C:\Users\jeanp\CONSULTANT
[I 2025-08-02 17:01:08.371 ServerApp] Jupyter Server 2.16.0 is running at:
[I 2025-08-02 17:01:08.371 ServerApp] http://localhost:8888/tree?token=4ffa15497d4177a100b32a62d8383b796cf2ce50fa406a07
[I 2025-08-02 17:01:08.371 ServerApp]     http://127.0.0.1:8888/tree?token=4ffa15497d4177a100b32a62d8383b796cf2ce50fa406a07
[I 2025-08-02 17:01:08.371 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2025-08-02 17:01:08.550 ServerApp]

    To access the server, open this file in a browser:
        file:///C:/Users/jeanp/AppData/Roaming/jupyter/runtime/jpserver-20660-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/tree?token=4ffa15497d4177a100b32a62d8383b796cf2ce50fa406a07
        http://127.0.0.1:8888/tree?token=4ffa15497d4177a100b32a62d8383b796cf2ce50fa406a07
[I 2025-08-02 17:01:10.354 ServerApp] Skipped non-installed server(s): bash-language-server, dockerfile-language-server-nodejs, javascript-typescript-langserver, jedi-language-server, julia-language-server, pyright, python-language-server, python-lsp-server, r-languageserver, sql-language-server, texlab, typescript-language-server, unified-language-server, vscode-css-languageserver-bin, vscode-html-languageserver-bin, vscode-json-languageserver-bin, yaml-language-server
```
## Suite à installations sous Powershell
* on a un nouveau répertoire sur le FileSystem Windows et qui contient tout notre environnement virtuel Python
```powershell
PS C:\Users\jeanp> cd .\CONSULTANT\env_python_for_projet_rcp217\
PS C:\Users\jeanp\CONSULTANT\env_python_for_projet_rcp217> dir


    Répertoire : C:\Users\jeanp\CONSULTANT\env_python_for_projet_rcp217 #notre répertoire qui contient l'environnement virtue


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        02/08/2025     16:58                etc
d-----        26/07/2025     17:45                Include
d-----        26/07/2025     17:45                Lib
d-----        02/08/2025     16:58                Scripts
d-----        02/08/2025     16:58                share
-a----        26/07/2025     17:45            213 pyvenv.cfg
```
* me propose le navigateur à démarrer vers l'URL *http://localhost:8888/tree*
* par défaut prend pour arborescence le répertoire dans lequel j'ai démarré le Jupyter
```python
import torch
```
* ne crée pas d'erreur dans le nouveau notebook (le serveur est bien démarré dans l'environnement virtuel)
```python
import torch2
```
* génère bien une erreur
## Un notebook comme au CNAM
* Menu View / Open Jupyter Lab
## Arrêter
* CTRL + C s'arrête bien tout de suite contrairement à [WSL](PYTHONLIBSWSL.md)
# Quitter l'environnement Virtualisé
* dans la console powershell normale
```powershell
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> deactivate
PS C:\Users\jeanp\CONSULTANT>
```
* dans la console powershell / admin (start as administrator)
```powershell
PS C:\WINDOWS\system32> Set-ExecutionPolicy Restricted                                                                                                                                                                                                                                                                                                                                                                     Modification de la stratégie d'exécution                                                                                                                                                                           La stratégie d’exécution permet de vous prémunir contre les scripts que vous jugez non fiables. En modifiant la stratégie d’exécution, vous vous exposez aux risques de sécurité décrits dans la rubrique d’aide   about_Execution_Policies à l’adresse https://go.microsoft.com/fwlink/?LinkID=135170. Voulez-vous modifier la stratégie d’exécution ?                                                                               [O] Oui  [T] Oui pour tout  [N] Non  [U] Non pour tout  [S] Suspendre  [?] Aide (la valeur par défaut est « N ») : O   
```
* on ne peut plus lancer le passage en environnement virtualisé python dans la console normale (Base de Registre modifiée)
  * exit pour quitter une console powershell
## ([support de l'environnement virtualisé ?](https://code.visualstudio.com/docs/python/environments))
* comme indiqué dans le [lien](https://code.visualstudio.com/docs/python/environments)
* CTRL + SHIFT + P (Ouvrir la Command Palette)
  * Dans la Command Palette entrer **python Select Interpreter** (il autocomplète attention les majuscules sont importantes)
  * sélectionner le virtual env
* Tester avec un import d'une librairie type pytorch (todo)