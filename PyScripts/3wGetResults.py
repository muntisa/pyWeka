# get Weka results using the info from
# List of Arff files: _ListArffInputs.txt
# List of commands: _ListWekaComNoNormal.txt
# write a LOG file

#------------------------------------------------
# Cristian R Munteanu
# University of A Coruna
# muntisa@gmail.com
#------------------------------------------------

import os, sys

#-----------------------------------------------------------------------------------------------------------------------
def GetFileLinesAsList(sFile):
    ListFile=[]
    if os.path.isfile(sFile):
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
def GetWekaRes(sOutWeka,PrecLim):
    # get the statistics from Weka using a precision limit (including the limit)
    
    # returned text
    sOut=""
    # read the Weka file
    if os.path.isfile(sOutWeka):
        foWeka=open(sOutWeka,"r")
        linesWeka = foWeka.readlines()
        foWeka.close()

        for i in range(len(linesWeka)):
            line=linesWeka[i]
            # get the TEST results
            if line.find("Stratified cross-validation")!=-1:
                sSet="TEST"
                # removing strange characters
                if line[-1]=="\n" : line = line[:-1]
                if line[-1]=="\r" : line = line[:-1]
                # print linesWeka[i]
                line=linesWeka[i+15]
                if line[-1]=="\n" : line = line[:-1]
                if line[-1]=="\r" : line = line[:-1]
                Negative=line.split()
                line=linesWeka[i+16]
                if line[-1]=="\n" : line = line[:-1]
                if line[-1]=="\r" : line = line[:-1]
                Positive=line.split()
                line=linesWeka[i+17]
                if line[-1]=="\n" : line = line[:-1]
                if line[-1]=="\r" : line = line[:-1]
                Avgs=line.split()
                #TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                sOut=sOut+sSet+"\t"+Negative[6]+"\t"+Negative[0]+"\t"+Negative[1]+"\t"+Negative[2]+"\t"+Negative[5]+"\t"+sOutWeka+"\n"
                sOut=sOut+sSet+"\t"+Positive[6]+"\t"+Positive[0]+"\t"+Positive[1]+"\t"+Positive[2]+"\t"+Positive[5]+"\t"+sOutWeka+"\n"
                sOut=sOut+sSet+"\t"+Avgs[1]+"\t"+Avgs[2]+"\t"+Avgs[3]+"\t"+Avgs[4]+"\t"+Avgs[7]+"\t"+sOutWeka+"\n"

                # if the TP rates are > Precision Limit
                if ( float(Negative[0])<PrecLim ) or (float(Positive[0])<PrecLim ):
                    sOut=""
        
            # get the TRAINING results
            if line.find("Error on training data")!=-1:
                sSet="Train"
                # removing strange characters
                if line[-1]=="\n" : line = line[:-1]
                if line[-1]=="\r" : line = line[:-1]
                # print linesWeka[i]
                line=linesWeka[i+15]
                if line[-1]=="\n" : line = line[:-1]
                if line[-1]=="\r" : line = line[:-1]
                Negative=line.split()
                line=linesWeka[i+16]
                if line[-1]=="\n" : line = line[:-1]
                if line[-1]=="\r" : line = line[:-1]
                Positive=line.split()
                line=linesWeka[i+17]
                if line[-1]=="\n" : line = line[:-1]
                if line[-1]=="\r" : line = line[:-1]
                Avgs=line.split()
                #TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                sOut=sOut+sSet+"\t"+Negative[6]+"\t"+Negative[0]+"\t"+Negative[1]+"\t"+Negative[2]+"\t"+Negative[5]+"\t"+sOutWeka+"\n"
                sOut=sOut+sSet+"\t"+Positive[6]+"\t"+Positive[0]+"\t"+Positive[1]+"\t"+Positive[2]+"\t"+Positive[5]+"\t"+sOutWeka+"\n"
                sOut=sOut+sSet+"\t"+Avgs[1]+"\t"+Avgs[2]+"\t"+Avgs[3]+"\t"+Avgs[4]+"\t"+Avgs[7]+"\t"+sOutWeka+"\n"

                # if the TP rates are > Precision Limit
                if ( float(Negative[0])<PrecLim ) and ( float(Positive[0])<PrecLim ):
                    sOut=""

    return sOut

#######################################################################################################################
## MAIN
#######################################################################################################################
 
sArffInputs=sys.argv[1]   # "_ListArffInputs.txt"
sCommands = sys.argv[2]   # "_ListWekaClassifiersNoNormal.txt"
outPath= sys.argv[3]      # "Results"
PrecLim= float(sys.argv[4]) # 0.1
sLog= sys.argv[5]         # "_LOG_results.txt"

# get the ARFF input file list
ListInputs=GetFileLinesAsList(sArffInputs)

# get the classifiers line list
ListClassifiers=GetFileLinesAsList(sCommands)

# LOG file
fLog=open("_"+str(PrecLim)+sLog,"a")

# Get the results
print "\n-> Getting Weka Results ... "
for sInput in ListInputs:

    print "\n--> Getting Weka results for "+sInput+" ... "
    sOut="" # to be printed in the output file

    # results with all classifier statistics for one input and precision limit
    sResults=outPath+"\\"+"_Res_"+str(PrecLim)+"_"+sInput+".txt"

    for item in ListClassifiers:
        if item.find(" ")!=-1:
            item=item.replace(" ", "")
            #item=item.split(" ")[0]
        sOutput=outPath+"\\"+"Classif"+sInput[:-5]+"_"+item+".txt" # one output for each Classifier
        sOutx=GetWekaRes(sOutput,PrecLim) # results from Weka
        # if any Weka result, add to the output string to be written
        if sOutx!="":
            sOut=sOut+sOutx
            sOut=sOut+"-"*60+"\n"

    # if any result, write header and into the output file
    print "\n"
    print "*"*40
    print "RESULTS for: "+str(sInput)
    print "*"*40
    if sOut!="":
        print "Generating "+sResults+" ..."
        fLog.write(sResults+"\n\n")
        sOut="Sets\tClass\tTPR\tFPR\tPrec\tROC\tFile\n"+"-"*60+"\n"+sOut
        # write the results
        fOut=open(sResults,"a")
        fOut.write(sOut)
        fLog.write(sOut+"\n")
        fOut.close()
    else:
        print "\n\n!!! NO RESULTS with TPR and FPR > "+str(PrecLim)+" !!!"

fLog.close()       
print "Done!"


