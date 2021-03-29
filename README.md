# SshTelegramNotify
The bot notifies about successful SSH connections to the server.

<h1><b>Install</b></h1>
<h3> Debian/Ubuntu Server <br> </h3>
<a> Create a new bot in BotFather.</a><br>
<a> Enter the commands: </a><br>
<code>
sudo apt install git<br> 
git clone https://github.com/Georgiy10427/SshTelegramNotify.git <br> 
cd SshTelegramNotify <br> 
sudo chmod 777 install.sh<br> 
sudo ./install.sh 
</code><br>
<a>Then follow the instructions of the installer.</a><br>
<b>The next time you log into the system on SSH after installation, you should receive a notification in your telegram.</b><br>
<h1> Uninstall </h1>
<a> Enter the command: </a> <br>
<code>
  rm /etc/profile.d/ssh-to-telegram.sh
</code><br>
<h3> <a link="https://gist.github.com/matriphe/9a51169508f266d97313"> The original script. </a>  </h3>
