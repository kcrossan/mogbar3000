'''Wrapper for track_info.h

Generated with:
C:/msys/bin/ctypesgen.py -l libcmus track_info.h player.h input.h output.h debug.h buffer.h -o cmus.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin' or sys.platform == 'linux2':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None
    name_formats = ["lib%s.so", "%s.so", "%s"]

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        for libname in [format % libname for format in self.name_formats]:
			result = self._ld_so_cache.get(libname)
			if result: yield result

			path = ctypes.util.find_library(libname)
			if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["libcmus"] = load_library("libcmus")

# 1 libraries
# End libraries

# No modules

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 33
for _lib in _libs.values():
    try:
        duration = (c_int).in_dll(_lib, 'duration')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 34
for _lib in _libs.values():
    try:
        bitrate = (c_long).in_dll(_lib, 'bitrate')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 35
for _lib in _libs.values():
    try:
        codec = (String).in_dll(_lib, 'codec')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 36
for _lib in _libs.values():
    try:
        ref = (c_int).in_dll(_lib, 'ref')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 37
for _lib in _libs.values():
    try:
        filename = (String).in_dll(_lib, 'filename')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 39
for _lib in _libs.values():
    try:
        tracknumber = (c_int).in_dll(_lib, 'tracknumber')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 40
for _lib in _libs.values():
    try:
        discnumber = (c_int).in_dll(_lib, 'discnumber')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 41
for _lib in _libs.values():
    try:
        date = (c_int).in_dll(_lib, 'date')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 42
for _lib in _libs.values():
    try:
        rg_track_gain = (c_double).in_dll(_lib, 'rg_track_gain')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 43
for _lib in _libs.values():
    try:
        rg_track_peak = (c_double).in_dll(_lib, 'rg_track_peak')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 44
for _lib in _libs.values():
    try:
        rg_album_gain = (c_double).in_dll(_lib, 'rg_album_gain')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 45
for _lib in _libs.values():
    try:
        rg_album_peak = (c_double).in_dll(_lib, 'rg_album_peak')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 46
for _lib in _libs.values():
    try:
        artist = (String).in_dll(_lib, 'artist')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 47
for _lib in _libs.values():
    try:
        album = (String).in_dll(_lib, 'album')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 48
for _lib in _libs.values():
    try:
        title = (String).in_dll(_lib, 'title')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 49
for _lib in _libs.values():
    try:
        genre = (String).in_dll(_lib, 'genre')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 50
for _lib in _libs.values():
    try:
        comment = (String).in_dll(_lib, 'comment')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 51
for _lib in _libs.values():
    try:
        albumartist = (String).in_dll(_lib, 'albumartist')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 52
for _lib in _libs.values():
    try:
        artistsort = (String).in_dll(_lib, 'artistsort')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 54
for _lib in _libs.values():
    try:
        collkey_artist = (String).in_dll(_lib, 'collkey_artist')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 55
for _lib in _libs.values():
    try:
        collkey_album = (String).in_dll(_lib, 'collkey_album')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 56
for _lib in _libs.values():
    try:
        collkey_title = (String).in_dll(_lib, 'collkey_title')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 57
for _lib in _libs.values():
    try:
        collkey_genre = (String).in_dll(_lib, 'collkey_genre')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 58
for _lib in _libs.values():
    try:
        collkey_comment = (String).in_dll(_lib, 'collkey_comment')
        break
    except:
        pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 59
for _lib in _libs.values():
    try:
        collkey_albumartist = (String).in_dll(_lib, 'collkey_albumartist')
        break
    except:
        pass

sort_key_t = c_size_t # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 64

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 92
class struct_track_info(Structure):
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 92
if hasattr(_libs['libcmus'], 'track_info_new'):
    track_info_new = _libs['libcmus'].track_info_new
    track_info_new.argtypes = [String]
    track_info_new.restype = POINTER(struct_track_info)

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\keyval.h: 4
class struct_keyval(Structure):
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 93
if hasattr(_libs['libcmus'], 'track_info_set_comments'):
    track_info_set_comments = _libs['libcmus'].track_info_set_comments
    track_info_set_comments.argtypes = [POINTER(struct_track_info), POINTER(struct_keyval)]
    track_info_set_comments.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 95
if hasattr(_libs['libcmus'], 'track_info_ref'):
    track_info_ref = _libs['libcmus'].track_info_ref
    track_info_ref.argtypes = [POINTER(struct_track_info)]
    track_info_ref.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 96
if hasattr(_libs['libcmus'], 'track_info_unref'):
    track_info_unref = _libs['libcmus'].track_info_unref
    track_info_unref.argtypes = [POINTER(struct_track_info)]
    track_info_unref.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 102
if hasattr(_libs['libcmus'], 'track_info_has_tag'):
    track_info_has_tag = _libs['libcmus'].track_info_has_tag
    track_info_has_tag.argtypes = [POINTER(struct_track_info)]
    track_info_has_tag.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 110
if hasattr(_libs['libcmus'], 'track_info_matches'):
    track_info_matches = _libs['libcmus'].track_info_matches
    track_info_matches.argtypes = [POINTER(struct_track_info), String, c_uint]
    track_info_matches.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 120
if hasattr(_libs['libcmus'], 'track_info_matches_full'):
    track_info_matches_full = _libs['libcmus'].track_info_matches_full
    track_info_matches_full.argtypes = [POINTER(struct_track_info), String, c_uint, c_uint, c_int]
    track_info_matches_full.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 123
if hasattr(_libs['libcmus'], 'track_info_cmp'):
    track_info_cmp = _libs['libcmus'].track_info_cmp
    track_info_cmp.argtypes = [POINTER(struct_track_info), POINTER(struct_track_info), POINTER(sort_key_t)]
    track_info_cmp.restype = c_int

# c:\\msys\\mingw\\bin\\../lib/gcc/mingw32/4.6.1/../../../../include/pthread.h: 589
class struct_pthread_mutex_t_(Structure):
    pass

pthread_mutex_t = POINTER(struct_pthread_mutex_t_) # c:\\msys\\mingw\\bin\\../lib/gcc/mingw32/4.6.1/../../../../include/pthread.h: 589

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\locking.h: 9
if hasattr(_libs['libcmus'], 'cmus_mutex_lock'):
    cmus_mutex_lock = _libs['libcmus'].cmus_mutex_lock
    cmus_mutex_lock.argtypes = [POINTER(pthread_mutex_t)]
    cmus_mutex_lock.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\locking.h: 10
if hasattr(_libs['libcmus'], 'cmus_mutex_unlock'):
    cmus_mutex_unlock = _libs['libcmus'].cmus_mutex_unlock
    cmus_mutex_unlock.argtypes = [POINTER(pthread_mutex_t)]
    cmus_mutex_unlock.restype = None

struct_keyval.__slots__ = [
    'key',
    'val',
]
struct_keyval._fields_ = [
    ('key', String),
    ('val', String),
]

enum_anon_6 = c_int # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 29

PLAYER_ERROR_SUCCESS = 0 # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 29

PLAYER_ERROR_ERRNO = (PLAYER_ERROR_SUCCESS + 1) # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 29

PLAYER_ERROR_NOT_SUPPORTED = (PLAYER_ERROR_ERRNO + 1) # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 29

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 38
try:
    player_status_names = (POINTER(POINTER(c_char))).in_dll(_libs['libcmus'], 'player_status_names')
except:
    pass

enum_player_status = c_int # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 39

PLAYER_STATUS_STOPPED = 0 # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 39

PLAYER_STATUS_PLAYING = (PLAYER_STATUS_STOPPED + 1) # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 39

PLAYER_STATUS_PAUSED = (PLAYER_STATUS_PLAYING + 1) # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 39

NR_PLAYER_STATUS = (PLAYER_STATUS_PAUSED + 1) # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 39

enum_replaygain = c_int # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 46

RG_DISABLED = 0 # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 46

RG_TRACK = (RG_DISABLED + 1) # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 46

RG_ALBUM = (RG_TRACK + 1) # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 46

RG_TRACK_PREFERRED = (RG_ALBUM + 1) # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 46

RG_ALBUM_PREFERRED = (RG_TRACK_PREFERRED + 1) # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 46

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 54
class struct_player_callbacks(Structure):
    pass

struct_player_callbacks.__slots__ = [
    'get_next',
]
struct_player_callbacks._fields_ = [
    ('get_next', CFUNCTYPE(UNCHECKED(c_int), POINTER(POINTER(struct_track_info)))),
]

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 58
class struct_player_info(Structure):
    pass

struct_player_info.__slots__ = [
    'mutex',
    'ti',
    'metadata',
    'status',
    'pos',
    'buffer_fill',
    'buffer_size',
    'error_msg',
    'file_changed',
    'metadata_changed',
    'status_changed',
    'position_changed',
    'buffer_fill_changed',
]
struct_player_info._fields_ = [
    ('mutex', pthread_mutex_t),
    ('ti', POINTER(struct_track_info)),
    ('metadata', c_char * ((255 * 16) + 1)),
    ('status', enum_player_status),
    ('pos', c_int),
    ('buffer_fill', c_int),
    ('buffer_size', c_int),
    ('error_msg', String),
    ('file_changed', c_uint, 1),
    ('metadata_changed', c_uint, 1),
    ('status_changed', c_uint, 1),
    ('position_changed', c_uint, 1),
    ('buffer_fill_changed', c_uint, 1),
]

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 84
try:
    player_info = (struct_player_info).in_dll(_libs['libcmus'], 'player_info')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 85
try:
    player_cont = (c_int).in_dll(_libs['libcmus'], 'player_cont')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 86
try:
    player_repeat_current = (c_int).in_dll(_libs['libcmus'], 'player_repeat_current')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 87
try:
    replaygain = (enum_replaygain).in_dll(_libs['libcmus'], 'replaygain')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 88
try:
    replaygain_limit = (c_int).in_dll(_libs['libcmus'], 'replaygain_limit')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 89
try:
    replaygain_preamp = (c_double).in_dll(_libs['libcmus'], 'replaygain_preamp')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 90
try:
    soft_vol = (c_int).in_dll(_libs['libcmus'], 'soft_vol')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 91
try:
    soft_vol_l = (c_int).in_dll(_libs['libcmus'], 'soft_vol_l')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 92
try:
    soft_vol_r = (c_int).in_dll(_libs['libcmus'], 'soft_vol_r')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 94
if hasattr(_libs['libcmus'], 'player_init'):
    player_init = _libs['libcmus'].player_init
    player_init.argtypes = [POINTER(struct_player_callbacks)]
    player_init.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 95
if hasattr(_libs['libcmus'], 'player_exit'):
    player_exit = _libs['libcmus'].player_exit
    player_exit.argtypes = []
    player_exit.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 98
if hasattr(_libs['libcmus'], 'player_set_file'):
    player_set_file = _libs['libcmus'].player_set_file
    player_set_file.argtypes = [POINTER(struct_track_info)]
    player_set_file.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 101
if hasattr(_libs['libcmus'], 'player_play_file'):
    player_play_file = _libs['libcmus'].player_play_file
    player_play_file.argtypes = [POINTER(struct_track_info)]
    player_play_file.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 103
if hasattr(_libs['libcmus'], 'player_play'):
    player_play = _libs['libcmus'].player_play
    player_play.argtypes = []
    player_play.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 104
if hasattr(_libs['libcmus'], 'player_stop'):
    player_stop = _libs['libcmus'].player_stop
    player_stop.argtypes = []
    player_stop.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 105
if hasattr(_libs['libcmus'], 'player_pause'):
    player_pause = _libs['libcmus'].player_pause
    player_pause.argtypes = []
    player_pause.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 106
if hasattr(_libs['libcmus'], 'player_seek'):
    player_seek = _libs['libcmus'].player_seek
    player_seek.argtypes = [c_double, c_int, c_int]
    player_seek.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 107
if hasattr(_libs['libcmus'], 'player_set_op'):
    player_set_op = _libs['libcmus'].player_set_op
    player_set_op.argtypes = [String]
    player_set_op.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 108
if hasattr(_libs['libcmus'], 'player_set_buffer_chunks'):
    player_set_buffer_chunks = _libs['libcmus'].player_set_buffer_chunks
    player_set_buffer_chunks.argtypes = [c_uint]
    player_set_buffer_chunks.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 109
if hasattr(_libs['libcmus'], 'player_get_buffer_chunks'):
    player_get_buffer_chunks = _libs['libcmus'].player_get_buffer_chunks
    player_get_buffer_chunks.argtypes = []
    player_get_buffer_chunks.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 111
if hasattr(_libs['libcmus'], 'player_set_soft_volume'):
    player_set_soft_volume = _libs['libcmus'].player_set_soft_volume
    player_set_soft_volume.argtypes = [c_int, c_int]
    player_set_soft_volume.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 112
if hasattr(_libs['libcmus'], 'player_set_soft_vol'):
    player_set_soft_vol = _libs['libcmus'].player_set_soft_vol
    player_set_soft_vol.argtypes = [c_int]
    player_set_soft_vol.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 113
if hasattr(_libs['libcmus'], 'player_set_rg'):
    player_set_rg = _libs['libcmus'].player_set_rg
    player_set_rg.argtypes = [enum_replaygain]
    player_set_rg.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 114
if hasattr(_libs['libcmus'], 'player_set_rg_limit'):
    player_set_rg_limit = _libs['libcmus'].player_set_rg_limit
    player_set_rg_limit.argtypes = [c_int]
    player_set_rg_limit.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 115
if hasattr(_libs['libcmus'], 'player_set_rg_preamp'):
    player_set_rg_preamp = _libs['libcmus'].player_set_rg_preamp
    player_set_rg_preamp.argtypes = [c_double]
    player_set_rg_preamp.restype = None

sample_format_t = c_uint # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\sf.h: 31

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 11
class struct_input_plugin(Structure):
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 13
if hasattr(_libs['libcmus'], 'ip_load_plugins'):
    ip_load_plugins = _libs['libcmus'].ip_load_plugins
    ip_load_plugins.argtypes = []
    ip_load_plugins.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 19
if hasattr(_libs['libcmus'], 'ip_new'):
    ip_new = _libs['libcmus'].ip_new
    ip_new.argtypes = [String]
    ip_new.restype = POINTER(struct_input_plugin)

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 24
if hasattr(_libs['libcmus'], 'ip_delete'):
    ip_delete = _libs['libcmus'].ip_delete
    ip_delete.argtypes = [POINTER(struct_input_plugin)]
    ip_delete.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 29
if hasattr(_libs['libcmus'], 'ip_open'):
    ip_open = _libs['libcmus'].ip_open
    ip_open.argtypes = [POINTER(struct_input_plugin)]
    ip_open.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 31
if hasattr(_libs['libcmus'], 'ip_setup'):
    ip_setup = _libs['libcmus'].ip_setup
    ip_setup.argtypes = [POINTER(struct_input_plugin)]
    ip_setup.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 36
if hasattr(_libs['libcmus'], 'ip_close'):
    ip_close = _libs['libcmus'].ip_close
    ip_close.argtypes = [POINTER(struct_input_plugin)]
    ip_close.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 41
if hasattr(_libs['libcmus'], 'ip_read'):
    ip_read = _libs['libcmus'].ip_read
    ip_read.argtypes = [POINTER(struct_input_plugin), String, c_int]
    ip_read.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 46
if hasattr(_libs['libcmus'], 'ip_seek'):
    ip_seek = _libs['libcmus'].ip_seek
    ip_seek.argtypes = [POINTER(struct_input_plugin), c_double]
    ip_seek.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 51
if hasattr(_libs['libcmus'], 'ip_read_comments'):
    ip_read_comments = _libs['libcmus'].ip_read_comments
    ip_read_comments.argtypes = [POINTER(struct_input_plugin), POINTER(POINTER(struct_keyval))]
    ip_read_comments.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 53
if hasattr(_libs['libcmus'], 'ip_duration'):
    ip_duration = _libs['libcmus'].ip_duration
    ip_duration.argtypes = [POINTER(struct_input_plugin)]
    ip_duration.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 54
if hasattr(_libs['libcmus'], 'ip_bitrate'):
    ip_bitrate = _libs['libcmus'].ip_bitrate
    ip_bitrate.argtypes = [POINTER(struct_input_plugin)]
    ip_bitrate.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 55
if hasattr(_libs['libcmus'], 'ip_codec'):
    ip_codec = _libs['libcmus'].ip_codec
    ip_codec.argtypes = [POINTER(struct_input_plugin)]
    if sizeof(c_int) == sizeof(c_void_p):
        ip_codec.restype = ReturnString
    else:
        ip_codec.restype = String
        ip_codec.errcheck = ReturnString

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 57
if hasattr(_libs['libcmus'], 'ip_get_sf'):
    ip_get_sf = _libs['libcmus'].ip_get_sf
    ip_get_sf.argtypes = [POINTER(struct_input_plugin)]
    ip_get_sf.restype = sample_format_t

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 58
if hasattr(_libs['libcmus'], 'ip_get_filename'):
    ip_get_filename = _libs['libcmus'].ip_get_filename
    ip_get_filename.argtypes = [POINTER(struct_input_plugin)]
    if sizeof(c_int) == sizeof(c_void_p):
        ip_get_filename.restype = ReturnString
    else:
        ip_get_filename.restype = String
        ip_get_filename.errcheck = ReturnString

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 59
if hasattr(_libs['libcmus'], 'ip_get_metadata'):
    ip_get_metadata = _libs['libcmus'].ip_get_metadata
    ip_get_metadata.argtypes = [POINTER(struct_input_plugin)]
    if sizeof(c_int) == sizeof(c_void_p):
        ip_get_metadata.restype = ReturnString
    else:
        ip_get_metadata.restype = String
        ip_get_metadata.errcheck = ReturnString

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 60
if hasattr(_libs['libcmus'], 'ip_is_remote'):
    ip_is_remote = _libs['libcmus'].ip_is_remote
    ip_is_remote.argtypes = [POINTER(struct_input_plugin)]
    ip_is_remote.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 61
if hasattr(_libs['libcmus'], 'ip_metadata_changed'):
    ip_metadata_changed = _libs['libcmus'].ip_metadata_changed
    ip_metadata_changed.argtypes = [POINTER(struct_input_plugin)]
    ip_metadata_changed.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 62
if hasattr(_libs['libcmus'], 'ip_eof'):
    ip_eof = _libs['libcmus'].ip_eof
    ip_eof.argtypes = [POINTER(struct_input_plugin)]
    ip_eof.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 63
if hasattr(_libs['libcmus'], 'ip_get_error_msg'):
    ip_get_error_msg = _libs['libcmus'].ip_get_error_msg
    ip_get_error_msg.argtypes = [POINTER(struct_input_plugin), c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        ip_get_error_msg.restype = ReturnString
    else:
        ip_get_error_msg.restype = String
        ip_get_error_msg.errcheck = ReturnString

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 64
if hasattr(_libs['libcmus'], 'ip_get_supported_extensions'):
    ip_get_supported_extensions = _libs['libcmus'].ip_get_supported_extensions
    ip_get_supported_extensions.argtypes = []
    ip_get_supported_extensions.restype = POINTER(POINTER(c_char))

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 65
if hasattr(_libs['libcmus'], 'ip_dump_plugins'):
    ip_dump_plugins = _libs['libcmus'].ip_dump_plugins
    ip_dump_plugins.argtypes = []
    ip_dump_plugins.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 12
try:
    volume_max = (c_int).in_dll(_libs['libcmus'], 'volume_max')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 13
try:
    volume_l = (c_int).in_dll(_libs['libcmus'], 'volume_l')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 14
try:
    volume_r = (c_int).in_dll(_libs['libcmus'], 'volume_r')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 16
if hasattr(_libs['libcmus'], 'op_load_plugins'):
    op_load_plugins = _libs['libcmus'].op_load_plugins
    op_load_plugins.argtypes = []
    op_load_plugins.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 17
if hasattr(_libs['libcmus'], 'op_exit_plugins'):
    op_exit_plugins = _libs['libcmus'].op_exit_plugins
    op_exit_plugins.argtypes = []
    op_exit_plugins.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 24
if hasattr(_libs['libcmus'], 'op_select'):
    op_select = _libs['libcmus'].op_select
    op_select.argtypes = [String]
    op_select.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 25
if hasattr(_libs['libcmus'], 'op_select_any'):
    op_select_any = _libs['libcmus'].op_select_any
    op_select_any.argtypes = []
    op_select_any.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 32
if hasattr(_libs['libcmus'], 'op_open'):
    op_open = _libs['libcmus'].op_open
    op_open.argtypes = [sample_format_t]
    op_open.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 39
if hasattr(_libs['libcmus'], 'op_drop'):
    op_drop = _libs['libcmus'].op_drop
    op_drop.argtypes = []
    op_drop.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 46
if hasattr(_libs['libcmus'], 'op_close'):
    op_close = _libs['libcmus'].op_close
    op_close.argtypes = []
    op_close.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 53
if hasattr(_libs['libcmus'], 'op_write'):
    op_write = _libs['libcmus'].op_write
    op_write.argtypes = [String, c_int]
    op_write.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 58
if hasattr(_libs['libcmus'], 'op_pause'):
    op_pause = _libs['libcmus'].op_pause
    op_pause.argtypes = []
    op_pause.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 59
if hasattr(_libs['libcmus'], 'op_unpause'):
    op_unpause = _libs['libcmus'].op_unpause
    op_unpause.argtypes = []
    op_unpause.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 64
if hasattr(_libs['libcmus'], 'op_buffer_space'):
    op_buffer_space = _libs['libcmus'].op_buffer_space
    op_buffer_space.argtypes = []
    op_buffer_space.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 69
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'op_reset'):
        continue
    op_reset = _lib.op_reset
    op_reset.argtypes = []
    op_reset.restype = c_int
    break

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 71
if hasattr(_libs['libcmus'], 'mixer_open'):
    mixer_open = _libs['libcmus'].mixer_open
    mixer_open.argtypes = []
    mixer_open.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 72
if hasattr(_libs['libcmus'], 'mixer_close'):
    mixer_close = _libs['libcmus'].mixer_close
    mixer_close.argtypes = []
    mixer_close.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 73
if hasattr(_libs['libcmus'], 'mixer_set_volume'):
    mixer_set_volume = _libs['libcmus'].mixer_set_volume
    mixer_set_volume.argtypes = [c_int, c_int]
    mixer_set_volume.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 74
if hasattr(_libs['libcmus'], 'mixer_read_volume'):
    mixer_read_volume = _libs['libcmus'].mixer_read_volume
    mixer_read_volume.argtypes = []
    mixer_read_volume.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 75
if hasattr(_libs['libcmus'], 'mixer_get_fds'):
    mixer_get_fds = _libs['libcmus'].mixer_get_fds
    mixer_get_fds.argtypes = [POINTER(c_int)]
    mixer_get_fds.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 77
if hasattr(_libs['libcmus'], 'op_add_options'):
    op_add_options = _libs['libcmus'].op_add_options
    op_add_options.argtypes = []
    op_add_options.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 78
if hasattr(_libs['libcmus'], 'op_get_error_msg'):
    op_get_error_msg = _libs['libcmus'].op_get_error_msg
    op_get_error_msg.argtypes = [c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        op_get_error_msg.restype = ReturnString
    else:
        op_get_error_msg.restype = String
        op_get_error_msg.errcheck = ReturnString

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 79
if hasattr(_libs['libcmus'], 'op_dump_plugins'):
    op_dump_plugins = _libs['libcmus'].op_dump_plugins
    op_dump_plugins.argtypes = []
    op_dump_plugins.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\output.h: 80
if hasattr(_libs['libcmus'], 'op_get_current'):
    op_get_current = _libs['libcmus'].op_get_current
    op_get_current.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        op_get_current.restype = ReturnString
    else:
        op_get_current.restype = String
        op_get_current.errcheck = ReturnString

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\debug.h: 14
if hasattr(_libs['libcmus'], 'debug_init'):
    debug_init = _libs['libcmus'].debug_init
    debug_init.argtypes = []
    debug_init.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\debug.h: 15
if hasattr(_libs['libcmus'], '__debug_bug'):
    _func = _libs['libcmus'].__debug_bug
    _restype = None
    _argtypes = [String, String]
    __debug_bug = _variadic_function(_func,_restype,_argtypes)

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\debug.h: 16
if hasattr(_libs['libcmus'], '__debug_print'):
    _func = _libs['libcmus'].__debug_print
    _restype = None
    _argtypes = [String, String]
    __debug_print = _variadic_function(_func,_restype,_argtypes)

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\debug.h: 18
if hasattr(_libs['libcmus'], 'timer_get'):
    timer_get = _libs['libcmus'].timer_get
    timer_get.argtypes = []
    timer_get.restype = c_uint64

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\debug.h: 19
if hasattr(_libs['libcmus'], 'timer_print'):
    timer_print = _libs['libcmus'].timer_print
    timer_print.argtypes = [String, c_uint64]
    timer_print.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\buffer.h: 7
try:
    buffer_nr_chunks = (c_uint).in_dll(_libs['libcmus'], 'buffer_nr_chunks')
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\buffer.h: 9
if hasattr(_libs['libcmus'], 'buffer_init'):
    buffer_init = _libs['libcmus'].buffer_init
    buffer_init.argtypes = []
    buffer_init.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\buffer.h: 10
if hasattr(_libs['libcmus'], 'buffer_free'):
    buffer_free = _libs['libcmus'].buffer_free
    buffer_free.argtypes = []
    buffer_free.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\buffer.h: 11
if hasattr(_libs['libcmus'], 'buffer_get_rpos'):
    buffer_get_rpos = _libs['libcmus'].buffer_get_rpos
    buffer_get_rpos.argtypes = [POINTER(POINTER(c_char))]
    buffer_get_rpos.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\buffer.h: 12
if hasattr(_libs['libcmus'], 'buffer_get_wpos'):
    buffer_get_wpos = _libs['libcmus'].buffer_get_wpos
    buffer_get_wpos.argtypes = [POINTER(POINTER(c_char))]
    buffer_get_wpos.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\buffer.h: 13
if hasattr(_libs['libcmus'], 'buffer_consume'):
    buffer_consume = _libs['libcmus'].buffer_consume
    buffer_consume.argtypes = [c_int]
    buffer_consume.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\buffer.h: 14
if hasattr(_libs['libcmus'], 'buffer_fill'):
    buffer_fill = _libs['libcmus'].buffer_fill
    buffer_fill.argtypes = [c_int]
    buffer_fill.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\buffer.h: 15
if hasattr(_libs['libcmus'], 'buffer_reset'):
    buffer_reset = _libs['libcmus'].buffer_reset
    buffer_reset.argtypes = []
    buffer_reset.restype = None

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\buffer.h: 16
if hasattr(_libs['libcmus'], 'buffer_get_filled_chunks'):
    buffer_get_filled_chunks = _libs['libcmus'].buffer_get_filled_chunks
    buffer_get_filled_chunks.argtypes = []
    buffer_get_filled_chunks.restype = c_int

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 83
try:
    SORT_INVALID = (-1)
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 85
try:
    TI_MATCH_ARTIST = (1 << 0)
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 86
try:
    TI_MATCH_ALBUM = (1 << 1)
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 87
try:
    TI_MATCH_TITLE = (1 << 2)
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 88
try:
    TI_MATCH_ALBUMARTIST = (1 << 3)
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 89
try:
    TI_MATCH_ALL = (~0)
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 117
try:
    player_info_lock = (cmus_mutex_lock (pointer((player_info.mutex))))
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 118
try:
    player_info_unlock = (cmus_mutex_unlock (pointer((player_info.mutex))))
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\config/debug.h: 4
try:
    DEBUG = 2
except:
    pass

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\debug.h: 23
def __STR(a):
    return a

# c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\buffer.h: 5
try:
    CHUNK_SIZE = (60 * 1024)
except:
    pass

track_info = struct_track_info # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\track_info.h: 92

player_callbacks = struct_player_callbacks # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 54

#player_info = struct_player_info # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\player.h: 58

input_plugin = struct_input_plugin # c:\\Documents and Settings\\Kevin\\My Documents\\Coding Projects\\libcmus\\input.h: 11

# No inserted files

