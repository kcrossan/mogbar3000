import cmus_bind
from cmus_bind import *
import ctypes
from ctypes import *

import playback
from playback import PLAYBACK_STATUS

class Cmus(object):
	STATUS_MAPPING = { PLAYER_STATUS_STOPPED: PLAYBACK_STATUS.STOP,
		PLAYER_STATUS_PLAYING: PLAYBACK_STATUS.PLAY,
		PLAYER_STATUS_PAUSED: PLAYBACK_STATUS.PAUSE }
	
	def __init__(self, next_cb):
		'''Creates a new output module that uses libcmus.
		next_cb: a function that when called returns the next track to play.'''
		
		#instance vars
		self.__next_cb = next_cb
		self.track = None
		
		#Initialize debugging
		debug_init()

		#initialize input and output plugins
		ip_load_plugins()
		op_load_plugins()
		
		#print input and output plugins
		#ip_dump_plugins()
		#op_dump_plugins()
		
		def __next_track(track):
			self.track = self.__next_cb()
			if self.track == None:
				return -1
			track[0] = track_info_new(String(self.track.filename))
			return 0
	
		#attach next_track callback
		get_next = CFUNCTYPE(UNCHECKED(c_int), POINTER(POINTER(struct_track_info)))
		get_next_func = get_next(__next_track)
		pcb = player_callbacks(get_next=get_next_func)

		#initialize player
		player_init(pointer(pcb))

		#set buffer size
		SECOND_SIZE = (44100 * 16 / 8 * 2)
		sec = 10
		player_set_buffer_chunks((sec * SECOND_SIZE + CHUNK_SIZE / 2) / CHUNK_SIZE)

		#set output device
		player_set_op(String('alsa'))
		mixer_open()

	def __check_error(self):
		if len(player_info.error_msg):
			raise Exception(player_info.error_msg)

	def play_track(self, track):
		track = track_info_new(String(track.filename))
		player_play_file(track)
		self.track = track
		self.__check_error()
	
	def play(self):
		player_play()
		self.__check_error()
	
	def stop(self):
		player_stop()
	
	def pause(self):
		player_pause()
	
	def seek(self, pos):
		player_seek(pos, 0, 1)
	
	def __pos(self):
		return player_info.pos
	pos = property(__pos)
	
	def __status(self):
		try:
			return STATUS_MAPPING[player_info.status]
		except KeyException:
			return PLAYBACK_STATUS.UNKNOWN
	status = property(__status)
