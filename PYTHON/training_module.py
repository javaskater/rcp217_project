import datetime  # for timestamping our training evolution
from dataloader_creation import TimeSeriesDatasetForPCoefficients # The Datasource (for training of for validation)
from torch.utils.data import DataLoader # The Pytorch Dataloader for the Datasource (for training of for validation)
from projetct16_module import Project16 # The model

# standard PyTorch
import torch.nn as nn
import torch.optim as optim
import torch

# From the Manning book's source code https://github.com/deep-learning-with-pytorch/dlwpt-code/blob/master/p1ch8/1_convolution.ipynb
def training_loop(n_epochs, optimizer, model, loss_fn, train_loader, device):
    for epoch in range(1, n_epochs + 1):  # <2>
        loss_train = 0.0
        for series, labels in train_loader:  # <3>
            series = series.to(device)
            labels = torch.IntTensor(labels).to(device=device)
            
            outputs = model(series)  # <4>
            
            loss = loss_fn(outputs, labels)  # <5>

            optimizer.zero_grad()  # <6>
            
            loss.backward()  # <7>
            
            optimizer.step()  # <8>

            loss_train += loss.item()  # <9>

        if epoch == 1 or epoch % 5 == 0:
            print('{} Epoch {}, Training loss {}'.format(
                datetime.datetime.now(), epoch,
                loss_train / len(train_loader)))  # <10>

if __name__ == '__main__':
    data_train = TimeSeriesDatasetForPCoefficients(['/home/jpmena/CONSULTANT/CNAM/rcp217_project/R/ts_generees_28082025'])
    train_loader = DataLoader(data_train, batch_size=50, shuffle=True)
    device = (torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu'))
    print(f"Training on device {device}.")
    model = Project16().to(device=device)  # We use the Datanetwork just created 
    optimizer = optim.SGD(model.parameters(), lr=1e-2)  #  <3>
    loss_fn = nn.CrossEntropyLoss()  #  <4>

    training_loop(  # <5>
        n_epochs = 50,
        optimizer = optimizer,
        model = model,
        loss_fn = loss_fn,
        train_loader = train_loader,
        device = device
    )
    # we save the model coefficients to be reused later (in the validation_module.py)
    data_path = '../R/' # at the same level as my time series
    torch.save(model.state_dict(), data_path + 'time_series_p_cefficients.pt')