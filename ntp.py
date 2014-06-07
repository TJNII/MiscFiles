#!/usr/bin/python -tt
# http://www.maxinbjohn.info/2007/12/03/ntp-client-in-python/

###########################################################
#                    Simple NTP Program                   #
#                    By  Maxin B. John (www.linuxify.net) #
#   Simple NTP Client program with command line option    #
###########################################################
from socket import *
import struct
import sys
import time
from optparse import OptionParser

Server = ''
parser = OptionParser()
parser.add_option("-s","--server",dest="server",help="NTP server to contact, default 0.fedora.pool.ntp.org")
(options,args) = parser.parse_args()

# Checking for NTP server parameter
if options.server == None:
    Server = '0.fedora.pool.ntp.org'
else:
    Server= options.server
    
EPOCH = 2208988800L    
client = socket( AF_INET, SOCK_DGRAM )
data = '\x1b' + 47 * '\0'
try:
    client.sendto( data, ( Server, 123 ))
    data, address = client.recvfrom( 1024 )
    
    if data:
        print 'Response received from:', address
        t = struct.unpack( '!12I', data )[10]
        t -= EPOCH
        print '\tTime=%s' % time.ctime(t)
except gaierror:
    print "Network error "
except error:
    print "Error!"
