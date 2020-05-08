import pandas as pd
import numpy as np

def read_cnv_file(fpath,sample_num):
    """
    Read a cnv file into a dataframe and create a new column for the sample
    number
    """
    
    df_out = pd.read_csv(fpath, sep = "\t")
    df_out["Sample#"] = sample_num
    return df_out


def filter_by_cnv(df, min_cnv_length, p_value_threshold):
    """
    Remove CNVs from a dataframe containing samples that fail to meet intial
    criteria
    """

    df = df.drop(df[df.Chrom == 'chrM'].index)
    df = df[(np.abs(df.Start - df.Stop) >= min_cnv_length) & (df.P_Value >= p_value_threshold)]
    return df

def find_common_cnvs(file1,file2, max_overlap):
    """
    Find CNVs common to both samples that meet qualifying criteria and create
    output file of results
    """

    common_cnvs = pd.DataFrame(columns = file1.columns)
    file2_byChrom = file2.groupby('Chrom')

    for i in range(len(file1)):
        file2_cnvs = file2_byChrom.get_group(file1.iloc[i].Chrom)
        file2_cnvs = file2_cnvs.loc[file2_cnvs.Type.isin(file1.iloc[[i]].Type)]
        file2_cnvs = file2_cnvs.loc[(np.abs(file2_cnvs.Start.subtract(file1.iloc[i].Start)) <= max_overlap)
            & (np.abs(file2_cnvs.Stop.subtract(file1.iloc[i].Stop)) <= max_overlap)]

        if(len(file2_cnvs) > 0):
            common_cnvs = pd.concat([common_cnvs, file1.iloc[[i]], file2_cnvs]).reset_index(drop = True)
            
    print(common_cnvs.info())
    return common_cnvs

def common_cnv_finder(fpath1,fpath2,file_out="common_cnvs.csv",min_cnv_length=1000, p_value_threshold=.90,
        max_overlap = 25):

    # Read datafiles
    df1 = read_cnv_file(fpath1,1)
    df2 = read_cnv_file(fpath2,2)

    # Do initial filtering
    df1 = filter_by_cnv(df1,min_cnv_length=min_cnv_length,p_value_threshold=p_value_threshold)
    df2 = filter_by_cnv(df2,min_cnv_length=min_cnv_length,p_value_threshold=p_value_threshold)

    common_cnvs = find_common_cnvs(df1,df2, max_overlap)
    common_cnvs_output = common_cnvs.to_csv(file_out)
    return common_cnvs

