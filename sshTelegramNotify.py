from os import getenv, system as system_exec
from os.path import exists as path_exists, isfile as file_exists
from socket import getfqdn, gethostname, error as SocketErrorException

from smtplib import SMTP, SMTPException
from datetime import datetime
import config

from ipaddr import IPAddress, IPNetwork
import telebot

import daemon
import sys


class MyDaemon(daemon.Daemon):
    def run(self):
        bot = telebot.TeleBot(config.token)
        _SSH_TTY = getenv("SSH_TTY")
        if _SSH_TTY:
            _SSH_MODE="SSH" 
        else: 
            _SSH_MODE="SFTP"
        _SSH_CONNECTION=getenv("SSH_CONNECTION")
        if _SSH_CONNECTION:
            ipaddr=_SSH_CONNECTION.split()[0]
            _LOGIN=getenv("USER")
            _TIME=datetime.utcnow().ctime()
            msg="On {TIME} {SSH_MODE} Authorization on {SERVERNAME} from user {USERNAME} with IP {IPADDR} successfully!".format(TIME=_TIME, SSH_MODE=_SSH_MODE, SERVERNAME=getfqdn(gethostname()), USERNAME=_LOGIN, IPADDR=ipaddr)
        bot.send_message(config.userId, msg)

if __name__ == "__main__":
    my_daemon = MyDaemon('/var/run/webserver.pid')

    if len(sys.argv) >= 2:
        if 'start' == sys.argv[1]:
            print('starting webserver')
            my_daemon.start()
        elif 'stop' == sys.argv[1]:
            print('stoping webserver')
            my_daemon.stop()
        elif 'restart' == sys.argv[1]:
            print('restarting webserver')
            my_daemon.restart()
    else:
        print("Unknown command")
        sys.exit(2)
    sys.exit(0)