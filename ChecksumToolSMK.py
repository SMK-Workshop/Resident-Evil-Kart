


####### Checksum calculator for Super Mario Kart #######

import sys


DEBUG_ON = False




HEADER_BASE_OFFSET = 0xC0

HEADER_TITLE_OFFSET      = 0xC0 - HEADER_BASE_OFFSET
HEADER_MAP_MODE_OFFSET   = 0xD5 - HEADER_BASE_OFFSET
HEADER_ROM_TYPE_OFFSET   = 0xD6 - HEADER_BASE_OFFSET
HEADER_ROM_SIZE_OFFSET   = 0xD7 - HEADER_BASE_OFFSET
HEADER_SRAM_SIZE_OFFSET  = 0xD8 - HEADER_BASE_OFFSET
HEADER_DEV_ID_OFFSET     = 0xD9 - HEADER_BASE_OFFSET
HEADER_VERS_NUM_OFFSET   = 0xDB - HEADER_BASE_OFFSET
HEADER_CHKSUM_CMP_OFFSET = 0xDC - HEADER_BASE_OFFSET
HEADER_CHKSUM_OFFSET     = 0xDE - HEADER_BASE_OFFSET

HEADER_NATIVE_COP_OFFSET   = 0xE4 - HEADER_BASE_OFFSET
HEADER_NATIVE_BRK_OFFSET   = 0xE6 - HEADER_BASE_OFFSET
HEADER_NATIVE_ABORT_OFFSET = 0xE8 - HEADER_BASE_OFFSET
HEADER_NATIVE_NMI_OFFSET   = 0xEA - HEADER_BASE_OFFSET
HEADER_NATIVE_IRQ_OFFSET   = 0xEE - HEADER_BASE_OFFSET

HEADER_EMULAT_COP_OFFSET   = 0xF4 - HEADER_BASE_OFFSET
HEADER_EMULAT_ABORT_OFFSET = 0xF8 - HEADER_BASE_OFFSET
HEADER_EMULAT_NMI_OFFSET   = 0xFA - HEADER_BASE_OFFSET
HEADER_EMULAT_RES_OFFSET   = 0xFC - HEADER_BASE_OFFSET
HEADER_EMULAT_IRQ_OFFSET   = 0xFE - HEADER_BASE_OFFSET
HEADER_EMULAT_BRK_OFFSET   = 0xFE - HEADER_BASE_OFFSET


def print_debug(*args, **kwargs):
	if DEBUG_ON: print('[DEBUG]', *args, **kwargs)

def print_info(*args, **kwargs):
	print('[INFO]', *args, **kwargs)

def print_warning(*args, **kwargs):
	print('[ERROR]', *args, **kwargs)

def raise_error(*args, **kwargs):
	print('[ERROR]', *args, **kwargs)
	raise ZeroDivisionError("")




# class for holding and checking data of ROM
class SNES_ROM:

	def __init__(self, filename):

		self.filename = str(filename)				# filename
		self._ROM_data = bytearray()				# ROM data
		self._ROM_data_size = -1					# size of ROM
		self._file = None							# file object

		self._data_ready = False			# has the file been read successfully
		self._header_offset = 0x00FFC0		# offset of header in ROM (unless remapped, this should be 0x00FFC0)

		self._read_file()	# read ROM file and store data


	# get if data is ready
	def data_is_ready(self):
		return self._data_ready

	# check if data is ready, raise error otherwise
	def check_data_ready(self):
		if not self.data_is_ready(): raise_error('ROM data not yet read.')


	# get actual size of ROM
	def get_ROM_byte_size(self):
		if self._ROM_data_size == -1: self._ROM_data_size = len(self._ROM_data)
		return self._ROM_data_size


	# read ROM file
	def _read_file(self):

		# try to open file
		bad_read = False
		try: 
			self._file = open(self.filename, 'rb')
		except FileNotFoundError:
			bad_read = True

		if bad_read: raise_error("File " + self.filename + " not found.")


		# get ROM data and size
		self._ROM_data = bytearray(self._file.read())
		self._ROM_data_size = len(self._ROM_data)

		# done with file for now
		self._file.close()

		# pad ROM to 1MB (for now. maybe 4 MB later?)
		MAX_ROM_SIZE = 0x100000	#0x400000
		print_info("Padding ROM to " + format(MAX_ROM_SIZE, '06x') + 'h bytes.')
		if self._ROM_data_size < MAX_ROM_SIZE:
			self._ROM_data += bytearray(MAX_ROM_SIZE - self._ROM_data_size)
			self._ROM_data_size = MAX_ROM_SIZE

		# set that file has been read successfully
		self._data_ready = True


	def get_header_data(self, start_offset, num_bytes=None):
		self.check_data_ready()	# check if data ready

		if num_bytes != None:
			end_offset = start_offset + num_bytes

		_s_offs = start_offset
		_e_offs = end_offset

		# if start offset < -40h or >= 40h, outside of bounds of header
		if start_offset < -0x40: raise_error('Start offset ' + str(end_offset) + ' is out of bounds of header.')
		if start_offset >= 0x40: raise_error('Start offset ' + str(end_offset) + ' is out of bounds of header.')
		# if start offset < 0, negative index so shift to positive index
		if start_offset < 0: start_offset += 0x40


		# if no number of bytes specified, return single byte
		if num_bytes == None:
			return self._ROM_data[self._header_offset + start_offset]


		
		# if end offset < -40h or >= 40h, outside of bounds of header
		if end_offset < -0x40: raise_error('Ending offset ' + str(end_offset) + ' is out of bounds of header.')
		if end_offset >= 0x40: raise_error('Ending offset ' + str(end_offset) + ' is out of bounds of header.')
		# if end offset < 0, negative index so shift to positive index
		if end_offset < 0: end_offset += 0x40


		# check that the offsets are properly ordered
		if end_offset < start_offset: 
			raise_error('Ending offset ' + str(_e_offs) + " (" + str(end_offset) + ") lower than start offset " + str(_s_offs) + " (" + str(start_offset) + ").")

		return self._ROM_data[self._header_offset + start_offset : self._header_offset + end_offset]


	# get ROM name
	def get_ROM_name(self):
		return self.get_header_data(HEADER_TITLE_OFFSET, 0x15).decode('ascii')


	# get checksum and checksum complement
	def get_ROM_checksum(self):
		cs = self.get_header_data(HEADER_CHKSUM_OFFSET, 0x2)
		return cs[0] + (cs[1] << 8)

	def get_ROM_checksum_complement(self):
		cs = self.get_header_data(HEADER_CHKSUM_CMP_OFFSET, 0x2)
		return cs[0] + (cs[1] << 8)





	# print diagnostics of ROM for debugging
	def print_diagnostics(self):
		self.check_data_ready()	# check if data ready

		print_debug('Actual ROM size: ' + format(self.get_ROM_byte_size(), "06x") + 'h bytes')
		print_debug('Header Data:')
		print_debug('\tROM Name: ' + self.get_ROM_name())
		print_debug('\tChecksum: ' + format(self.get_ROM_checksum(), "04x").upper())
		print_debug('\tComplement: ' + format(self.get_ROM_checksum_complement(), "04x").upper())

		# other diagnostics


	# calculate checksum
	def calc_checksum(self):
		self.check_data_ready()	# check if data ready


		CS_CMP_ADDR_0 = self._header_offset + HEADER_CHKSUM_CMP_OFFSET + 0
		CS_CMP_ADDR_1 = self._header_offset + HEADER_CHKSUM_CMP_OFFSET + 1
		CS_ADDR_0     = self._header_offset + HEADER_CHKSUM_OFFSET + 0
		CS_ADDR_1     = self._header_offset + HEADER_CHKSUM_OFFSET + 1

		pseudo_rom_data = bytearray([])

		po2_size = 2**(len(bin(self._ROM_data_size)[2:]) - 1)	# this is stupid but it works lmao

		po2_rom_data = self._ROM_data[:po2_size]
		chunk_size = self.get_ROM_byte_size() - po2_size

		extra_rom_size = 0
		extra_rom_data = []

		if chunk_size != 0:
			non_po2_chunk = self._ROM_data[po2_size:]
			while extra_rom_size < po2_size:
				extra_rom_data += non_po2_chunk
				extra_rom_size += chunk_size
			extra_rom_data = extra_rom_data[:po2_size]




		addr = 0
		s = 0
		for val in po2_rom_data:
			if addr == CS_CMP_ADDR_0 or addr == CS_CMP_ADDR_1:
				s += 0xFF
			elif addr == CS_ADDR_0 or addr == CS_ADDR_1:
				s += 0x00
			else:
				s += val
			s &= 0xFFFF
			addr += 1

		t = 0
		for val in extra_rom_data:
			if addr == CS_CMP_ADDR_0 or addr == CS_CMP_ADDR_1:
				t += 0xFF
			elif addr == CS_ADDR_0 or addr == CS_ADDR_1:
				t += 0x00
			else:
				t += val
			t &= 0xFFFF
			addr += 1

		return (s + t) & 0xFFFF

	# write checksum to ROM data
	def write_checksum(self, checksum):
		checksum_complement = 0xFFFF - checksum

		self._ROM_data[self._header_offset + HEADER_CHKSUM_CMP_OFFSET + 0] = checksum_complement & 0xFF
		self._ROM_data[self._header_offset + HEADER_CHKSUM_CMP_OFFSET + 1] = (checksum_complement >> 8) & 0xFF
		self._ROM_data[self._header_offset + HEADER_CHKSUM_OFFSET + 0] = checksum & 0xFF
		self._ROM_data[self._header_offset + HEADER_CHKSUM_OFFSET + 1] = (checksum >> 8) & 0xFF



	# write changes to file
	def write_changes(self):
		self.check_data_ready()	# check if data ready



		# try to open file
		bad_read = False
		try: 
			self._file = open(self.filename, 'wb')
		except FileNotFoundError:
			bad_read = True

		if bad_read: raise_error("File " + self.filename + " not found.")


		# write data to file
		self._file.write(self._ROM_data)

		# done with file
		self._file.close()








def Calculate_Checksum(sys_args):
	try:
		Calculate_Checksum_sub(sys_args)
	except ZeroDivisionError:
		pass

def Calculate_Checksum_sub(sys_args):

	# check that filename is supplied
	if len(sys_args) < 2: raise_error("No file specified to calculate checksum.")

	# get filename
	filename = str(sys_args[1])

	# open file and set up
	ROM = SNES_ROM(filename)

	

	# print before starting calculation
	print_info("Calculating checksum for " + filename)

	# print some diagnostics for debugging
	if DEBUG_ON: ROM.print_diagnostics()

	# calculate checksum
	checksum = ROM.calc_checksum()

	
	print_info('Checksum   : ' + format(checksum, "04x").upper())
	print_info('Complement : ' + format(0xFFFF - checksum, "04x").upper())

	# write checksum to rom data
	ROM.write_checksum(checksum)


	# write changes to file
	ROM.write_changes()

	print_info('Successfully wrote checksum to ' + filename)





	














if __name__ == "__main__":



	Calculate_Checksum(sys.argv)

	#Calculate_Checksum(["", "Super Mario Kart (U).sfc"])

