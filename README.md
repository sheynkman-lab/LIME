# Welcome to LIME (Long-read Isoform Mapping to (alternative splicing) Events)
**Contents**

- [Data](#data)
- [Instructions](#instructions)
- [Output](#output)
## Data
### Files and folders needed to run LIME** 
#### rMATS output
- Output folder of rMATS [Shen et al, 2014](https://pubmed.ncbi.nlm.nih.gov/25480548/)
- Used files: [SE, MXE, A3SS, A5SS].MATS.[JC or JCEC].txt
Note: these files are automatically named by rMATS. Renaming these files will result in file identification errors. **Please do not rename or relocate any rMATS output files, and instead provide a path to the folder. Path should not contain a slash at the end; see run.sh for example code**

#### Long-read RNA sequencing data corresponding to conditions compared in rMATS
- This pipeline is developed using open source Pacific Biosciences long-read RNA sequencing data. We downloaded the call sets from the ENCODE portal [Sloan et al. 2016](https://www.encodeproject.org/) with the following identifiers: [ENCSR507JOF](https://www.encodeproject.org/experiments/ENCSR507JOF/), [ENCSR148IIG](https://www.encodeproject.org/experiments/ENCSR148IIG/)
- To run LIME in its current state, please ensure you have downloaded the following files: 
- Condition 1
    - Annotation file: .gtf
    - Transcript quantification file: .tsv
- Condition 2
    - Transcript quantification file: .tsv
Note: examine .tsv file to identify the name of the column containing transcript raw count data. For data downloaded for the ENCODE project, this column often has the following structure: repENSCRxxxxxx

#### Data structure examples:
##### Example SE.MATS.JCEC.txt file. This file is automatically named by rMATS 
```
ID	GeneID	geneSymbol	chr	strand	exonStart_0base	exonEnd	upstreamES	upstreamEE	downstreamES	downstreamEE	ID	IJC_SAMPLE_1	SJC_SAMPLE_1	IJC_SAMPLE_2	SJC_SAMPLE_2	IncFormLen	SkipFormLen	PValue	FDR	IncLevel1	IncLevel2	IncLevelDifference
22	"ENSG00000229236.3"	"TTTY10"	chrY	-	20524267	20524440	20521131	20521300	20575105	20575219	22	2,0,0	0,0,0	0,0,0	0,1,0	322	149	1	1.0	1.0,NA,NA	NA,0.0,NA	1.0
24	"ENSG00000012817.16"	"KDM5D"	chrY	-	19723340	197234319721129	19721311	19731771	19731930	24	0,0,2	52,27,40,0,0	66,52,31	242	149	1	1.0	0.0,0.0,0.027	0.0,0.0,0.0	0.009
25	"ENSG00000012817.16"	"KDM5D"	chrY	-	19739527	197396619735620	19735750	19741317	19741488	25	61,45,72	4,2,1	84,82,51	5,3,0	284	149	1	1.0	0.889,0.922,0.974	0.898,0.935,1.0	-0.016
26	"ENSG00000012817.16"	"KDM5D"	chrY	-	19739527	197396619735620	19735750	19741734	19741857	26	32,21,29	0,3,0	38,44,25	0,0,0	284	149	1	1.0	1.0,0.786,1.0	1.0,1.0,1.0	-0.071
```

##### Example of long-read RNA sequencing data annotation (.gtf) file from ENCODE 

```
chr1	HAVANA	gene	11869	13670	.	+	.	gene_id "ENSG00000223972.5"; gene_name "DDX11L1"; gene_status "KNOWN"; gene_type "transcribed_unprocessed_pseudogene"; talon_gene "1"; havana_gene "OTTHUMG00000000961.2"; level "2";
chr1	HAVANA	transcript	11869	14409	.	+	.	gene_id "ENSG00000223972.5"; transcript_id "ENST00000456328.2"; gene_name "DDX11L1"; gene_status "KNOWN"; gene_type "transcribed_unprocessed_pseudogene"; transcript_type "processed_transcript"; transcript_status "KNOWN"; transcript_name "DDX11L1-202"; talon_gene "1"; talon_transcript "1"; havana_transcript "OTTHUMT00000362751.1"; level "2"; source "HAVANA"; tag "basic"; transcript_support_level "1";
chr1	HAVANA	exon	11869	12227	.	+	.	gene_id "ENSG00000223972.5"; transcript_id "ENST00000456328.2"; gene_type "transcribed_unprocessed_pseudogene"; gene_status "KNOWN"; gene_name "DDX11L1"; transcript_type "processed_transcript"; transcript_status "KNOWN"; transcript_name "DDX11L1-202"; exon_number "1"; exon_id "ENSE00002234944.1"; talon_gene "1"; talon_transcript "1"; talon_exon "1"; exon_status "KNOWN"; level "2"; source "HAVANA"; tag "basic";
chr1	HAVANA	exon	12613	12721	.	+	.	gene_id "ENSG00000223972.5"; transcript_id "ENST00000456328.2"; gene_type "transcribed_unprocessed_pseudogene"; gene_status "KNOWN"; gene_name "DDX11L1"; transcript_type "processed_transcript"; transcript_status "KNOWN"; transcript_name "DDX11L1-202"; exon_number "2"; exon_id "ENSE00003582793.1"; talon_gene "1"; talon_transcript "1"; talon_exon "3"; exon_status "KNOWN"; level "2"; source "HAVANA"; tag "basic";
chr1	HAVANA	exon	13221	14409	.	+	.	gene_id "ENSG00000223972.5"; transcript_id "ENST00000456328.2"; gene_type "transcribed_unprocessed_pseudogene"; gene_status "KNOWN"; gene_name "DDX11L1"; transcript_type "processed_transcript"; transcript_status "KNOWN"; transcript_name "DDX11L1-202"; exon_number "3"; exon_id "ENSE00002312635.1"; talon_gene "1"; talon_transcript "1"; talon_exon "5"; exon_status "KNOWN"; level "2"; source "HAVANA"; tag "basic";
```
##### Example of long-read RNA sequencing data quantification (.tsv) file from ENCODE 
```
gene_ID	transcript_ID	annot_gene_id	annot_transcript_id	annot_gene_name	annot_transcript_name	n_exons	length	gene_novelty	transcript_novelty	ISM_subtype	rep1ENCSR507JOF
10	19	ENSG00000238009.6	ENST00000453576.2	AL627309.1	AL627309.1-204	2	336	Known	Known	None	1
13	22	ENSG00000268903.1	ENST00000494149.2	AL627309.6	AL627309.6-201	1	755	Known	Known	None	3
20	32	ENSG00000279457.4	ENST00000623083.4	FO538757.1	FO538757.1-201	10	1397	Known	Known	None	6
48	126	ENSG00000285268.1	ENST00000644482.1	AL669831.7	AL669831.7-201	1	114	Known	Known	None	1
```

## Instructions
### The following parameters are necessary to run LIME
``` 
  --condition1 TEXT        Name of condition 1
  --condition2 TEXT        Name of condition 2
  --rmats_out_folder PATH  Path to output of rMATS
  -t, --type TEXT          specify whether using JC or JCEC read-based data
                           from rMATS output (to do: update this to be a selector option)
  --c1_quantcol TEXT       name of condition 1 quantification.tsv column
                           corresponding to condition 1 counts
  --c2_quantcol TEXT       name of condition 2 quantification.tsv column
                           corresponding to condition 2 counts
  --c1annot PATH           Path to long read annotation GTF for condition 1
  --c1quant PATH           Path to long read quantification TSV for condition
                           1
  --c2quant PATH           Path to long read quantification TSV for condition
                           2
  -o, --outputpath PATH    Path to output
``` 
**For a list of commands, run lime --help**

### How to run LIME
#### Clone repository to Desktop
#### Create output folder to spefcify in parameters
#### Ensure you have the python packages Click, gtfparse, and pandas installed. If necessary, create a conda environment to install these packages. An example using pip is outlined below
``` pip install pandas gtfparse Click ```
#### Step 2: Run the following command to install LIME:
``` pip install --editable . ```
#### run LIME with the following command line prompt
``` lime --condition1 --condition2 --rmats_out_folder --type --c1_quantcol --c2_quantcol --c1annot --c1quant --c2quant --outputpath ```

> run.sh contains an example command line prompt for LIME

 configured with paths to the tester input files in project storage. Please run the following command in your terminal after cloning the repository and navigating to the main folder splice-event-to-isoform-pipeline in Terminal:
``` bash run.sh ```

## Output
### Temporary file structures
#### Example of SE.csv
##### Information correlates with output of rMATS SE.MATS.JC.txt
```
ID,GeneID,geneSymbol,chr,strand,exonStart_0base,exonEnd,upstreamES,upstreamEE,downstreamES,downstreamEE,ID.1,IJC_SAMPLE_1,SJC_SAMPLE_1,IJC_SAMPLE_2,SJC_SAMPLE_2,IncFormLen,SkipFormLen,PValue,FDR,IncLevel1,IncLevel2,IncLevelDifference,incJunction,excJunction,incID,excID
se.22,ENSG00000229236.3,TTTY10,chrY,-,20524267,20524440,20521131,20521300,20575105,20575219,22,"2,0,0","0,0,0","0,0,0","0,1,0",298,149,1.0,1.0,"1.0,NA,NA","NA,0.0,NA",1.0,20521300-20524267:20524440-20575105,20521300:20575105,se.22.inc,se.22.exc
se.24,ENSG00000012817.16,KDM5D,chrY,-,19723340,19723433,19721129,19721311,19731771,19731930,24,"0,0,2","52,27,44","0,0,0","66,52,31",242,149,1.0,1.0,"0.0,0.0,0.027","0.0,0.0,0.0",0.009,19721311-19723340:19723433-19731771,19721311:19731771,se.24.inc,se.24.exc
se.25,ENSG00000012817.16,KDM5D,chrY,-,19739527,19739662,19735620,19735750,19741317,19741488,25,"61,45,72","4,2,1","84,82,51","5,3,0",284,149,1.0,1.0,"0.889,0.922,0.974","0.898,0.935,1.0",-0.016,19735750-19739527:19739662-19741317,19735750:19741317,se.25.inc,se.25.exc
se.26,ENSG00000012817.16,KDM5D,chrY,-,19739527,19739662,19735620,19735750,19741734,19741857,26,"32,21,29","0,3,0","38,44,25","0,0,0",284,149,1.0,1.0,"1.0,0.786,1.0","1.0,1.0,1.0",-0.071,19735750-19739527:19739662-19741734,19735750:19741734,se.26.inc,se.26.exc
```
#### Example of merged annotation and quantification .csv files
```
gene_id,gene_name,transcript_id,feature,seqname,strand,exon_number,start,end,rep1ENCSR507JOF,tpm_WTC11,rep1ENCSR148IIG,tpm_EC
ENSG00000223972.5,DDX11L1,,gene,chr1,+,,11869,13670,0.0,0.0,0.0,0.0
ENSG00000223972.5,DDX11L1,ENST00000456328.2,transcript,chr1,+,,11869,14409,0.0,0.0,0.0,0.0
ENSG00000223972.5,DDX11L1,ENST00000456328.2,exon,chr1,+,1,11869,12227,0.0,0.0,0.0,0.0
ENSG00000223972.5,DDX11L1,ENST00000456328.2,exon,chr1,+,2,12613,12721,0.0,0.0,0.0,0.0
```
### Mapping files
#### File 1: Each row is a unique combination of Transcript (ENCODE data) and event (rMATS data)
##### Columns:
- gene_id: ENSG ID for gene, as defined in [Ensembl](https://www.ebi.ac.uk/training/online/courses/ensembl-browsing-genomes/navigating-ensembl/investigating-a-gene/#:~:text=Ensembl%20gene%20IDs%20begin%20with,of%20species%20other%20than%20human.)
- gene_name: associated string with gene_id
- strand: + or -
- rMATS_eventID: rMATS assigns **Event-type specific** ID numbers to each event. The structure of rMATS_eventIDs from LIME includes the event type (se, mxe, a3ss, or a5ss currently) concatenated to this ID number and an indication of whether the inclusion or exclusion form of the event was mapped to the isoform (inc or exc), resulting in a unique ID that can be used to distinguish between any event
- rMATS_coord: the coordinate of junctions in the rMATS event
- c1_rmats_psi/c2_rmats_psi: the Percent Spliced In (PSI) values associated with the rMATS event in sample conditions 1 and 2, respectively; a proxy to characterize the event's prevalence in one or the other condition
- rMATS_dpsi: the delta Percent Spliced In, or difference between conditions' averaged PSI values. For more information about PSI as defined by rMATS, see [Shen et al, 2014](https://pubmed.ncbi.nlm.nih.gov/25480548/)
- transcript_ID: the Ensembl ID assigned to each transcript, received from long read .gtf annotation file. Known transcripts from Ensembl begin with the identifier "ENST", while novel transcripts in the examples provided here begin with ENCLB. This may vary depending on the data input.
- long-read-UJC: UJC stands for Unique Junction Chain. This identifying label combines information about each Transcript's chromosome (chrx), the strand (+ or -), and the associated Transcript ID (ENST... or ENCLB...)
- lr_tpm_c1/lr_tpm_c2: Transcript Per Million values for the transcript in long read sample conditions 1 and 2, respectively.
```
gene_id,gene_name,strand,rMATS_eventID,rMATS_coord,c1_rmats_psi,c2_rmats_psi,rmats_dpsi,transcript_id,long-read_UJC,lr_tpm_c1,lr_tpm_c2
ENSG00000228794.8,LINC01128,+,se.42041.exc,826923-829002:829104-851926,"1.0,1.0,1.0","0.867,NA,1.0",0.067,ENCLB377SXJT000206868,chr1|+|ENCLB377SXJT000206868|827775-829002:829104-847653:847806-851926:852014-852670:852766-853390,0.428698997144436,0.0
ENSG00000228794.8,LINC01128,+,se.42042.exc,827775-829002:829104-841199,"1.0,1.0,1.0","1.0,1.0,0.826",0.058,ENCLB377SXJT000206868,chr1|+|ENCLB377SXJT000206868|827775-829002:829104-847653:847806-851926:852014-852670:852766-853390,0.428698997144436,0.0
ENSG00000228794.8,LINC01128,+,se.42043.exc,827775-829002:829104-851926,"1.0,0.806,1.0","1.0,1.0,1.0",-0.065,ENCLB377SXJT000206868,chr1|+|ENCLB377SXJT000206868|827775-829002:829104-847653:847806-851926:852014-852670:852766-853390,0.428698997144436,0.0
ENSG00000228794.8,LINC01128,+,se.42044.exc,829104-841199:841373-847653,"0.158,0.0,0.6","0.385,0.086,0.231",0.019,ENCLB377SXJT000206868,chr1|+|ENCLB377SXJT000206868|827775-829002:829104-847653:847806-851926:852014-852670:852766-853390,0.428698997144436,0.0
```