# Weka Standardization
# Standardizes all numeric attributes in the given dataset to have zero mean and unit variance
# (apart from the class attribute, if set).
# http://weka.sourceforge.net/doc.dev/weka/filters/unsupervised/attribute/Standardize.html

import os, sys

#--------------------------------------
def WekaStandardize(sInput,sOutput):
    # we consider that input is ARFF
    # sOutput=sInput[:-5]+"_STD.arff"
    print "-> Weka Standardization for "+sOutput+" ..."
    cmd = 'java weka.filters.unsupervised.attribute.Standardize -i %s -o %s' % (sInput, sOutput)
    print cmd
    os.system(cmd)
    return

#--------------------------------------

#############################
## MAIN

sOrig=sys.argv[1]  # original data file to standardize
sStd=sys.argv[2]   # file with standardized data

WekaStandardize(sOrig,sStd)


