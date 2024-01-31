

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




def clean_word(w, signed=True):

	v = int(w.replace("$", ""), 16) #& 0xFFFF

	if signed and v > 0x8000: v -= 0x10000

	return v




def parse_file(file_name):

	lines = []

	TRACK_DATA = {}
	for i in range(len(MAP_NAMES)):
		TRACK_DATA[str(i)] = {
			"track_name": MAP_NAMES[i],
			"zones": [],
			"cameras": []
		}


	with open(file_name, "r") as f:
		for LINE in f:
			line = LINE.split(";")[0].lstrip().rstrip()

			if line == "": continue

			lines.append(line)


	curr_track_num = -1
	in_zone_block = False
	in_camera_block = False


	for line in lines:

		if line[:4] == "zone":
			in_zone_block = True
			in_camera_block = False
			curr_track_num = int(line[5:7], 16)

			#print("[ZONE_" + format(curr_track_num, "02X") + "]")

		elif line[:6] == "camera":
			in_camera_block = True
			in_zone_block = False
			curr_track_num = int(line[7:9], 16)

			#print("[CAMERA_" + format(curr_track_num, "02X") + "]")

		else:

			if in_zone_block:
				#print("\t" + line)
				zones = line[3:].split(",")

				zone_nums = []

				for z_raw in zones:
					z = z_raw.replace("cam($", "").replace(")", "")
					TRACK_DATA[str(curr_track_num)]["zones"].append(int(z, 16))
					zone_nums.append(int(z, 16))

				#print(zone_nums)

				

			elif in_camera_block:
				#print("\t" + line)

				cam_data = (line.replace("%CAMERA(", "").replace(")", "")).split(",")

				cam_vals = [
					clean_word(cam_data[0], signed=True),
					clean_word(cam_data[1], signed=True),
					clean_word(cam_data[2], signed=False),
				]

				#print([format(c, "04X") for c in cam_vals])
				#print(cam_vals)

				TRACK_DATA[str(curr_track_num)]["cameras"].append(cam_vals)


			else:
				continue


	return TRACK_DATA

			









if __name__ == "__main__":


	DATA_ASM_FILE = "../code/zones.asm"


	TRACK_DATA = parse_file(DATA_ASM_FILE)
	
	WRITE_JSON("cam_data.json", TRACK_DATA)



