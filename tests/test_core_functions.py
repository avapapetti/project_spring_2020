import pytest
import pandas as pd
import numpy as np
import random
from pathlib import Path

# import core functions as the alias ccf for convenience
import common_cnv_finder.core_functions as ccf

# Define and read some input files contained in the data subdirectory of tests
test_data_dir = Path(__file__).parent / "data"
file1 = pd.read_csv(test_data_dir / "SL88823_20180802.cnv.csv", sep = "\t")
file2 = pd.read_csv(test_data_dir / "SL88824_20180802.cnv.csv", sep = "\t")

file1['Sample#'] = 1
file2['Sample#'] = 2


def test_common_csv_finder():
    # define an expected result:
    expected = ... # you will need to decide what you expect and code it here
    # call common_csv_finder, you may have to subset it or something like that
    # to make it easier to test. Then just write a basic sanity check. If you
    # can, think of a test for false positives and false negatives
    result = ccf.common_csv_finder(file1,file2,file_out="test_output.csv")
    processed_result = ... # do some subsetting or whatever
    assert processed_result == expected



# def test_cnv_drop():
#     file1_new = file1.drop(file1[file1.Chrom == 'chrM'].index)
#     chroms = file1_new.Chrom.unique()
#     assert 'chrM' not in chroms

# test_cnv_drop()

# def test_cnv_filtering():
#     test_min_cnv_length = 1000
#     test_p_value = .90
    
#     file2_filtered1 = file2[(np.abs(file2.Start - file2.Stop) >= test_min_cnv_length) & (file2.P_Value >= test_p_value)]

#     file2_filtered2 = file2.copy()
#     file2_filtered2['CNV_Length'] = np.abs(file2.Start - file2.Stop)
#     file2_filtered2 = file2_filtered2[file2_filtered2.CNV_Length >= test_min_cnv_length]
#     file2_filtered2 = file2_filtered2[file2_filtered2.P_Value >= test_p_value]
  
#     assert file2_filtered2.CNV_Length.min() >= test_min_cnv_length
#     assert file2_filtered2.P_Value.min() >= test_p_value
#     assert file2_filtered1.equals(file2_filtered2.drop(['CNV_Length'], axis = 1))
    

# test_cnv_filtering()

# def test_byChrom():
#     file2_byChrom = file2.groupby('Chrom')
#     assert file2_byChrom.ngroups == file2.Chrom.nunique()

# test_byChrom()

# def test_get_group():
#     file1_random_cnv = file1.iloc[random.randrange(len(file1)-1)]
#     file2_byChrom = file2.groupby('Chrom')
#     test_file2_cnvs = file2_byChrom.get_group(file1_random_cnv.Chrom)
    
#     assert test_file2_cnvs.Chrom.unique()[0] == file1_random_cnv.Chrom

# test_get_group()

# def test_type_match():
#     file1_cnv_del = file1[file1.Type == 'DELETION']
#     test_file2_cnvs = file2.loc[file2.Type.isin(file1_cnv_del.Type)]
#     assert file1_cnv_del.Type.unique() == test_file2_cnvs.Type.unique()

# test_type()

# def test_overlap():
#     test_min_overlap = 25
#     test_file2_cnvs2 = file2.copy()
    
#     file1_random_cnv = file1.iloc[random.randrange(len(file1)-1)]
#     test_file2_cnvs2['Start_Overlap'] = np.abs(file2.Start.subtract(file1_random_cnv.Start))
#     test_file2_cnvs2['Stop_Overlap'] = np.abs(file2.Stop.subtract(file1_random_cnv.Stop))
#     test_file2_cnvs2 = test_file2_cnvs2.loc[(test_file2_cnvs2.Start_Overlap <= test_min_overlap) & 
#         (test_file2_cnvs2.Stop_Overlap <= test_min_overlap)]
    
#     if(len(test_file2_cnvs2) > 0):
#         assert test_file2_cnvs2.Start_Overlap.max() <= test_min_overlap
#         assert test_file2_cnvs2.Stop_Overlap.max() <= test_min_overlap

# test_overlap()