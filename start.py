input("press enter to continue... ")

from test import ip

import telepot

TOKEN=input("please, enter the token bot: ")
chat_id=input("please, enter the chat id: ")

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

if(platform.system() == "Windows"):
    import subprocess
    proc = subprocess.check_output("ipconfig" ).decode('utf-8')
    bot.sendMessage(chat_id,proc)
if(platform.system() == "Linux"):
    import subprocess
    proc_1 = subprocess.check_output("ifconfig" ).decode('utf-8')
    bot.sendMessage(chat_id,proc_1)
bot.sendMessage(chat_id,getpass.getuser())

print("\nthank you to have used my tool :-)")

input("\n\n\n\n\npress enter to finish... ")

bot.sendMessage(chat_id,'enjoy ;)')
