import os
import sys
import pandas as pd
import numpy as np
import re

# change directory
os.chdir("/media/ganesh/RA/KSU/NGS/smallRNAseq/JeffUrilydation/TIE_")
print(os.getcwd())
m0 = pd.read_csv(sys.argv[1], sep="\t")
#print(m0.head())
#Drop NA null values
#m0 = m0.dropna(inplace=True)

# check for untemplated sequences
m0 = m0.rename(columns={m0.columns[0]: 'miRNA_ID'})
#print(m0.columns[0])
print(m0.head())
#m1 = m0[m0['miRNA_ID'].str.replace(".","", case=True, na=False)]
m0['miRNA_ID'] = m0['miRNA_ID'].str.replace(".","")
print(m0.head())
m1 = m0[m0['miRNA_ID'].str.contains("t$", case=True, na=False)] # & m0['miRNA_ID'].str.match("A|a|AA|Aa|aa")]
m1 = m1[(m1.iloc[:, 3:37] > 1).sum(axis=1) >= 10]
#m1 = m1[(m1[:, 3:36] > 0).all(axis=1)]
#print(m1.shape())
print(m1.head(20))
m2 = m0.head(1)
#m4 = m2.iloc[0,0]
#print(m4)
m3 = m1[(m1.iloc[:,3] >= m2.iloc[0,3]) | (m1.iloc[:,4] >= m2.iloc[0,4]) | (m1.iloc[:,5] >= m2.iloc[0,5]) | (m1.iloc[:,6] >= m2.iloc[0,6]) | (m1.iloc[:,7] >= m2.iloc[0,7]) |
        (m1.iloc[:,8] >= m2.iloc[0,8]) | (m1.iloc[:,9] >= m2.iloc[0,9]) | (m1.iloc[:,10] >= m2.iloc[0,10]) | (m1.iloc[:,11] >= m2.iloc[0,11]) | (m1.iloc[:,12] >= m2.iloc[0,12]) |
        (m1.iloc[:,13] >= m2.iloc[0,13]) | (m1.iloc[:,14] >= m2.iloc[0,14]) | (m1.iloc[:,15] >= m2.iloc[0,15]) | (m1.iloc[:,16] >= m2.iloc[0,16]) | (m1.iloc[:,17] >= m2.iloc[0,17]) |
        (m1.iloc[:,18] >= m2.iloc[0,18]) | (m1.iloc[:,19] >= m2.iloc[0,19]) | (m1.iloc[:,20] >= m2.iloc[0,20]) | (m1.iloc[:,21] >= m2.iloc[0,21]) | (m1.iloc[:,22] >= m2.iloc[0,22]) |
        (m1.iloc[:,23] >= m2.iloc[0,23]) | (m1.iloc[:,24] >= m2.iloc[0,24]) | (m1.iloc[:,25] >= m2.iloc[0,25]) | (m1.iloc[:,26] >= m2.iloc[0,26]) | (m1.iloc[:,27] >= m2.iloc[0,27]) |
        (m1.iloc[:,28] >= m2.iloc[0,28]) | (m1.iloc[:,29] >= m2.iloc[0,29]) | (m1.iloc[:,30] >= m2.iloc[0,30]) | (m1.iloc[:,31] >= m2.iloc[0,31]) | (m1.iloc[:,32] >= m2.iloc[0,32]) |
        (m1.iloc[:,33] >= m2.iloc[0,33]) | (m1.iloc[:,34] >= m2.iloc[0,34]) | (m1.iloc[:,35] >= m2.iloc[0,35]) | (m1.iloc[:,36] >= m2.iloc[0,36]) | (m1.iloc[:,37] >= m2.iloc[0,37])]
#print(m2.iloc[0,2])
print(m3)


#m2 = m2.transpose()
m4 = pd.concat([m2, m3], ignore_index=True)
#m1 = m1.append(m0.iloc[0,])
#print(m0.iloc[0,])
#print(m1.iloc[0,])
print(m4)
m4.to_csv(sys.argv[2], header=True, sep="\t", index=None)

