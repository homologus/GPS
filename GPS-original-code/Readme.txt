The R code in this directory first appeared in the following paper -

https://www.nature.com/articles/ncomms4513

"Geographic population structure analysis of worldwide human populations infers their 
biogeographical origins", Eran Elhaik et al., Nature Communications 5, Article number: 3513 (2014).

"This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/".


The files
---------
Putative ancestral pops\PAP.bed - plink files of the putative ancestral populations
Putative ancestral pops\PAP.bam - plink files of the putative ancestral populations
Putative ancestral pops\PAP.fam - plink files of the putative ancestral populations
Gen.csv - GEN file (includes genetic signture of reference populations)
Geo.csv - GEO file (includes geographical coordinates of reference populations)
data.csv - input file with test participants.
GPS_results.txt - partial output file for the data.csv.
GPS.R - the GPS scripts. It accepts the data.csv (with the fixed Gen.csv and Geo.csv) and outputs GPS_results.txt.


How to start?
-------------
You have an individual you with to test. First, you need to get its 9 gene pools.
Do the following:
1. Use Plink to merge the individual DNA with the PAP files.
2. Run admixture in a supervised mode using the PAP populations. This will give you P and Q files.
3. save the .Q file, there will be 9 columns there. Use it as the input to GPS.

The input file for GPS
-----------------------
The input structure of data.csv includes the sample ID, 9 admixture coefficients and group ID. 
The last column is for your own records and is not used by GPS for predictions.

SAMPLE_ID	Admixture1	Admixture2	Admixture3	Admixture4	Admixture5	Admixture6	Admixture7	Admixture8	Admixture9	GROUP_ID
GRC12076288	0.0221	0.5524	0	0.3492	0	0	0	0.0762	0	Abkhazians
GRC12076300	0.0228	0.5162	0.0069	0.3522	0	0	0	0.0921	0.0098	Abkhazians

Run GPS
-------
Run GPS.R with the input file and Reference population files.
GPS(directory_name="D:/GPS")

The output file
---------------
The output file looks like this:
GROUP_ID	#	SAMPLE_ID	Closest_population	Latitude	Longitude
Abkhazians	1	GRC12076288	Abkhazians_0	39.5307070554391	46.885015601252
Abkhazians	2	GRC12076300	Abkhazians_0	41.3675042534655	47.0145274096427
Abkhazians	3	GRC12076312	Ingush_3	42.9137139523191	39.0598623753912

