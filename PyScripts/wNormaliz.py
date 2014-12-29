# Weka Normalization

# Normalizes all numeric values in the given dataset
# (apart from the class attribute, if set).
# The resulting values are by default in [0,1] for the data used to compute
# the normalization intervals. But with the scale and translation parameters one can change that,
# e.g., with scale = 2.0 and translation = -1.0 you get values in the range [-1,+1].
# http://weka.sourceforge.net/doc.dev/weka/filters/unsupervised/attribute/Normalize.html

#------------------------------------------------
# Cristian R Munteanu
# University of A Coruna
# muntisa@gmail.com
#------------------------------------------------

import os, sys


#--------------------------------------
def WekaNormalize(sInput,sOutput):
    # we consider that input is ARFF
    # sOutput=sInput[:-5]+"_Norm.arff"
    print "-> Weka Normalization for "+sOutput+" ..."
    cmd = 'java weka.filters.unsupervised.attribute.Normalize -i %s -o %s' % (sInput, sOutput)
    print cmd
    os.system(cmd)

    return

#--------------------------------------

#############################
## MAIN

sOrig=sys.argv[1]     # ARFF file with original data
sNormal=sys.argv[2]   # ARFF file with normalized data

WekaNormalize(sOrig,sNormal)


