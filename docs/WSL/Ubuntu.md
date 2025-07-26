# passing from Ubuntu 22/04 to Ubuntu 24.04
## Actuel
* on est sous WSL en Ubuntu 22.04
```bash
jpmena@LAPTOP-E2MJK1UO:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.4 LTS
Release:        22.04
Codename:       jammy
```
## Ugrading en suivant [cet article](https://phoenixnap.com/kb/wsl-upgrade-ubuntu)
* prérequis: [supprimer RStudio par snap](../INSTALLATIONS/R.md)
### Sauvegarder Uubuntu actuelle
* Sous Powersell (Abandon sauvegarde trop longue JE n'ai que 8Go de RAM et cela prend réellement trop de temps, mon ordinateur est figé tout ce temps)
```powershell
PS C:\Users\jeanp> wsl -l
Distributions du Sous-système Windows pour Linux :
Ubuntu (par défaut)
docker-desktop
docker-desktop-data
PS C:\Users\jeanp> wsl --export Ubuntu C:/Images/Ubuntu2204.tar
Exportation en cours. Cette opération peut prendre quelques minutes. (1279 MB): ./var/lib/docker/volumes/ddev-ssh-agent_socket_dir/_data/socket: pax format cannot archive sockets: ./var/lib/docker/volumes/ddev-ssh-agent_socket_dir/_data/proxy-socket: pax format cannot archi (15918 MB): ./root/.cache/at-spi/bus_0: pax format cannot arch (15919 MB): ./tmp/scoped_dirQiL5pP/SingletonSocket: pax format cannot arch (27417 MB)
^C # Abandon je n'en peux plus presque 1/2 heure et rien de terminé
```
* Sous WSL/Ubuntu mise à niveau comme une distribution classique:
```powershell
PS C:\Users\jeanp> wsl -d Ubuntu
```
* ce qui nous passe en bash on met à jour les paquets
```bash
jpmena@LAPTOP-E2MJK1UO:/mnt/c/Users/jeanp$ sudo apt update && sudo apt upgrade -y
################################"""
Processing triggers for dbus (1.12.20-2ubuntu4.1) ...
Processing triggers for php8.1-cli (8.1.33-1+ubuntu22.04.1+deb.sury.org+1) ...
Processing triggers for libapache2-mod-php8.1 (8.1.33-1+ubuntu22.04.1+deb.sury.org+1) ...
```
* Toujours en bash on vérifie avant la mise à jour
  * rien à faire Prompt est déjà à lts
```bash
jpmena@LAPTOP-E2MJK1UO:/mnt/c/Users/jeanp$ sudo vim /etc/update-manager/release-upgrades
jpmena@LAPTOP-E2MJK1UO:/mnt/c/Users/jeanp$ tail -1 /etc/update-manager/release-upgrades
Prompt=lts
```
## Main on lance la mise à jour
```bash
jpmena@LAPTOP-E2MJK1UO:/mnt/c/Users/jeanp$ sudo do-release-upgrade
Checking for a new Ubuntu release

= Welcome to Ubuntu 24.04 LTS 'Noble Numbat' =

The Ubuntu team is proud to announce Ubuntu 24.04 LTS 'Noble Numbat'.
#########################
To sign up for future Ubuntu announcements, please subscribe to Ubuntu''s
very low volume announcement list at:

  http://lists.ubuntu.com/mailman/listinfo/ubuntu-announce


Continue [yN]
##### plantage ne trouve pas ddev.com
# je supprime les entrées et recommence
jpmena@LAPTOP-E2MJK1UO:/etc/apt/sources.list.d$ sudo rm  ddev.list ddev.list.distUpgrade
Err https://cli.github.com/packages stable InRelease
  The following signatures were invalid: EXPKEYSIG 23F3D4EA75716059 GitHub CLI <opensource+cli@github.com>
Fetched 4416 B in 0s (0 B/s)

Error during update

A problem occurred during the update. This is usually some sort of
network problem, please check your network connection and retry.
## JE supprime les source fautives et je recommence
jpmena@LAPTOP-E2MJK1UO:/etc/apt/sources.list.d$ sudo rm github-cli.li
# je relance, il va plus loin
73 packages are going to be removed. 237 new packages are going to be
installed. 1106 packages are going to be upgraded.

You have to download a total of 4822 M. This download will take about
16 minutes with a 40Mbit connection and about 2 hours 8 minutes with
a 5Mbit connection.

Fetching and installing the upgrade can take several hours. Once the
download has finished, the process cannot be canceled.

 Continue [yN]  Details [d]
```
## Mise à jour OK
```bash
jpmena@LAPTOP-E2MJK1UO:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 24.04.2 LTS
Release:        24.04
Codename:       noble
```