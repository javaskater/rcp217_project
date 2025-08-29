# Objectif dernier Step
* cf [réponse de Marin du samedi 23 aout 2025 à 16:31](../Questions/2-PYTHONSTEPS.md)
  * avant la dernière étape de passage de 300 à 10 
  * *on a 10 feature maps de taille 64 - 9 = 55.* (si kernel de 10 et stride de 1)
  * *Il font donc une moyenne temporelle (average pooling temporel) sur chaque feature map pour obtenir 10 nombres*
* (passer de 300 de taille 64 à 10 feature maps de taille 64 - 9 = 55)
* faire la moyenne sur chaque feature map et sortir un tenseur de taille (batch size, 10)
* le softmax sera dans le [module principal](./5-GLOBAL.md)
# le code de ce step 
* [créé en tant que module PyTorch](../../PYTHON/averaging_module.py)
* (to ask) doit on obtenir 
  * un tenseur de shape (1,1,10) (batch size , nb of feature maps, width of a feature map)
  * ou un tenseur de shape (1,10) (batch_size, output_length)
## partie convolution et moyenne
* le test local du module Pytorch AVERAGING donne
```bash
# passage en environnement virtualisé Pytorch pour RCP217
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project$ source env_python_for_projet_rcp217/bin/activate
# lancement de la partie main du code du module (test local du module)
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/PYTHON$ python averaging_module.py 
[main] Calling AVERAING
[AVERAGING/forward] after CONV/NORM/RELU shape of x torch.Size([1, 10, 55])
[AVERAGING/forward] after mean operation shape of x torch.Size([1, 10])
torch.Size([1, 10])
```
* on repasse au [module principal](./5-GLOBAL.md) où on ajoute le softmax