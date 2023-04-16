import pandas as pd
from pathlib import Path
# from LIME.readData import *
# from LIME.map import *
from readData import *
from map import *
from gtfparse import read_gtf

candidates = ["PECAM1", "CD44", "VASH1"]

def rMATSload(rmats_out_folder, type, srpath):
    type = "JCEC"
    se = loadSE(rmats_out_folder, type, srpath)
    print("se done")
    mxe = loadMXE(rmats_out_folder, type, srpath)
    print("mxe done")
    a3ss = loadA3SS(rmats_out_folder, type, srpath)
    print("a3ss done")
    a5ss = loadA5SS(rmats_out_folder, type, srpath)
    print("a5ss done")
    return

def loadForCandidates():
    print("Beginning to run code... ")
    print("\nLoading rMATS events...")
    ## change this to be WTC11-1-annot/
    master_outpath = "/Volumes/sheynkman/projects/shay_thesis/output/candidate_mapping/EC-annot/"
    master_annotpath = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/01_annotation/"
    master_quantpath = "/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/02_quantification/"
    # only needed to do this once!
    # rmats_out_folder = "/Volumes/sheynkman/projects/shay_thesis/input-data/01_ips-s1s2_rmats-out_input"
    # rMATSload(rmats_out_folder, "JCEC", master_outpath)

    c1_quantcol = "rep1ENCSR507JOF"
    c2_quantcol = "rep1ENCSR148IIG"
    print("\nDefined master_outpath")
    for candidate in candidates:
        #Making a directory for each candidate
        c_outpath = master_outpath + candidate + "/"
        print("\n\nChecking if", candidate, "outpath exists... ")
        if not os.path.exists(c_outpath):
            print("Outpath for", candidate, "doesn't exist yet... ")
            os.mkdir(c_outpath)
            print("Now outpath for", candidate, "exists.")
        elif os.path.exists(c_outpath):
            print("Outpath for", candidate, "exists already.")
        print("Outpaths are successfully defined.")

        #Defining paths for annotation and quantification
        c_annotpath = master_annotpath + "EC-" + candidate + ".gtf"
        c_quantpath_1 = master_quantpath + "WTC11-1-" + candidate + ".tsv"
        c_quantpath_2 = master_quantpath + "EC-" + candidate + ".tsv"
        outputfile = c_outpath + "merge-" + candidate + ".csv"
        print(c_annotpath, "\n", c_quantpath_1, "\n", c_quantpath_2, "\n", outputfile)
        
        print("Loading LR annot from ", c_annotpath, "...")
        lrannot = loadLRannot(c_annotpath)
        print("Loading LRquant_c1 from", c_quantpath_1, "...")
        lrquant_c1 = loadLRquant(c_quantpath_1, c1_quantcol, "WTC11-1")
        print("Loading LRquant_c2 from", c_quantpath_2, "...")
        lrquant_c2 = loadLRquant(c_quantpath_2, c2_quantcol, "EC")
        print("merging all data and storing to", outputfile, "...")
        lr_alldata = mergeAnnotQuants(lrannot, lrquant_c1, lrquant_c2)
        print("Storing now...")
        lr_alldata.to_csv(outputfile, index = False)
    

loadForCandidates()

def mapCandidateData():
    #change this to be WTC11-1-annot
    master_inpath = "/Volumes/sheynkman/projects/shay_thesis/output/candidate_mapping/EC-annot/"
    for candidate in candidates:
        c_outpath = master_inpath + candidate
        maqpath = c_outpath + "/merge-" + candidate + ".csv"
        print(c_outpath, "\n", maqpath) 
        mergeannotquants = pd.read_csv(maqpath)

        # cdh5_annot = loadLRannot("/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/01_annotation/EC-CDH5.gtf")
        # cdh5_quant = loadLRquant("/Volumes/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/02_quantification/EC-CDH5.tsv", count_column_name = "rep1ENCSR148IIG", condition_name = "EC")
        # mergeannotquants = mergeOneAnnotQuant(cdh5_annot, cdh5_quant)
        # mergeannotquants['tpm_WTC11-1'] = 0
        
        objectDict = getLRDict(mergeannotquants)
        sepath = master_inpath + "SE.csv"
        mxepath = master_inpath + "MXE.csv"
        a3sspath = master_inpath + "A3SS.csv"
        a5sspath = master_inpath + "A5SS.csv"

        se = pd.read_csv(sepath)
        mxe = pd.read_csv(mxepath)
        a3ss = pd.read_csv(a3sspath)
        a5ss = pd.read_csv(a5sspath)
        print("starting to map for gene", candidate)
        mapper(objectDict, se, "se", c_outpath)
        mapper(objectDict, mxe, "mxe", c_outpath)
        mapper(objectDict, a3ss, "a3ss", c_outpath)
        mapper(objectDict, a5ss, "a5ss", c_outpath)
        
mapCandidateData()