# Run all the scripts to obtain Weka classification models
# using a CSV parameter file
#------------------------------------------------

import os, sys
import time, datetime
#------------------------------------------------

def RunWekaClassif(sParamFile):

    startAt = datetime.datetime.now()
    sHeader="@ Weka script to search for classification models @\n"
    sHeader=sHeader+"(muntisa@gmail.com)\n"
    sHeader=sHeader+"="*30+"\n"
    sHeader=sHeader+"\nJob started at "+startAt.strftime("%Y-%m-%d %H:%M")+" ... \n"

    print sHeader

    #-------------------------------------------------------------
    # PARAMETERs (CSV file)
    #-------------------------------------------------------------
    fParam=open(sParamFile, "r")
    linesParam = fParam.readlines()
    fParam.close()

    #  1: Input File = Par_Orig.csv * File to be processed (ARFF/CSV)
    #  2: Attributes = _Attributes.csv * List of attribute combinations
    #  3: Classifier = _Classifiers4NormData.txt * List of Weka classifiers + Weka parameters
    #  4: Path to Results = Results * Folder for result files			
    #  5: CSV to ARFF = Y *Conversion of CSV input file to ARFF (Y/N)
    #  6: Normalise = Y * Normalise the input file (Y/N)
    #  7: Standardise = Y * Standardise the input file (Y/N)
    #  8: Use original input = Y * Use the original input too (Y/N)			
    #  9: 2 Class Filter = Y * Filter for 2 classes (Y/N)			
    # 10: Attribute Variations = Y * Generate ARFFs with specific attribute + list of files (use Attributes file)			
    # 11: Run Weka = Y * Use the Classifier file
    # 12: Get Results = Y * Get the results
    # 13: Classification Precision = 0.7,0.75,0.8 * List with the target models

    lParams=["Params"] # list with calculation parameters
    nParams=14 # number of params in the calculation

    for line in linesParam:
        if len(line)>1: # not null lines
            if line[-1]=="\n" : line = line[:-1]
            if line[-1]=="\r" : line = line[:-1]
            Curr=line.split(",") # CSV file  (comma separated)
            if Curr[0]!="":
                for p in range(1,nParams+1): # get the params in a list in the order from the file
                    if Curr[0]==str(p):
                        lParams.append(Curr[2])

    # General LOG file for the initial input
    sLog="LOG_"+lParams[1]+".txt" # general log using the initial input file CSV/ARFF

    # write the parameters used
    fLog=open(sLog,"a")
    fLog.write(sHeader)
    fLog.close()
    
    #-------------------------------------------------------------
    # CONVERSION
    #-------------------------------------------------------------

    sOrig=lParams[1] # CSV / ARFF file
    sFiles=[] # list with files to process each step

    #****************
    # CSV to ARFF
    #****************
    if lParams[5]=="Y" or lParams[5]=="y":
        sCSV=lParams[1]
        sArff=sCSV[:-4]+".arff" # inputs *.csv

        if sOrig[-4:]==".csv": # if no CSV file, you neeed one!
            # Convert CSV to ARFF
            cmd = 'python wCsv2Arff.py %s %s' % (sCSV, sArff)
            print "*"*30
            print "CONVERSION CSV -> ARFF"
            print "*"*30
            print "==> "+cmd
            os.system(cmd)

            sOrig=sArff
            
        else:
            print " !!! You need to input a CSV file !!!"
            print " --> Please modify the Parameters file and try again."
            return      
    else:
        if sOrig[-5:]!=".arff": # if no ARFF file, you neeed one!
            print " !!! You need to convert the input file in an ARFF one in order to use Weka !!!"
            print " --> Please modify the Parameters file and try again."
            return

    # include the original file in the processing
    if lParams[8]=="Y":
        sFiles.append(sOrig)
        
    #****************
    # Normalisation
    #****************
    if lParams[6]=="Y" or lParams[6]=="y":
        sNormal="n"+sOrig[:-5]+".arff" # output with normalized data *.arff
        # Normalize ARFF -> nARFF
        cmd = 'python wNormaliz.py %s %s' % (sOrig, sNormal)
        print "*"*30
        print "NORMALIZATION"
        print "*"*30
        print "==> "+cmd
        os.system(cmd)

        # add the normalize input to processing
        sFiles.append(sNormal)

    #*******************
    # STANDARDIZACION
    #*******************
    if lParams[7]=="Y" or lParams[7]=="y":
        sStd="s"+sOrig[:-5]+".arff" # output with normalized data *.arff
        # Standardize ARFF -> nARFF
        cmd = 'python wStandardiz.py %s %s' % (sOrig, sStd)
        print "*"*30
        print "STANDARDIZATION"
        print "*"*30
        print "==> "+cmd
        os.system(cmd)

        # add the normalize input to processing
        sFiles.append(sStd)
        
    #-------------------------------------------------------------
    # CLASS FILTER
    #-------------------------------------------------------------
    if lParams[9]=="Y" or lParams[9]=="y":

        sFiles2=[] # list with the inputs by classes
        
        # list with the class pairs separated by ":", ex: EA-CONTROL:DCL_A-CONTROL
        lClasses=(lParams[10]).split(":")

        # for each input file: orig, normal, standard
        for iFile in sFiles:

            # for each pair of Classes
            for iClass in lClasses:
                # get the class pair (separated by "-"), ex. EA-CONTROL
                (Class1,Class2)=iClass.split("-")

                sClasses=iFile[:-5]+"_"+Class1+"-"+Class2+".arff" # inputs *.csv
                # Filter the classes
                cmd = 'python wFilter2Classes.py %s %s %s %s' % (iFile,Class1,Class2,sClasses)
                print "*"*30
                print "CLASS FILTER"
                print "*"*30
                print "==> "+cmd
                os.system(cmd)

                # add the normalize input to processing
                sFiles2.append(sClasses)

        sFiles=[] # the list of processing files is initiated
        sFiles=sFiles2 # the processing file list is replaced with the class pair filtered files!
    
    #-------------------------------------------------------------
    # ATTRIBUTE FILTER & Inputs
    #-------------------------------------------------------------
    if lParams[11]=="Y" or lParams[11]=="y":
        sAttFile=lParams[2] # list with combinations of attributes
                
        # for each input file: orig, normal, standard / filterd by class pairs
        for iFile in sFiles:
            sArffList="_Arffs_"+iFile[:-5]+".txt" # list with files to be processed by Weka
            # Attribute filter -> generate inputs files and the list
            cmd = 'python 1wGenerateInputs.py %s %s %s' % (iFile,sAttFile,sArffList)
            print "*"*30
            print "ATTRIBUTE FILTER & Generate inputs"
            print "*"*30
            print "==> "+cmd
            os.system(cmd)
    else:
        # if no atts filter, write the Arff list file with the initial files
        for iFile in sFiles:
            sArffList="_Arffs_"+iFile[:-5]+".txt" # list with files to be processed by Weka
            fArffList=open(sArffList,"w")
            fArffList.write(iFile)
            fArffList.close()
    
    #-------------------------------------------------------------
    # RUN Weka Classifiers
    #-------------------------------------------------------------
    if lParams[12]=="Y" or lParams[12]=="y":
        sClassifierList=lParams[3]
        sPathRes=lParams[4]
        
        for iFile in sFiles:
            sArffList="_Arffs_"+iFile[:-5]+".txt" # list with files to be processed by Weka
            cmd = 'python 2wRunCalcs.py %s %s %s ' % (sArffList,sClassifierList,sPathRes)
            print "*"*30
            print "RUNNING Weka"
            print "*"*30
            print "==> "+cmd
            os.system(cmd)

            #-------------------------------------------------------------
            # RESULTS (only if Run Weke before!!)
            #-------------------------------------------------------------
            if lParams[13]=="Y" or lParams[13]=="y":
                lPreciz=(lParams[14]).split(":") # list of precisions to get the results
                #for each precision one result file
                for iPrec in lPreciz: 
                    cmd = 'python 3wGetResults.py %s %s %s %s %s' % (sArffList,sClassifierList,sPathRes,iPrec,sLog)
                    print "*"*30
                    print "Getting RESULTS"
                    print "*"*30
                    print "==> "+cmd
                    os.system(cmd)
                
            
    endAt = datetime.datetime.now()
    sFooter=""
    sFooter=sFooter+"="*30+"\n"
    sFooter=sFooter+"\nJob ended at "+endAt.strftime("%Y-%m-%d %H:%M")+" ... \n"
    print sFooter

    # write the parameters used
    fLog=open(sLog,"a")
    fLog.write(sFooter)
    fLog.close()
    
    return

#====================================================================
# MAIN
#====================================================================

sRunParam="Params.csv" # CSV file
RunWekaClassif(sRunParam)



