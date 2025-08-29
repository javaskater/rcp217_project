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
# Resnet steps
* Pour la construction de chaque RESNET Step cf. [doc associée](./2-RESNET.md)
## 4 Resnet Step de kernel 10

* à la fin on a 300 feature maps de taille 100 - 4*9 = 64
## 6 Resnet Steps de kernel 1

* à la fin on a 300 feature maps de taille 64 - 6*0 = 64
## Résultat après les RESNET Blocs
```bash
# passage en environnement virtualisé PyTorch
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project$ source env_python_for_projet_rcp217/bin/activate
# lancement de la partie main dans le code du module
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
# training (en cours)
## Erreur CrossEntropyLoss
* dois-je passer en one-hot encoding pour associer avec le SoftMax
  * non d'après [l'étude du livre Manning (vers la fin page 269)](./0-PYTHON_LECTURE.md) et [raponse de Vikas dans ce forum PyTorch](https://discuss.pytorch.org/t/is-this-the-right-way-to-use-cross-entropyloss/63066)
> Your labels are single values in {0, 1, 2}, that is, they are integer categorical labels.
## Suivre l'exemple du livre
* cf. [lecture livre Manning au sujet de page 269](./0-PYTHON_LECTURE.md) ce sui renvoie vers [les blocs 30 et 31 de ce cahier Jupyter](https://github.com/deep-learning-with-pytorch/dlwpt-code/blob/master/p1ch8/1_convolution.ipynb)
## Le code Python
* [Training module Python](../../PYTHON/training_module.py)
### Test
* Rappel: prérequis passage en environnement virtualisé Python pour Pytorch et Jupyter (librairies de Serge Rosmorduc)
```bash
# passage en environnement virtualisé
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project$ source env_python_for_projet_rcp217/bin/activate
# lancement de la partie main du fichier module
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/PYTHON$ python training_module.py
# quitter l'environnement virtualisé
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/PYTHON$ deactivate 
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/PYTHON$
```
* Gros problème
```bash
Traceback (most recent call last):
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/PYTHON/training_module.py", line 41, in <module>
    training_loop(  # <5>
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/PYTHON/training_module.py", line 16, in training_loop
    outputs = model(imgs)  # <4>
              ^^^^^^^^^^^
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/PYTHON/projetct16_module.py", line 42, in forward
    x = self.conv1_init(x)
        ^^^^^^^^^^^^^^^^^^
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/torch/nn/modules/conv.py", line 310, in forward
    return self._conv_forward(input, self.weight, self.bias)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/torch/nn/modules/conv.py", line 306, in _conv_forward
    return F.conv1d(input, weight, bias, self.stride,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: conv1d() received an invalid combination of arguments - got (list, Parameter, NoneType, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types:
```
* si j'auoute le todevice j'ai l'erreur avant
```bash
Training on device cpu.
Traceback (most recent call last):
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/PYTHON/training_module.py", line 45, in <module>
    training_loop(  # <5>
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/PYTHON/training_module.py", line 16, in training_loop
    series = series.to(device)
             ^^^^^^^^^
AttributeError: 'list' object has no attribute 'to'
```
* ligne 23 du [Dataloader en Python](../../PYTHON/dataloader_creation.py) chaque time serie devient une liste et non un Tensor
```python
for ligne_time_serie_str in csvFile:
    ligne_time_serie = list(map(float, ligne_time_serie_str)) #est ce que cela ne devrait pas t'il être un Tenseur
    print(ligne_time_serie)
    self.X.append(ligne_time_serie)
```
* en effet series.to(device) passe
* en revanche la commande suivante ne passe pas
```bash
File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/PYTHON/training_module.py", line 17, in training_loop
    labels = labels.to(device)
             ^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'to'
```
* En suivant [la réponse 4 de ce Post Stackoverflow](https://stackoverflow.com/questions/63825841/attributeerror-tuple-has-no-attribute-to) on nous propose de faire un one-hot vector ?
* je teste dans [le code de validation](../../PYTHON/validation_module.py) à la ligne 25 commentée ci dessous:
```python
def training_loop(n_epochs, optimizer, model, loss_fn, train_loader, device):
    for epoch in range(1, n_epochs + 1):  # <2>
        loss_train = 0.0
        for series, labels in train_loader:  # <3>
            series = series.to(device)
            labels = torch.IntTensor(labels).to(device=device) # en suivant le lien StackOverflow
```
* et j'obtiens l'erreur
```bash
    labels = torch.IntTensor(labels).to(device=device)
             ^^^^^^^^^^^^^^^^^^^^^^^
ValueError: too many dimensions 'str'
```
* Question posée au professeur (to ask after putting the code on GitHub)...
# validation (todo)
* code repris du bloc [38 et 39 du code du livre MAnning](https://github.com/deep-learning-with-pytorch/dlwpt-code/blob/master/p1ch8/1_convolution.ipynb)
* Je récupère les coefficients sauvegardés lors du training
## Suivre l'exemple du livre
* cf. [le bloc 38 de ce cahier Jupyter](https://github.com/deep-learning-with-pytorch/dlwpt-code/blob/master/p1ch8/1_convolution.ipynb)
# En attente de la solution à mon problème PyTorch
* cf. [la réponse 4 de ce Post Stackoverflow](https://stackoverflow.com/questions/63825841/attributeerror-tuple-has-no-attribute-to)
* [Question en cours posée le 28/08/2025](../Questions/3-PYTORCH_TENSORS.md)