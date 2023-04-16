# rMATS to BED12 file
# while raw_input doesn't equal "done", keep taking lines of rMATS and converting them to BED lines

# input:
# ID	GeneID	geneSymbol	chr	strand	exonStart_0base	exonEnd	upstreamES	upstreamEE	downstreamES	downstreamEE	ID	IJC_SAMPLE_1	SJC_SAMPLE_1	IJC_SAMPLE_2	SJC_SAMPLE_2	IncFormLen	SkipFormLen	PValue	FDR	IncLevel1	IncLevel2	IncLevelDifference
# 22	"ENSG00000229236.3"	"TTTY10"	chrY	-	20524267	20524440	20521131	20521300	20575105	20575219	22	2,0,0	0,0,0	0,0,0	0,1,0	322	149	1	1.0	1.0,NA,NA	NA,0.0,NA	1.0

# 68086 "ENSG00000099250.18" "NRP1" chr10 - 33202890 33202993 3197620 33197709 33207571 33207625 68086 11,13,5 0,1,2 1825,1171,1067 40,16,20 254 149 1 1.0 1.0,0.884,0.5950 0.964,0.977,0.969 -0.144
# 68087 "ENSG00000099250.18" "NRP1" chr10 - 33202911 33202995 33197649 33197709 33207571 33207716 68087 8,10,3 0,1,2 1107,777,690 40,16,20 233 149 1 1.0 1.0,0.865,0.49 0.947,0.969,0.957 -0.173

# output

def rMATStoBEDSE():
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
        FirstExonStart_0base = event[5] 
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

        # inclusion form
        
        #blockSizes
        UEsize = int(upstreamEE) - int(upstreamES)
        DEsize = int(downstreamEE) - int(downstreamES)
        MEsize = int(exonEnd) - int(FirstExonStart_0base)

        
        #blockStarts
        UEstart = int(upstreamES) - int(upstreamES)
        MEstart = int(FirstExonStart_0base) - int(upstreamES)
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
        print('track name=inclusion"', ID, '" description=inclusion"', ID, '" itemRgb="On"', sep="")
        print(chrom, chromStart, chromEnd, name, score, strand, thickStart, thickEnd, itemRgb, blockCount, blockSizes, blockStarts, sep = " ")


        blockCount = "2"
        blockSizes = str(UEsize) + "," + str(DEsize)
        blockStarts = str(UEstart) + "," + str(DEstart)

        print('track name=exclusion"', ID, '" description=exclusion"', ID, '" itemRgb="On"', sep="")
        print(chrom, chromStart, chromEnd, name, score, strand, thickStart, thickEnd, itemRgb, blockCount, blockSizes, blockStarts, sep = " ")

        
        print("END OF BED LINE")
        print()
    return

# rMATStoBEDSE()

# 6043	"ENSG00000114861.23"	"FOXP1"	chr3	-	70972010	70972180	70972554	70972676	70970735	70970805	70976940	70977042	6043	21,15,20	20,37,26	268,188,316	0,0,0	271	319	0	0.0	0.553,0.323,0.475	1.0,1.0,1.0	-0.55


def rMATStoBEDMXE():
    rmatsline = ""
    while rmatsline != "done":
        rmatsline = input("PASTE RMATS CODE HERE OR TYPE 'done' TO FINISH PROGRAM: ")
        event = rmatsline.split("\t")
        # for i in range(0, len(event)-1):
        #     print(i, ":", event[i])

        ID= event[0]
        GeneID= event[1]
        geneSymbol= event[2]
        geneSymbol = geneSymbol.replace('"', '')
        chrom = event[3]
        strand= event[4]
        FirstExonStart_0base= event[5]
        FirstExonEnd= event[6]
        SecExonStart_0base= event[7]
        SecExonEnd= event[8]
        upstreamES= event[9]
        upstreamEE= event[10]
        downstreamES= event[11]
        downstreamEE= event[12]
        ID= event[13]
        IJC_SAMPLE_1= event[14]
        SJC_SAMPLE_1= event[15]
        IJC_SAMPLE_2= event[16]
        SJC_SAMPLE_2= event[17]
        IncFormLen= event[18]
        SkipFormLen= event[19]
        PValue= event[20]
        FDR= event[21]
        IncLevel1= event[22]
        IncLevel2= event[23]
        IncLevelDifference= event[24]

        
        
        #blockSizes
        UEsize = int(upstreamEE) - int(upstreamES)
        DEsize = int(downstreamEE) - int(downstreamES)
        exon1size = int(FirstExonEnd) - int(FirstExonStart_0base)
        exon2size = int(SecExonEnd) - int(SecExonStart_0base)

        #blockStarts
        UEstart = int(upstreamES) - int(upstreamES)
        DEstart = int(downstreamES) - int(upstreamES)
        exon1start = int(FirstExonStart_0base) - int(upstreamES)
        exon2start = int(SecExonStart_0base) - int(upstreamES)
 
        chrom = chrom
        chromStart = upstreamES
        chromEnd = downstreamEE
        name = ID
        score = "500"
        thickStart = upstreamES
        thickEnd = downstreamEE
        itemRgb = "255,0,0"
        blockCount = 3
        incBlockSizes = str(UEsize) + "," + str(exon1size) + "," + str(DEsize)
        incBlockStarts = str(UEstart) + "," + str(exon1start) + "," + str(DEstart)
        excBlockSizes = str(UEsize) + "," + str(exon2size) + "," + str(DEsize)
        excBlockStarts = str(UEstart) + "," + str(exon2start) + "," + str(DEstart)

        print("BED FILE FOR", geneSymbol, "MXE event", ID, "below\n")
        print('track name="', geneSymbol, ' MXE inc ', ID, '" description="', geneSymbol, " MXE ", ID, ' inclusion" itemRgb="On"', sep="")
        print(chrom, chromStart, chromEnd, name, score, strand, thickStart, thickEnd, itemRgb, blockCount, incBlockSizes, incBlockStarts, sep = " ")
        print('track name="', geneSymbol, ' MXE exc ', ID, '" description="', geneSymbol, " MXE ", ID, ' exclusion" itemRgb="On"', sep="")
        print(chrom, chromStart, chromEnd, name, score, strand, thickStart, thickEnd, itemRgb, blockCount, excBlockSizes, excBlockStarts, sep = " ")
        print("\n\n")

    return


rMATStoBEDSE()
