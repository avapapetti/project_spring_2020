import pytest
import pandas as pd
import numpy as np
import random
from pathlib import Path

# import core functions as the alias ccf for convenience
import common_cnv_finder.core_functions as ccf

# Define and read some input files contained in the data subdirectory of tests
test_data_dir = Path(__file__).parent / "Data"
file1 = pd.read_csv(test_data_dir / "Test_Sample1.cnv.csv", sep = "\t")
file2 = pd.read_csv(test_data_dir / "Test_Sample2.cnv.csv", sep = "\t")

file1['Sample#'] = 1
file2['Sample#'] = 2

file3 = pd.read_csv(test_data_dir / "expected_cnvs.csv", sep = "\t")


def test_read_cnv_file():
    expected = file3.columns
    result = ccf.read_cnv_file(test_data_dir / "Test_Sample1.cnv.csv",1)
    assert expected.equals(result.columns)

    
def test_filter_by_cnv():
    expected = file1
    expected = expected.loc[expected.Chrom != 'chrM']
    expected['CNV_Length'] = np.abs(file1.Start - file1.Stop)
    expected = expected.loc[expected.CNV_Length >= 1000]
    result = ccf.filter_by_cnv(file1, min_cnv_length = 1000, p_value_threshold = .90)
    
    assert 'chrM' not in result.Chrom
    assert expected.CNV_Length.min() >= 1000
    pd.testing.assert_frame_equal(result, expected.drop(columns = ['CNV_Length']), check_dtype=False) 


def test_common_cnv_finder():
    expected = file3
    result = ccf.common_cnv_finder(test_data_dir / "Test_Sample1.cnv.csv",test_data_dir /
        "Test_Sample2.cnv.csv",file_out="test_output.csv", min_cnv_length = 1000,
        p_value_threshold = 0.90, max_overlap = 25)
    
    pd.testing.assert_frame_equal(result, expected, check_dtype=False)    
    

def test_find_common_cnvs():
    expected = file3
    result = ccf.find_common_cnvs(ccf.filter_by_cnv(file1, min_cnv_length = 1000, p_value_threshold = .90),
        ccf.filter_by_cnv(file2, min_cnv_length = 1000, p_value_threshold = .90), max_overlap = 25)
    pd.testing.assert_frame_equal(result, expected, check_dtype=False)