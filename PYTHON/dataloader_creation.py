from torch.utils.data import Dataset, DataLoader
import os
import re
import csv

class TimeSeriesDatasetForPCoefficients(Dataset):
    def __init__(self, path_to_the_timeseries_files: str):
        super().__init__()
        self.X = [] # les Time series
        self.y = [] # le coefficient p correspondant
        for fichier_time_serie_name in os.listdir(path_to_the_timeseries_files):
            if fichier_time_serie_name.endswith(".csv"):
                coeff_pq_search = re.search('ar_([0-9]{1})__ma_([0-9]{1})', fichier_time_serie_name, re.IGNORECASE)
                if coeff_pq_search:
                    p = coeff_pq_search.group(1)
                    q = coeff_pq_search.group(2)
                    chemin_complet_fichier_time_serie = os.path.join(path_to_the_timeseries_files, fichier_time_serie_name)
                    print(f"[TimeSeriesDatasetForPCoefficients: init] fichier trouvé {chemin_complet_fichier_time_serie} avec pattern pour p oefficient: {p} et pour q coefficient: {q}")
                    with open(chemin_complet_fichier_time_serie, mode ='r')as file:
                        csvFile = csv.reader(file, delimiter =';')
                        next(csvFile) # skip the header
                        for ligne_time_serie_str in csvFile:
                            ligne_time_serie = list(map(float, ligne_time_serie_str))
                            print(ligne_time_serie)
                            self.X.append(ligne_time_serie)
                    self.y.append(p)

    def __len__(self):
        assert len(self.X) == len(self.y)
        return len(self.y)
    
    def __getitem__(self, index):
        assert index < len(self.y)
        return self.X[index], self.y[index]
    
if __name__ == '__main__':
    data_train = TimeSeriesDatasetForPCoefficients('/home/jpmena/CONSULTANT/CNAM/rcp217_project/R/ts_generees_29072025')
    print(f"[main] la taille de notre data train est {len(data_train)}")
    data_train_loader = DataLoader(data_train, batch_size=50, shuffle=True)
    print(len(data_train_loader))