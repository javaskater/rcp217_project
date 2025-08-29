# pas de réponse lors du [TP10](https://jhub3.cnam.fr/user/24592/lab/tree/MonDossier/RCP217/TP10_07042025/TP02_corrige.ipynb)
* on est sous Keras et non Pythorch et on accepte les numpy arrays
# Question posée au professeur le 28/08/2025 18:45
J’ai mis le code avec ma documentation sous GitHub juste pour la livraison (après je retourne sur monrepository privé sous GitLab)

## Problème restant:
J’ai posé mon problème en Markdown [sur mon projet GitHub](https://github.com/javaskater/rcp217_project/blob/main/docs/PYTHON_STEPS/5-GLOBAL.md#le-code-python)


Il semble que mon problème vient de ce que fournit le DataLoader en fonction de ce que fournit le Dataset (cf [lien GitHub sur le code du DataSet](https://github.com/javaskater/rcp217_project/blob/main/PYTHON/dataloader_creation.py)) :

Je l’ai résolu pour la partie données time serie mais le problème se pose pour les label (entier de 0 à 9) ?

### Question subsidiaire : 
en sortie du Softmax on a 10 probabilitées

La CrossErrorEntropy prend ces 10 sorties de Softmax en entrée d’un côté et la valeur du label de l’autre (un entier entre 0 et 9). Ne devrait t’on pas transformer cette valeur de label en encodage one-hot ?
(*D'après [la réponse 4 de ce Post Stackoverflow](https://stackoverflow.com/questions/63825841/attributeerror-tuple-has-no-attribute-to) on nous propose de faire un one-hot vector ?*)