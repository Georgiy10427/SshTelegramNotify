# SshTelegramNotify
The bot notifies about successful SSH connections to the server.

## Install
### Debian/Ubuntu Server <br> </h3>
Create a new bot in BotFather.
Enter the command:
```
sudo apt update 
sudo apt install git 
git clone https://github.com/Georgiy10427/SshTelegramNotify.git 
cd SshTelegramNotify 
sudo chmod 777 install.sh 
sudo ./install.sh 
```
Then follow the instructions of the installer.
The next time you log into the system on SSH after installation, you should receive a notification in your telegram.
## Uninstall 
Enter the command:
```
  rm /etc/profile.d/ssh-to-telegram.sh
```
> The original script: https://gist.github.com/matriphe/9a51169508f266d97313 
> The original script is not licensed.
