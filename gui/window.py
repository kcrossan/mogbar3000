import pygtk
pygtk.require('2.0')
import gtk

import controls
from controls import Controls
import actions
from actions import Actions
#import login
#from login import Login
import options
from options import Options
import playlist
from playlist import Playlist

class Window(gtk.Window):
	'''The application's main window, which will contain all other controls.'''
	
	def __init__(self, interface):
		gtk.Window.__init__(self)
		self.set_title("mogbar3000")
		
		#Create child widgets
		self.statusbar = gtk.Statusbar()
		self.controls = Controls(interface)
		self.notebook = gtk.Notebook()
		self.notebook.set_scrollable(True)
		
		#Add children to VBox
		self.box = gtk.VBox()
		self.box.pack_start(self.controls, False, False, 0)
		self.box.pack_start(self.notebook, True, True, 0)
		self.box.pack_start(self.statusbar, False, False, 0)
		self.add(self.box)
		
		self.connect('delete_event', gtk.main_quit)
		
		def create_playlist(tracks, name):
			self.notebook.append_page(Playlist(interface), name)
		interface.create_playlist = create_playlist
		
		def add_tracks(tracks):
			cur = self.notebook.get_current_page()
			if cur == None: return
			cur.store.append()
		
		#done loading
		self.show_all()
		
	
