# Filter ARFF inputs with Weka filters for 2 clases
# YOU NEED TO REMOVE other classes manually in the line of class definition!!!!!
# input: ARFF file to filter, Class 1, Class 2
# output: 2 classes ARFF with the name including both classes

import os, sys

#--------------------------------------
def WekaFilter2Classes(sInput,Class1,Class2,sOutput):
    # we consider that input is CSV

    # temp file
    temp="temp"
    # sOutput=sInput[:-5]+"_"+Class1+"-"+Class2+".arff" # inputs *.csv
    print "-> Weka Normalization for "+sOutput+" ..."
    cmd = 'java weka.filters.unsupervised.instance.SubsetByExpression -c last -E "(CLASS is \'%s\') or (CLASS is \'%s\')" -i %s -o %s' % (Class1,Class2,sInput,temp)
    print cmd
    os.system(cmd)


    # remove the extra classes from ARFF files (due to Weka error)

    fTemp=open(temp,"r")
    lines=fTemp.readlines()
    fTemp.close()

    newlines=""

    for line in lines:
        if line.find(Class1)!=-1 and line.find(Class2)!=-1:
            x=line.find("{")
            line=line[1:x]+"{"+Class1+","+Class2+"}\n"
            # print "line = ",line
            newlines=newlines+line
            # raw_input("Press Enter to continue...")
            
        else:
            newlines=newlines+line
            #print "NOt=", newlines
            # raw_input("Press Enter to continue...")
    
    fArff=open(sOutput,"w")
    fArff.write(newlines)
    fArff.close()
    
    return
#--------------------------------------

#############################
## MAIN

sFile=sys.argv[1]   # ARFF to be filtered
Class1=sys.argv[2]   # first class
Class2=sys.argv[3]   # second class
sOut=sys.argv[4]     # output file

WekaFilter2Classes(sFile,Class1,Class2,sOut)


