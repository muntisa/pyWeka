# Convert CSV file (comma separated fieds) to Arff Weka input files
# (last column = classs)
# input: CSV file name
# output : ARFF file with the same name
#------------------------------------------------
# Cristian R Munteanu
# University of A Coruna
# muntisa@gmail.com
#------------------------------------------------

import os, sys


#--------------------------------------
def WekaCsv2Arff(sInput,sOutput):
    # we consider that input is CSV
    # sOutput=sInput[:-4]+".arff" # inputs *.csv
    print "-> Weka CSV Conversion to ARFF of "+sOutput+" ..."
    cmd = 'java weka.core.converters.CSVLoader %s > %s' % (sInput, sOutput)
    print cmd
    os.system(cmd)

    return

#--------------------------------------

#############################
## MAIN

sFile=sys.argv[1]  # CSV file to be converted
sOut=sys.argv[2]   # converted ARFF file

WekaCsv2Arff(sFile,sOut)


