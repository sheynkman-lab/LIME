import pandas as pd
from LIME.readData import *
from LIME.TranscriptClass import *
import os

# returns simple dictionary of transcript_id --> mapDict
# should write a function to use this to create transcript-centric table & event-centric table


def mapper(objectDictionary, rmats, type, outputpath):
    print("Running mapping algorithm on", type, "events")
    df = pd.DataFrame(columns = ["gene_id", "gene_name", "strand", "eventID", "event_coord", "c1_event_psi", "c2_event_psi", "event_dpsi", "transcript_id", "long-read_UJC", "lr_tpm_c1", "lr_tpm_c2"])
    for lrUJC in objectDictionary.keys():
        tobj = objectDictionary[lrUJC]
        gene_id = tobj.gene_id # 
        gene_name = tobj.gene_name #
        transcript_id = tobj.transcript_id #
        tpm_c1 = tobj.tpm_WTC11
        tpm_c2 = tobj.tpm_EC
        for index, eventRow in rmats.iterrows():
            if str(eventRow["incJunction"]) in lrUJC:
                # print("found event", str(eventRow["incID"]), "in", lrUJC)
                eventID = eventRow["incID"] #
                strand = eventRow["strand"] #
                coord = eventRow["incJunction"]
                c1_psi = eventRow["IncLevel1"]
                c2_psi = eventRow["IncLevel2"]
                dpsi = eventRow["IncLevelDifference"]
                row = [gene_id, gene_name, strand, eventID, coord, c1_psi, c2_psi, dpsi, transcript_id, lrUJC, tpm_c1, tpm_c2]
                df.loc[len(df)] = row
                # print(row)
            if str(eventRow["excJunction"] in lrUJC):
                # print("found event", str(eventRow["excID"]), "in", lrUJC)
                eventID = eventRow["excID"]
                strand = eventRow["strand"]
                coord = eventRow["excJunction"]
                c1_psi = eventRow["IncLevel1"]
                c2_psi = eventRow["IncLevel2"]
                dpsi = eventRow["IncLevelDifference"]
                row = [gene_id, gene_name, strand, eventID, coord, c1_psi, c2_psi, dpsi, transcript_id, lrUJC, tpm_c1, tpm_c2]
                df.loc[len(df)] = row
                # print(row)
    print(df)
    # df.to_csv("/Volumes/sheynkman/projects/shay_thesis/output/mapping_LINC01128_2.csv", index = False)
    # outputfile = str(outputpath) + "/mapping_LINC01128.csv"
    # df.to_csv(outputfile, index = False)
    write_map_output(df, output_folder_path = outputpath, type = type)
    return df

def write_map_output(mapperOutputDF, output_folder_path, type):
    filepath = ""
    type = type.lower()
    if type == "se":
        filepath = str(output_folder_path) + "/se_map.csv"
    elif type == "mxe":
        filepath = str(output_folder_path) + "/mxe_map.csv"
    elif type == "a3ss":
        filepath = str(output_folder_path) + "/a3ss_map.csv"
    elif type == "a5ss":
        filepath = str(output_folder_path) + "/a5ss_map.csv"
    else:
        filepath = "ERROR! INCORRECT EVENT TYPE ID"
        print("unusable type found.")
        return
    mapperOutputDF.to_csv(filepath, index = False)
    print("output printed to", filepath)
    return 

# mergeannotquants_LINC = pd.read_csv("/Volumes/sheynkman/projects/shay_thesis/output/01_tmp/02_long-read-pandas/mnzpLINC01128.csv")
# objectDictionary = getLRDict(mergeannotquants_LINC)
# SELINC = pd.read_csv("/Volumes/sheynkman/projects/shay_thesis/output/01_tmp/01_short-read_pandas/LINC_data/SELINC.csv")
# MXELINC = pd.read_csv("/Volumes/sheynkman/projects/shay_thesis/output/01_tmp/01_short-read_pandas/LINC_data/MXELINC.csv")
# seMap = mapper(objectDictionary, SELINC, "se", outputpath = "/Volumes/sheynkman/projects/shay_thesis/output")
# mxeMap = mapper(objectDictionary, MXELINC, "mxe", outputpath = "/Volumes/sheynkman/projects/shay_thesis/output/MXE_map_LINC.csv")
# seMap.to_csv("/Volumes/sheynkman/projects/shay_thesis/output/SE_map_LINC.csv", index = False)
# mxeMap.to_csv("/Volumes/sheynkman/projects/shay_thesis/output/MXE_map_LINC.csv", index = False)
