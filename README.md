# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)

Common CNV Finder is a Python tool that finds similar copy number variant (CNV) regions found within two different genomic datasets. It accepts these datasets as CSV files with columns ['Chrom', 'Start', 'Stop', 'Type', 'P_Value'].

Common CNV Finder removes CNVs based on specific parameters, such as:
    1. User-defined minimum CNV length
    2. User-defined P-value threshold
    3. Inaccurate CNV calls located on 'chrM'.
    
It then generates an output file containing the CNVs common to both samples based on additional criteria:
     1. CNV located on same chromosome
     2. CNV is of same type (Deletion or Duplication)
     3. CNV start sites are within a user-defined distance of each other (i.e. 25 bp)
     4. CNV stop sites are within a user-defined distance of each other.
     
 The output file has the same format as the input and can be exported as a CSV.
