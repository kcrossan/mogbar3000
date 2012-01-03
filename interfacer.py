class Interfacer(object):
	def __init__(self, options, output):
		
		def next_track_cb():
			return self.get_next_track()
		
		#"global" vars
		self.options = options
		self.output = output(next_track_cb)
		
		#implementation functions
		self.create_playlist = None
		self.add_tracks = None
		self.get_next_track = None
		self.get_prev_track = None
	
	def play_prev_track(self):
		if output.pos > 10:
			output.seek(0)
		else:
			prev = self.get_prev_track()
			if prev != None:
				output.play_track(prev)
			else:
				output.stop()
	
	def play_next_track(self):
		next = self.get_next_track()
		if next != None:
			output.play_track(next)
		else:
			output.stop()
	
	
