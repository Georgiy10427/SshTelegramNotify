import telebot, random

codeRand = random.randint(1111, 9999)
bot = telebot.TeleBot("1147186033:AAFtbWGyVtLEZGfHboYOS1-_1dErAIa-V8E")
print("Please, send " + str(codeRand) + " text message to bot.")
print("Wait...")

@bot.message_handler(content_types=['text'])
def start(message):
    if str(codeRand) in message.text:
        print("Your id: " + str(message.from_user.id))
        bot.send_message(message.from_user.id, "Success!")
        print("Press Ctrl + C to exit...")
    exit(0)

bot.polling()