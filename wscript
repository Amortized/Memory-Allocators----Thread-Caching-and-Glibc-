#! /usr/bin/evn python
# encoding: utf-8

import sys
import Options, UnitTest
from TaskGen import feature, after
import Task, Utils

srcdir = '.'
blddir = 'build'

def set_options(opt):
    opt.tool_options('compiler_cxx')

    opt.add_option('--debug', help='Build debug variant',
                   action='store_true', dest="build_debug", default=True
                  )

    opt.add_option('--release', help='Build release variant',
                  action='store_false', dest="build_debug"
                 )

def configure(conf):
    conf.check_tool('compiler_cxx')

    #
    # Configure platform
    #
    if sys.platform.startswith('linux'):
        conf.env.CXXDEFINES = ['LINUX']
    elif sys.platform.startswith('darwin'):
        conf.env.CXXDEFINES = ['MAC_OS']

    #
    # Configure libraries
    #
    conf.env.LIB_PTHREAD = [ 'pthread' ]
    conf.env.LIB_PROFILE = [ 'profiler' ]
    conf.env.LIB_RT = ['rt']
    conf.env.LIB_TCMALLOC = [ 'tcmalloc' ]

    #
    # Configure a debug environment
    #
    env = conf.env.copy()
    env.set_variant('debug')
    conf.set_env_name('debug', env)
    conf.setenv('debug')
    conf.env.CXXFLAGS = ['-g', '-Wall', '--pedantic',
                         '-fno-omit-frame-pointer']
    #conf.env.LINKFLAGS = ['-export-dynamic']

    #
    # Configure a release environment
    #
    env = conf.env.copy()
    env.set_variant('release')
    conf.set_env_name('release', env)
    conf.setenv('release')
    conf.env.CXXFLAGS = ['-O3', '-g', '-Wall', '--pedantic',
                         '-fno-omit-frame-pointer']

def build(bld):
    #****************************************
    # libs
    #

    # header only libs; just documenting
    # lock.hpp
    # unit_test.hpp

    bld.new_task_gen( features = 'cxx cstaticlib',
                      source = """ log_message.cpp
                                   log_writer.cpp
                               """,
                      includes = '.. .',
                      uselib = 'PTHREAD',
                      target = 'logging',
                      name = 'logging'
                    )

    bld.new_task_gen( features = 'cxx cstaticlib',
                      source = """ thread.cpp
                                   thread_registry.cpp
                               """,
                      includes = '.. .',
                      uselib = 'PTHREAD',
                      uselib_local = 'logging',
                      target = 'concurrency',
                      name = 'concurrency'
                    )



    #*****new static lib for scalable-memory-allocator test
    bld.new_task_gen( features = 'cxx cstaticlib',
                      source = """ memtest_binsmgr.cpp
                               """,
                      includes = '.. .',
                      #****Memory-checking adopted
                      #defines = ['TEST=1'],
                      uselib = 'PTHREAD',
                      uselib_local = 'logging',
                      target = 'memtest',
                      name = 'memtest'
                    )

#    bld.new_task_gen( features = 'cxx cshlib',
#                      source = """ mytrad_malloc.cpp
#                               """,
#                      includes = '.. .',
#                      uselib = '.. .',
#                      uselib_local = '',
#                      target = 'my_traditional_malloc',
#                      name = 'my_traditional_malloc'
#                    )


    #****************************************
    # tests / benchmarks
    #

    #*****new test for shared-library my_traditional_malloc
    bld.new_task_gen( features = 'cxx cprogram',
                      source = 'memalloc_benchmark.cpp',
                      includes = '.. .',
                      defines = ['LD_LIBRARY_PATH=.'],
                      lib          = ['MyMalloc'],
		      uselib_local = """ memtest
                                         concurrency
                                     """,
                      target = 'memalloc_benchmark_mymalloc',
                      unit_test = 1
                    )

    #*****new benchmark for scalable-memory-allocator test
    bld.new_task_gen( features = 'cxx cprogram',
                      source = 'memalloc_benchmark.cpp',
                      includes = '.. .',
                      lib          = ['llalloc'],
                      libpath      = ['/usr/lib'],
                      uselib_local = """ memtest
                                         concurrency
                                     """,
                      target = 'memalloc_benchmark_llalloc',
                      unit_test = 1
                    )
    #*****tcmalloc version
    bld.new_task_gen( features = 'cxx cprogram',
                      source = 'memalloc_benchmark.cpp',
                      includes = '.. .',
                      uselib = 'TCMALLOC',
                      uselib_local = """ memtest
                                         concurrency
                                     """,
                      target = 'memalloc_benchmark_tcmalloc',
                      unit_test = 1
                    )
    #*****glibc version
    bld.new_task_gen( features = 'cxx cprogram',
                      source = 'memalloc_benchmark.cpp',
                      includes = '.. .',
                      uselib_local = """ memtest
                                         concurrency
                                     """,
                      target = 'memalloc_benchmark_glibc',
                      unit_test = 1
                    )




    #****************************************
    # Binaries
    #


    #
    # Build debug variant, if --debug was set
    #
    if Options.options.build_debug:
        clone_to = 'debug'
    else:
        clone_to = 'release'
    for obj in [] + bld.all_task_gen:
        obj.clone(clone_to)
        obj.posted = True # dont build in default environment
