# installation de librairies Python sous Linux
* Dans le [TP1 du CNAM (lien JupyterHub)](https://jhub3.cnam.fr/user/24592/lab/tree/MonDossier/RCP217/TP1_03022025/README.md)
  * Serge Rosmorduc proposait d'installer les extensions suivantes dans un environnement virtuel
```bash
 pip install "numpy<2.0"
 pip install torch=="2.2.2" torchvision=="0.17.2" torchaudio=="2.2.2"
 pip install matplotlib=="3.10.0"
 pip install scikit-learn=="1.6.1"
 pip install ipykernel=="6.29.5"
```
## [Créer et activer un environnement virtuel](https://docs.python.org/3/tutorial/venv.html) sur le PC de travail
* Mettre plein le répertoire *env_python_for_projet_rcp217* en .gitignore. OK
```bash
jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ python3 --version
Python 3.12.3 # version actuelle de Python sur mon Socle Linux du travail
jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ python3 -m venv env_python_for_projet_rcp217
jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ source env_python_for_projet_rcp217/bin/activate
(env_python_for_projet_rcp217) jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ 
# on peut utiliser indifféremment pip ou pip3
(env_python_for_projet_rcp217) jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ pip --version
pip 24.0 from /home/jmena01/CONSULTANT/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/pip (python 3.12)
(env_python_for_projet_rcp217) jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ pip3 --version
pip 24.0 from /home/jmena01/CONSULTANT/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/pip (python 3.12)
```
## on installe les librairies dans l'environnement virtuel
```bash
(env_python_for_projet_rcp217) jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ pip install "numpy<2.0"
Collecting numpy<2.0
  Downloading numpy-1.26.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (61 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.0/61.0 kB 1.9 MB/s eta 0:00:00
Downloading numpy-1.26.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.0/18.0 MB 40.4 MB/s eta 0:00:00
Installing collected packages: numpy
Successfully installed numpy-1.26.4
## torch qui est un gros morceau
(env_python_for_projet_rcp217) jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ pip install torch=="2.2.2" torchvision=="0.17.2" torchaudio=="2.2.2"
############################################################################# Beaucoup de téléchargements longs
Successfully installed MarkupSafe-3.0.2 filelock-3.18.0 fsspec-2025.7.0 jinja2-3.1.6 mpmath-1.3.0 networkx-3.5 nvidia-cublas-cu12-12.1.3.1 nvidia-cuda-cupti-cu12-12.1.105 nvidia-cuda-nvrtc-cu12-12.1.105 nvidia-cuda-runtime-cu12-12.1.105 nvidia-cudnn-cu12-8.9.2.26 nvidia-cufft-cu12-11.0.2.54 nvidia-curand-cu12-10.3.2.106 nvidia-cusolver-cu12-11.4.5.107 nvidia-cusparse-cu12-12.1.0.106 nvidia-nccl-cu12-2.19.3 nvidia-nvjitlink-cu12-12.9.86 nvidia-nvtx-cu12-12.1.105 pillow-11.3.0 sympy-1.14.0 torch-2.2.2 torchaudio-2.2.2 torchvision-0.17.2 typing-extensions-4.14.1
(env_python_for_projet_rcp217) jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ pip install matplotlib=="3.10.0"
################################""
Successfully installed contourpy-1.3.2 cycler-0.12.1 fonttools-4.59.0 kiwisolver-1.4.8 matplotlib-3.10.0 packaging-25.0 pyparsing-3.2.3 python-dateutil-2.9.0.post0 six-1.17.0
(env_python_for_projet_rcp217) jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ pip install scikit-learn=="1.6.1"
###################################
Successfully installed joblib-1.5.1 scikit-learn-1.6.1 scipy-1.16.0 threadpoolctl-3.6.0
# Gros morceau (finalement rapide)
(env_python_for_projet_rcp217) jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ pip install ipykernel=="6.29.5"
####################################
Successfully installed asttokens-3.0.0 comm-0.2.2 debugpy-1.8.15 decorator-5.2.1 executing-2.2.0 ipykernel-6.29.5 ipython-9.4.0 ipython-pygments-lexers-1.1.1 jedi-0.19.2 jupyter-client-8.6.3 jupyter-core-5.8.1 matplotlib-inline-0.1.7 nest-asyncio-1.6.0 parso-0.8.4 pexpect-4.9.0 platformdirs-4.3.8 prompt_toolkit-3.0.51 psutil-7.0.0 ptyprocess-0.7.0 pure-eval-0.2.3 pygments-2.19.2 pyzmq-27.0.0 stack_data-0.6.3 tornado-6.5.1 traitlets-5.14.3 wcwidth-0.2.13
## La commande jupyter run bloque (ne fait rien terminer avec Ctrl + D)
```
## [Jouer avec l'environnement virtualisé](https://python.land/virtual-environments/virtualenv)
```bash
# entrer dans l'environnement virtualisé
jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ source env_python_for_projet_rcp217/bin/activate
# sortir de l'environnement virtualisé
(env_python_for_projet_rcp217) jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ deactivate
```
## est ce que ce les Jupyter Notebooks sont inclus ?
* Non il faut passer une commande supplémentaire [pip install notebook](https://www.codecademy.com/article/how-to-use-jupyter-notebooks)
```bash
## Oublié de Serge Rosmorduc
(env_python_for_projet_rcp217) jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ pip install notebook
############################################################################
Successfully installed anyio-4.9.0 argon2-cffi-25.1.0 argon2-cffi-bindings-21.2.0 arrow-1.3.0 async-lru-2.0.5 attrs-25.3.0 babel-2.17.0 beautifulsoup4-4.13.4 bleach-6.2.0 certifi-2025.7.14 cffi-1.17.1 charset_normalizer-3.4.2 defusedxml-0.7.1 fastjsonschema-2.21.1 fqdn-1.5.1 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.10 isoduration-20.11.0 json5-0.12.0 jsonpointer-3.0.0 jsonschema-4.25.0 jsonschema-specifications-2025.4.1 jupyter-events-0.12.0 jupyter-lsp-2.2.6 jupyter-server-2.16.0 jupyter-server-terminals-0.5.3 jupyterlab-4.4.5 jupyterlab-pygments-0.3.0 jupyterlab-server-2.27.3 lark-1.2.2 mistune-3.1.3 nbclient-0.10.2 nbconvert-7.16.6 nbformat-5.10.4 notebook-7.4.4 notebook-shim-0.2.4 overrides-7.7.0 pandocfilters-1.5.1 prometheus-client-0.22.1 pycparser-2.22 python-json-logger-3.3.0 pyyaml-6.0.2 referencing-0.36.2 requests-2.32.4 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1 rfc3987-syntax-1.1.0 rpds-py-0.26.0 send2trash-1.8.3 setuptools-80.9.0 sniffio-1.3.1 soupsieve-2.7 terminado-0.18.1 tinycss2-1.4.0 types-python-dateutil-2.9.0.20250708 uri-template-1.3.0 urllib3-2.5.0 webcolors-24.11.1 webencodings-0.5.1 websocket-client-1.8.0
# on lance
(env_python_for_projet_rcp217) jmena01@m077-2281091:~/CONSULTANT/rcp217_project$ jupyter notebook
[I 2025-07-25 09:53:03.509 ServerApp] jupyter_lsp | extension was successfully linked.
[I 2025-07-25 09:53:03.513 ServerApp] jupyter_server_terminals | extension was successfully linked.
[I 2025-07-25 09:53:03.517 ServerApp] jupyterlab | extension was successfully linked.
[I 2025-07-25 09:53:03.519 ServerApp] notebook | extension was successfully linked.
[I 2025-07-25 09:53:03.520 ServerApp] Writing Jupyter server cookie secret to /home/jmena01/.local/share/jupyter/runtime/jupyter_cookie_secret
[I 2025-07-25 09:53:03.679 ServerApp] notebook_shim | extension was successfully linked.
[I 2025-07-25 09:53:03.689 ServerApp] notebook_shim | extension was successfully loaded.
[I 2025-07-25 09:53:03.690 ServerApp] jupyter_lsp | extension was successfully loaded.
[I 2025-07-25 09:53:03.691 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2025-07-25 09:53:03.692 LabApp] JupyterLab extension loaded from /home/jmena01/CONSULTANT/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/jupyterlab
[I 2025-07-25 09:53:03.692 LabApp] JupyterLab application directory is /home/jmena01/CONSULTANT/rcp217_project/env_python_for_projet_rcp217/share/jupyter/lab
[I 2025-07-25 09:53:03.692 LabApp] Extension Manager is 'pypi'.
[I 2025-07-25 09:53:03.741 LabApp] Extensions will be fetched using proxy, proxy host and port: ('proxy.infra.dgfip', '3128')
[I 2025-07-25 09:53:03.743 ServerApp] jupyterlab | extension was successfully loaded.
[I 2025-07-25 09:53:03.746 ServerApp] notebook | extension was successfully loaded.
[I 2025-07-25 09:53:03.746 ServerApp] Serving notebooks from local directory: /home/jmena01/CONSULTANT/rcp217_project
[I 2025-07-25 09:53:03.746 ServerApp] Jupyter Server 2.16.0 is running at:
[I 2025-07-25 09:53:03.746 ServerApp] http://localhost:8888/tree?token=cb9ed5c5f107988840436fa358b23a747bd1a0e545d0d0ea
[I 2025-07-25 09:53:03.746 ServerApp]     http://127.0.0.1:8888/tree?token=cb9ed5c5f107988840436fa358b23a747bd1a0e545d0d0ea
[I 2025-07-25 09:53:03.746 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2025-07-25 09:53:03.824 ServerApp] 
    
    To access the server, open this file in a browser:
        file:///home/jmena01/.local/share/jupyter/runtime/jpserver-39828-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/tree?token=cb9ed5c5f107988840436fa358b23a747bd1a0e545d0d0ea
        http://127.0.0.1:8888/tree?token=cb9ed5c5f107988840436fa358b23a747bd1a0e545d0d0ea
[I 2025-07-25 09:53:04.172 ServerApp] Skipped non-installed server(s): bash-language-server, dockerfile-language-server-nodejs, javascript-typescript-langserver, jedi-language-server, julia-language-server, pyright, python-language-server, python-lsp-server, sql-language-server, texlab, typescript-language-server, unified-language-server, vscode-css-languageserver-bin, vscode-html-languageserver-bin, vscode-json-languageserver-bin, yaml-language-server
```
* ouvre automatiquement Firefox sur http://localhost:8888/tree
  * Faire un *Start Jupyter Lab* pour avoir la configuration comme au CNAM
* pour fermer *CTRL +  C* et confirmation **y**
# Ajout d'extension à Visual Studio Code 
* L'extension Python
## ([support de l'environnement virtualisé ?](https://code.visualstudio.com/docs/python/environments))
* comme indiqué dans le [lien](https://code.visualstudio.com/docs/python/environments)
* CTRL + SHIFT + P (Ouvrir la Command Palette)
  * Dans la Command Palette entrer **python Select Interpreter** (il autocomplète attention les majuscules sont importantes)
  * sélectionner le virtual env
* Tester avec un import d'une librairie type pytorch (todo)
# [Installation des extensions pour VSCode](https://code.visualstudio.com/docs/languages/python)
## installation de l'extension Python pour VSCode
* il s'agit de la [Microsoft Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
# installation des librairies Python Sous Windows dans environnement virtuel
* cf [Python sous Windows](./PYTHONWINDOWS.md) OK cf. lien juste avant