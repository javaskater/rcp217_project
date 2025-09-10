# my previously created modules
from dataloader_creation import TimeSeriesDatasetForPCoefficients # The Datasource (for training of for validation)
from torch.utils.data import DataLoader # The Pytorch Dataloader for the Datasource (for training of for validation)
from projetct16_module import Project16 # The model

# standard PyTorch
import torch.nn as nn
import torch.optim as optim
import torch

# standard Python
import collections
import datetime  # for timestamping our training evolution

# From the Manning book's source code https://github.com/deep-learning-with-pytorch/dlwpt-code/blob/master/p1ch8/1_convolution.ipynb
def validate(model, train_loader, val_loader):
    accdict = {}
    for name, loader in [("train", train_loader), ("val", val_loader)]:
        correct = 0
        total = 0

        with torch.no_grad():
            for series, labels in loader:
                series = series.to(device=device)
                labels = torch.tensor(labels).to(device=device)
                series2D = series.unsqueeze(1) # add the one channel dimension betwwen the batch_size dimension and the serie's length
                outputs = model(series2D) 
                _, predicted = torch.max(outputs, dim=1) # <1>
                total += labels.shape[0]
                correct += int((predicted == labels).sum())

        print("Accuracy {}: {:.2f}".format(name , correct / total))
        accdict[name] = correct / total
    return accdict

if __name__ == '__main__':
    data_train = TimeSeriesDatasetForPCoefficients(['/home/jpmena/CONSULTANT/CNAM/rcp217_project/R/ts_generees_28082025'])
    train_loader = DataLoader(data_train, batch_size=50, shuffle=True)
    data_val = TimeSeriesDatasetForPCoefficients(['/home/jpmena/CONSULTANT/CNAM/rcp217_project/R/ts_generees_29082025'])
    val_loader = DataLoader(data_val, batch_size=50, shuffle=True)
    device = (torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu'))
    print(f"Training on device {device}.")
    
    loaded_model = Project16().to(device=device)
    data_path = '../R/' # at the same level as my time series
    loaded_model.load_state_dict(torch.load(data_path+ 'time_series_p_cefficients.pt',map_location=device))
    optimizer = optim.SGD(loaded_model.parameters(), lr=1e-2)  #  <3>
    loss_fn = nn.CrossEntropyLoss()  #  <4>
    
    # we launch the validation on the training set and the validation set only to compare
    all_acc_dict = collections.OrderedDict()
    all_acc_dict["baseline"] = validate(loaded_model, train_loader, val_loader)