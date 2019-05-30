import requests
import urllib
import random
import re
import emoji
from emoji import unicode_codes

class Ukko:
    def __init__(self):
        self.commands = {
            'hakemus': self.handleHakemus,
        }
        self.paska = "saatana:D LOHKAREET LENTELEE"

    def getCommands(self):
        return self.commands

    def handleHakemus(self, bot, update, args=''):
        if random.randint(0, 9) == 0:
            bot.sendMessage(chat_id=update.message.chat_id, text='hyy-vä')
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text='tapan sut')

    def getTEK(self, bot, update, args=''):
        if random.randint(0, 12) == 0:
            for word in update.message.text.lower().split(' '):
                if re.match(r'.*tek.*', word) and word != 'tek':
                    bot.sendMessage(chat_id=update.message.chat_id, text='ai ' + word.replace('tek', 'TEK') + ' xD')
                    return

    def nauru(self, bot, update, args=''):
        huumori = ["Räh", "Kjeh", "RÄÄH", "Räh kjeh"]
        if random.randint(0, 1) == 0:
            bot.sendMessage(chat_id=update.message.chat_id, text=random.choice(huumori))

    def messageHandler(self, bot, update):
        msg = update.message
        #print(msg)
        if msg.text is not None:
            if 'hakemus' in msg.text.lower():
                self.handleHakemus(bot, update)
            elif re.match(r'räh|kjeh|rääh|kjeeh|rhä|kejh|kjäh|rur', msg.text.lower()):
                self.nauru(bot, update)
            elif re.match(r'.*[tT]ek.*', msg.text):
                self.getTEK(bot, update)
