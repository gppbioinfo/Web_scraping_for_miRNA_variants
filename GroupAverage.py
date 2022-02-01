import sys
import os
import pandas as pd

def GetData(infile, outfile):
	m0 = pd.read_csv(infile, sep="\t", header=None, names=['featuretype','miR','Cancertype','Tissue','Score'], usecols=[0,1,2,3,4])
	print(m0.head())

	m1=m0.pivot(index=["featuretype","miR","Cancertype"], columns="Tissue",values="Score").fillna("0.0")
	m1.columns = m1.columns.str.replace(' ', '.', regex=True)
	m1.columns = m1.columns.str.replace('-', '.', regex=True)
	m1.columns = m1.columns.str.replace('\\.\\.\\.', '.', regex=True)
	m1.to_csv(outfile, index=True, header=True, sep='\t')

	#m1.plot(kind="bar")
	#print(pp)
	'''
	print(m0)
	m1 = (m0.assign(col=m0.groupby(['Cancertype','Tissue']).cumcount()+1)
		.set_index(['Cancertype','Tissue','col'])
		.unstack('col')
		.sort_index(level=(1,0), axis=1)
		)
	m1.columns = [f'{x}{y}' for x,y in m1.columns]
	print(m1)
	m1.to_csv(outfile, index=True, header=True, sep='\t')
	'''

GetData(sys.argv[1],sys.argv[2])