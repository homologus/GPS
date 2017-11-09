# GPS 

From - 

https://www.nature.com/articles/ncomms4513

"Geographic population structure analysis of worldwide human populations infers their
biogeographical origins", Eran Elhaik et al., Nature Communications 5, Article number: 3513 (2014).



## STEP3 - GPS

Create data.csv file with nine components of your genotype. The first field is some 
arbitrary ID, the next nine fields are numbers (more on them later) and the last field is another 
arbitrary ID.

Then open R and run - 

~~~~~~
> source("GPS.r")
~~~~~~

You will see GPS_results.txt file bein created. 


Where does one get those nine numbers from? For that, you need to run admixture, as 
described below.


## STEP2  - admixture

Run admixture on a merged bed file -

~~~~~~
admixture merge.bed 9
~~~~~~

It will run like this and produce output merge.9.P and merge.9.Q.  The 
last line of the merge.9.Q goes into the STEP3 above, but after the columns
are rearranged for different populations.


~~~~~~
****                   ADMIXTURE Version 1.3.0                  ****
****                    Copyright 2008-2015                     ****
****           David Alexander, Suyash Shringarpure,            ****
****                John  Novembre, Ken Lange                   ****
****                                                            ****
****                 Please cite our paper!                     ****
****   Information at www.genetics.ucla.edu/software/admixture  ****

Random seed: 43
Point estimation method: Block relaxation algorithm
Convergence acceleration algorithm: QuasiNewton, 3 secant conditions
Point estimation will terminate when objective function delta < 0.0001
Estimation of standard errors disabled; will compute point estimates only.
Size of G: 136x127906
Performing five EM steps to prime main algorithm
1 (EM)  Elapsed: 11.566 Loglikelihood: -1.99456e+07     (delta): 5.33545e+06
2 (EM)  Elapsed: 11.558 Loglikelihood: -1.95205e+07     (delta): 425130
3 (EM)  Elapsed: 11.494 Loglikelihood: -1.93882e+07     (delta): 132261
4 (EM)  Elapsed: 11.468 Loglikelihood: -1.92926e+07     (delta): 95561.3
5 (EM)  Elapsed: 11.526 Loglikelihood: -1.92091e+07     (delta): 83566.3
Initial loglikelihood: -1.92091e+07
Starting main algorithm
1 (QN/Block)    Elapsed: 26.027 Loglikelihood: -1.67348e+07     (delta): 2.47431e+06
2 (QN/Block)    Elapsed: 26.134 Loglikelihood: -1.60765e+07     (delta): 658244
3 (QN/Block)    Elapsed: 28.404 Loglikelihood: -1.58492e+07     (delta): 227346
4 (QN/Block)    Elapsed: 27.462 Loglikelihood: -1.57058e+07     (delta): 143416
5 (QN/Block)    Elapsed: 28.543 Loglikelihood: -1.56208e+07     (delta): 84991.2
6 (QN/Block)    Elapsed: 27.79  Loglikelihood: -1.55589e+07     (delta): 61826.6
7 (QN/Block)    Elapsed: 27.731 Loglikelihood: -1.54891e+07     (delta): 69883.4
8 (QN/Block)    Elapsed: 29.083 Loglikelihood: -1.54431e+07     (delta): 45997.5
9 (QN/Block)    Elapsed: 27.088 Loglikelihood: -1.54172e+07     (delta): 25894.5
10 (QN/Block)   Elapsed: 27.645 Loglikelihood: -1.53988e+07     (delta): 18413.6
11 (QN/Block)   Elapsed: 27.65  Loglikelihood: -1.53815e+07     (delta): 17262.3
12 (QN/Block)   Elapsed: 27.071 Loglikelihood: -1.53719e+07     (delta): 9630.6
13 (QN/Block)   Elapsed: 28.29  Loglikelihood: -1.53678e+07     (delta): 4067.83
14 (QN/Block)   Elapsed: 28.802 Loglikelihood: -1.53652e+07     (delta): 2567.53
15 (QN/Block)   Elapsed: 28.908 Loglikelihood: -1.53638e+07     (delta): 1422.45
16 (QN/Block)   Elapsed: 28.949 Loglikelihood: -1.53635e+07     (delta): 289.511
17 (QN/Block)   Elapsed: 28.977 Loglikelihood: -1.53635e+07     (delta): 1.81869
18 (QN/Block)   Elapsed: 27.068 Loglikelihood: -1.53635e+07     (delta): 0.00245512
19 (QN/Block)   Elapsed: 26.874 Loglikelihood: -1.53635e+07     (delta): 3.92459e-06
Summary:
Converged in 19 iterations (603.815 sec)
Loglikelihood: -15363516.794368
Fst divergences between estimated populations:
        Pop0    Pop1    Pop2    Pop3    Pop4    Pop5    Pop6    Pop7
Pop0
Pop1    0.178
Pop2    0.206   0.120
Pop3    0.309   0.248   0.254
Pop4    0.141   0.177   0.197   0.295
Pop5    0.179   0.193   0.193   0.286   0.148
Pop6    0.209   0.129   0.090   0.286   0.214   0.216
Pop7    0.214   0.180   0.208   0.294   0.183   0.177   0.227
Pop8    0.258   0.193   0.200   0.113   0.241   0.233   0.233   0.241
Writing output files.
~~~~~~



## STEP1 - plink

In this step, you need to merge your genotype file with the genotypes of 134 persons
provided by GPS. GPS-provided files are saved as PAP.bed, PAP.bim and PAP.fam.

~~~~~~
plink --noweb --bfile PAP --merge me.ped me.map --make-bed --out merge
~~~~~~


## STEP0 - cleaning genotype file



## Reference

Please cite -

https://www.nature.com/articles/ncomms4513

"Geographic population structure analysis of worldwide human populations infers their
biogeographical origins", Eran Elhaik et al., Nature Communications 5, Article number: 3513 (2014).


