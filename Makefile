#
# a very simple Makefile for miniLZO
#
# Copyright (C) 1996-2011 Markus F.X.J. Oberhumer
#

PROGRAM = libminilzo.so
SOURCES = minilzo.c

# Make sure that minilzo.h, lzoconf.h and lzodefs.h are in the
# current dircectory. Otherwise you may want to adjust CPPFLAGS.
##CPPFLAGS = -I../include/lzo -I.

default:
	gcc -fPIC -g -c -Wall $(SOURCES)
	gcc -shared -Wl,-soname,$(PROGRAM) *.o -o $(PROGRAM)

install:
	cp $(PROGRAM) /usr/local/lib64
	mkdir -p /usr/local/include/minilzo
	cp *.h /usr/local/include/minilzo

clean:
	rm -f $(PROGRAM) $(PROGRAM).exe $(PROGRAM).map $(PROGRAM).tds
	rm -f *.err *.o *.obj

.PHONY: default clean

