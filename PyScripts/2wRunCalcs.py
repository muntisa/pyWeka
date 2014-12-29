# run Weka calculations using 2 inputs:
# List of Arff files: _ListArffInputs.txt
# List of commands: _ListWekaComNoNormal.txt

import os, sys

#-----------------------------------------------------------------------------------------------------------------------
def GetFileLinesAsList(sFile):
    ListFile=[]
    f=open(sFile,"r")
    lines = f.readlines()
    f.close()

    for line in lines:
        # removing strange characters
        if line[-1]=="\n" : line = line[:-1]
        if line[-1]=="\r" : line = line[:-1]
        ListFile.append(line)
        
    return ListFile
#-----------------------------------------------------------------------------------------------------------------------
def RemoveEmptyFile(sFile):
    if os.path.isfile(sFile):
        fsize=os.path.getsize(sFile)
        if fsize==0:
            os.remove(sFile)
    return
#-----------------------------------------------------------------------------------------------------------------------
def RunWekaClassifiers(ClassifierList,sInput,outPath):    
    for item in ClassifierList:
        sClass=item
        if item.find(" ")!=-1:
            item=item.replace(" ", "")
            #item=item.split(" ")[0]
        sOutput=outPath+"\\"+"Classif"+sInput[:-5]+"_"+item+".txt" # one output for each Classifier
        cmd = 'java weka.classifiers.%s -t %s -i > %s' % (sClass, sInput, sOutput)
        print cmd
        os.system(cmd)
        RemoveEmptyFile(sOutput)
    return

#######################################################################################################################
## MAIN
#######################################################################################################################
 
sArffInputs=sys.argv[1] # "_ListArffInputs.txt"
sCommands = sys.argv[2] # "_ListWekaClassifiersNoNormal.txt"
outPath=sys.argv[3]     # "Results"


# get the ARFF input file list
ListInputs=GetFileLinesAsList(sArffInputs)

# get the classifiers line list
ListClassifiers=GetFileLinesAsList(sCommands)

# run the calculations
print "\n==> Running Weka Classifiers ... "
for item in ListInputs:
    print "--> Running "+item
    RunWekaClassifiers(ListClassifiers,item,outPath)
print "Done!"


