# [Dernière réponse de Marin à ma question sur le Forum privé de Moodle / CNAM PARIS](https://par.moodle.lecnam.net/mod/forumng/discuss.php?d=25320)
## La dernière réponse (Samedi 23/08/2025 à 16:31)

Bonjour,

Pour résumer l'idée de l'article : Les auteurs veulent prédire les ordres p et q d’un modèle ARMA en traitant directement la série temporelle brute comme entrée (sans extraire d’abord des caractéristiques comme l’autocorrélation). Pour cela, ils adaptent un **ResNet 1D** (réseaux résiduels, avec skip connections), mais appliqué à des séries temporelles plutôt qu’à des images.

Dans la suite, les extraits du papier sont donnés en anglais et commencent par '-'

Mes questions sur ce réseau:

+ première étape on part de Times series à 100 entrées avec une kernel de 10 et stride de 10

Je crois que les séries en entrée sont de taille 1000 :

**- Sec 1 : The length of our time series during training is set to 1000.**

  + ce qui nous fait en sortie 300 output channels de 10 données chacun, on nous dit de concaténer ces données est ce que on doit obtenir une sortie de dimension 2d de taille 10 x 300 ou de dimension 1D de longeur 30000

1ere couche est une convolution classique : 
Filter width = 10, stride 10, input size = 1000 
La sortie est donc un ensemble de 300 feature maps de taille 100 chacune.

+ On passe ensuite par 4 RESNET blocs est ce que ce que l'on appelle un RESNET Bloc est une succession de Cond2D séparés par des RELU . Je n'ai pas vu de RESNET blocs de avec des Conv1D ?

Un [bloc Resnet](https://en.wikipedia.org/wiki/Residual_neural_network) c'est juste une couche (ou plusieurs) de convolution F avec laquelle on additionne l'entrée y = x + F(x).

  + Est ce que la dimension de sortie des 4 RESNET Blocs est 10 données  x 300 features maps 

**- We do not use padding in our setup. Without padding however, the time series shrinks whenever it goes through a convolutional layer. Data flowing through the skip connection have to be truncated at the tail to enable addition to output of residual layers.**
**- We use the same number of feature maps for all but the last layer**
**- Filter in subsequent convolutional layers are also of width 10 but move at stride 1.**

Donc, après la 1ere couche de convolution il y a 4 couches résiduelles (ResNet : skip connection + conv ReLU)
**- There are 4 residual blocks of ReLU before addition structure used.**
Chaque bloc résiduel réduit la dimension des feature maps de 10 - 1 = 9, donc après 4 blocs la réduction est de 9x4=36 et en sortie in a 300 feature maps de taille 100 - 36 = 64.

+ on passe enfin par 6 1x1 convolutional layers with stride 0 

  + stride 0 ne nous permet pas d'avancer dans la série

Pour préserver la tailles des features maps ils utilisent ensuite 6 couches de skip + convolution 1x1 :
**- A 1x1 convolution layer convolves along the `feature dimension', i.e. across feature maps while stride in temporal dimension is 0. In other words, it does not reduce the length of time series passing through it.**

  + Est ce qu'on part pour chaque convolutional layer de une données de 3000 de long ou de 300 layers de 10 données chacune ?

L'entrée de chaque layer est la sortie du layer précédent, ctd 300 feature maps de taille 64.

  + est ce que en sortie de chaque layer on a une seule ou 300 feature maps ?

Oui, toujours 300 feature maps.

  + est ce que entre chaque layer on a un RELU ?

Chaque bloc ResNet = convolution → batch norm → ReLU → addition avec skip connection. L’activation ReLU est appliquée avant l’addition (d’après He et al. 2016 cela donne une meilleure stabilité). Comme il n’y a pas de padding, il faut tronquer la fin de la sortie du skip path pour pouvoir additionner.

 + Pour le dernier convolutional layer on passe de 300 feature mapas à 10 feauture maps

**- A final convolutional layer convolves along the width dimension again and reduces the number of feature maps to match the number of classes, which is 10 in our study.**

Une dernière couche de convolution (le papier ne précise pas explicitement la largeur du noyau de la dernière conv.). Après cette dernière couche de convolution (si taille filtre = 10, stride = 1, sans padding) on a 10 feature maps de taille 64 - 9 = 55.

   + est ce que chaque feature maps (input, output) et composée de 10 données ?

Comme vu en haut la taille des feature maps est 55.

   + et on ferait 10 mayennes sur 10 données chacune ? et une softmax sur ces 10 données ?

**- An averaging along width dimension (i.e. temporal dimension) is done to these ten feature maps before softmax calculation. This averaging step essentially allows our architectures to process longer time series.**

Il font donc une moyenne temporelle (average pooling temporel) sur chaque feature map pour obtenir 10 nombres, qu'ils passent ensuite dans un softmax pour obtenir le résultat de la classification.

+ quel serait l'erreur pour la descente de gradient ?

**- We use cross-entropy criterion as loss function**

J'espère avoir répondu à vos questions, en pratique vous n’êtes pas obligé d’implémenter à la lettre ce réseau, vous pouvez expérimenter en changeant l'architecture, mais aussi le modèle (en utilisant pourquoi pas un MLP à la place, ou même un modèle SVM ou boosting et les comparer).