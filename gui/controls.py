import pygtk
pygtk.require('2.0')
import gtk

class Controls(gtk.HBox):
	def __init__(self, interfacer):
		gtk.HBox.__init__(self)
		
		self.interfacer = interfacer
		
		self.pack_start(gtk.Button("Controls"), True, True, 0)
		
