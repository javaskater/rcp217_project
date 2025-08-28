# Choix du projet 16
* [page des choix](./docs/CHOIX.md)
* [le pdf de l'article sur lequel s'appuie le projet](./docs/1804.04299v2.pdf)
# installation de l'environnement
## Python via vritual environment en suivant les librairies recommandées par Serge RosMorduc
* [sous Ubuntu 24.04 Pure (poste de travail au bureau)](./docs/INSTALLATIONS/PYTHONLIBS.md)
* [sur mon PC Windows 11 sous Windows Subsystem For Linux (WSL) / Ubuntu passée de 22 à 24](./docs/INSTALLATIONS/PYTHONLIBSWSL.md)
  * [pour le passage de Ubuntu 22 à Ubuntu 24 sous WSL](./docs/WSL/Ubuntu.md) 
* [Sur mon PC Windows 11 en restant purement sous Windows](./docs/INSTALLATIONS/PYTHONWINDOWS.md)
## R
* [sur mon PC Windows sous WSL et purement sous Windows](./docs/INSTALLATIONS/R.md)
# Partie génération des time series sous R
* [La doc de la génération sous R avec mes liens vers les scripts R](./docs/GENERATION/R.md)
  * il y a [l'essai de trouver manuellement des coefficients dans le cercle unité](./R/testGenerateARMASeries_methode1.R)
    * ne fonctionne pas
  * la méthode brutale de [générer des coefficients aléatoires tant que la série ne se crée pas](./R/testGenerateARMASeries_methode2.R)
    * méthode que j'ai adoptée pour la [génération finale](./R/GenerateARMASeries_final.R) mais qui prend plus de 10 minute pour générer 100 séries 
# Partie Python: chargement et réseau
* toute la documentation et les scripts associés se trouvent dans [](./docs/PYTHON_STEPS/5-GLOBAL.md)
  * liens à suivre qui ramènent vers les scripts et les autres pages
  * Question à poser au professeur sur l'entrainement et la validation (to ask)
    * à priori un problème sur la sortie du Dataloader 
* Noter [le lien vers la lecture préliminaire de mon livre Manning sur PyTorch](./docs/PYTHON_STEPS/0-PYTHON_LECTURE.md)