# SshTelegramNotify
The bot notifies about successful SSH connections to the server.

## Install
### Debian/Ubuntu Server <br> </h3>
#### 1.Create a new bot in BotFather.
#### 2.Enter the commands:
```
sudo apt update 
sudo apt install git 
git clone https://github.com/Georgiy10427/SshTelegramNotify.git 
cd SshTelegramNotify 
sudo chmod 777 install.sh 
sudo ./install.sh 
```
#### 3.Then follow the instructions of the installer.
The next time you log into the system on SSH after installation, you should receive a notification in your telegram.
## Uninstall 
Enter the command:
```
  rm /etc/profile.d/ssh-to-telegram.sh
```
## License
*This software is licensed under the GPL V3.*
> The [original script](https://gist.github.com/matriphe/9a51169508f266d97313) is not licensed.
