import pygtk
pygtk.require('2.0')
import gtk

class Options(gtk.VBox):
	def __init__(self, interfacer):
		self.interfacer = interfacer
		
