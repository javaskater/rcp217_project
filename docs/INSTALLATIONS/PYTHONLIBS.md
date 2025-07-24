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
## [Créer et activer un environnement virtuel](https://docs.python.org/3/tutorial/venv.html) 
* Mettre plein de répertoires en .gitignore (todo)
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
## TODO torch qui est un gros morceau
```
# Ajout d'extension à Visual Studio Code