



MAP_MC3 = 0x00  # 2-5 y
MAP_GV2 = 0x01  # 2-2 y
MAP_DP2 = 0x02  # 2-3 y
MAP_BC2 = 0x03  # 2-4 y
MAP_VL2 = 0x04  # 4-4 y
MAP_RR  = 0x05  # 4-5 y
MAP_KB2 = 0x06  # 4-2 y
MAP_MC1 = 0x07  # 1-1 y
MAP_GV3 = 0x08  # 4-3 y
MAP_BC3 = 0x09  # 3-4 y
MAP_CI2 = 0x0A  # 3-2 y
MAP_DP3 = 0x0B  # 4-1 y
MAP_VL1 = 0x0C  # 3-3 y
MAP_KB1 = 0x0D  # 3-1 y
MAP_MC4 = 0x0E  # 3-5 y
MAP_MC2 = 0x0F  # 1-5 y
MAP_GV1 = 0x10  # 1-3 y
MAP_BC1 = 0x11  # 1-4 y
MAP_CI1 = 0x12  # 2-1 y
MAP_DP1 = 0x13  # 1-2 y

MAP_BT3 = 0x14
MAP_BT4 = 0x15
MAP_BT1 = 0x16
MAP_BT2 = 0x17





MAP_NUM = MAP_MC1







import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import json

import math


import pygame
from pygame.gfxdraw import *
from pygame.locals import *


if False:
	import pygame._view













MAP_PAD_TILES = 16





#S_W = S_H = WINDOW_SIZE

EDIT_W = EDIT_H = 512 + (MAP_PAD_TILES * 8 * 2)//2
EDIT_X = 0
EDIT_Y = 0

VIEW_W = 512
VIEW_H = 512






map_w = map_h = 1024 + (MAP_PAD_TILES * 8 * 2)

map_offset_w = map_offset_h = -(MAP_PAD_TILES * 8)

VIEW_X = EDIT_W
VIEW_Y = 0

ZOOM_SCL = 1024 / map_w


#P1_RASTER_OFFSET = 0x0000
P1_CENTER_OFFSET = 0x0066

_P1_L_fe = 0x0040
_P1_L_es = 0x0100

_P1_A_zs = 0x3400
_P1_V_of = 0x0066
_P1_V_va = 0x0018


BG_MODE_BLANK = -1
BGMODE0 = 0
BGMODE1 = 1
BGMODE7 = 7


SNES_W = 256
SNES_H = 224

TYPE_NUM = type(0)
TYPE_LIST = type(list([]))


def READ_JSON(json_file):

	with open(json_file) as jf:
		data = json.load(jf)

	return data


def WRITE_JSON(json_file, data):
	with open(json_file, 'w') as f:
		f.write(json.dumps(data, indent=1))



def frmt_byte(b):
	return format(b, "02X")

def frmt_word(w):
	return format(w, "04X")


def frmt_byte_asar(b):
	if b >= 0:
		return "$" + frmt_byte(b)
	else:
		return "-$" + frmt_byte(-b)

def frmt_word_asar(w):
	if w >= 0:
		return "$" + frmt_word(w)
	else:
		#return "-$" + frmt_word(-w)
		return "$" + frmt_word(0x10000 + w)


def frmt_byte_h(b):
	if b >= 0:
		return frmt_byte(b) + "h"
	else:
		return "-" + frmt_byte(-b) + "h"

def frmt_word_h(w):
	if b >= 0:
		return frmt_word(b) + "h"
	else:
		return "-" + frmt_word(-b) + "h"


def UNMASK(v, b):
	return v - (v & b)


def CLIP(a):
	if a & 0x2000:
		return (a) | (~0x3FF)
	else:
		return (a) & 0x3FF



MAP_NAMES = (
	"Mario Circuit 3", #00h
	"Ghost Valley 2",  #01h
	"Donut Plains 2",  #02h
	"Bowser Castle 2", #03h
	"Vanilla Lake 2",  #04h
	"Rainbow Road",    #05h
	"Koopa Beach 2",   #06h
	"Mario Circuit 1", #07h
	"Ghost Valley 3",  #08h
	"Bowser Castle 3", #09h
	"Choco Island 2",  #0Ah
	"Donut Plains 3",  #0Bh
	"Vanilla Lake 1",  #0Ch
	"Koopa Beach 1",   #0Dh
	"Mario Circuit 4", #0Eh
	"Mario Circuit 2", #0Fh
	"Ghost Valley 1",  #10h
	"Bowser Castle 1", #11h
	"Choco Island 1",  #12h
	"Donut Plains 1",  #13h

	"Battle Course 3", #14h
	"Battle Course 4", #15h
	"Battle Course 1", #16h
	"Battle Course 2", #17h
)

MAP_OOB_TILES = (
	"OOB_MC",
	"OOB_GV",
	"OOB_DP",
	"OOB_BC",
	"OOB_VL",
	"OOB_RR",
	"OOB_KB",
	"OOB_MC",
	"OOB_GV",
	"OOB_BC",
	"OOB_CI",
	"OOB_DP",
	"OOB_VL",
	"OOB_KB",
	"OOB_MC",
	"OOB_MC",
	"OOB_GV",
	"OOB_BC",
	"OOB_CI",
	"OOB_DP",


	"OOB_VL",
	"OOB_MC",
	"OOB_DP",
	"OOB_KB",
)


NUM_ZONES = (
	40, #00h
	45, #01h
	37, #02h
	66, #03h
	29, #04h
	46, #05h
	25, #06h
	30, #07h
	46, #08h
	51, #09h
	29, #0Ah
	35, #0Bh
	23, #0Ch
	36, #0Dh
	41, #0Eh
	35, #0Fh
	33, #10h
	35, #11h
	24, #12h
	37, #13h

	53,#20, #14h
	53,#20, #15h
	43,#13, #16h
	53,#20, #17h
)






class Editor:

	def __init__(self, S_X, S_Y, S_W, S_H):

		self.S_X = S_X
		self.S_Y = S_Y

		self.S_W = S_W
		self.S_H = S_H

		self.ZOOM = 1

		self.X_SHIFT = 0
		self.Y_SHIFT = 0

		self.HELD_CAM_NUM = None
		self.DROPPED_CAM = False

		self.SELECTED_ZONE = None






	def get_map_mouse_pos(self):

		m_x, m_y = pygame.mouse.get_pos()

		return (
			int((((m_x - self.S_X) / self.S_W) * map_w) + map_offset_w),
			int((((m_y - self.S_Y) / self.S_H) * map_h) + map_offset_h)
		)




	'''
	def INCREASE_ZOOM(self):
		if self.ZOOM < 4:
			self.ZOOM += 1

	def DECREASE_ZOOM(self):
		if self.ZOOM > 0:
			self.ZOOM -= 1
	'''

	def get_zoom(self):
		return self.ZOOM

	def set_held_cam(self, held_cam_num):
		self.HELD_CAM_NUM = held_cam_num

	def drop_cam(self):
		self.HELD_CAM_NUM = None
		self.DROPPED_CAM = True

	def get_held_cam(self):
		return self.HELD_CAM_NUM


	def set_selected_zone(self, zone_num):
		self.SELECTED_ZONE = zone_num

	def unselect_zone(self):
		self.SELECTED_ZONE = None

	def get_selected_zone(self):
		return self.SELECTED_ZONE






BALLOON_SPRITE = None
NUM_0_SPRITE = None
NUM_1_SPRITE = None
NUM_2_SPRITE = None
NUM_3_SPRITE = None
NUM_4_SPRITE = None
NUM_5_SPRITE = None
NUM_6_SPRITE = None
NUM_7_SPRITE = None
NUM_8_SPRITE = None
NUM_9_SPRITE = None

NUM_SPRITES = []

PI = math.pi


def to_angle(a):
	return (((a / 0x10000) * -1) + 0.25) * 2 * PI


FOV_ANGLE = 25 * PI / 180


class CAM:

	def __init__(self):

		self.x = -1000
		self.y = -1000
		self.z = -1000
		self.a = 0

		self.transparent = False


	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, _x):
		self._x = _x
	
	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, _y):
		self._y = _y

	@property
	def z(self):
		return self._z

	@z.setter
	def z(self, _z):
		self._z = _z
	
	@property
	def a(self):
		return self._a

	@a.setter
	def a(self, _a):
		self._a = _a

	@property
	def transparent(self):
		return self._transparent

	@transparent.setter
	def transparent(self, _transparent):
		self._transparent = _transparent



	def display_on(self, surface, cam_number=None, show_balloon=False, show_lines=False):

		disp_x = self.x - map_offset_w
		disp_y = self.y - map_offset_h


		c = math.cos(to_angle(self.a + 0x4000))
		s = -math.sin(to_angle(self.a + 0x4000))

		c2 = math.cos(to_angle(self.a))
		s2 = -math.sin(to_angle(self.a))

		cF = math.cos(to_angle(self.a))
		sF = -math.sin(to_angle(self.a))

		cFL = math.cos(to_angle(self.a) + FOV_ANGLE)
		sFL = -math.sin(to_angle(self.a) + FOV_ANGLE)

		cFR = math.cos(to_angle(self.a) - FOV_ANGLE)
		sFR = -math.sin(to_angle(self.a) - FOV_ANGLE)


		r2 = 0x1800 / 256
		#r1 = 0x10F8 / 256
		r0 = 0



		if self._transparent:
			LINE_COL = (200, 0, 200, 100)
			LINE_COL2 = (255, 0, 0, 40)
			#rF = 0x600
			#rF2 = 0xC00
			rF = 0x100
			rF2 = 0x200
		else:
			LINE_COL = (200, 0, 200, 220)
			LINE_COL2 = (255, 0, 0, 100)
			rF = 0x100
			rF2 = 0x200


		rB = 0x03

		rLR = 0x0020

		#rF = 0x100

		C = (disp_x, disp_y)

		L = (disp_x - rLR*c, disp_y - rLR*s)
		R = (disp_x + rLR*c, disp_y + rLR*s)

		LB = L
		RB = R

		LF = (L[0] + rF*cFL, L[1] + rF*sFL)
		RF = (R[0] + rF*cFR, R[1] + rF*sFR)

		LF2 = (L[0] + rF2*cFL, L[1] + rF2*sFL)
		RF2 = (R[0] + rF2*cFR, R[1] + rF2*sFR)

		# NOTE: camera stuff here isn't exact, but the difference is very small


		
		BALLOON_SPR = BALLOON_SPRITE.copy()

		if self._transparent: BALLOON_SPR.set_alpha(100)

		
		if show_balloon:
			surface.blit(pygame.transform.scale(BALLOON_SPR.copy(), (32, 32)),
				(
					disp_x - 16, 
					disp_y - 15
				)
			)
		


		if show_lines:

			surf = pygame.Surface((surface.get_rect()[2],surface.get_rect()[3]), SRCALPHA)
			if self._transparent:
				surf.set_alpha(100)
			else:
				surf.set_alpha(200)
			'''
			#pygame.draw.polygon(surf, LINE_COL2, [LF2, RF2, RF, LF])
			#pygame.draw.polygon(surf, LINE_COL, [LF, RF, R, L])
			'''
			#pygame.draw.aaline(surface, LINE_COL, C, L)
			pygame.draw.aaline(surf, LINE_COL2, LF2, RF2)
			pygame.draw.aaline(surf, LINE_COL2, LF2, LF)
			pygame.draw.aaline(surf, LINE_COL2, RF2, RF)
			pygame.draw.aaline(surf, LINE_COL, LF, RF)
			pygame.draw.aaline(surf, LINE_COL, LF, L)
			pygame.draw.aaline(surf, LINE_COL, RF, R)
			pygame.draw.aaline(surf, LINE_COL, L, R)
			

			surface.blit(surf, (0, 0))

		if cam_number != None:
			num_A = cam_number // 10
			num_B = cam_number % 10

			surface.blit(pygame.transform.scale(NUM_SPRITES[num_A].copy(), (16, 16)),
				(
					#(disp_x + r2*c2) - 16, 
					#(disp_y + r2*s2) - 8
					(disp_x + r0*c) - 16, 
					(disp_y + r0*s) - 8
				)
			)

			surface.blit(pygame.transform.scale(NUM_SPRITES[num_B].copy(), (16, 16)),
				(
					#(disp_x + r2*c2) - 0, 
					#(disp_y + r2*s2) - 8
					(disp_x + r0*c) - 0, 
					(disp_y + r0*s) - 8
				)
			)




		return surface





'''
class ZONE:

	def __init__(self):

		self.x = -1000
		self.y = -1000
		self.w = 0
		self.h = 0
		self.z_type = 0

		self.transparent = False


	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, _x):
		self._x = _x
	
	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, _y):
		self._y = _y

	@property
	def w(self):
		return self._w

	@w.setter
	def w(self, _w):
		self._w = _w

	@property
	def h(self):
		return self._h

	@h.setter
	def h(self, _h):
		self._h = _h

	@property
	def z_type(self):
		return self._z_type

	@z_type.setter
	def z_type(self, _z_type):
		self._z_type = _z_type

	@property
	def transparent(self):
		return self._transparent

	@transparent.setter
	def transparent(self, _transparent):
		self._transparent = _transparent



	def display_on(self, surface, cam_number=None, show_balloon=False, show_lines=False):

		disp_x = self.x - map_offset_w
		disp_y = self.y - map_offset_h

		return surface
'''


class CAM_DATA(object):
	
	def __init__(self, json_file=""):
		self._json_file = json_file

		if json_file != "":
			self._data = READ_JSON(self._json_file)
			self._create_cam_data(self._data)


	def _set_data(self, data):
		self._data = data


	def _create_cam_data(self, data=None):
		if data != None:
			self._set_data(data)

		data = self._data


		self._CAMERAS = {}

		self._ZONES = {}

		for tnum in range(0x18):
			track = self._data[str(tnum)]

			cam_data = {
				"size": len(track["cameras"]),
				"cams": [],
			}

			zone_data = {
				"size": len(track["zones"]),
				"zones": track["zones"]
			}

			for c in track["cameras"]:
				cam = CAM()
				cam.x = c[0]
				cam.y = c[1]
				cam.a = c[2]

				cam_data["cams"].append(cam)


			self._CAMERAS[tnum] = cam_data
			self._ZONES[tnum] = zone_data

	def save_cameras(self):
		TRACK_DATA = {}

		for tnum in range(0x18):
			track = {
				"track_name": MAP_NAMES[tnum],
				"zones": self._ZONES[tnum]["zones"],
				"cameras": []
			}

			for c in self._CAMERAS[tnum]["cams"]:
				track["cameras"].append((c.x, c.y, c.a))

			TRACK_DATA[str(tnum)] = track

		print('[INFO] SAVING CAM DATA to', self._json_file)

		WRITE_JSON(self._json_file, TRACK_DATA)


	def print_cameras(self, track_num=None):

		# TODO: print all?
		if track_num == None:
			track_num = MAP_NUM


		zone_dict = self._ZONES[track_num]
		cam_dict = self._CAMERAS[track_num]


		print("; ==============================================")
		print("; Track " + frmt_byte(track_num) + ": " + MAP_NAMES[track_num])
		print("; ==============================================")
		print("zone_" + frmt_byte(track_num) + ":\t\t; (" + str(zone_dict["size"]) + " zones)")

		z_idx = 0
		for z in zone_dict["zones"]:
			if z_idx == 0:
				print("\t\tdb\t", end="")
			else:
				print(",", end="")

			print("cam(" + frmt_byte_asar(z) + ")", end="")

			z_idx += 1
			if z_idx == 4: 
				z_idx = 0
				print("")

		if z_idx != 0: print("")
		print("")
		print("camera_" + frmt_byte(track_num) + ":")
		print("\t\t;       xpos  ypos  angle")

		for c in cam_dict["cams"]:
			print("\t\t%CAMERA(" + frmt_word_asar(c.x) + "," + frmt_word_asar(c.y) + "," + frmt_word_asar(c.a) + ")")
		print("\t\t; ...")
		print("")
		print("; ==============================================")







		







KEY_NAMES = {
	pygame.K_n: "n",
	pygame.K_q: "q",
	pygame.K_e: "e",
	pygame.K_p: "p",
	pygame.K_m: "m",
	pygame.K_s: "s",
	pygame.K_c: "c",
	pygame.K_l: "l",
	pygame.K_z: "z",
	pygame.K_RIGHT: "right",
	pygame.K_LEFT: "left",
	pygame.K_UP: "up",
	pygame.K_DOWN: "down",
}


CURR_FRAME_KEYS = {
	"n": False,
	"q": False,
	"e": False,
	"p": False,
	"m": False,
	"s": False,
	"c": False,
	"l": False,
	"z": False,
	"right": False,
	"left": False,
	"up": False,
	"down": False,
}

PREV_FRAME_KEYS = {}
KEYS_NEW = {}
KEYS_RELEASED = {}

for k_button in CURR_FRAME_KEYS:
	PREV_FRAME_KEYS[k_button] = CURR_FRAME_KEYS[k_button]
	KEYS_NEW[k_button] = CURR_FRAME_KEYS[k_button]
	KEYS_RELEASED[k_button] = CURR_FRAME_KEYS[k_button]



def GET_MAP_INITIALS(MAP_NUM):

	if MAP_NUM == 0x05: 	# RR
		return "RR"
	elif MAP_NUM >= 0x14 and MAP_NUM <= 0x17:	# battle course
		return "BT" + MAP_NAMES[MAP_NUM][-1]
	else:
		return ''.join([s[0] for s in MAP_NAMES[MAP_NUM].split(" ")])




chk_g = 1684340580
chk_r = 1694458980
chk_o = 1694484580
chk_y = 1694498660

l_alph = 240

raw_cols_to_out_cols = {
	0: (0, 0, 0, 0),
	chk_g: (100, 255, 100, l_alph),
	chk_r: (255, 100, 100, l_alph),
	chk_o: (255, 200, 100, l_alph),
	chk_y: (255, 255, 100, l_alph),
}


def create_map_img(MAP_NUM):
	global MAP_IMAGE_FILE

	MAP_INITIALS = GET_MAP_INITIALS(MAP_NUM)

	MAP_IMAGE_FILE = "assets/maps/" + MAP_INITIALS + "/" + MAP_INITIALS + ".png"
	#OOB_TILE_FILE = "assets/OOB_tiles/" + MAP_OOB_TILES[MAP_NUM] + ".png"
	ZONE_IMAGE_FILE = "assets/maps/" + MAP_INITIALS + "/checkpoints.png"

	ZONE_DATA_FILE = "assets/maps/" + MAP_INITIALS + "/track.smkc"



	base_map = pygame.image.load(MAP_IMAGE_FILE).convert_alpha()
	#oob_tile = pygame.image.load(OOB_TILE_FILE).convert_alpha()
	zone_map = pygame.image.load(ZONE_IMAGE_FILE).convert_alpha()

	MAP = pygame.Surface((map_w, map_h), SRCALPHA)

	MAP.fill((0, 0, 0, 255))

	# add outer ring of oob tiles




	# add central map
	MAP.blit(base_map, (-map_offset_w, -map_offset_h))

	#MAP.blit(zone_map, (-map_offset_w, -map_offset_h))


	zones_data = parse_zone_data_file(ZONE_DATA_FILE)





	ZONES_BUFF = []
	ZONES_BUFF.append([-1 for _ in range(64 + 2)])
	for row in zones_data: ZONES_BUFF.append([-1] + row + [-1])
	ZONES_BUFF.append([-1 for _ in range(64 + 2)])


	pix_arr = pygame.PixelArray(zone_map)

	z_w = 16 # width of one tile

	lw = 2	# outline width


	for y in range(64):
		y_i = y + 1
		py  = y*z_w

		pT = py
		pB = py + (z_w - lw)

		for x in range(64):
			x_i = x + 1
			px  = x*z_w

			pL = px
			pR = px + (z_w - lw)

			zone_num = ZONES_BUFF[y_i][x_i]

			if zone_num == 0xFF: continue

			try:
				line_col = raw_cols_to_out_cols[pix_arr[px, py]]
			except KeyError:
				line_col = (100, 200, 100, l_alph)

			### sides ###

			# top
			if ZONES_BUFF[y_i - 1][x_i + 0] != zone_num: 
				for i in range(z_w): 
					for o in range(lw): pix_arr[pL + i, pT + o] = line_col

			# bottom
			if ZONES_BUFF[y_i + 1][x_i + 0] != zone_num: 
				for i in range(z_w): 
					for o in range(lw): pix_arr[pL + i, pB + o] = line_col

			# left
			if ZONES_BUFF[y_i + 0][x_i - 1] != zone_num: 
				for i in range(z_w): 
					for o in range(lw): pix_arr[pL + o, pT + i] = line_col

			# right
			if ZONES_BUFF[y_i + 0][x_i + 1] != zone_num: 
				for i in range(z_w): 
					for o in range(lw): pix_arr[pR + o, pT + i] = line_col


			### corners ###

			# top-left
			if ZONES_BUFF[y_i - 1][x_i - 1] != zone_num: 
				for i in range(lw): 
					for o in range(lw): pix_arr[pL + i, pT + o] = line_col

			# top-right
			if ZONES_BUFF[y_i - 1][x_i + 1] != zone_num: 
				for i in range(lw): 
					for o in range(lw): pix_arr[pR + i, pT + o] = line_col

			# bottom-left
			if ZONES_BUFF[y_i + 1][x_i - 1] != zone_num: 
				for i in range(lw): 
					for o in range(lw): pix_arr[pL + i, pB + o] = line_col

			# bottom-right
			if ZONES_BUFF[y_i + 1][x_i + 1] != zone_num: 
				for i in range(lw): 
					for o in range(lw): pix_arr[pR + i, pB + o] = line_col



	pix_arr.close()

	zone_map.set_alpha(200)



	return MAP, zone_map, zones_data, base_map



def parse_zone_data_file(file_name):

	zones_data = [[0xFF for j in range(64)] for i in range(64)]

	in_zone_block = False

	zone_num = 0



	ZONE_BYTE_DATA = []

	ZONE_TARGET_DATA = []

	with open(file_name, "r") as f:
		for LINE in f:
			line = LINE.rstrip()

			if line == "": 
				in_zone_block = False
				continue

			elif line == "#AREA":
				in_zone_block = True
				continue

			elif in_zone_block:

				z_spd = int(line[1:3], 16)
				z_tx = int(line[3:5], 16)
				z_ty = int(line[5:7], 16)

				z_cmd = int(line[33:35], 16)
				z_x = int(line[35:37], 16)
				z_y = int(line[37:39], 16)
				z_w = int(line[39:41], 16)
				z_h = int(line[41:43], 16)

				zone_data_bytes = [z_cmd, z_x, z_y, z_w]
				zone_target_bytes = [z_tx, z_ty, z_spd]

				if z_cmd == 0xFF: continue

				elif z_cmd == 0x00: # rectangle
					zone_data_bytes.append(z_h)
					for y_off in range(z_h):
						for x_off in range(z_w):
							zones_data[z_y + y_off][z_x + x_off] = zone_num

				elif z_cmd == 0x02: # up-left corner triangle
					z_h = z_w
					for y_off in range(z_h):
						for x_off in range(z_w):
							zones_data[z_y + y_off][z_x + x_off] = zone_num
						z_w -= 1

				elif z_cmd == 0x04: # up-right corner triangle
					z_h = z_w
					for y_off in range(z_h):
						for x_off in range(z_w):
							zones_data[z_y + y_off][z_x - x_off] = zone_num
						z_w -= 1

				elif z_cmd == 0x06: # down-right corner triangle
					z_h = z_w
					for y_off in range(z_h):
						for x_off in range(z_w):
							zones_data[z_y - y_off][z_x - x_off] = zone_num
						z_w -= 1

				elif z_cmd == 0x08: # down-left corner triangle
					z_h = z_w
					for y_off in range(z_h):
						for x_off in range(z_w):
							zones_data[z_y - y_off][z_x + x_off] = zone_num
						z_w -= 1


				ZONE_BYTE_DATA += zone_data_bytes
				ZONE_TARGET_DATA += zone_target_bytes

				zone_num += 1


	with open("zones.bin", 'wb') as f: f.write(bytes(ZONE_BYTE_DATA + [0xFF]))
	#with open("targets.bin", 'wb') as f: f.write(bytes(ZONE_TARGET_DATA + [0xFF]))
	with open("targets.bin", 'wb') as f: f.write(bytes(ZONE_TARGET_DATA))

	return zones_data



def ANGLE2ABCD(ANGLE):
	# ANGLE IN SHOULD BE WORD ANGLE
	ANGLE = (ANGLE & 0xFFFF) >> 8


	M_OFFS = 0x4000
	N_OFFS = 0xA000
	BLOCK_SIZE = 0x60 * 2

	ANGLE_1 = (ANGLE) & 0xFF
	ANGLE_2 = (ANGLE + 0x40) & 0xFF
	ANGLE_3 = (ANGLE - 0x40) & 0xFF

	if ANGLE_1 > 0x7F: ANGLE_1 ^= 0xFF
	if ANGLE_2 > 0x7F: ANGLE_2 ^= 0xFF
	if ANGLE_3 > 0x7F: ANGLE_3 ^= 0xFF


	M7A_addr = M_OFFS + (BLOCK_SIZE * ANGLE_1)   # M7A = M * cos(a)
	M7D_addr = N_OFFS + (BLOCK_SIZE * ANGLE_1)   # M7D = N * cos(a)
	M7C_addr = M_OFFS + (BLOCK_SIZE * ANGLE_3)   # M7C = M * sin(a)
	M7B_addr = N_OFFS + (BLOCK_SIZE * ANGLE_2)   # M7B = N * -sin(a)


	return (M7A_addr, M7B_addr, M7C_addr, M7D_addr)

class SNES_RENDER:


	def __init__(self, map_png="", oob_png=""):

		self.set_map_png(map_png)
		self.set_oob_png(oob_png)

		self.set_bgmode_HDMA()
		self.set_m7A_HDMA()
		self.set_m7B_HDMA()
		self.set_m7C_HDMA()
		self.set_m7D_HDMA()



		#self._BLANK_SURFACE = pygame.Surface((SNES_W, SNES_H), SRCALPHA)

		self.SCREEN_SURFACE = pygame.Surface((SNES_W, SNES_H), SRCALPHA)




	def set_map_png(self, map_png):

		if map_png == "": return

		self._map_png_file = map_png

		_map_png_surf = pygame.image.load(map_png).convert_alpha()

		self._map_png_px_arr = pygame.PixelArray(_map_png_surf)

		self._map_png = [[self._map_png_px_arr[x, y] for x in range(0x400)] for y in range(0x400)]

		self._map_png_px_arr.close()

		_map_png_surf = None


	def set_map_surf(self, map_surf):

		self._map_png_px_arr = pygame.PixelArray(map_surf)

		self._map_png = [[self._map_png_px_arr[x, y] for x in range(0x400)] for y in range(0x400)]

		self._map_png_px_arr.close()



	def set_oob_png(self, oob_png):

		if oob_png == "": return

		self._oob_png_file = oob_png

		_oob_png_surf = pygame.image.load(oob_png).convert_alpha()

		self._oob_png_px_arr = pygame.PixelArray(_oob_png_surf)

		self._oob_png = [[self._oob_png_px_arr[x, y] for x in range(0x8)] for y in range(0x8)]

		self._oob_png_px_arr.close()

		_oob_png_surf = None




	def _get_mode7_pixel_at(self, x, y):

		if x >= 0 and x < 0x400 and y >= 0 and y < 0x400:
			return self._map_png[y][x]

		x &= 7
		y &= 7
		return self._oob_png[y][x]



	def _parse_HDMA_table(self, HDMA_table_instructions=[]):

		if HDMA_table_instructions == []: return [0 for _ in range(SNES_H)]


		val_per_line = []

		for num_lines, data in HDMA_table_instructions:
			if type(data) == TYPE_NUM:
				val_per_line += [data for _ in range(num_lines)]
			else:
				val_per_line += data[:num_lines]

		if len(val_per_line) == 0: val_per_line = [0]

		if len(val_per_line) < SNES_H:
			val_per_line += [val_per_line[-1]]*(SNES_H - len(val_per_line))

		return val_per_line


	def set_bgmode_HDMA(self, bgmode_HDMA_table=[]):
		self._BG_MODE_HDMA = self._parse_HDMA_table(bgmode_HDMA_table)

	def set_m7A_HDMA(self, m7A_HDMA_table=[]):
		self._M7A_HDMA = self._parse_HDMA_table(m7A_HDMA_table)

	def set_m7B_HDMA(self, m7B_HDMA_table=[]):
		self._M7B_HDMA = self._parse_HDMA_table(m7B_HDMA_table)

	def set_m7C_HDMA(self, m7C_HDMA_table=[]):
		self._M7C_HDMA = self._parse_HDMA_table(m7C_HDMA_table)

	def set_m7D_HDMA(self, m7D_HDMA_table=[]):
		self._M7D_HDMA = self._parse_HDMA_table(m7D_HDMA_table)


	def set_BG_HV(self, H, V):
		if H > 0x0FFF: H -= 0x2000
		self._BG_H = H

		if V > 0x0FFF: V -= 0x2000
		self._BG_V = V


	def set_m7_XY(self, X, Y):
		if X > 0x0FFF: X -= 0x2000
		self._M7_X = X

		if Y > 0x0FFF: Y -= 0x2000
		self._M7_Y = Y


	def set_m7_ABCD(self, A, B, C, D):
		if A > 0x7FFF: A -= 0x10000
		self._M7_A = A

		if B > 0x7FFF: B -= 0x10000
		self._M7_B = B

		if C > 0x7FFF: C -= 0x10000
		self._M7_C = C

		if D > 0x7FFF: D -= 0x10000
		self._M7_D = D


	def set_BG_mode(self, BG_mode):
		self._BG_MODE = BG_mode



	def _get_mode7_coord(self, h, v):


		x_calc = ((self._M7_A * self._CLIP_DH) & ~63) + (self._M7_A * h) + ((self._M7_B * v) & ~63) + ((self._M7_B * self._CLIP_DV) & ~63) + (self._M7_X << 8)
		y_calc = ((self._M7_C * self._CLIP_DH) & ~63) + (self._M7_C * h) + ((self._M7_D * v) & ~63) + ((self._M7_D * self._CLIP_DV) & ~63) + (self._M7_Y << 8)


		return (x_calc >> 8, y_calc >> 8)







	def RENDER_SCREEN(self, IRQ_FUNCS=[]):

		#SCREEN_SURFACE = self._BLANK_SURFACE.copy()
		self.SCREEN_SURFACE.fill((0, 0, 0, 0))
		

		_SCREEN = pygame.PixelArray(self.SCREEN_SURFACE)

		#SAMPLE_PTS = []


		for v in range(SNES_H):

			self._VCNT = v

			self._BG_MODE = self._BG_MODE_HDMA[v]


			for irq_v, func, args in IRQ_FUNCS:
				if v == irq_v:
					func(*args)




			if self._BG_MODE == BGMODE7:
				self._CLIP_DH = CLIP(self._BG_H - self._M7_X)
				self._CLIP_DV = CLIP(self._BG_V - self._M7_Y)

				self.set_m7_ABCD(self._M7A_HDMA[v], self._M7B_HDMA[v], self._M7C_HDMA[v], self._M7D_HDMA[v])








			for h in range(SNES_W):
				self._HCNT = h

				if self._BG_MODE == BGMODE0:
					pass

				if self._BG_MODE == BGMODE1:
					pass

				elif self._BG_MODE == BGMODE7:
					x,y = self._get_mode7_coord(self._HCNT, self._VCNT+1)
					px = self._get_mode7_pixel_at(x, y)

					_SCREEN[self._HCNT, self._VCNT] = px

					#SAMPLE_PTS.append((self._HCNT, self._VCNT+1, x, y))






		_SCREEN.close()


		return self.SCREEN_SURFACE#, SAMPLE_PTS













MAP_IMAGE_FILE = ""



MODE_PLACE_CAM = 0
MODE_SEL_ZONE = 1


SHOW_ZONES_IN_CAM = True



if __name__ == "__main__":


	print("[INFO] INITIALIZING")

	pygame.init()

	S_W = EDIT_W + 20 + VIEW_W
	S_H = max(EDIT_H, VIEW_H)


	SCREEN = pygame.display.set_mode((S_W, S_H))

	BG = pygame.Surface((map_w, map_h), SRCALPHA)

	BALLOON_SPRITE = pygame.image.load("assets/balloon.png").convert_alpha()

	print("[INFO] CREATING MAP")

	MAP, ZONE_MAP, ZONES_DATA, BASE_MAP = create_map_img(MAP_NUM)

	SEL_ZONES = ZONE_MAP.copy()

	print("[INFO] LOADING NUMBER SPRITES")

	NUMBER_SPRITES = pygame.image.load("assets/numbers.png").convert_alpha()

	NUM_0_SPRITE = pygame.Surface((8,8), SRCALPHA)
	NUM_1_SPRITE = pygame.Surface((8,8), SRCALPHA)
	NUM_2_SPRITE = pygame.Surface((8,8), SRCALPHA)
	NUM_3_SPRITE = pygame.Surface((8,8), SRCALPHA)
	NUM_4_SPRITE = pygame.Surface((8,8), SRCALPHA)
	NUM_5_SPRITE = pygame.Surface((8,8), SRCALPHA)
	NUM_6_SPRITE = pygame.Surface((8,8), SRCALPHA)
	NUM_7_SPRITE = pygame.Surface((8,8), SRCALPHA)
	NUM_8_SPRITE = pygame.Surface((8,8), SRCALPHA)
	NUM_9_SPRITE = pygame.Surface((8,8), SRCALPHA)

	NUM_0_SPRITE.blit(NUMBER_SPRITES, (-0*8, -0*8))
	NUM_1_SPRITE.blit(NUMBER_SPRITES, (-1*8, -0*8))
	NUM_2_SPRITE.blit(NUMBER_SPRITES, (-2*8, -0*8))
	NUM_3_SPRITE.blit(NUMBER_SPRITES, (-3*8, -0*8))
	NUM_4_SPRITE.blit(NUMBER_SPRITES, (-4*8, -0*8))
	NUM_5_SPRITE.blit(NUMBER_SPRITES, (-0*8, -1*8))
	NUM_6_SPRITE.blit(NUMBER_SPRITES, (-1*8, -1*8))
	NUM_7_SPRITE.blit(NUMBER_SPRITES, (-2*8, -1*8))
	NUM_8_SPRITE.blit(NUMBER_SPRITES, (-3*8, -1*8))
	NUM_9_SPRITE.blit(NUMBER_SPRITES, (-4*8, -1*8))

	NUM_SPRITES.append(NUM_0_SPRITE)
	NUM_SPRITES.append(NUM_1_SPRITE)
	NUM_SPRITES.append(NUM_2_SPRITE)
	NUM_SPRITES.append(NUM_3_SPRITE)
	NUM_SPRITES.append(NUM_4_SPRITE)
	NUM_SPRITES.append(NUM_5_SPRITE)
	NUM_SPRITES.append(NUM_6_SPRITE)
	NUM_SPRITES.append(NUM_7_SPRITE)
	NUM_SPRITES.append(NUM_8_SPRITE)
	NUM_SPRITES.append(NUM_9_SPRITE)


	print("[INFO] READING CAMERA DATA")

	CD = CAM_DATA("cam_data.json")


	print("[INFO] CREATING EDITOR")

	EDITOR = Editor(EDIT_X, EDIT_Y, EDIT_W, EDIT_H)
	

	print("[INFO] CREATING HDMA DATA")

	M7_HDMA_DATA = []
	data = []
	with open("m7_hdma.bin", 'rb') as f:
		data = f.read()

	i = 0
	n = 0
	for b in data:
		if i == 0:
			n += b
			i = 1
		else:
			M7_HDMA_DATA.append(n + (b << 8))
			n = 0
			i = 0



	print("[INFO] CREATING RENDERER")

	RENDERER = SNES_RENDER(map_png=MAP_IMAGE_FILE, oob_png="oob_tile.png")
	#RENDERER = SNES_RENDER(map_png=MAP_IMAGE_FILE, oob_png="oob_grass.png")

	MAP_WITH_ZONES = BASE_MAP.copy()
	ZONE_MAP_M7 = ZONE_MAP.copy()
	ZONE_MAP_M7.set_alpha(150)
	MAP_WITH_ZONES.blit(ZONE_MAP_M7, (0, 0))

	if SHOW_ZONES_IN_CAM: RENDERER.set_map_surf(MAP_WITH_ZONES)
	else: RENDERER.set_map_surf(BASE_MAP)


	print("[INFO] READY")



	def GET_M7_HDMA_ABCD_TABLES_FROM_ANGLE(ANGLE, table_size=0x60, cutoff_point=None):
		if cutoff_point == None: cutoff_point = table_size

		a,b,c,d = ANGLE2ABCD(ANGLE)
		a = (a - 0x4000) // 2
		b = (b - 0x4000) // 2
		c = (c - 0x4000) // 2
		d = (d - 0x4000) // 2

		cutoff_point = max(1, cutoff_point)

		tbl_A = M7_HDMA_DATA[a:a+table_size][:cutoff_point]
		tbl_B = M7_HDMA_DATA[b:b+table_size][:cutoff_point]
		tbl_C = M7_HDMA_DATA[c:c+table_size][:cutoff_point]
		tbl_D = M7_HDMA_DATA[d:d+table_size][:cutoff_point]

		if len(tbl_A) < table_size: tbl_A += [tbl_A[-1]]*(table_size - len(tbl_A))
		if len(tbl_B) < table_size: tbl_B += [tbl_B[-1]]*(table_size - len(tbl_B))
		if len(tbl_C) < table_size: tbl_C += [tbl_C[-1]]*(table_size - len(tbl_C))
		if len(tbl_D) < table_size: tbl_D += [tbl_D[-1]]*(table_size - len(tbl_D))

		return (tbl_A, tbl_B, tbl_C, tbl_D)


	P1_M7_SIZE = 0x58
	P2_M7_SIZE = 0x58


	BGMODE_HDMA = [
		(0x18, BGMODE1),
		(P1_M7_SIZE, BGMODE7), # P1 BG Mode 7
		(0x18 + P2_M7_SIZE, BGMODE1),
		#(P2_M7_SIZE, BGMODE7), # P2 BG Mode 7
	]

	M7A_HDMA = [
		(0x18, 0),
		(P1_M7_SIZE, None), # P1 M7A
		(0x18 + P2_M7_SIZE, 0),
		#(P2_M7_SIZE, None), # P2 M7A
	]

	M7B_HDMA = [
		(0x18, 0),
		(P1_M7_SIZE, None), # P1 M7B
		(0x18 + P2_M7_SIZE, 0),
		#(P2_M7_SIZE, None), # P2 M7B
	]

	M7C_HDMA = [
		(0x18, 0),
		(P1_M7_SIZE, None), # P1 M7C
		(0x18 + P2_M7_SIZE, 0),
		#(P2_M7_SIZE, None), # P2 M7C
	]

	M7D_HDMA = [
		(0x18, 0),
		(P1_M7_SIZE, None), # P1 M7D
		(0x18 + P2_M7_SIZE, 0),
		#(P2_M7_SIZE, None), # P2 M7D
	]





	FRAME_CNT = 0
	P_MOUSE_LEFT_PRESSED = False
	P_MOUSE_RIGHT_PRESSED = False
	P_SCROLL_UP_PRESSED = False
	P_SCROLL_DOWN_PRESSED = False

	PAUSED = False

	clock = pygame.time.Clock()
	done = False

	cam_number = 0
	zone_number = 0
	EDIT_MODE = MODE_PLACE_CAM

	MAP_BUFF_BG = BG.copy()

	CAM_BUFF_BG = BG.copy()

	MAP_UPDATED = True
	CAMS_UPDATED = True

	while not done:
		clock.tick(15)

		SCROLL_UP = False
		SCROLL_DOWN = False



		for event in pygame.event.get():
			if event.type == QUIT: 
				done = True
				#PRINT_GATE_DATA(CURR_GATE_SET, MADE_NEW_SET)

			elif event.type == pygame.KEYDOWN:
				#parse keys pressed here
				if event.key in KEY_NAMES:
					k_button = KEY_NAMES[event.key]
					KEYS_RELEASED[k_button] = False
					PREV_FRAME_KEYS[k_button] = CURR_FRAME_KEYS[k_button]
					CURR_FRAME_KEYS[k_button] = True

					KEYS_NEW[k_button] = not PREV_FRAME_KEYS[k_button]

			elif event.type == pygame.KEYUP:
				#parse keys released here
				if event.key in KEY_NAMES:
					k_button = KEY_NAMES[event.key]
					KEYS_NEW[k_button] = False
					PREV_FRAME_KEYS[k_button] = CURR_FRAME_KEYS[k_button]
					CURR_FRAME_KEYS[k_button] = False

					KEYS_RELEASED[k_button] = PREV_FRAME_KEYS[k_button]

			elif event.type == pygame.MOUSEWHEEL:

				if event.y < 0:
					SCROLL_DOWN = True
				elif event.y > 0:
					SCROLL_UP = True

		for k_button in CURR_FRAME_KEYS:

			if CURR_FRAME_KEYS[k_button] == True:
				if PREV_FRAME_KEYS[k_button] == True:
					KEYS_NEW[k_button] = False
				elif PREV_FRAME_KEYS[k_button] == False:
					KEYS_NEW[k_button] = True

			elif CURR_FRAME_KEYS[k_button] == False:
				if PREV_FRAME_KEYS[k_button] == True:
					KEYS_RELEASED[k_button] = True
				elif PREV_FRAME_KEYS[k_button] == False:
					KEYS_RELEASED[k_button] = False

		for k_button in CURR_FRAME_KEYS:
			PREV_FRAME_KEYS[k_button] = CURR_FRAME_KEYS[k_button]

		MOUSE_LEFT_PRESSED = pygame.mouse.get_pressed()[0]
		MOUSE_LEFT_CLICKED =  MOUSE_LEFT_PRESSED and not P_MOUSE_LEFT_PRESSED
		MOUSE_LEFT_RELEASE = (not MOUSE_LEFT_PRESSED) and P_MOUSE_LEFT_PRESSED
		P_MOUSE_LEFT_PRESSED = MOUSE_LEFT_PRESSED

		MOUSE_RIGHT_PRESSED = pygame.mouse.get_pressed()[2]
		MOUSE_RIGHT_CLICKED =  MOUSE_RIGHT_PRESSED and not P_MOUSE_RIGHT_PRESSED
		MOUSE_RIGHT_RELEASE = (not MOUSE_RIGHT_PRESSED) and P_MOUSE_RIGHT_PRESSED
		P_MOUSE_RIGHT_PRESSED = MOUSE_RIGHT_PRESSED

		'''
		SCROLL_UP_PRESSED = pygame.mouse.get_pressed()[3]
		SCROLL_UP = SCROLL_UP_PRESSED and not P_SCROLL_UP_PRESSED
		P_SCROLL_UP_PRESSED = SCROLL_UP_PRESSED

		SCROLL_DOWN_PRESSED = pygame.mouse.get_pressed()[4]
		SCROLL_DOWN = SCROLL_DOWN_PRESSED and not P_SCROLL_DOWN_PRESSED
		P_SCROLL_DOWN_PRESSED = SCROLL_DOWN_PRESSED
		'''


		#last_cam = CD._CAMERAS[MAP_NUM]["cams"][cam_number]





		
		mx, my = EDITOR.get_map_mouse_pos()




		#BG.blit(MAP, (0, 0))

		

		#CAM_BUFF_BG.fill((0, 0, 0, 0))


		if EDIT_MODE == MODE_PLACE_CAM:
			#BG.blit(ZONE_MAP, (-map_offset_w, -map_offset_h))
			
			if MOUSE_LEFT_CLICKED:
				if EDITOR.get_held_cam() == None:
					for c in range(len(CD._CAMERAS[MAP_NUM]["cams"])):
						cam = CD._CAMERAS[MAP_NUM]["cams"][c]
						dx = mx - cam.x
						dy = my - cam.y
						if -0x18 < dx < 0x18 and -0x18 < dy < 0x18:
							EDITOR.set_held_cam(c)
							cam_number = c
							break
				else:
					#
					EDITOR.drop_cam()

				CAMS_UPDATED = True


			if MOUSE_RIGHT_CLICKED:
				if EDITOR.get_held_cam() != None:
					cnum = EDITOR.get_held_cam()
					del CD._CAMERAS[MAP_NUM]["cams"][cnum]
					CD._CAMERAS[MAP_NUM]["size"] -= 1
					EDITOR.drop_cam()
					cam_number = cnum - 1

					if cnum == 0:
						new_cam = CAM()
						new_cam.x = 0x200
						new_cam.y = 0x200
						#new_cam.z = 0
						new_cam.a = 0

						CD._CAMERAS[MAP_NUM]["cams"].append(new_cam)
						CD._CAMERAS[MAP_NUM]["size"] += 1

						cam_number = 0

					for z_idx in range(len(CD._ZONES[MAP_NUM]['zones'])):
						if CD._ZONES[MAP_NUM]['zones'][z_idx] > cam_number:
							CD._ZONES[MAP_NUM]['zones'][z_idx] -= 1

					CAMS_UPDATED = True

				else:
					new_cam = CAM()
					new_cam.x = -1000
					new_cam.y = -1000
					#new_cam.z = 0
					new_cam.a = 0

					EDITOR.set_held_cam(CD._CAMERAS[MAP_NUM]["size"])

					CD._CAMERAS[MAP_NUM]["cams"].append(new_cam)
					CD._CAMERAS[MAP_NUM]["size"] += 1

					cam_number = EDITOR.get_held_cam()

					CAMS_UPDATED = True



			for c in range(len(CD._CAMERAS[MAP_NUM]["cams"])):
				CD._CAMERAS[MAP_NUM]["cams"][c].transparent = False



			HELD_CAM = EDITOR.get_held_cam()

			if HELD_CAM != None:
				CD._CAMERAS[MAP_NUM]["cams"][HELD_CAM].transparent = True
				cx = mx & 0xFFFC
				if cx > 0x7FFF: cx -= 0x10000
				CD._CAMERAS[MAP_NUM]["cams"][HELD_CAM].x = cx
				cy = my & 0xFFFC
				if cy > 0x7FFF: cy -= 0x10000
				CD._CAMERAS[MAP_NUM]["cams"][HELD_CAM].y = cy
				CAMS_UPDATED = True



			if KEYS_NEW["q"] == True or SCROLL_DOWN:
				if HELD_CAM != None:
					CD._CAMERAS[MAP_NUM]["cams"][HELD_CAM].a = (CD._CAMERAS[MAP_NUM]["cams"][HELD_CAM].a + 0x0400) & 0xFFFF
					CAMS_UPDATED = True

			elif KEYS_NEW["e"] == True or SCROLL_UP:
				if HELD_CAM != None:
					CD._CAMERAS[MAP_NUM]["cams"][HELD_CAM].a = (CD._CAMERAS[MAP_NUM]["cams"][HELD_CAM].a - 0x0400) & 0xFFFF
					CAMS_UPDATED = True
	




			if KEYS_NEW["right"] == True:
				CAMS_UPDATED = True
				if HELD_CAM == None:
					cam_number = cam_number + 1
					if cam_number >= CD._CAMERAS[MAP_NUM]["size"]:
						cam_number = 0
				else:
					if CURR_FRAME_KEYS['up'] == True: a = 0x2000
					elif CURR_FRAME_KEYS['down'] == True: a = 0x6000
					else: a = 0x4000
					CD._CAMERAS[MAP_NUM]["cams"][HELD_CAM].a = a


			elif KEYS_NEW["left"] == True:
				CAMS_UPDATED = True
				if HELD_CAM == None:
					cam_number = cam_number - 1
					if cam_number < 0:
						cam_number = CD._CAMERAS[MAP_NUM]["size"] - 1
				else:
					if CURR_FRAME_KEYS['up'] == True: a = 0xE000
					elif CURR_FRAME_KEYS['down'] == True: a = 0xA000
					else: a = 0xC000
					CD._CAMERAS[MAP_NUM]["cams"][HELD_CAM].a = a

			elif KEYS_NEW["up"] == True:
				if HELD_CAM != None:
					if CURR_FRAME_KEYS['left'] == True: a = 0xE000
					elif CURR_FRAME_KEYS['right'] == True: a = 0x2000
					else: a = 0x0000
					CD._CAMERAS[MAP_NUM]["cams"][HELD_CAM].a = a
					CAMS_UPDATED = True

			elif KEYS_NEW["down"] == True:
				if HELD_CAM != None:
					if CURR_FRAME_KEYS['left'] == True: a = 0xA000
					elif CURR_FRAME_KEYS['right'] == True: a = 0x6000
					else: a = 0x8000
					CD._CAMERAS[MAP_NUM]["cams"][HELD_CAM].a = a
					CAMS_UPDATED = True



		elif EDIT_MODE == MODE_SEL_ZONE:

			#BG.blit(ZONE_MAP, (-map_offset_w, -map_offset_h))




			if mx < 0 or my < 0 or mx > 0x3FF or my > 0x3FF: zone_sel = 0xFF
			else: zone_sel = ZONES_DATA[my >> 4][mx >> 4]



			#CD._ZONES[tnum][]

			'''
			if MOUSE_RIGHT_CLICKED:

				
				cam_selected = False
				for c in range(len(CD._CAMERAS[MAP_NUM]["cams"])):
					cam = CD._CAMERAS[MAP_NUM]["cams"][c]
					dx = mx - cam.x
					dy = my - cam.y
					if -0x18 < dx < 0x18 and -0x18 < dy < 0x18:
						#EDITOR.set_held_cam(c)
						cam_number = c
						cam_selected = True
						break
			'''

			if MOUSE_LEFT_CLICKED:

				cam_selected = False
				for c in range(len(CD._CAMERAS[MAP_NUM]["cams"])):
					cam = CD._CAMERAS[MAP_NUM]["cams"][c]
					dx = mx - cam.x
					dy = my - cam.y
					if -0x18 < dx < 0x18 and -0x18 < dy < 0x18:
						#EDITOR.set_held_cam(c)
						cam_number = c
						cam_selected = True
						CAMS_UPDATED = True
						MAP_UPDATED = True
						break


				if cam_selected == False:
					#print(zone_sel)
					if zone_sel != 0xFF:
						#print(CD._ZONES[MAP_NUM])
						cam_number = CD._ZONES[MAP_NUM]['zones'][zone_sel]
						EDITOR.set_selected_zone(zone_sel)
						CAMS_UPDATED = True
						MAP_UPDATED = True
					else:
						EDITOR.set_selected_zone(None)


			elif MOUSE_RIGHT_CLICKED:

				if zone_sel != 0xFF:
					#cam_number = CD._ZONES[tnum][zone_sel]
					EDITOR.set_selected_zone(zone_sel)
				else:
					EDITOR.set_selected_zone(None)

				zone_sel = EDITOR.get_selected_zone()

				if zone_sel != None:
					CD._ZONES[MAP_NUM]['zones'][zone_sel] = cam_number
					print('[INFO] Set Zone ' + format(zone_sel, "02X") + ' to CAM ' + format(cam_number, "02d"))
					MAP_UPDATED = True
					CAMS_UPDATED = True








			if KEYS_NEW["right"] == True:
				cam_number = cam_number + 1
				if cam_number >= CD._CAMERAS[MAP_NUM]["size"]:
					cam_number = 0
				CAMS_UPDATED = True

			elif KEYS_NEW["left"] == True:
				cam_number = cam_number - 1
				if cam_number < 0:
					cam_number = CD._CAMERAS[MAP_NUM]["size"] - 1
				CAMS_UPDATED = True



		#if CAMS_UPDATED or MAP_UPDATED:
		#	SCREEN.fill((128, 128, 128, 255))
			
		

		if CAMS_UPDATED:

			CAM_BUFF_BG.fill((0, 0, 0, 0))
			c_num = 0
			for c in CD._CAMERAS[MAP_NUM]["cams"]:
				s = False
				if c_num == cam_number: s = True
				c.display_on(CAM_BUFF_BG, cam_number=c_num, show_balloon=s, show_lines=True)
				c_num += 1

			last_cam = CD._CAMERAS[MAP_NUM]["cams"][cam_number]

			_P1_X = last_cam.x
			_P1_Y = last_cam.y - 1
			_P1_A_as = last_cam.a & 0xFF00

			_P1_H = _P1_X - 0x7F - 1 #???
			_P1_V = _P1_Y - _P1_V_of + 1

			#print(format(_P1_X, "04X"))
			#print(format(_P1_Y, "04X"))
			#print(format(_P1_H, "04X"))
			#print(format(_P1_V, "04X"))


			P1_M7_A,P1_M7_B,P1_M7_C,P1_M7_D = GET_M7_HDMA_ABCD_TABLES_FROM_ANGLE(_P1_A_as, cutoff_point=None)

			M7A_HDMA[1] = (P1_M7_SIZE, P1_M7_A)
			#M7A_HDMA[3] = (P2_M7_SIZE, P2_M7_A)

			M7B_HDMA[1] = (P1_M7_SIZE, P1_M7_B)
			#M7B_HDMA[3] = (P2_M7_SIZE, P2_M7_B)

			M7C_HDMA[1] = (P1_M7_SIZE, P1_M7_C)
			#M7C_HDMA[3] = (P2_M7_SIZE, P2_M7_C)

			M7D_HDMA[1] = (P1_M7_SIZE, P1_M7_D)
			#M7D_HDMA[3] = (P2_M7_SIZE, P2_M7_D)

			RENDERER.set_m7A_HDMA(M7A_HDMA)
			RENDERER.set_m7B_HDMA(M7B_HDMA)
			RENDERER.set_m7C_HDMA(M7C_HDMA)
			RENDERER.set_m7D_HDMA(M7D_HDMA)

			RENDERER.set_bgmode_HDMA(BGMODE_HDMA)


			IRQ_FUNCS = [
				(0x00, RENDERER.set_m7_XY, (_P1_X, _P1_Y)),
				(0x00, RENDERER.set_BG_HV, (_P1_H, _P1_V)),
				#(0x70, RENDERER.set_m7_XY, (_P2_X, _P2_Y)),
				#(0x70, RENDERER.set_BG_HV, (_P2_H, _P2_V)),
			]


			OUT_SCREEN = RENDERER.RENDER_SCREEN(IRQ_FUNCS=IRQ_FUNCS)

			CAM_BG = pygame.transform.scale(CAM_BUFF_BG, (EDIT_W, EDIT_H))

			# Place Camera Number over Camera view
			num_A = cam_number // 10
			num_B = cam_number % 10
			OUT_SCREEN.blit(pygame.transform.scale(NUM_SPRITES[num_A].copy(), (16, 16)), (0, 6))
			OUT_SCREEN.blit(pygame.transform.scale(NUM_SPRITES[num_B].copy(), (16, 16)), (16, 6))

			CAM_PREVIEW = pygame.transform.scale(OUT_SCREEN, (SNES_W*2, SNES_H*2))

			CAMS_UPDATED = False

		if MAP_UPDATED:
			MAP_BUFF_BG.blit(MAP, (0, 0))
			MAP_BUFF_BG.blit(ZONE_MAP, (-map_offset_w, -map_offset_h))
			if EDIT_MODE == MODE_SEL_ZONE:
				SEL_ZONES = ZONE_MAP.copy()
				pix_arr = pygame.PixelArray(SEL_ZONES)
				for py in range(SEL_ZONES.get_height()):
					for px in range(SEL_ZONES.get_width()):
						px_zone = ZONES_DATA[py >> 4][px >> 4]
						if px_zone == 0xFF or CD._ZONES[MAP_NUM]['zones'][px_zone] != cam_number:
							pix_arr[px, py] = (0, 0, 0, 0)
				pix_arr.close()
				SEL_ZONES.set_alpha(240)
				MAP_BUFF_BG.blit(SEL_ZONES, (-map_offset_w, -map_offset_h))

			MAP_BG = pygame.transform.scale(MAP_BUFF_BG, (EDIT_W, EDIT_H))

			MAP_UPDATED = False
		


		SCREEN.fill((128, 128, 128, 255))


		#if S_W < 1024:
		#	SCREEN.blit(pygame.transform.smoothscale(BG, (EDIT_W, EDIT_H)), (EDIT_X, EDIT_Y))
		#else:
		#	SCREEN.blit(pygame.transform.scale(BG, (EDIT_W, EDIT_H)), (EDIT_X, EDIT_Y))

		SCREEN.blit(MAP_BG, (EDIT_X, EDIT_Y))
		SCREEN.blit(CAM_BG, (EDIT_X, EDIT_Y))
		#SCREEN.blit(pygame.transform.scale(BG, (EDIT_W, EDIT_H)), (EDIT_X, EDIT_Y))



		

		SCREEN.blit(CAM_PREVIEW, (VIEW_X + 10, VIEW_Y + 30))








		if KEYS_NEW["m"] == True:
			print(format(mx, "04X") + "h, " + format(my, "04X") + "h")

		

		if KEYS_NEW["s"] == True:
			CD.save_cameras()
		'''
		elif KEYS_NEW["l"] == True:

			MAP, ZONE_MAP, ZONES_DATA = create_map_img(MAP_NUM)

			RENDERER = SNES_RENDER(map_png=MAP_IMAGE_FILE, oob_png="oob_grass.png")

			cam_number = 0
		'''


		if KEYS_NEW["p"] == True:
			CD.print_cameras(track_num=MAP_NUM)

		if KEYS_NEW["c"] == True:
			EDIT_MODE = EDIT_MODE + 1
			if EDIT_MODE == 2: EDIT_MODE = 0

			EDITOR.drop_cam()
			EDITOR.unselect_zone()
			MAP_UPDATED = True
			CAMS_UPDATED = True

		if KEYS_NEW["z"] == True:

			SHOW_ZONES_IN_CAM = not SHOW_ZONES_IN_CAM

			if SHOW_ZONES_IN_CAM: RENDERER.set_map_surf(MAP_WITH_ZONES)
			else: RENDERER.set_map_surf(BASE_MAP)

			CAMS_UPDATED = True


		pygame.display.update()

		FRAME_CNT += 1