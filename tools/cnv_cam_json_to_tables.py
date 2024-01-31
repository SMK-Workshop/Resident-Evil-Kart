



import json




def READ_JSON(json_file):

	with open(json_file) as jf:
		data = json.load(jf)

	return data


def WRITE_JSON(json_file, data):
	with open(json_file, 'w') as f:
		f.write(json.dumps(data, indent=1))






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



def track_data_to_str(track_num, zone_data, cam_data):

	OUT_LINES = []

	OUT_LINES.append("; ==============================================")
	OUT_LINES.append("; Track " + format(track_num, "02X") + ": " + MAP_NAMES[track_num])
	OUT_LINES.append("; ==============================================")
	OUT_LINES.append("zone_" + format(track_num, "02X") + ":\t\t; (" + str(len(zone_data)) + " zones)")

	line_idx = 0
	curr_line = ""
	for zone in zone_data:

		if line_idx == 0:
			curr_line = "\t\tdb\t"
		else:
			curr_line += ","

		curr_line += "cam($" + format(zone, "02X") + ")"

		line_idx += 1

		if line_idx == 4:
			line_idx = 0
			OUT_LINES.append(curr_line)

	if line_idx != 0:
		OUT_LINES.append(curr_line)

	OUT_LINES.append("")

	OUT_LINES.append("camera_" + format(track_num, "02X") + ":")
	OUT_LINES.append("\t\t;       xpos  ypos  angle")

	for cam in cam_data:
		x_pos = cam[0]
		y_pos = cam[1]
		angle = cam[2]

		OUT_LINES.append("\t\t%CAMERA(" + frmt_word_asar(x_pos) + "," + frmt_word_asar(y_pos) + "," + frmt_word_asar(angle) + ")")

	OUT_LINES.append("\t\t; ...")
	OUT_LINES.append("")
	OUT_LINES.append("; ==============================================")

	return "\n".join(OUT_LINES)








raw_start = """















macro CAMERA(xpos,ypos,angle)
		; Specify position and angle of camera
		dw	<xpos>*4,<ypos>*4,<angle>
endmacro

; Specify which camera to use for this zone
function cam(camera_idx) = camera_idx*6



; track order
;
; 00-04 | MC3 GV2 DP2 BC2 VL2
; 05-09 | RR  KB2 MC1 GV3 BC3
; 0A-0E | CI2 DP3 VL1 KB1 MC4
; 0F-13 | MC2 GV1 BC1 CI1 DP1
;
; 14-17 | BT3 BT4 BT1 BT2






TRACK_ZONES:
		; race tracks
		dw	zone_00,zone_01,zone_02,zone_03,zone_04
		dw	zone_05,zone_06,zone_07,zone_08,zone_09
		dw	zone_0A,zone_0B,zone_0C,zone_0D,zone_0E
		dw	zone_0F,zone_10,zone_11,zone_12,zone_13
		; battle tracks
		dw	zone_15,zone_15,zone_16,zone_15

TRACK_CAMERAS:
		; race tracks
		dw	camera_00,camera_01,camera_02,camera_03,camera_04
		dw	camera_05,camera_06,camera_07,camera_08,camera_09
		dw	camera_0A,camera_0B,camera_0C,camera_0D,camera_0E
		dw	camera_0F,camera_10,camera_11,camera_12,camera_13
		; battle tracks
		dw	camera_15,camera_15,camera_16,camera_15


"""




if __name__ == "__main__":

	JSON_FILE = "cam_data.json"

	'''
	TRACKS = {}

	for tnum in range(0x18):

		zones = [0 for _ in range(NUM_ZONES[tnum])]
		cams = [
			(0x0000, 0x0000, 0x6000),
			(0x0200, 0x0200, 0x2000)
		]

		track = {
			"track_name": MAP_NAMES[tnum],
			"zones": zones,
			"cameras": cams
		}

		TRACKS[str(tnum)] = track

	WRITE_JSON(JSON_FILE, TRACKS)
	'''

	TRACKS = READ_JSON(JSON_FILE)

	LINES = raw_start.split("\n")

	for tnum in range(0x18):

		if tnum == 0x00:
			LINES.append("; =============================================================================")
			LINES.append(";\t\tRACE TRACKS")
			LINES.append("; =============================================================================")
			LINES.append("")

		elif tnum == 0x14:
			LINES.append("")
			LINES.append("; =============================================================================")
			LINES.append("")
			LINES.append("")
			LINES.append("")
			LINES.append("")
			LINES.append("")
			LINES.append("")
			LINES.append("")
			LINES.append("")
			LINES.append("")
			LINES.append("")
			LINES.append("")
			LINES.append("; =============================================================================")
			LINES.append(";\t\tBATTLE TRACKS")
			LINES.append("; =============================================================================")
			LINES.append("")
			LINES.append("; figure out what exactly to do with these :P")
			LINES.append("")

		else:
			LINES.append("")
			LINES.append("")
			LINES.append("")
			LINES.append("")
			LINES.append("")

		track_data = TRACKS[str(tnum)]

		LINES.append(track_data_to_str(tnum, track_data["zones"], track_data["cameras"]))

	LINES.append("; ==============================================")


	#print("\n".join(LINES))

	with open("../code/zones.asm", 'w') as f:
		f.write("\n".join(LINES))
		