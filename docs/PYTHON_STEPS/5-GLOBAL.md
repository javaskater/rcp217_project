# Le code est sous 
* [Module Project16 (sous forme de module PyTorch)](../../PYTHON/projetct16_module.py)
# Step1n (passage de 1 times serie à 1000 points à 300 series à 100 datas)
* Testé à 15:30 le 27/08/2025
```bash
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/PYTHON$ python projetct16_module.py 
[main] Calling Project16 with kernel 10
[Project16/forward] after first convolution and relu shape of x torch.Size([1, 300, 100])
torch.Size([1, 300, 100])
```
# TODO Resnet steps
* Pour la construction de chaque RESNET Step cf. [doc associée](./2-RESNET.md)
## 4 Resnet Step de kernel 10

* à la fin on a 300 feature maps de taille 100 - 4*9 = 64
## 6 Resnet Steps de kernel 1

* à la fin on a 300 feature maps de taille 64 - 6*0 = 64
## Résultat après les RESNET Blocs
```bash
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/PYTHON$ python projetct16_module.py 
[main] Calling Project16 with kernel 10
[Project16/forward] after first convolution and relu shape of x torch.Size([1, 300, 100])
[ResNet1D/forward] after CONV shape of x torch.Size([1, 300, 91])
[ResNet1D/forward] after BatcNorm shape of x torch.Size([1, 300, 91])
[ResNet1D/forward] after RELU shape of x torch.Size([1, 300, 91])
[ResNet1D/forward] after CONV shape of x torch.Size([1, 300, 82])
[ResNet1D/forward] after BatcNorm shape of x torch.Size([1, 300, 82])
[ResNet1D/forward] after RELU shape of x torch.Size([1, 300, 82])
[ResNet1D/forward] after CONV shape of x torch.Size([1, 300, 73])
[ResNet1D/forward] after BatcNorm shape of x torch.Size([1, 300, 73])
[ResNet1D/forward] after RELU shape of x torch.Size([1, 300, 73])
[ResNet1D/forward] after CONV shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after BatcNorm shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after RELU shape of x torch.Size([1, 300, 64])
[Project16/forward] after 4 RESNET1D Blocks of kernel 10 shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after CONV shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after BatcNorm shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after RELU shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after CONV shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after BatcNorm shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after RELU shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after CONV shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after BatcNorm shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after RELU shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after CONV shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after BatcNorm shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after RELU shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after CONV shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after BatcNorm shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after RELU shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after CONV shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after BatcNorm shape of x torch.Size([1, 300, 64])
[ResNet1D/forward] after RELU shape of x torch.Size([1, 300, 64])
[Project16/forward] after 6 RESNET1D Blocks of kernel 1 shape of x torch.Size([1, 300, 64])
torch.Size([1, 300, 64])
```
# Dernier step 
* (passer de 300 de taille 64 à 10 feature maps de taille 64 - 9 = 55)
* faire la moyenne sur chaque feature map et sortir un tenseur de taille (batch size, 10)
* cf. [documentation dédiée de l'étape 4](./4-AVERAGING.md)
# Softmax
* ajouter une couche de Softmax dans le module principal [fin du PROJECT 16](../../PYTHON/projetct16_module.py)
* [exemple de l'utilisation du softmax](https://how.dev/answers/what-is-pytorch-softmax)
# TODO Erreur
# TODO training