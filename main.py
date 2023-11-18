from openai import OpenAI
import telebot


gptapi = 'СЮДА_ВСТАВЬ_СВОЙ_АПИ_КЛЮЧ_OpenAI'
client = OpenAI(api_key=gptapi, )

token = 'СЮДА_ВСТАВЬ_СВОЙ_АПИ_КЛЮЧ_Telegram'
bot = telebot.TeleBot(token, parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как поживаешь?")

@bot.message_handler(func=lambda m: True)
def chat_with_chatGPT(message):
    print('-------------VOPROS------------->>>')
    print(message.text)
    vopros = message.text
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": vopros, }],
        model="gpt-3.5-turbo",)
    print("<<<----------OTVET----------------")
    otvet = completion.choices[0].message.content
    print(otvet)
    bot.reply_to(message, otvet)


print('-------Bot run--------')
bot.infinity_polling()
