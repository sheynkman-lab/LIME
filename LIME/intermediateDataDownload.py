import pandas as pd
from pathlib import Path
from LIME.readData import *
from LIME.map import *
from gtfparse import read_gtf
def makeIntData():
    rmats_out_folder = "/Volumes/sheynkman/projects/shay_thesis/input-data/01_ips-s1s2_rmats-out_input"
    # c1annot = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/01_annotation/WTC11-1.gtf"
    c1annot = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/BIO334-lr-input/EC_candidates.gtf"
    c1quant = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/BIO334-lr-input/WTC11-1_candidates.tsv"
    c2quant = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/BIO334-lr-input/EC_candidates.tsv"
    c1_quantcol = "rep1ENCSR507JOF"
    c2_quantcol = "rep1ENCSR148IIG"
    condition1 = "WTC11"
    condition2 = "EC"
    output = "/Volumes/sheynkman/projects/shay_thesis/BIO334_output"
    print("defining tmppath")
    tmppath = output + "/tmp"
    print("defining outpath")
    outpath = output + "/out"
    print("defining srpath")
    srpath = tmppath + "/SR_data"
    print("defining lrpath")
    lrpath = tmppath + "/LR_data"
    print("defining mappath")
    mappath = outpath + "/mapdata"
    if not os.path.exists(tmppath):
        print("tmppath doens't exist yet")
        os.mkdir(tmppath)
        os.mkdir(srpath)
        os.mkdir(lrpath)
        print("now tmppath exists")
    if not os.path.exists(outpath):
        print("outpath doesn't exist yet")
        os.mkdir(outpath)
        os.mkdir(mappath)
        print("now outpath exists")
    
    type = "JC"
    se = loadSE(rmats_out_folder, type, srpath)
    print("se done")
    mxe = loadMXE(rmats_out_folder, type, srpath)
    print("mxe done")
    a3ss = loadA3SS(rmats_out_folder, type, srpath)
    print("a3ss done")
    a5ss = loadA5SS(rmats_out_folder, type, srpath)
    print("a5ss done")
    lrannot = loadLRannot(c1annot)

    os.mkdir(tmppath + "/rMATSoutput")

    print("lr annot done")
    lrquant_c1 = loadLRquant(c1quant, c1_quantcol, condition1)
    print("lrquant1 done")
    lrquant_c2 = loadLRquant(c2quant, c2_quantcol, condition2)
    print("lrquant2 done")
    print("merging")
    lr_alldata = mergeAnnotQuants(lrannot, lrquant_c1, lrquant_c2)
    print("SE, MXE, A3SS, A5SS datasets in tmp")
    print("Now saving tmp output for LR data in TMP")
    outputfilelr = lrpath + "/merge.csv"
    lr_alldata.to_csv(outputfilelr, index = False)

    # outputfilelr = "/Volumes/sheynkman/projects/shay_thesis/output/01_tmp/02_long-read-pandas/merge.csv"
    # lr_alldata.to_csv(outputfilelr, index = False)
    # mergeannotquants_LINC = pd.read_csv("/Volumes/sheynkman/projects/shay_thesis/output/01_tmp/02_long-read-pandas/mnzpLINC01128.csv")
    # SELINC = pd.read_csv("/Volumes/sheynkman/projects/shay_thesis/output/01_tmp/01_short-read_pandas/SELINC.csv")
    # objectDictionary = getLRDict(mergeannotquants_LINC)
    # mapper(objectDictionary, SELINC, outputpath = "/Volumes/sheynkman/projects/shay_thesis/output")
    return

def mapIntData(mergeannotquants_path, sr_intpath, mappath):
    print("reading MAQ")
    mergeannotquants = pd.read_csv(mergeannotquants_path)
    objectDictionary = getLRDict(mergeannotquants)
    print("MAQ read")
    print("setting paths")
    sepath = sr_intpath + "/candidate_srdata/SE_candidates.csv"
    mxepath = sr_intpath + "/candidate_srdata/MXE_candidates.csv"
    a3sspath = sr_intpath + "/candidate_srdata/A3SS_candidates.csv"
    a5sspath = sr_intpath + "/candidate_srdata/A5SS_candidates.csv"

    print("reading se")
    se = pd.read_csv(sepath)
    print("reading mxe")
    mxe = pd.read_csv(mxepath)
    print('reading a3')
    a3ss = pd.read_csv(a3sspath)
    print('reading a5')
    a5ss = pd.read_csv(a5sspath)

    mapper(objectDictionary, se, "se", mappath)
    mapper(objectDictionary, mxe, "mxe", mappath)
    mapper(objectDictionary, a3ss, "a3ss", mappath)
    mapper(objectDictionary, a5ss, "a5ss", mappath)
    print("done")


mapIntData("/Volumes/sheynkman/projects/shay_thesis/BIO334_output/tmp/LR_data/merge.csv", "/Volumes/sheynkman/projects/shay_thesis/BIO334_output/tmp/SR_data", "/Volumes/sheynkman/projects/shay_thesis/BIO334_output/out/mapdata")