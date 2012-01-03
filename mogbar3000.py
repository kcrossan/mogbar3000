import os

import playback.cmus as cmus

import pygtk
pygtk.require('2.0')
import gtk

import gui.window

import interfacer
import options

def main(playlist):
	interface = interfacer.Interfacer(options.load(), cmus.Cmus)

	main_window = gui.window.Window(interface)
	
	gtk.main()
	return 0

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

