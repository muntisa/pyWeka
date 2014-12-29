# crete ARFF input files and the list of them
# by removing attributes from a list

# Inputs:
# 1) ARFF with all the attributes
# 2) List of Variables index as CSV file (Label/ID,VarNo1,...) {not included the CLASS!}
# 3) Output file: list with the generated ARFF files (with limited attributes)

import os, sys

#---------------------------------------------------------------------
def ListOfListsCSV(sCSV):
    Vars=[] # list with vars and labels
    # get the list of lists with all data from a CSV file
    if os.path.isfile(sCSV):
        fVars=open(sCSV,"r")
        linesVars = fVars.readlines()
        fVars.close()

        for line in linesVars:
            if len(line)>1: # not null lines
                if line[-1]=="\n" : line = line[:-1]
                if line[-1]=="\r" : line = line[:-1]
                Curr=line.split(",") # CSV file  (comma separated)
                if Curr[0]!="": Vars.append(Curr)
    return Vars

#---------------------------------------------------------------------
def GetNoOfWekaVars(sArff):
    nVars=0
    if os.path.isfile(sArff):
        fArff=open(sArff,"r")
        linesArff = fArff.readlines()
        fArff.close()

        for line in linesArff:
            if line.find("@attribute")!=-1:nVars+=1
        
    return nVars-1 # not included the last = CLASS
#---------------------------------------------------------------------
def WriteArffFromListVars(sVarNoFile,sArff,sListInputs):
    # write Weka input files from a list of variables and Arff file
    # using Weka remove filter

    # write a list with the arff input files to be processed and have been generated
    fInputs=open(sListInputs,"w") 

    # get the list of Variable Names and ID/labels
    Vars=ListOfListsCSV(sVarNoFile)
    print "-> Generating "+str(len(Vars))+" input files ..."

    # get the number of variables in initial Arff data file
    nWekaVars=GetNoOfWekaVars(sArff)

    # for each input file
    for itemVars in Vars:
    
        sAtts2Remove="" # string to use for remove filter in Weka (variable numbers)
        iV=0 # number of final variables in the filtered model
        for j in range(1,nWekaVars+1):
            if str(j) in itemVars: 
                iV+=1 # no. of vars in the filtered Arff

            else: # if the variable in the initial Arff is not found in our list of vars, add it to be removed
                sAtts2Remove=sAtts2Remove+str(j)+","
                

        sAtts2Remove=sAtts2Remove[:-1] # removing the last comma

        # write an input file Arff
        FileName=sArff[:-5]+"_"+itemVars[0]+"("+str(iV)+")"+".arff" # ARFF name+label of Var Serie +no of vars
        fInputs.write(FileName+"\n")
            
        # run Weka remove attribute command
        # sOutput=outPath+"\\"+"Classif"+sInput+"_"+item+".txt" # one output for each Classifier
        cmd = 'java weka.filters.unsupervised.attribute.Remove -R %s -i %s -o %s' % (sAtts2Remove, sArff, FileName)
        print "Creating Weka input files by removing attributes ... "
        print cmd
        os.system(cmd) 

    fInputs.close()    
    return
    
#---------------------------------------------------------------------

######################################################
## MAIN
######################################################

sArff=sys.argv[1]       # "Template.arff"
sVarNoFile=sys.argv[2]  # "_List_VarNo.csv"#
sListInputs=sys.argv[3] # "_ListArffInputs.txt" #

# generate Weka arff input files using a list of variables and an initial file (all variable file)
# the input file names are inside the list file as the first column
# generate a file with the list of input files to be processed with Weka
WriteArffFromListVars(sVarNoFile,sArff,sListInputs)
 
    
