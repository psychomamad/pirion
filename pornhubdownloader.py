from pyrogram import Client,filters
from pyrogram.types import ReplyKeyboardMarkup
import math
import os
import youtube_dl
import pornhub
import random
# ======            ======#
api_id = 14636477
api_hash = 'cb939fa48d9ec95cc9f6b99e841ef59b'
Token = '5118609060:AAFKoaXcL0jK0tVSx_7IOyhkaWcaa6kjByw' #توکن ربات
# ======            ======#
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=Token)
#---------  (  ) ---------#
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
def setfile(name,chat_id,data=''):
    try:
        f = open('data\\'+chat_id+'\\'+name, "w", encoding="Utf-8")
        f.write(data)
    except:
        f = open('data\\'+chat_id+'\\'+name, "a", encoding="Utf-8")
        f.write(data)
    return True
def getfile(name,chat_id):
    f = open('data\\'+chat_id+'\\'+name, "r", encoding="Utf-8")
    contents = f.read()
    return contents
#---------  (  ) ---------#
back = ReplyKeyboardMarkup(['🔙'],resize_keyboard=True)
menu = ReplyKeyboardMarkup(
            [
                ["🔍search video"],
                ["📥download video"],
                ["🪧help"]
            ],resize_keyboard=True)
#---------  (  ) ---------#
@app.on_message(filters.text and filters.private)
async def Bot(Client , message):
    text = message.text
    chat_id = message.chat.id
    chatid = str(chat_id)
    if os.path.isdir(f"data\\{chatid}"):
        pass
    else:
        os.mkdir(f"data\\{chatid}")
        setfile('step.txt',chatid)
    step = getfile('step.txt',chatid)
    if text == '/start' or text == '🔙':
        setfile('step.txt',chatid)
        await message.reply_text('🌷Welcome to Robot Porn Downloader.\n\n🐍 @Glysit', quote=True,reply_markup=menu)
    if text == '🔍search video':
        setfile('step.txt',chatid,'s')
        await message.reply_text('🔎 Send your **text** to **search video**.\n⚠️ **Do not be long **.\n\n🐍 @Glysit', quote=True,reply_markup=back)
    if text == '📥download video':
        setfile('step.txt',chatid,'d')
        await message.reply_text('📹send your **video link** to **download**.\n\n🐍 @Glysit', quote=True,reply_markup=back)
    if text == '🪧help':
        await message.reply_text('**In the search section, you can search for the desired video**.\n**In the download section, you can download it by sending the movie link**.\n\n🐍 @python3_channel', quote=True)
    if step == 's' and text != '🔙':
        r = random.randrange(10)
        try:
            search_keywords = [str(""+text)]
            client = pornhub.PornHub(search_keywords)
            for video in client.getVideos(5,page=int(r)):
                await app.send_photo(chat_id,str(video["background"]),f"ᑎᗩᗰE: <code>"+video["name"]+"</code>\n𝗟𝗶𝗻𝗸: `"+video["url"]+"`\n𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻："+video["duration"])
            await app.send_message(chat_id=chat_id,text="🔙We returned to the main menu",reply_markup=menu)
            setfile('step.txt',chatid)
        except:
            await message.reply_text("❌TᕼEᖇE Iᔕ ᗩ ᑭᖇOᗷᒪEᗰ!")
    if step == 'd' and text != '🔙':
            m = await message.reply_text("𝗽𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁")
            try:
                dire = '/data/{}/%(title)s.%(ext)s'.format(chatid)
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': dire,
                    'nooverwrites': True,
                    'no_warnings': False,
                    'ignoreerrors': True,
                    }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([text])
                    await m.edit_text('✅download\n🔜Upload')
                    for item in os.scandir('data/{}'.format(chatid)):
                        if '.mp4' in item.name:
                            size = convert_size(os.path.getsize('data\\{}\\{}'.format(chatid,item.name)))
                            await app.send_document(chat_id, 'data\\{}\\{}'.format(chatid,item.name),caption=f'''
    📹ɴᴀᴍᴇ : {item.name}
    📦ꜱɪᴢᴇ : {size}
    🔗ʟɪɴᴋ : {text}
                                        ''')
                            os.remove('data\\{}\\{}'.format(chat_id,item.name))
                            await app.send_message(chat_id=chat_id,text="🔙We returned to the main menu",reply_markup=menu)
                    setfile('step.txt',chatid)
                    await m.edit_text('✅download\n✅Upload')
            except:
                await message.reply_text("❌TᕼEᖇE Iᔕ ᗩ ᑭᖇOᗷᒪEᗰ!")
app.run()
