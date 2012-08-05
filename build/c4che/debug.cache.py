AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
CCFLAGS_MACBUNDLE = ['-fPIC']
CC_VERSION = ('4', '6', '1')
COMPILER_CXX = 'g++'
CPP = '/usr/bin/cpp'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXDEFINES = ['LINUX']
CXXDEFINES_ST = '-D%s'
CXXFLAGS = ['-g', '-Wall', '--pedantic', '-fno-omit-frame-pointer']
CXXLNK_SRC_F = ''
CXXLNK_TGT_F = ['-o', '']
CXX_NAME = 'gcc'
CXX_SRC_F = ''
CXX_TGT_F = ['-c', '-o', '']
DEST_BINFMT = 'elf'
DEST_CPU = 'x86'
DEST_OS = 'linux'
FULLSTATIC_MARKER = '-static'
LIBPATH_ST = '-L%s'
LIB_PROFILE = ['profiler']
LIB_PTHREAD = ['pthread']
LIB_RT = ['rt']
LIB_ST = '-l%s'
LIB_TCMALLOC = ['tcmalloc']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINK_CXX = ['/usr/bin/g++']
PREFIX = '/usr/local'
RANLIB = '/usr/bin/ranlib'
RPATH_ST = '-Wl,-rpath,%s'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
STATICLIBPATH_ST = '-L%s'
STATICLIB_MARKER = '-Wl,-Bstatic'
STATICLIB_ST = '-l%s'
_VARIANT_ = 'debug'
macbundle_PATTERN = '%s.bundle'
program_PATTERN = '%s'
shlib_CXXFLAGS = ['-fPIC', '-DPIC']
shlib_LINKFLAGS = ['-shared']
shlib_PATTERN = 'lib%s.so'
staticlib_LINKFLAGS = ['-Wl,-Bstatic']
staticlib_PATTERN = 'lib%s.a'