import os

import cPickle as pickle

def conf_paths():
	'''Returns a tuple containing the configuration directory and the main program configuration file.'''
	conf_dir = os.path.join(os.path.expanduser('~'), '.mogbar3000')
	conf_file = os.path.join(conf_dir, 'all.conf')
	return (conf_dir, conf_file)

def load():
	'''Attempts to load the program's configuration.
	If no configuration is present, returns an empty Options object.'''
	(_,conf_file) = conf_paths()
	if not os.path.exists(conf_file):
		return Options()
	return pickle.load(conf_file)

class Options(dict):
	'''Stores program options to disk in user's home directory.
	Supports any data that can be handled by Python's pickle module.'''
	
	def save(self):
		'''Writes the options dictionary to the configuration file.
		Uses the Python pickler to do so.'''
		(conf_dir,conf_file) = conf_paths()
		if not os.path.exists(conf_dir):
			os.mkdir(conf_dir)
		with open(conf_file, 'w') as ofile:
			pickle.dump(self, ofile)
	
