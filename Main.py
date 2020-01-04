import pyautogui as pag
import keyboard 
import random, time
import sys
import os 
import msvcrt #To use kbhit 

from BtnPos import *
from Opencv import *
from Telegram import *
from auto import *
pag.FAILSAFE= False

def main():
	MacroStart()
  
def getKeyState():
	was_pressed = False
	if keyboard.is_pressed('x'):
		if not was_pressed:
			print ('(매크로 일시정지)')
			variable = input('INPUT SOMETHING!\n')
			print ('(매크로 재개)')
	else:
		was_pressed = True

def Click_RandDelay():
	pag.mouseDown()
	time.sleep(random.uniform(0.12345, 0.32111))
	pag.mouseUp()

	
def moveToBtn(btnName):
	pag.moveTo(
		x=random.uniform(btnName['top_left']['x'], btnName['bottom_right']['x']),
		y=random.uniform(btnName['top_left']['y'], btnName['bottom_right']['y']),
		duration=random.uniform(0.12345, 0.32111)
	)
	Click_RandDelay()

# 수정필요
def checkRefill():
	# Check if refill is neccessary
	time.sleep(1)
	pos3 = imagesearch("./images/shop.png")
	if(pos3[0] != -1):
		#Check if the desired number of refill is hit.
		refill = refill + 1	
		if(refill == mod_refill):
			print("End of Script.")
			sys.exit()

		search("./images/shop.png")
		time.sleep(1)
		search("./images/recharge.png")
		time.sleep(0.5)
		sendMessage('에너지 충전')
		CaptureScreenshot()
		#check for the quiz.
		quiz_pos = imagesearch('./images/quiz.png')
		if(quiz_pos[0] != -1):
			pyautogui.screenshot("quiz" + str(screenshot_quiz) + ".png")
			screenshot_quiz = screenshot_quiz + 1
			restart()
		else:
			#print("Refill: " + str(refill))
			search("./images/yes-recharge.png")
			search("./images/ok.png")
			search("./images/close.png")

		if conditional == 1:
			search("./images/replay.png")

		elif conditional == 2:
			search("./images/prepare-failed.png")
	
def Emoticon(type):
	if (type == 1):
		os.system('cls')	
		print('대기중 (／*ω*)／')
		time.sleep(0.2)
		os.system('cls')	
		print('대기중 ＼(*ω*＼)')
		time.sleep(0.2)
	if (type == 2):
		os.system('cls')	
		print('                   ○(^0^)○')	
		time.sleep(0.2)
		os.system('cls')	
		print('                    (○^0^)=○     ○(⊙ω⊙)○')
		time.sleep(0.3)
		os.system('cls')	
		print('                    (○^0^)==○☆(○>ω<)○')
		time.sleep(0.3)
		os.system('cls')	
		print('                    (○^0^)=○       (○>ω<)○')
		time.sleep(0.3)
		os.system('cls')	
		print('                   ○(^0^)○')
		time.sleep(0.2)
		os.system('cls')	
		print('○(⊙ω⊙)○     ○=(^0^○)')
		time.sleep(0.3)
		os.system('cls')	
		print('    ○(>ω<○)☆○==(^0^○)')
		time.sleep(0.3)
		os.system('cls')	
		print('○(>ω<○)       ○=(^0^○)')
		time.sleep(0.3)
	
def Play_DimensionHole():
	while True:
		
		conditional = -1	

		while (conditional == -1):
			pos = imagesearch('./images/victory-paint.png')
			pos2 = imagesearch('./images/no.png')
			if(pos[0] != -1):			#If Victory img is found
				conditional = 1
			elif(pos2[0] != -1):		#If Fail is found.
				conditional = 2
				
			print(conditional)
			
			
		if conditional == 1:
			time.sleep(3)
			print('전투 결과 터치 1')
			click_image("./images/victory-paint.png", pos, "left", 0.2, offset=5)
			time.sleep(1)
			print('전투 결과 터치 2')
			click_image("./images/victory-paint.png", pos, "left", 0.2, offset=5)
			
			search("./images/ok.png")
			# 확인버튼 누르기
			
			search("./images/replay.png")
			# 다시하기 버튼 누르기
			sendMessage('차원홀 클리어')
			print('CLEAR')
			
		elif conditional == 2:
			search("./images/no.png")
			sendMessage('차원홀 게임오버')
			time.sleep(2)
			pyautogui.click(button='left')
			search("./images/prepare-failed.png")
			search("./images/start.png")
		# else:
			# Emoticon(2)
			
def Play_Secret():
	time.sleep(2)
	while True:
		time.sleep(random.uniform(0.12345, 0.32111))
		moveToBtn(MagicHall_ConfirmBtn_Item2)
		# 확인버튼 누르기
		time.sleep(random.uniform(0.12345, 0.32111))
		moveToBtn(restartBtn)
		# 다시하기 버튼 누르기
		print('CLEAR')
			
def Play_MagicHall():
	while True:
		if VictoryResult() == 'CLEAR':
			moveToBtn(resultBtn)
			# 전투결과 한번 누르기
			
			moveToBtn(resultBtn)
			# 전투결과 두번 누르기
			
			time.sleep(1)
			moveToBtn(MagicHall_ConfirmBtn_Item1)
			# 확인버튼 누르기
			
			time.sleep(1)
			moveToBtn(MagicHall_ConfirmBtn_Item2)
			# 각인된 소환석 확인버튼 누르기
			
			moveToBtn(restartBtn)
			# 다시하기 버튼
			print('CLEAR')
			
		else:
			print('WAITING')
			
def Play_AscensionTop():
	while True:
		conditional = -1
		while (conditional == -1):
			pos = imagesearch('./images/victory-paint.png', 0.8)
			pos2 = imagesearch('./images/no.png', 0.8)
			if(pos[0] != -1):			#If Victory img is found
				conditional = 1
			elif(pos2[0] != -1):		#If Fail is found.
				conditional = 2
			print(conditional)
					
			if conditional == 1:
				time.sleep(3)
				print('전투 결과 터치 1')
				click_image("./images/victory-paint.png", pos, "left", 0.2, offset=5)
				time.sleep(1)
				print('전투 결과 터치 2')
				click_image("./images/victory-paint.png", pos, "left", 0.2, offset=5)
				
				time.sleep(1)
				#INSERT RUNE CHECKING STUFF HERE
				search("./images/ok.png")
				
				search("./images/replay.png")
				search("./images/start.png", 0.5)
				
				time.sleep(1)
				
			elif conditional == 2:
				print('게임오버')
				sendMessage('게임오버')
				CaptureScreenshot()
				time.sleep(1)		
				search("./images/no.png")
				time.sleep(2)
				pyautogui.click(button='left')
				search("./images/prepare-failed.png")
				time.sleep(1)
			
			
def Play_Giant():
	screenshot_counter = 0
	screenshot_quiz = 0
	refill = 0
	mod_refill = 0
	mod_refill = int(input("에너지 리필 개수: "))

	while (refill < mod_refill):
		getKeyState()
		conditional = -1	

		while (conditional == -1):
			pos = imagesearch('./images/victory-paint.png', 0.8)
			pos2 = imagesearch('./images/no.png', 0.8)
			if(pos[0] != -1):			#If Victory img is found
				conditional = 1
			elif(pos2[0] != -1):		#If Fail is found.
				conditional = 2
				
			# print(conditional)
			Emoticon(2)
				
		if conditional == 1:
			time.sleep(3)
			print('전투 결과 터치 1')
			click_image("./images/victory-paint.png", pos, "left", 0.2, offset=5)
			time.sleep(1)
			print('전투 결과 터치 2')
			click_image("./images/victory-paint.png", pos, "left", 0.2, offset=5)
			
			time.sleep(1)
			#INSERT RUNE CHECKING STUFF HERE
			sell_pos = imagesearch("./images/sell.png")
			if(sell_pos[0] != -1):
				rune_pos = imagesearch("./images/sixstar.png",0.9)
				if(rune_pos[0] != -1):
					# pyautogui.screenshot("./screenshots/6/" + str(screenshot_counter) + ".png")
					sendMessage('6성룬 획득')
					CaptureScreenshot()
					search("./images/ok.png")
				else:
					if(isRuneType("swift")):
						search("./images/ok.png")						
					else:
						search("./images/sell.png")
						search("./images/yes-sell.png")
			else:
				search("./images/ok.png", 0.8)


			# search("./images/ok.png", 0.6) # for 할로윈 이벤트
			search("./images/replay.png")
			
			# sendMessage(RuneGrade + ' 획득!\n' + '\n=============\n' + 
			# '[실시간 획득현황]\n' + 
			# '재료 아이템 : ' + str(report['ITEM']) + '개\n' + 
			# '5성 희귀 : ' + str(report['5☆ RARE']  ) + '개\n' + 
			# '5성 영웅 : ' + str(report['5☆ HERO']  ) + '개\n' + 
			# '5성 전설 : ' + str(report['5☆ LEGEND']) + '개\n' + 
			# '6성 희귀 : ' + str(report['6☆ RARE']  ) + '개\n' + 
			# '6성 영웅 : ' + str(report['6☆ HERO']  ) + '개\n' + 
			# '6성 전설 : ' + str(report['6☆ LEGEND']) + '개\n')
			
			time.sleep(1)
			
		elif conditional == 2:
			print('게임오버')
			sendMessage('게임오버')
			CaptureScreenshot()
			time.sleep(1)		
			search("./images/no.png")
			time.sleep(2)
			pyautogui.click(button='left')
			search("./images/prepare-failed.png")
			time.sleep(1)
			
		# Check if refill is neccessary
		time.sleep(1)
		pos3 = imagesearch("./images/shop.png")
		if(pos3[0] != -1):
			#Check if the desired number of refill is hit.
			refill = refill + 1	
			if(refill == mod_refill):
				print("End of Script.")
				sys.exit()
	
			search("./images/shop.png")
			time.sleep(1)
			search("./images/recharge.png")
			time.sleep(0.5)
			sendMessage('에너지 충전')
			CaptureScreenshot()
			#check for the quiz.
			quiz_pos = imagesearch('./images/quiz.png')
			if(quiz_pos[0] != -1):
				pyautogui.screenshot("quiz" + str(screenshot_quiz) + ".png")
				screenshot_quiz = screenshot_quiz + 1
				restart()
			else:
				#print("Refill: " + str(refill))
				search("./images/yes-recharge.png")
				search("./images/ok.png")
				search("./images/close.png")
	
			if conditional == 1:
				search("./images/replay.png")
	
			elif conditional == 2:
				search("./images/prepare-failed.png")
			
		#Need to click start if the run failed.
		if conditional == 2:
			search("./images/start.png", 0.5)
		
		time.sleep(1)
			
def Play_Volcano():
	screenshot_counter = 0
	screenshot_quiz = 0
	refill = 0
	mod_refill = 0
	mod_refill = int(input("에너지 리필 개수: "))
	while True:
		conditional = -1
		while (conditional == -1):
			pos = imagesearch('./images/victory-paint.png', 0.8)
			pos2 = imagesearch('./images/no.png', 0.8)
			if(pos[0] != -1):			#If Victory img is found
				conditional = 1
			elif(pos2[0] != -1):		#If Fail is found.
				conditional = 2
			Emoticon(2);
					
		if conditional == 1:
			print('CLEAR')	
			time.sleep(3)
			print('전투 결과 터치 1')
			click_image("./images/victory-paint.png", pos, "left", 0.2, offset=5)
			time.sleep(0.5)
			print('전투 결과 터치 2')
			click_image("./images/victory-paint.png", pos, "left", 0.2, offset=5)
		
			time.sleep(1)
			sell_pos = imagesearch("./images/sell.png")

			if(sell_pos[0] != -1):
				search("./images/sell.png")
				search("./images/yes-sell.png")
			else:
				search("./images/ok.png")
			
			search("./images/replay.png")
			

			search("./images/homun.png")
			search("./images/start.png")
			
		elif conditional == 2:
			print('게임오버')
			time.sleep(1)		
			search("./images/no.png")
			time.sleep(2)
			pyautogui.click(button='left') # 아무곳이나 터치
			search("./images/prepare-failed.png")
			time.sleep(1)
		
		# Check if refill is neccessary
		time.sleep(1)
		pos3 = imagesearch("./images/shop.png")
		if(pos3[0] != -1):
			#Check if the desired number of refill is hit.
			refill = refill + 1	
			if(refill == mod_refill):
				print("End of Script.")
				sys.exit()
	
			search("./images/shop.png")
			time.sleep(1)
			search("./images/recharge.png")
			time.sleep(0.5)
			sendMessage('에너지 충전')
			CaptureScreenshot()
			#check for the quiz.
			quiz_pos = imagesearch('./images/quiz.png')
			if(quiz_pos[0] != -1):
				pyautogui.screenshot("quiz" + str(screenshot_quiz) + ".png")
				screenshot_quiz = screenshot_quiz + 1
				restart()
			else:
				#print("Refill: " + str(refill))
				search("./images/yes-recharge.png")
				search("./images/ok.png")
				search("./images/close.png")
	
			if conditional == 1:
				search("./images/replay.png")
	
			elif conditional == 2:
				search("./images/prepare-failed.png")
			
		#Need to click start if the run failed.
		if conditional == 2:
			search("./images/start.png", 0.5)
			
		time.sleep(1)

def Play_Rade():
	while True:
		if VictoryResult() == 'CLEAR_Rade':
			print('CLEAR')
			
			time.sleep(3)
			print('전투 결과 터치 1')
			moveToBtn(resultBtn)
			# 전투결과 한번 누르기
			
			print('전투 결과 터치 2')
			moveToBtn(resultBtn)
			# 전투결과 두번 누르기
			
			time.sleep(1)
			print('보상확인')
			moveToBtn(Rade_ConfirmBtn_Item1)
			# 전투결과 두번 누르기
			
			print('다시하기로 이동')
			moveToBtn(restartBtn)
			

# def Test():
	# while True:
		# start_pos = imagesearch('./images/start.png', 0.5)
		# if(start_pos[0] != -1):
		
			
def MacroStart():
	print(" 1. 차원홀 \n 2. 마력의 던전 \n 3. 거인/용의 던전 \n 4. 화산 \n 5. 이계 레이드 \n 6. 시험의 탑\n 7. 비던\n")
	select = int(input("어느 던전에 입장하시겠습니까?: "))
	
	
	if select == 1:
		Play_DimensionHole()
	elif select == 2:
		Play_MagicHall()
	elif select == 3:
		Play_Giant()
	elif select == 4:
		Play_Volcano()	
	elif select == 5:
		Play_Rade()
	elif select == 6:
		Play_AscensionTop()	
	elif select == 7:
		Play_Secret()

main()


# while True:
 # x, y = pag.position()
 # print('x: %s, y: %s' % (x,y))