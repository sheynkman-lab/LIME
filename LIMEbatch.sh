#!/bin/bash

#SBATCH -J LIMEbatch1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --mem=64Gb
#SBATCH -t 5:00:00
#SBATCH -p standard
#SBATCH -A sheynkman_lab
#SBATCH -o lime.out
#SBATCH -e lime.err

pip install --editable .
lime --condition1 WTC11 --condition2 EC --rmats_out_folder /project/sheynkman/projects/shay_thesis/input-data/01_ips-s1s2_rmats-out_input --type JC --c1_quantcol rep1ENCSR507JOF --c2_quantcol rep1ENCSR148IIG --c1annot /project/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/01_annotation/WTC11-1.gtf --c1quant /project/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/02_quantification/WTC11-1.tsv --c2quant /project/sheynkman/projects/shay_thesis/input-data/02_long-read-EC-WTC11-1_input/02_quantification/EC.tsv --outputpath /project/sheynkman/projects/shay_thesis/output/batchtest