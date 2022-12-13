import telepot as telepot 
from telepot.loop import MessageLoop 

TOKEN = '' 
bot = telepot.Bot(TOKEN) 

START_MESSAGE = "Привет! Это бот - калькулятор /nНачни вводить выражение вида '2+3' " 

def handle(msg): 
""" Process request like '3+2' """ 
content_type, chat_type, chat_id = telepot.glance(msg) 
text = msg["text"] 
try: 
answer = eval(text) 
except: 
answer = "Я пока не умею такое считать" 
bot.sendMessage(chat_id, "Ответ: {}".format(answer)) 


MessageLoop(bot, handle).run_as_thread() 

# Keep the program running. 
while True: 
n = input('To stop enter "stop":') 
if n.strip() == 'stop':