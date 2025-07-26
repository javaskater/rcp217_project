# installation de [Python sous Windows](https://www.python.org/downloads/)
* C'est la 3.13.15 que l'on installe (27.5. Mo)
## Virtual environments pour installer nos librairies de RCP217
* cf [le travail des Python Libs sous venv](./PYTHONLIBS.md) 
```powershell
PS C:\Users\jeanp\CONSULTANT> python -m venv env_python_for_projet_rcp217
PS C:\Users\jeanp\CONSULTANT> .\env_python_for_projet_rcp217\Scripts\activate
.\env_python_for_projet_rcp217\Scripts\activate : Impossible de charger le fichier
C:\Users\jeanp\CONSULTANT\env_python_for_projet_rcp217\Scripts\Activate.ps1, car l’exécution de scripts est désactivée
sur ce système. Pour plus d’informations, consultez about_Execution_Policies à l’adresse
https://go.microsoft.com/fwlink/?LinkID=135170.
Au caractère Ligne:1 : 1
+ .\env_python_for_projet_rcp217\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : Erreur de sécurité : (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```
## problème Windows refuse par défaut l'exécution de scripts Powershell (résolu)
* [Comment autoriser les scripts powershell](https://casits.artsandsciences.fsu.edu/how-run-powershell-scripts-windows-11)
  * faire cela depuis une console d'admin [lien vers ouvrir une console d'admin (elle est sur fond bleu)](https://learn.microsoft.com/en-us/answers/questions/1338912/how-to-run-powershell-as-administrator)
```powershell
PS C:\WINDOWS\system32> Set-ExecutionPolicy Unrestricted                                                                                                                                                                                        Modification de la stratégie d'exécution                                                                                La stratégie d’exécution permet de vous prémunir contre les scripts que vous jugez non fiables. En modifiant la         stratégie d’exécution, vous vous exposez aux risques de sécurité décrits dans la rubrique d’aide                        about_Execution_Policies à l'’adresse https://go.microsoft.com/fwlink/?LinkID=135170. Voulez-vous modifier la stratégie  d’'exécution ?                                                                                                           [O] Oui  [T] Oui pour tout  [N] Non  [U] Non pour tout  [S] Suspendre  [?] Aide (la valeur par défaut est « N ») : O 
``` 
* ça marche (console non admin déjà ouverte auparavant)
```powershell
PS C:\Users\jeanp\CONSULTANT> .\env_python_for_projet_rcp217\Scripts\activate
(env_python_for_projet_rcp217) PS C:\Users\jeanp\CONSULTANT> deactivate
PS C:\Users\jeanp\CONSULTANT> deactivate
PS C:\Users\jeanp\CONSULTANT> .\env_python_for_projet_rcp217\Scripts\activate
```
* une fois terminé passage en Restricted depuis la console bleue (admin Powershell)
```powershell
PS C:\WINDOWS\system32> Set-ExecutionPolicy Restricted                                                                                                                                                                                          Modification de la stratégie d'exécution                                                                                La stratégie d’exécution permet de vous prémunir contre les scripts que vous jugez non fiables. En modifiant la         stratégie d’exécution, vous vous exposez aux risques de sécurité décrits dans la rubrique d’aide                        about_Execution_Policies à l’adresse https://go.microsoft.com/fwlink/?LinkID=135170. Voulez-vous modifier la stratégie  d’exécution ?                                                                                                           [O] Oui  [T] Oui pour tout  [N] Non  [U] Non pour tout  [S] Suspendre  [?] Aide (la valeur par défaut est « N ») : O  
```