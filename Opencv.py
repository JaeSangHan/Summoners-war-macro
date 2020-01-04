import pyautogui as pag
import mss, cv2
import numpy as np
from PIL import ImageGrab
import random
from datetime import datetime


from Telegram import *

report = {'ITEM':0, '5☆ RARE':0, '5☆ HERO':0, '5☆ LEGEND':0, '6☆ RARE':0, '6☆ HERO':0, '6☆ LEGEND':0}

# 스크린샷
def CaptureScreenshot():
	now = datetime.now()
	currenttime = now.strftime('[%Y-%m-%d] %I%p-%Mm-%Ss')
	img=ImageGrab.grab()
	saveas="{}{}".format(currenttime,'.png')
	img.save(saveas)
	sendImage(img, currenttime)

# 승리했는지 판별
def compute_victory(img):
	mean = np.mean(img, axis=(0,1))
	
	result = ''
	
	# print(mean[0], mean[1], mean[2])
	if mean[0] > 35 and mean[0] < 50 and mean[1] > 125 and mean[1] < 135 and mean [2] > 150 and mean[2] < 165:
		result = 'CLEAR'
	
	elif mean[0] > 24 and mean[0] < 34 and mean[1] > 71 and mean[1] < 81 and mean [2] > 101 and mean[2] < 111:
		result = 'CLEAR_Rade'
		
	elif mean[0] > 38 and mean[0] < 40 and mean[1] > 59 and mean[1] < 61 and mean [2] > 83 and mean[2] < 86:
		result = 'DEFEATED'
		
	else:
		result = 'WAITING'
	
	if(result == 'DEFEATED'):
		print(mean[0], mean[1], mean[2])
	
	# print(result)
	return result
		
# 룬 종류 판별
def compute_rune(img):
	mean = np.mean(img, axis=(0,1))
	
	result = ''
	
	# print(mean[0], mean[1], mean[2])
	if mean[0] > 102 and mean[0] < 108 and mean[1] > 91 and mean[1] < 97 and mean [2] > 74 and mean[2] < 80:
		result = '5☆ RARE'
		report['5☆ RARE'] += 1
	elif mean[0] > 96 and mean[0] < 102 and mean[1] > 74 and mean[1] < 80 and mean [2] > 106 and mean[2] < 112:
		result = '5☆ HERO'
		report['5☆ RARE'] += 1
	elif mean[0] > 77 and mean[0] < 83 and mean[1] > 76 and mean[1] < 82 and mean [2] > 127 and mean[2] < 133:
		result = '5☆ LEGEND'
		report['5☆ LEGEND'] += 1
	elif mean[0] > 107 and mean[0] < 113 and mean[1] > 98 and mean[1] < 104 and mean [2] > 85 and mean[2] < 91:
		result = '6☆ RARE'
		report['6☆ RARE'] += 1
	elif mean[0] > 102 and mean[0] < 108 and mean[1] > 86 and mean[1] < 92 and mean [2] > 108 and mean[2] < 114:
		result = '6☆ HERO'
		report['6☆ HERO'] += 1
	elif mean[0] > 89 and mean[0] < 105 and mean[1] > 88 and mean[1] < 94 and mean [2] > 123 and mean[2] < 129:
		result = '6☆ LEGEND'
		report['6☆ LEGEND'] += 1
	else:
		result = 'ITEM'
		report['ITEM'] += 1
	
	#print(result)
	
	return result
	

# 룬 판별
rune_icon_pos = {'left': 775, 'top':422, 'width': 58, 'height': 13}
def RuneResult():
	with mss.mss() as sct:
		rune_img = np.array(sct.grab(rune_icon_pos))[:,:,:3]
		
		# cv2.imshow('rune_img', rune_img)
		# cv2.waitKey(0)
		
		return compute_rune(rune_img)

victory_icon_pos = {'left': 808, 'top':302, 'width': 315, 'height': 49}
def VictoryResult():
	with mss.mss() as sct:
		victory_img = np.array(sct.grab(victory_icon_pos))[:,:,:3]
		
		# cv2.imshow('victory_img', victory_img)
		# cv2.waitKey(0)
	
		return compute_victory(victory_img)

			
defeat_icon_pos = {'left': 725, 'top':580, 'width': 190, 'height': 40}
def DefeatResult():
	with mss.mss() as sct:
		defeat_img = np.array(sct.grab(defeat_icon_pos))[:,:,:3]
		
		# cv2.imshow('defeat_img', defeat_img)
		# cv2.waitKey(0)
	
		return compute_victory(defeat_img)


# while True:
	# DefeatResult()
# 승리 판별