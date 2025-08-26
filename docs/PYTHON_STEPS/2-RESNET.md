# Bonne référence pour fabriquer un [réseau RESNET in Pytorch](https://www.digitalocean.com/community/tutorials/writing-resnet-from-scratch-in-pytorch)
# mes questions
* résumées dans [ce fil de discussion sur le CNAM](https://par.moodle.lecnam.net/mod/forumng/discuss.php?d=25320) 
  * je me suis abonné au fil de discussion   
# [REST Net Block Definition](https://en.wikipedia.org/wiki/Residual_neural_network)
* Je me suis connecté sur [le forum Pytorch avec mon SSO GMail pythonrubylang](https://discuss.pytorch.org/t/how-to-write-resnet-block-for-1-dimensional-data/48420)
  * mais la question n'a pas de réponse
* une [implémentation que je peux utiliser pour RESNET](https://medium.com/@karuneshu21/how-to-resnet-in-pytorch-9acb01f36cf5)
# [Tests resnet1D](../../PYTHON/resnet1d_module.py)
* mettre l'option debug pour les print (todo)
* mettre dans la doc la réponse de Marin du 23/08/2025 (todo)
* les stride nuls ne sont pas acceptés (à voir avec le prof)
* pour un kernel de 10 on passe de 100 à 91 qu'est ce que cela donne avec 4 Resnet de stride 10 (il avait marqué dans le mail)
  * *donc après 4 blocs la réduction est de 9x4=36 et en sortie in a 300 feature maps de taille 100 - 36 = 64.*