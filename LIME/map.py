import pandas as pd
# from LIME.readData import *
# from LIME.TranscriptClass import *
from readData import *
from TranscriptClass import *
import os

# returns simple dictionary of transcript_id --> mapDict
# should write a function to use this to create transcript-centric table & event-centric table


def mapper(objectDictionary, rmats, type, outputpath):
    df = pd.DataFrame(columns = ["gene_id", "gene_name", "strand", "eventID", "event_coord", "c1_event_psi", "c2_event_psi", "event_dpsi", "transcript_id", "long-read_UJC", "lr_tpm_c1", "lr_tpm_c2"])
    print("starting to map for", type, "events")
    for lrUJC in objectDictionary.keys():
        tobj = objectDictionary[lrUJC]
        gene_id = tobj.gene_id # 
        gene_name = tobj.gene_name #
        transcript_id = tobj.transcript_id #
        tpm_c1 = tobj.tpm_WTC11
        tpm_c2 = tobj.tpm_EC
        for index, eventRow in rmats.iterrows():
            incJunction = str(eventRow["incJunction"])
            excJunction = str(eventRow["excJunction"])
            if incJunction in lrUJC:
                print("!+")
                # print(str(eventRow["incID"]), "coords", incJunction, "maps to", lrUJC)
                eventID = eventRow["incID"] #
                strand = eventRow["strand"] #
                coord = eventRow["incJunction"]
                c1_psi = eventRow["IncLevel1"]
                c2_psi = eventRow["IncLevel2"]
                dpsi = eventRow["IncLevelDifference"]
                row = [gene_id, gene_name, strand, eventID, coord, c1_psi, c2_psi, dpsi, transcript_id, lrUJC, tpm_c1, tpm_c2]
                df.loc[len(df)] = row
            elif excJunction in lrUJC:
                print("!-")
                # print(str(eventRow["excID"]), "coords", excJunction, "maps to", lrUJC)
                eventID = eventRow["excID"]
                strand = eventRow["strand"]
                coord = eventRow["excJunction"]
                c1_psi = eventRow["IncLevel1"]
                c2_psi = eventRow["IncLevel2"]
                dpsi = eventRow["IncLevelDifference"]
                row = [gene_id, gene_name, strand, eventID, coord, c1_psi, c2_psi, dpsi, transcript_id, lrUJC, tpm_c1, tpm_c2]
                df.loc[len(df)] = row
    # print(df)
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