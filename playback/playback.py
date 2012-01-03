#from http://stackoverflow.com/questions/36932/whats-the-best-way-to-implement-an-enum-in-python
def enum(**enums):
    return type('Enum', (), enums)

PLAYBACK_STATUS = enum(STOP=1, PLAY=2, PAUSE=3, UNKNOWN=4)
