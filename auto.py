import time 
import pyautogui
import sys
from imagesearch import *
import pytesseract
from PIL import Image
from pytesseract import image_to_string
import os


def search(image_directory, precision = 0.6):
	time.sleep(0.5)
	button = imagesearch(image_directory, precision)
	print(button)
	if button[0] != -1:
		click_image(image_directory, button, "left", 0.2, offset=5)
	else:
		print(image_directory + "is not found")

def search_loop(image_directory):
	search_bool = 0
	while(search_bool != 1):
		search_pos = imagesearch(image_directory)
		if(search_pos[0] != -1):
			search(image_directory)
			search_bool = 1

def restart():
	#Restart the application
	search('./images/sw_tab.png')
	time.sleep(0.5)
	search('./images/sw_close.png')
	time.sleep(2)
	search('./images/sw_icon.png')

	#Check for "Touch to start"
	restart = -1
	while(restart == -1):
		start_pos = imagesearch('./images/touch_to_start.png')
		if(start_pos[0] != -1):
			restart = 0

	time.sleep(3)

	#Check for adds and close them.
	ad = 0
	while(ad < 5):
		start_ad_pos = imagesearch('./images/start_ad_close.png')
		if(start_ad_pos[0] != -1):
			search('./images/start_ad_close.png')
			ad = ad + 1
		else:
			ad = 10

	search('./images/touch_to_start.png')

	time.sleep(2)
	search('./images/sw_intro_skip.png')

	time.sleep(2)
	search('./images/ad_close_2.png')
	time.sleep(.5)
	search('./images/ad_close_3.png')
	time.sleep(5)

	search('./images/battle_icon.png')
	time.sleep(2)
	search('./images/cairos_dungeon.png')
	time.sleep(2)
	search('./images/giant_tab.png')

	search('./images/gb10_icon.png')
	time.sleep(2)
	search('./images/start_battle_screen2.png')
	time.sleep(2)

	#Check if a refill is necessary
	pos3 = imagesearch("./images/shop.png")
	if(pos3[0] != -1):
		search("./images/shop.png")
		time.sleep(1)
		search("./images/recharge.png")
		time.sleep(0.5)

		#check for the quiz.
		quiz_pos = imagesearch('./images/quiz.png')
		if(quiz_pos[0] != -1):
			pyautogui.screenshot("quiz" + str(screenshot_quiz) + ".png")
			screenshot_quiz = screenshot_quiz + 1
			restart()

		search("./images/yes-recharge.png")
		search("./images/ok.png")
		search("./images/close.png")
		search('./images/start_battle_screen.png')
		time.sleep(1)
		search("./images/start.png")
	else:
		search("./images/start.png")

	autoplay = 0
	while(autoplay != 1):
		autoplay_pos = imagesearch("./images/autoplay_button_gb10.png")
		if(autoplay_pos[0] != -1):
			search("./images/autoplay_button_gb10.png")
			autoplay = 1

	print("Restart Command Ended.")

def checkSlot(image_directory , slot_num):
	slot_pos = imagesearch(image_directory)
	if(slot_pos[0] != -1):
		print("Slot " + str(slot_num))
		return slot_num
	else:
		return -1

'''
Detects and returns the rune slot number.
'''
def detectRuneSlot():
	slot_num = -1
	counter = 1

	while(counter < 7):
		image_directory = './images/rune/slot_' + str(counter) + '.png'
		slot_num = checkSlot(image_directory, counter)
		if(slot_num != -1):
			return slot_num
		else:
			counter = counter + 1


def getRuneStats():
	# load the example image and convert it to grayscale
	image = cv2.imread('./screenshots/123.png')

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	#gray = cv2.GaussianBlur(gray, (5,5), 0)
	gray = cv2.medianBlur(gray, 3)

	#kernel = np.ones((5, 5), np.uint8)
	#cv2.dilate(im, kernel, iterations = 1)
	#cv2.erode(gray, kernel, iterations = 1)

	
	#gray = cv2.bilateralFilter(gray,9,75,75)
	#gray = cv2.addWeighted(image, 1.5, gaussian_3, -0.5, 0, image)

	#scale = 2.5
	#width = int(gray.shape[1] * scale)
	#height = int(gray.shape[0] * scale )
	#dim = (width, height)

	#gray = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)


	gray = cv2.resize(gray, None, fx=3, fy=3, interpolation=cv2.INTER_LINEAR)

	# write the grayscale image to disk as a temporary file so we can apply OCR to it
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	text = pytesseract.image_to_string(Image.open(filename))
	os.remove(filename)
	print(text)

	cv2.imshow("Output", gray)
	cv2.waitKey(0)

def hasSPD():
	pos = imagesearch('./images/rune/spd.png')
	if(pos[0] != -1):
		return True
	else:
		return False

def isRuneType(rune_type):
	if(rune_type == "swift"):
		pos = imagesearch('./images/rune/set/swift_2.png')
	elif(rune_type == "energy"):
		pos = imagesearch('./images/rune/set/energy.png')
	elif(rune_type == "blade"):
		pos = imagesearch('./images/rune/set/blade.png')
	elif(rune_type == "despair"):
		pos = imagesearch('./images/rune/set/despair.png')
	elif(rune_type == "fatal"):
		pos = imagesearch('./images/rune/set/fatal.png')
	else:
		print ("Unknown Rune Type.")

	if(pos[0] != -1):
		return True
	else:
		return False





	







