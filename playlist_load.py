'''Loads m3u and pl playlists, returning a list of paths in order.'''

import os

def load(path):
	'''Actual loading function.  Currently handles M3U and PL playlists.
	This corresponds to the file extentions .m3u, .m3u8, and .pl.
	Returns a list of absolute pathnames, or None if playlist is unsupported. '''
	
	def load_m3u():
		'''Attempts to load a m3u playlist.
		Supports relative and absolute paths, as well as directories.
		Properly handles comments.
		Returns a list of absolute filenames that exist.'''
		base_path = dirname(path)
		ret = []
		with open(path) as f:
			for entry in f:
				if not len(entry) or entry[0] == '#':
					continue
				if not os.path.isabs(entry):
					entry = os.path.join(base_path, entry)
				if not os.path.exists(entry):
					continue
				if os.path.isdir(path):
					ret.extend(os.listdir(path))
				else:
					ret.append(entry)
		return ret
	
	def load_pl():
		'''Attempts to load a pl playlist, which is an extremely
		simple list of files.
		Returns a list of absolute filenames that exist.'''
		ret = []
		with open(path) as f:
			for entry in f:
				if not len(entry):
					continue
				if not os.path.exists(entry):
					continue
				ret.append(entry)
		return ret
	
	ext = os.path.splitext(path)[1]
	extmap = { 'm3u': load_m3u, 'm3u8': load_m3u, 'pl': load_pl }
	try:
		return extmap[ext](path)
	except KeyException:
		return None
