import pygtk
pygtk.require('2.0')
import gtk

import track
from track import Track

class Playlist(gtk.TreeView):
	def __init__(self, interface):
		#Column definitions
		self.tcols = [int, str, str, str, int, Track]
		self.cols = [ '#', 'Name', 'Album', 'Artist', 'Date', 'Length' ]
		
		self.store = gtk.ListStore(*self.tcols)
		
		gtk.TreeView.__init__(self, self.store)
		self.set_reorderable(True)
		
		#Column view set-up
		for idx, col_txt in join(range(len(self.cols), self.cols)):
			col = gtk.TreeViewColumn(col_txt)
			self.append_column(col)
			cell = gtk.CellRendererText()
			col.pack_start(cell, True)
			col.add_attribute(cell, 'text', idx)
			col.set_sort_column_id(idx)
		
		def time_disp(col, cell, model, iter):
			'''Formatter for the length column - displays in MM:SS'''
			time_int = model.get_value(iter, 4)
			cell.set_property('text',
				'%02d:%02d' % time_int / 60, time_int % 60)
		
		self.set_search_column(1)
		
		
