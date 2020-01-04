import telegram   #텔레그램 모듈을 가져옵니다.
from io import BytesIO

def sendMessage(string):
	my_token = ''   								#put your token here
	bot = telegram.Bot(token = my_token)
	# chat_id = bot.getUpdates()[-1].message.chat.id
	chat_id = '' 									#put your id here
	
	if (string and not string.isspace()):
		bot.sendMessage(chat_id=chat_id, text=string)
		print('Send message completed')
	else:	
		return
		
def sendImage(img, string):
	my_token = ''   								#put your token here
	bot = telegram.Bot(token = my_token)
	# chat_id = bot.getUpdates()[-1].message.chat.id
	chat_id = '' 									#put your id here
	
	if (string and not string.isspace()):
		bio = BytesIO()
		bio.name = string
		img.save(bio, 'JPEG')
		bio.seek(0)
		bot.send_photo(chat_id, photo=bio)
		print('Send image completed')
	else:	
		return