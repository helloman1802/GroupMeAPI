from groupy import Group, Bot
from groupy.object.listers import FilterList
import re
from time import sleep
import wolframalpha

group = Group.list().first

bot = Bot.list().first
client = wolframalpha.Client("GWWEUW-2WULJX383Q")




#str(group.messages().newest
while True:
    pat1 = "(pops).*"
    string_of_message = str(group.messages().newest.text)
    reg1 = re.search(pat1, string_of_message)
    print (string_of_message)
    sleep(1)

    if reg1:
        search = client.query(reg1.group())
        try:
            bot.post(next(search.results).text)


        except Exception as e:
            bot.post("Matt's flabs are preventing me from figuring out the problem.")
