from interface import Interface
import sys

interface = Interface()

if len(sys.argv) > 1:
	print interface.messageFB(sys.argv[1], sys.argv[2])
else:
	print "include message as arg"
