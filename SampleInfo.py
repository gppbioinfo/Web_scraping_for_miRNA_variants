import glob
import sys
import os
import pandas as pd
import re
import numpy as np
import pathlib

#os.chdir("/media/ganesh/RA/KSU/NGS/smallRNAseq/JeffUrilydation/TIE_/")
wdDir = os.getcwd()
#filesiso = o{s.listdi}r("/media/ganesh/RA/KSU/NGS/smallRNAseq/JeffUrilydation/TIE_/filtereMiRs")
#print(filesiso)
def getFile(selFile, metFile, outFile): #, outfile):
    outFile = open(outFile, "w") or die;
    #Selected miRNA file
    Dname = selFile.split("-")
    print(f'{Dname[3]}')
    SeqmiR=[]
    SeqIso=[]
    with open(selFile, 'r') as useq:
        uline = useq.readlines()
        uline1 = useq.readlines()
        stu = uline[1].split("\t")
        SeqmiR.append(stu[0])
        #print(len(uline1))
        stu1 = uline[2].split("\t")
        SeqIso.append(stu1[0])
   # print(SeqmiR[0])
   # print(SeqIso[0])
    
    ### Load Cancer metaData
    metainfo = pd.read_csv(metFile, sep="\t")
    ##print(metainfo.head())
    cancelList = metainfo['dataset'].unique()
    #print(cancelList)
    metagroup = metainfo.groupby(['dataset', 'sample_type'])['renamed'].apply(list).to_dict()
    #print(metagroup)

    for key, value in dict.items(metagroup):
        #print(f"{key} \t {value}")
        #print(key[0])
        FolFile=glob.glob("/media/ganesh/RA/KSU/NGS/smallRNAseq/JeffUrilydation/TIE_/"+Dname[3]+"*/*/"+Dname[0]+"-"+Dname[1]+"-"+Dname[2]+"-"+Dname[3]+"_"+key[0]+"_align.txt", recursive=True)
        #print(FolFile)

        # Cancer specific results
        MetaCan = {}

        #Loading cancer specific file
        if FolFile:
            #print("File is exists!")
            isomirs = pd.read_csv(FolFile[0], sep="\t")
            isomirs = isomirs.rename(columns={isomirs.columns[0]: 'miRNA_ID'})
            isomirs['miRNA_ID'] = isomirs['miRNA_ID'].str.replace(".","", regex=True)
            isomirs['miRNA_ID'] = isomirs['miRNA_ID'].str.replace(" ","", regex=True)
            #print(isomirs['miRNA_ID'])
            isomirs.columns = isomirs.columns.str.replace(' ', '', regex=True)
            isomirs1 = isomirs[isomirs['miRNA_ID'] == SeqmiR[0].strip()]
            #print(f"{SeqIso[0]}\t{isomirs['miRNA_ID']}")
            isoSeqU = SeqIso[0].strip().upper()
            isomirs2 = isomirs[isomirs['miRNA_ID'] == SeqIso[0]]
            #isomirs2 = isomirs[isomirs['miRNA_ID'].str.lowe.fullmatch(pat=SeqmiR[0].lower(), case=False, na=None)]
            #print(isomirs2.head())
            #print(isomirs1.head())
           

            ## Checking through tissue types
            Tissutype=["Additional Metastatic","Additional - New Primary","Blood Derived Cancer - Bone Marrow Post-treatment","Cell Lines","Control Analyte","Metastatic","Primary Blood Derived Cancer - Bone Marrow","Primary Blood Derived Cancer - Peripheral Blood","Primary Tumor","Recurrent Blood Derived Cancer - Bone Marrow","Recurrent Blood Derived Cancer - Peripheral Blood","Recurrent Tumor","sample_type","Solid Tissue Normal"]
            for tss in Tissutype:
                if tss == str(key[1]):
                    #if re.search(r'Solid', str(key[1])):
                    ##print(f"Columns for => {key[0]}\t {key[1]} \t{value}")
                    ##print(type(value))
                    #isoCon = isomirs1[isomirs1.columns & value]
                    #for miRNA 
                    isoCon = isomirs1[np.intersect1d(isomirs1.columns, value)]
                    isoConmn = isoCon.mean(axis=1)
                    #print(isoCon)
                    if len(isoConmn):
                        #print("True")
                        #print(isoConmn.to_string().split(' ')[4])
                        outFile.write(f"miRNA\t{Dname[0]}-{Dname[1]}-{Dname[2]}\t{key[0]}\t{key[1]}\t{isoConmn.to_string().split(' ')[4]}\n")
                    else:
                        continue
                    

                    #for isomiR
                    isoConiso = isomirs2[np.intersect1d(isomirs2.columns, value)]
                    #isoConiso= isomirs2[isomirs2.columns & value]
                    #print(isoConiso)                    
                    isoConmniso = isoConiso.mean(axis=1)
                    #print(isoConmniso)
                    #isoCon = isomirs[np.intersect1d(isomirs.columns, value)]
                    #print(isomirs.columns)
                    #isoCon = isomirs[[c for c in isomirs.columns if c in value]]
                    if len(isoConmniso):                        
                        #print(isoConmniso)
                        outFile.write(f"isomiR\t{Dname[0]}-{Dname[1]}-{Dname[2]}\t{key[0]}\t{key[1]}\t{isoConmniso.to_string().split(' ')[4]}\n")
                    else:
                        #print("empty")
                        continue
                    #FinExp[key[1]] = isoConm
                                     
                   
        else:
            continue
    outFile.close()

getFile(sys.argv[1], sys.argv[2], sys.argv[3])
