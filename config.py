#################################
# Etiraf Club Bot #
#################################
# Repo Sahibi - aykhan_s
# Telegram - t.me/aykhan_s
# Support - t.me/RoBotlarimTg
# GitHub - aykhan026
#################################
#################################
# Bu repo sıfırdan yığılıb
# Başka github hesabına yükləməy olmaz
# Reponu öz adına çıxaran peysərdi...!!!
#################################
#################################
#
import os
import heroku3
from telethon import TelegramClient, events
#
# Buranı qurdalama
# Yalnız deploy buttonuyla botunu yarat
# 
api_id = int(os.environ.get("APP_ID", "10300036"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
admin_qrup = int(os.environ.get("ADMIN_QRUP", "-845809113"))
etiraf_qrup = int(os.environ.get("ETIRAF_QRUP", "-1001856348176"))
kanal = os.environ.get("kanal")
log_qrup = int(os.environ.get("LOG_QRUP", "-821257533"))
botad = os.environ.get("BOT_AD")
etirafmsg = os.environ.get("Salam")
startmesaj = os.environ.get("Salam")
etirafyaz = os.environ.get("Salam")
qrupstart = os.environ.get("Salam")
gonderildi = os.environ.get("Salam")
support = os.environ.get("TheBorzSohbet")
sahib = os.environ.get("ordayam_5_deqiqeye")
support2 = os.environ.get("TheBorzMaf")
#
# RoBotlarimTg
# RoBotlarimTg
# RoBotlarimTg

