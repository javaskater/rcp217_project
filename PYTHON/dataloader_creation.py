from torch.utils.data import Dataset, DataLoader
from torch import FloatTensor, IntTensor
import os
import re
import csv

class TimeSeriesDatasetForPCoefficients(Dataset):
    def __init__(self, list_of_pathes_to_the_timeseries_files: list):
        super().__init__()
        self.X = [] # les Time series
        self.y = [] # le coefficient p correspondant
        for path_to_the_timeseries_files in list_of_pathes_to_the_timeseries_files:
            for fichier_time_serie_name in os.listdir(path_to_the_timeseries_files):
                if fichier_time_serie_name.endswith(".csv"):
                    coeff_pq_search = re.search('ar_([0-9]{1})__ma_([0-9]{1})', fichier_time_serie_name, re.IGNORECASE)
                    if coeff_pq_search:
                        p_str = coeff_pq_search.group(1)
                        p = int(p_str)
                        q_str = coeff_pq_search.group(2)
                        q = int(q_str)

                        chemin_complet_fichier_time_serie = os.path.join(path_to_the_timeseries_files, fichier_time_serie_name)
                        print(f"[TimeSeriesDatasetForPCoefficients: init] fichier trouvé {chemin_complet_fichier_time_serie} avec pattern pour p oefficient: {p} et pour q coefficient: {q}")
                        with open(chemin_complet_fichier_time_serie, mode ='r')as file:
                            csvFile = csv.reader(file, delimiter =';')
                            next(csvFile) # skip the header
                            for ligne_time_serie_str in csvFile:
                                ligne_time_serie = FloatTensor(list(map(float, ligne_time_serie_str)))
                                print(ligne_time_serie)
                                self.X.append(ligne_time_serie)
                        p_tensor = IntTensor([p]) # Ce doit être un tenseur avec une seule donnée: l'ordre attenduexit()

                        self.y.append(p_tensor)

    def __len__(self):
        assert len(self.X) == len(self.y)
        return len(self.y)
    
    def __getitem__(self, index):
        assert index < len(self.y)
        return self.X[index], self.y[index]
    
if __name__ == '__main__':
    data_train = TimeSeriesDatasetForPCoefficients(['/home/jpmena/CONSULTANT/CNAM/rcp217_project/R/ts_generees_28082025'])
    print(f"[main] la taille de notre data train est {len(data_train)}")
    data_train_loader = DataLoader(data_train, batch_size=50, shuffle=True)
    print(len(data_train_loader))