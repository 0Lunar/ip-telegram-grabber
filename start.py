input("press enter to continue... ")

from test import ip

import telepot

TOKEN=input("please, enter the token bot: ")
chat_id=input("please, enter the chat id: ")

bot=telepot.Bot(TOKEN)
bot.sendMessage(chat_id,ip )
bot.sendMessage(chat_id,'https://whatismyipaddress.com/ip/' + ip)
