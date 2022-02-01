#!/bin/sh
###############################################
# All codes run into python3 or later version.
###############################################

# Downloading miRNA specific all cancer condition data including sequence and expression.

python parseTIE.py

# Checking uridylated isomiRs sequences, comparing expression with canonical miRNA
 
# Input folder name with metafile for each miRNA

for inputFile in $(ls */*-align.txt)

python CheckUnTempExp.py $inputFile $outputFile

# Taking input from above script and checking samplewise expression and calculate average for each isomiRs sequences and their miRNA

python SampleInfo.py $outputFile ../public_metadata.txt $outputFile.Cancer_meantissue.txt

python GroupAverage.py $outputFile.Cancer_meantissue.txt $outputFile.Cancer_meantissueFinal.txt

# Plot expression for each miRNA 

Rscript plotChart2.R

done

