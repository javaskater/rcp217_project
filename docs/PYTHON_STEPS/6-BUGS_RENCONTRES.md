# Tests en environnement virtualisé partie training:
## Première erreur
* Mon label doit être un un tenseur avec une seule valeur (l'ordre de p)
  * et non un one-hot-encoding de l'ordre de p (coefficient ar) cf. [réponse de Marin du 28/08/2025](../Questions/3-PYTORCH_TENSORS.md)
* je teste en environnement virtualisé sur mon PC la création d'une tenseur avec une seule valeur entière
```python
>>> import torch
>>> a = 53
>>> at = torch.IntTensor([a]) # C’est ce que l’on attend (ne pas oublier de placer l’entier dans une liste)
>>> at
tensor([53], dtype=torch.int32)
>>> at2 = torch.IntTensor(a) # Attention cette forme génère un Tenseur de 53 éléments aléatoires
>>> at2
tensor([    279806,          0,          0,          0,         -1,          0,
        1869903169, 1769234797, 1819042147, 1868701817,  543452789, 1919250543,
        1919906913, 1952524064,  976907877, 1667592307, 1600938345, 2037541217,
         661217631, 1953068832, 1668489320, 1634559336,  975794984, 1629495306,
         980313460, 1701868346, 1818323299, 1919508831, 1767989113, 1852134440,
         544370547,  757082488, 1700012094, 1919906670, 1629495306,  980313460,
        1701868346, 1818323299, 1919508831, 1767989113, 1953853230, 1852134440,
         544370547,  706751608, 1700012076, 1919906670,  690053416, 1953853216,
        1043144745, 1852134432,  678588275,  170467681,       2560],
       dtype=torch.int32)
```
* Cela ne suffit pas, les coefficients p et q que je récupère de l’expression régulière sur le nom du fichier sont des châines python et non des entiers. De là l’erreur quand je fais tourner l’entraînement du modèle [lien GitHub  le script Python d’entraînement](../../PYTHON/training_module.py) :
```python
 p_tensor = IntTensor([p]) # Ce doit être un tenseur avec une seule donnée: l'ordre attendu
               ^^^^^^^^^^^^^^
ValueError: too many dimensions 'str'
```
* C’est pour cela qu’il faut les transformer en entiers avant des les retourner cf [Réponse 14 à cette question StackOverflow](https://stackoverflow.com/questions/65804689/with-bert-text-classification-valueerror-too-many-dimensions-str-error-occur).


## 2ème erreur  Quand je continue le script d’entrainement il me met l’erreur
```bash
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
RuntimeError: Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1001]
```
Réponse dans ce [Post StackOverflow (cas qui a trop de dimensions)](https://stackoverflow.com/questions/77287416/how-to-remove-runtimeerror-expected-2d-unbatched-or-3d-batched-input-to-con) on a attend le en dim  channel et le nombre d’éléments 
* Test de unsqueeze en environnement virtualisé
```python
>>> import torch
>>> a = torch.IntTensor(4)
>>> a
tensor([779680823,         0,         0,         0], dtype=torch.int32)
>>> a2 = a.unsqueeze(0)
>>> a2
tensor([[779680823,         0,         0,         0]], dtype=torch.int32)
Un second unsqueze est nécessaire pour la taille de batch de 1 également (cf. le main du RESNET1D module – lien GitHub)
Si je reste sur un batch non unitaire cela donne en training
        for series, labels in train_loader:  # <3>
            series = series.to(device)
            labels = labels.to(device=device)

            if debug == True:
                print(f"[training_loop] series batch before unsqueeze {series.shape}")                
            series2D = series.unsqueeze(1) # add the one channel dimension between the batch_size dimension and the serie's length
            if debug == True:
                print(f"[training_loop] series batch after unsqueeze {series2D.shape}")  
```
* en sortie sur console en mode debug on a bien *batchsize x 1 (entrée de Cons1D) x taille de la serie en enrée*
```bash
[training_loop] series batch before unsqueeze torch.Size([50, 1001])
[training_loop] series batch after unsqueeze torch.Size([50, 1, 1001]) # ce que attend le programme batchsize x 1 (entrée de Cons1D) x taille de la serie en enrée
[training_loop] outputs shape torch.Size([50, 10]) labels shape torch.Size([50, 1])
```
## 3ème erreur Erreur à la Loss Function :
```bash
[training_loop] series batch before unsqueeze torch.Size([50, 1001])
[training_loop] series batch after unsqueeze torch.Size([50, 1, 1001])
[training_loop] outputs shape torch.Size([50, 10]) labels shape torch.Size([50, 1])
Traceback (most recent call last):
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/PYTHON/training_module.py", line 84, in <module>
    training_loop(  # <5>
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/PYTHON/training_module.py", line 29, in training_loop
    loss = loss_fn(outputs, labels)  # <5>
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/torch/nn/modules/loss.py", line 1179, in forward
    return F.cross_entropy(input, target, weight=self.weight,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jpmena/CONSULTANT/CNAM/rcp217_project/env_python_for_projet_rcp217/lib/python3.12/site-packages/torch/nn/functional.py", line 3059, in cross_entropy
    return torch._C._nn.cross_entropy_loss(input, target, weight, _Reduction.get_enum(reduction), ignore_index, label_smoothing)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: 0D or 1D target tensor expected, multi-target not supported
```
Cf. [Réponse 16 de ce post de Stack Overflow signale l’erreur et la corrige](https://stackoverflow.com/questions/71399847/runtimeerror-0d-or-1d-target-tensor-expected-multi-target-not-supported-i-was).
* le tenseur des labels ne doit avoir qu'une seule dimension pas plusieurs 
* Petit test en environnement virtualisé
```python
>>> import torch 
>>> a = torch.IntTensor([[2],[3]])
>>> a.shape
torch.Size([2, 1])
>>> b=a.squeeze(1)
>>> b
tensor([2, 3], dtype=torch.int32)
>>> b.shape
torch.Size([2])
```
* Donc je squeeze les labels ramenant de 2 dimensions à une dimension
## 4ème erreur  Autre problème Loss Function Label type :
```bash
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: expected scalar type Long but found Int
```
* On transforme directement dans le training le Tenseur des labels de int en long ce qui donne en une instruction
```python
labels = labels.squeeze(1).long() # cf erreur 3 et 4 dans le compte rendu
```
## 5ème Erreur à loss.backward
```bash
RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation: [torch.FloatTensor [50, 300, 64]], which is output 0 of ReluBackward0, is at version 1; expected version 0 instead. Hint: enable anomaly detection to find the operation that failed to compute its gradient, with torch.autograd.set_detect_anomaly(True).
```
cf. [Réponse de ce forum Pytorch](https://discuss.pytorch.org/t/encounter-the-runtimeerror-one-of-the-variables-needed-for-gradient-computation-has-been-modified-by-an-inplace-operation/836)
### Premier essaie
* on modifie (met en forme les series et les labels) avant de les envoyer vers le device.
* J’ai toujours le problème, il semble que cela se passe dans mon RESNET1D
### Deuxième esst
* Cela se passe à la fin de la fonction [forward de mon RESNET1D](../../PYTHON/resnet1d_module.py) 
* Je corrige par pour éviter les in-place replacement ce qui donne à la fin de la fonction *forward*
```python
        # identity with trucation
        in_x_truncated = in_x[...,:x.shape[2]]
        x_out = x + in_x_truncated

        # final relu
        x_out_after_relu = self.relu(x_out)
        
        return x_out_after_relu
```
## Ca tourne enfin
* lancement
```bash
jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project$ source env_python_for_projet_rcp217/bin/activate # on passe dans l'environnement virtualisé PyTorch
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project$ cd PYTHON/
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/PYTHON$ python training_module.py 
```
* Dans la log on a 
```bash
Training on device cpu.
2025-09-13 14:37:17.538155 Epoch 1, Training loss 2.3026925325393677
2025-09-13 14:37:22.983517 Epoch 5, Training loss 2.2925405502319336
2025-09-13 14:37:30.649062 Epoch 10, Training loss 2.2856345176696777
2025-09-13 14:37:37.624956 Epoch 15, Training loss 2.276905655860901
2025-09-13 14:37:44.568807 Epoch 20, Training loss 2.2781039476394653
2025-09-13 14:37:51.815883 Epoch 25, Training loss 2.273137092590332
2025-09-13 14:37:58.535008 Epoch 30, Training loss 2.2641263008117676
2025-09-13 14:38:05.355048 Epoch 35, Training loss 2.2680059671401978
2025-09-13 14:38:12.040122 Epoch 40, Training loss 2.2669788599014282
2025-09-13 14:38:18.883312 Epoch 45, Training loss 2.2708911895751953
2025-09-13 14:38:25.638264 Epoch 50, Training loss 2.2621127367019653
```
# Tests en environnement virtualisé partie validation:
* on a repris les corrections de la partie entraînement précédent
* premier lancement (en environnement virtualisé PyTorch cf. ci dessus)
```bash
(env_python_for_projet_rcp217) jpmena@LAPTOP-E2MJK1UO:~/CONSULTANT/CNAM/rcp217_project/PYTHON$ python validation_module.py 
```
* Dans la log on a :
```bash
Validating on device cpu.
/home/jpmena/CONSULTANT/CNAM/rcp217_project/PYTHON/validation_module.py:25: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
  labels = torch.tensor(labels).squeeze(1).long().to(device=device) # cf erreur 3 et 4 dans le compte rendu
Accuracy train: 0.31
Accuracy val: 0.19
```
## Se débarasser du Warning ?
* on remplace 
```python
labels = torch.tensor(labels).squeeze(1).long().to(device=device) # cf erreur 3 et 4 dans le compte rendu
```
* par  (car labels est déjà un PyTorch Tensor)
```python
labels = labels.squeeze(1).long().to(device=device) # cf erreur 3 et 4 dans le compte rendu
```
## Cela fonctionne sans warning
* dans la log on a :
```bash
tensor([ 1.0000,  0.8663,  1.5100,  ..., -3.7304, -0.9471,  1.2509])
Validating on device cpu.
Accuracy train: 0.26
Accuracy val: 0.18
```