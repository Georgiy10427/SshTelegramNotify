token = input("Please, enter you bot token: ")
import telebot, random, re

script = """
USERID="TeleUserId"
KEY="TeleToken"
TIMEOUT="10"
URL="https://api.telegram.org/bot$KEY/sendMessage"
DATE_EXEC="$(date "+%d %b %Y %H:%M")"
TMPFILE='/tmp/ipinfo-$DATE_EXEC.txt'
if [ -n "$SSH_CLIENT" ]; then
	IP=$(awk '{print $1}' <<< $SSH_CLIENT)
	PORT=$(awk '{print $3}' <<< $SSH_CLIENT)
	HOSTNAME=$(hostname -f)
	IPADDR=$(hostname -I | awk '{print $1}')
	curl http://ipinfo.io/$IP -s -o $TMPFILE
	CITY=$(jq -r '.city' < $TMPFILE)
	REGION=$(cat $TMPFILE | jq '.region' | sed 's/"//g')
	COUNTRY=$(cat $TMPFILE | jq '.country' | sed 's/"//g')
	ORG=$(cat $TMPFILE | jq '.org' | sed 's/"//g')
	TEXT="$DATE_EXEC: Вход пользователя ${USER} по ssh на $HOSTNAME ($IPADDR) из $IP - $ORG - $CITY, $REGION, $COUNTRY через порт $PORT"
	curl -s --max-time $TIMEOUT -d "chat_id=$USERID&disable_web_page_preview=1&text=$TEXT" $URL > /dev/null
	rm $TMPFILE
fi
"""
codeRand = random.randint(1000, 9999)
bot = telebot.TeleBot(token)
print("Please, send " + str(codeRand) + " text message to bot.\n")
print("Wait...")

@bot.message_handler(content_types=['text'])
def start(message):
    if str(codeRand) in message.text:
        print("Your id: " + str(message.from_user.id))
        bot.send_message(message.from_user.id, "Success!")
        f = open("/etc/profile.d/ssh-to-telegram.sh", "w")
        f.write(re.sub(r'TeleToken', str(token), re.sub(r'TeleUserId', str(message.from_user.id), script)))
        f.close()
        #print(re.sub(r'TeleToken', str(token), re.sub(r'TeleUserId', str(message.from_user.id), script)))
        print("Press Ctrl + C to exit...\n")
    exit(0)

bot.polling()
