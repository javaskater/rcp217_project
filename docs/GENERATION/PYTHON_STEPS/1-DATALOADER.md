
# Préparation des données
* on supprime la partie .csv.ZoneIDentifier
```bash
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project$ cd R/ts_generees_29072025/
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/R/ts_generees_29072025$ mv ts_generees_29072025/*.csv .
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/R/ts_generees_29072025$ rm -rf ts_generees_29072025
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/R/ts_generees_29072025$ 
```
* on met le répertoire ts_generes* dans le .gitignore
# Créer un Dataloader de nos timeseries
* [cf. accordeon tab *Creating Custom Datasets in PyTorch*](https://www.digitalocean.com/community/tutorials/dataloaders-abstractions-pytorch)
* todo: voir dans le TP des vidéos (il utilise [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) qui retourne des arrays pas des DataFrame)
## R2cupérer tous les fichiers csv
* en environnement virtualisé le chemin relatif ne fonctionne pas, on est obligé de mettre un chemin absolu
```python
if __name__ == '__main__':
    data_train = TimeSeriesDatasetForPCoefficients('/home/jpmena/CONSULTANT/CNAM/rcp217_project/R/ts_generees_29072025')
    #data_train_loader = DataLoader(data_train, batch_size=50, shuffle=True)
    #print(len(data_train))
```
* ce qui donne
```bash
# on est dans l'environnement virtuel où torch est connu
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/PYTHON$ python dataloader_creation.py  | wc -l
100 # on retrouve bien nos 100 time series générées
```
* [numpy](https://blog.finxter.com/5-best-ways-to-convert-csv-data-to-floats-in-python/#:~:text=The%20genfromtxt()%20function%20can,defined%20by%20the%20dtype%20parameter.&text=The%20code%20uses%20NumPy's%20genfromtxt,into%20an%20array%20of%20floats.) permet de convertir des données csv en float cf [usage de map in python](https://www.geeksforgeeks.org/python/python-map-function/)
# TODO 
* utiliser les mêmes DataSet pour le p comme pour le q
* prendre une liste de chemin (mes diférrentes initialisations)

# à 13h04 le 04/08/2025 notre Dataloader fonctionne