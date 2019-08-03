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
            bot.sendMessage(chat_id=update.message.chat_id, text='Soraahan tuo tahtoisi :)')
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

    def getABB(self, bot, update, args=''):
        stiksut = ["CAADBAADKgADiR7LDSt7kRS0nxjVAg", "CAADBAADSwADiR7LDctHDtCmX288Ag", "CAADBAADNgADiR7LDWx2U5l4lHtZAg", "CAADBAADTAADiR7LDefZ-ip0q9ZtAg"]
        bot.sendSticker(chat_id=update.message.chat_id, sticker=random.choice(stiksut))

    def gettasky(self, bot, update, args=''):
        stiksut = ["CAADBAADFAAD3ekjF7eBdhX6XMD6Ag", "CAADBAADEwAD3ekjF_83pyeNMoKHAg"]
        bot.sendSticker(chat_id=update.message.chat_id, sticker=random.choice(stiksut))

    def toihin(self, bot, update, args=''):
        vastaus = ['Oikeisiin TÖI-HIN!', 'Menisit sinäkin TÖI-HIN!', 'Sinäkin teekkaripelle siellä: T Ö I H I N!!!', 'TÖY_-HIIHIHIIIN']
        bot.sendMessage(chat_id=update.message.chat_id, text=random.choice(vastaus))

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
            elif 'abb' in msg.text.lower():
                self.getABB(bot, update)
            elif '🅰️🅱️🅱️' in msg.text:
                self.getABB(bot, update)
            elif 'tasky' in msg.text.lower():
                self.gettasky(bot, update)
            elif re.match(r'töihin|töi-hin|hommiin|homs|töy|töi|oikeisiin|menisit|vätys', msg.text.lower()):
                self.toihin(bot, update)
