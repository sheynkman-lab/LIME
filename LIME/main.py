import pandas as pd
from pathlib import Path
import click
from LIME.readData import *
from LIME.map import *
from gtfparse import read_gtf


@click.command()
    
@click.option('--condition1', help = "specify name of condition 1")
@click.option('--condition2', help = "specify name of condition 2")
@click.option('--rmats_out_folder', type = click.Path(exists = True, path_type=Path), help = "Path to output of rMATS")
@click.option('-t', '--type', help = "specify whether using JC or JCEC read-based data from rMATS output")
@click.option('--c1_quantcol', help = 'name of condition 1 quantification.tsv column corresponding to condition 1 counts')
@click.option('--c2_quantcol', help = 'name of condition 2 quantification.tsv column corresponding to condition 2 counts')
@click.option('--c1annot', type = click.Path(exists = True, path_type=Path), help = "Path to long read annotation GTF for condition 1")
#@click.option('--c2annot', required = True, type = click.Path(exists = True, path_type=Path), help = "Path to long read annotation GTF for condition 2")
@click.option('--c1quant', type = click.Path(exists = True, path_type=Path), help = "Path to long read quantification TSV for condition 1")
@click.option('--c2quant', type = click.Path(exists = True, path_type=Path), help = "Path to long read quantification TSV for condition 2")
@click.option('-o', '--outputpath', type = click.Path(exists = True, path_type = Path), help = "Path to output folder. Default '.'")

def cli(condition1: str, condition2: str, rmats_out_folder: Path, type: str, c1_quantcol: str, c2_quantcol: str, c1annot: Path, c1quant: Path, c2quant: Path, outputpath: Path):
    click.echo('')
    tmppath = outputpath + "/tmp"
    outpath = outputpath + "/out"
    if not os.path.exists(tmppath):
        tmpfolder = os.makedirs(tmppath)
    outfolder = os.mkdir(outpath)
    
    # intermediate = str(outputpath) + "/int"
    # if not os.path.exists(intermediate):
    #     os.makedirs(intermediate)
        
    se = loadSE(rmats_out_folder, type, str(tmppath))
    mxe = loadMXE(rmats_out_folder, type, str(tmppath))
    a3ss = loadA3SS(rmats_out_folder, type, str(tmppath))
    a5ss = loadA5SS(rmats_out_folder, type, str(tmppath))

    lrannot = loadLRannot(c1annot)
    lrquant_c1 = loadLRquant(c1quant, c1_quantcol, condition1)
    lrquant_c2 = loadLRquant(c2quant, c2_quantcol, condition2)

    lr_alldata = mergeAnnotQuants(lrannot, lrquant_c1, lrquant_c2)
    objectDictionary = getLRDict(lr_alldata)
    seMap = mapper(objectDictionary, se, "se", (str(outfolder) + "/se_map.csv"))
    mxeMap = mapper(objectDictionary, mxe, "mxe", (str(outfolder) + "/mxe_map.csv"))
    a3ssMap = mapper(objectDictionary, a3ss, "a3ss", (str(outfolder) + "/a3ss_map.csv"))
    a5ssMap = mapper(objectDictionary, a5ss, "a5ss", (str(outfolder) + "/a5ss_map.csv"))
    # print(df)
    # outputfile = str(outputpath) + "/mappingtable.csv"
    # df.to_csv(outputfile, index = False)