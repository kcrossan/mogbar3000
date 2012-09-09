import os
import time

import playback.cmus_bind
from playback.cmus_bind import *
import ctypes
from ctypes import *

import interfacer
import options

import mutagen

cur_track = 0
def main(playlist):
	global cur_track
	base_dir = 'E:\Albums\FLAC CDs\Cage The Elephant\Cage The Elephant'
	tracks_raw = os.listdir(base_dir)
	tracks_raw.sort()
	print tracks_raw
	tracks = []
	for track in tracks_raw:
		tracks.append(mutagen.File(os.path.join(base_dir,track), easy=True))
	def next_track():
		global cur_track
		try:
			track = os.path.join(base_dir, tracks_raw[cur_track])
			#print "next_track: " + track["title"][0]
			cur_track += 1
			return track
		except Exception as e:
			print e
			return None

	def __next_track(track):
		print 'in __next_track'
		ttrack = next_track()
		if ttrack == None:
			print 'no track'
			return -1
		track[0] = track_info_new(String(ttrack))
		return 0

	#Initialize debugging
	debug_init()

	#initialize input and output plugins
	ip_load_plugins()
	op_load_plugins()
	
	#print input and output plugins
	ip_dump_plugins()
	op_dump_plugins()
	
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

	#set output device to default
	player_set_op(None)
	mixer_open()

	#interface = interfacer.Interfacer(options.load(), cmus.Cmus)
	#interface.get_next_track = next_track
	#interface.output.play()
	player_play()
	print player_info.error_msg
	while True:
		#print interface.output.pos
		print player_info.pos
		time.sleep(1)

	# main_window = gui.window.Window(interface)
	
	# gtk.main()
	# return 0

def process_playlist(files):
	ret = []
	for file in files:
		if not len(file):
			continue
		if not os.path.isabs(file):
			file = os.path.abspath(file)
		if not os.path.exists(file):
			continue
		if os.path.isdir(path):
			ret.extend(os.listdir(path))
		else:
			ret.append(entry)
	return ret

if __name__ == "__main__":
	import sys
	main(process_playlist(sys.argv[1:-1]))

