# rMATS to BED12 file
# while raw_input doesn't equal "done", keep taking lines of rMATS and converting them to BED lines

# input:
# ID	GeneID	geneSymbol	chr	strand	exonStart_0base	exonEnd	upstreamES	upstreamEE	downstreamES	downstreamEE	ID	IJC_SAMPLE_1	SJC_SAMPLE_1	IJC_SAMPLE_2	SJC_SAMPLE_2	IncFormLen	SkipFormLen	PValue	FDR	IncLevel1	IncLevel2	IncLevelDifference
# 22	"ENSG00000229236.3"	"TTTY10"	chrY	-	20524267	20524440	20521131	20521300	20575105	20575219	22	2,0,0	0,0,0	0,0,0	0,1,0	322	149	1	1.0	1.0,NA,NA	NA,0.0,NA	1.0

# 68086 "ENSG00000099250.18" "NRP1" chr10 - 33202890 33202993 3197620 33197709 33207571 33207625 68086 11,13,5 0,1,2 1825,1171,1067 40,16,20 254 149 1 1.0 1.0,0.884,0.5950 0.964,0.977,0.969 -0.144
# 68087 "ENSG00000099250.18" "NRP1" chr10 - 33202911 33202995 33197649 33197709 33207571 33207716 68087 8,10,3 0,1,2 1107,777,690 40,16,20 233 149 1 1.0 1.0,0.865,0.49 0.947,0.969,0.957 -0.173

# output

def rMATStoBED():
    rmatsline = ""
    while rmatsline != "done":
        rmatsline = input("PASTE RMATS CODE HERE OR TYPE 'done' TO FINISH PROGRAM: ")
        event = rmatsline.split("\t")
        # for i in range(0, len(event)-1):
        #     print(i, ":", event[i])

        ID = event[0]
        GeneID = event[1]
        geneSymbol = event[2]
        chr = event[3] 
        strand = event[4] 
        exonStart_0base = event[5] 
        exonEnd = event[6] 
        upstreamES = event[7] 
        upstreamEE = event[8] 
        downstreamES = event[9] 
        downstreamEE = event[10] 
        incFormLen = event[16] 
        SkipFormLen = event[17] 
        PValue = event[18] 
        FDR = event[19] 
        IncLevel1 = event[20] 
        IncLevel2 = event[21]
        
        #blockSizes
        UEsize = int(upstreamEE) - int(upstreamES)
        DEsize = int(downstreamEE) - int(downstreamES)
        MEsize = int(exonEnd) - int(exonStart_0base)

        
        #blockStarts
        UEstart = int(upstreamES) - int(upstreamES)
        MEstart = int(exonStart_0base) - int(upstreamES)
        DEstart = int(downstreamES) - int(upstreamES)

        # chrom chromStart chromEnd name score strand thickStart thickEnd itemRgb blockCount blockSizes blockStarts 
        chrom = chr
        chromStart = upstreamES 
        chromEnd = downstreamEE
        name = ID
        score = "500"
        thickStart = upstreamES
        thickEnd = downstreamEE
        itemRgb = "255,0,0"
        blockCount = "3"
        blockSizes = str(UEsize) + "," + str(MEsize) + "," + str(DEsize)
        blockStarts = str(UEstart) + "," + str(MEstart) + "," + str(DEstart)
        
        print()
        print("YOUR BED LINE IS BELOW!!")
        print('track name="', ID, '" description="', ID, '" itemRgb="On"', sep="")
        print(chrom, chromStart, chromEnd, name, score, strand, thickStart, thickEnd, itemRgb, blockCount, blockSizes, blockStarts, sep = " ")
        print("END OF BED LINE")
        print()
    return

rMATStoBED()