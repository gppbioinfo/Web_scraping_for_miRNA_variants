#!/bin/sh



for ii in $(ls *-align.txt_uridylated.txt )
do

echo $ii

python3.8 SampleInfo.py $ii ../public_metadata.txt $ii\.Cancer_meantissue.txt

python3.8 GroupAverage.py $ii\.Cancer_meantissue.txt $ii\.Cancer_meantissueFinal.txt

done
