import pyautogui as pag
import random, time

 
dummyBtn = {
	'top_left': {
	 'x': 470,
	 'y': 630
	},
	'bottom_right': {
	 'x': 670,
	 'y': 685
	}
}
# 전투 시작버튼

combatBtn = {
	'top_left': {
	 'x': 1230,
	 'y': 600
	},
	'bottom_right': {
	 'x': 1405,
	 'y': 680
	}
}
# 전투 시작버튼

resultBtn = {
	'top_left': {
	 'x': 635,
	 'y': 515
	},
	'bottom_right': {
	 'x': 915,
	 'y': 575
	}
}
# 전투 종료 후 아무곳이나 터치

restartBtn = {
	'top_left': {
	 'x': 635,
	 'y': 515
	},
	'bottom_right': {
	 'x': 915,
	 'y': 575
	}
}
#다시하기 버튼

reviveCancleBtn = {
	'top_left': {
	 'x': 1025,
	 'y': 585
	},
	'bottom_right': {
	 'x': 1200,
	 'y': 635
	}
}
#부활 취소 버튼

# # # # # # # # # # # # # # # # # # # # # # # 차원홀 # # # # # # # # # # # # # # # # # # # # # # # 
DimensionHole_ConfirmBtn_Item1 = {
	'top_left': {
	 'x': 910,
	 'y': 690
	},
	'bottom_right': {
	 'x': 1020,
	 'y': 730
	}
}
# 차원홀 아이템 확인 버튼 (마법재료, 룬 파편 등)

# # # # # # # # # # # # # # # # # # # # # # # 마력의 던전 # # # # # # # # # # # # # # # # # # # # # # # 
MagicHall_ConfirmBtn_Item1 = {
	'top_left': {
	 'x': 905,
	 'y': 710
	},
	'bottom_right': {
	 'x': 1000,
	 'y': 750
	}
}
# 마력의던전 아이템 확인 버튼 (마법재료, 룬 파편 등)

MagicHall_ConfirmBtn_Item2 = {
	'top_left': {
	 'x': 900,
	 'y': 650
	},
	'bottom_right': {
	 'x': 1000,
	 'y': 700
	}
}
# 마력의던전 아이템 확인 버튼 (각인된 소환석, 미지의 소환서)

# # # # # # # # # # # # # # # # # # # # # # # Giant's keep # # # # # # # # # # # # # # # # # # # # # # #

Giant_sellRuneBtn = {
	'top_left': {
	 'x': 820,
	 'y': 675
	},
	'bottom_right': {
	 'x': 940,
	 'y': 715
	}
}
# 룬 판매 버튼 

Giant_getRuneBtn = {
	'top_left': {
	 'x': 990,
	 'y': 670
	},
	'bottom_right': {
	 'x': 1115,
	 'y': 720
	}
}
# 룬 확인 버튼 

Giant_sellRuneOkBtn = {
	'top_left': {
	 'x': 820,
	 'y': 560
	},
	'bottom_right': {
	 'x': 935,
	 'y': 600
	}
}
# 룬 판매확인 버튼 

# # # # # # # # # # # # # # # # # # # # # # # Rade # # # # # # # # # # # # # # # # # # # # # # #

Rade_ConfirmBtn_Item1 = {
	'top_left': {
	 'x': 900,
	 'y': 685
	},
	'bottom_right': {
	 'x': 1030,
	 'y': 730
	}
}
# 보상 확인 버튼 
