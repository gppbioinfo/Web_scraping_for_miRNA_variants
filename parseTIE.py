import sys

from bs4 import BeautifulSoup
import pandas
import requests
import urllib.request
import os
#print(sys.version)
#print(os.getcwd())
os.chdir(os.path.dirname(os.path.abspath(__file__)))

for pagenumber in range(1,141):
	#print(pagenumber)
	pgurl = "https://isomir.ccr.cancer.gov/browse/"+str(pagenumber)
	#print(pgurl)
	req = requests.get(pgurl)
	soup = BeautifulSoup(req.text, 'html.parser')

	dwlink = soup.find_all('a', class_='download_link', href=True)
	print(len(dwlink))
	if len(dwlink) == 0:
		continue
	#print(dwlink['href']) #https://isomir.ccr.cancer.gov/file/download/align/ACTTCTTTATATG-align.txt
	#print(dwlink[-1]['href'])
	#Download all files in directory
	DWlink="https://isomir.ccr.cancer.gov"+dwlink[-1]['href']
	print(DWlink)
	os.system('wget '+"https://isomir.ccr.cancer.gov"+dwlink[-1]['href'])

	#for finelLink in dwlink:
	#	downladLink = "https://isomir.ccr.cancer.gov"+finelLink['href']
		#print(downladLink)
		#urllib.request.urlretrieve(downladLink)

	'''
with open("/media/ganesh/RA/KSU/NGS/smallRNAseq/JeffUrilydation/TIE_/hsa-miR-1-5p.html") as fp:
	soup = BeautifulSoup(fp, 'html.parser')
	#print(soup)
	dwlink = soup.find_all('a', class_='download_link', href=True, limit=1)
	#print(dwlink['href'])
	for finelLink in dwlink:
		print(finelLink['href'])
	#print(dwlink)
	#ul_mir =  soup.find('a', class_='downlosad_link')
	#print(ul_mir)
	#for ull in ul_mir:
	#	dwlink = ull.a.text
	#	print(ull)
		#liname = ull.ul.text.split() #https://isomir.ccr.cancer.gov/file/download/all/ACTTCTTTATATG_2-4/hsa-miR-1-5p_hsa-mir-1-1_2-4_ACTTCTTTATATG_2-4.zip
		#print(f'{liname[2]}/{}')
	'''