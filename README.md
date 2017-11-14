# GPS 

From - 

https://www.nature.com/articles/ncomms4513

"Geographic population structure analysis of worldwide human populations infers their
biogeographical origins", Eran Elhaik et al., Nature Communications 5, Article number: 3513 (2014).


## STEP0 - converting genotype file

In this step, you need to convert genotype file to a format plink likes. Three small
Python scripts (clean.py, data.map.py, data.ped.py) in the folder STEP0-clean-genotype 
will perform this step.

Input of this step is the genotype file.
Output of this step is two files - me.ped and me.map.


## STEP1 - plink

In this step, you need to merge your genotype file (me.map, me.ped)  with the genotypes 
of 135 persons provided by GPS (PAP.bed, PAP.bim and PAP.fam). 

Go to STEP1-plink folder and run - 

~~~~
plink --noweb --bfile PAP --merge me.ped me.map --make-bed --out merge
~~~~

plink will create files merge.bed, merge.bim and merge.fam that you can use
in the following step.



## STEP2  - admixture


Go to STEP2-admixture folder and run admixture on the  merged bed file. Please note
that we added a merge.pop file with information on the 135 individuals.

~~~~~~
admixture merge.bed --supervise 9 -j12
~~~~~~

The output on the terminal for the admixture run is shown below. It will produce output 
files merge.9.P and merge.9.Q.  The 
last line of the merge.9.Q is used in the GPS algorithm on STEP3.


~~~~~~
****                   ADMIXTURE Version 1.3.0                  ****
****                    Copyright 2008-2015                     ****
****           David Alexander, Suyash Shringarpure,            ****
****                John  Novembre, Ken Lange                   ****
****                                                            ****
****                 Please cite our paper!                     ****
****   Information at www.genetics.ucla.edu/software/admixture  ****

Parallel execution requested.  Will use 12 threads.
Random seed: 43
Point estimation method: Block relaxation algorithm
Convergence acceleration algorithm: QuasiNewton, 3 secant conditions
Point estimation will terminate when objective function delta < 0.0001
Estimation of standard errors disabled; will compute point estimates only.
Supervised analysis mode.  Examining .pop file...
Size of G: 136x127906
Performing five EM steps to prime main algorithm
1 (EM)  Elapsed: 2.929  Loglikelihood: -1.53698e+07     (delta): 1.92504e+07
2 (EM)  Elapsed: 2.918  Loglikelihood: -1.53665e+07     (delta): 3317.52
3 (EM)  Elapsed: 2.968  Loglikelihood: -1.53664e+07     (delta): 118.587
4 (EM)  Elapsed: 2.902  Loglikelihood: -1.53663e+07     (delta): 53.444
5 (EM)  Elapsed: 2.905  Loglikelihood: -1.53663e+07     (delta): 46.6457
Initial loglikelihood: -1.53663e+07
Starting main algorithm
1 (QN/Block)    Elapsed: 7.451  Loglikelihood: -1.53636e+07     (delta): 2641.34
2 (QN/Block)    Elapsed: 7.421  Loglikelihood: -1.53635e+07     (delta): 112.888
3 (QN/Block)    Elapsed: 7.892  Loglikelihood: -1.53635e+07     (delta): 3.03972
4 (QN/Block)    Elapsed: 7.834  Loglikelihood: -1.53635e+07     (delta): 1.35304
5 (QN/Block)    Elapsed: 8.025  Loglikelihood: -1.53635e+07     (delta): 0.408226
6 (QN/Block)    Elapsed: 7.951  Loglikelihood: -1.53635e+07     (delta): 0.0207714
7 (QN/Block)    Elapsed: 7.864  Loglikelihood: -1.53635e+07     (delta): 5.81145e-07
Summary:
Converged in 7 iterations (70.171 sec)
Loglikelihood: -15363516.383274
Fst divergences between estimated populations:
        Pop0    Pop1    Pop2    Pop3    Pop4    Pop5    Pop6    Pop7
Pop0
Pop1    0.197
Pop2    0.295   0.254
Pop3    0.177   0.120   0.248
Pop4    0.141   0.206   0.309   0.178
Pop5    0.183   0.208   0.294   0.180   0.214
Pop6    0.148   0.193   0.286   0.193   0.179   0.177
Pop7    0.214   0.090   0.286   0.129   0.209   0.227   0.216
Pop8    0.241   0.200   0.113   0.193   0.258   0.241   0.233   0.233
Writing output files.
~~~~~~

The last line in the file has nine numbers, which will go as the input for the
next step. 


## STEP3 - GPS

Create data.csv file with nine components of your genotype. The first field is some
arbitrary ID, the next nine fields are numbers and the last field is another
arbitrary ID.

Then open R and run -

~~~~
> source("GPS.r")
~~~~

You will see GPS_results.txt file bein created.




## Reference

Please cite -

https://www.nature.com/articles/ncomms4513

"Geographic population structure analysis of worldwide human populations infers their
biogeographical origins", Eran Elhaik et al., Nature Communications 5, Article number: 3513 (2014).


