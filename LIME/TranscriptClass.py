import pandas as pd
class Transcript():
    def __init__(self, gene_id, gene_name, transcript_id, feature, seqname, strand, tpm_WTC11, tpm_EC, exonsdict):
        self.gene_id = gene_id
        self.gene_name = gene_name
        self.transcript_id = transcript_id
        self.feature = feature
        self.seqname = seqname
        self.strand = strand
        self.tpm_WTC11 = tpm_WTC11
        self.tpm_EC = tpm_EC
        self.exonsdict = exonsdict
        self.junctionString = Transcript.makeJunctionString(self, self.exonsdict)
        self.UJC = Transcript.makeUJC(self)
        self.row = Transcript.rowDict(self)

    def makeUJC(self):
        printstring = self.seqname + "|" + self.strand + "|" + self.transcript_id + "|" + self.junctionString
        return(printstring)

    def rowDict(self):
        row = {"gene_id":self.gene_id, "gene_name":self.gene_name, "transcript_id":self.transcript_id, "feature":self.feature, "tpm_WTC11":self.tpm_WTC11, "tpm_EC":self.tpm_EC, "UJC": self.UJC}
        row = pd.Series(row)
        return row
        
import pandas as pd
class Transcript():
    def __init__(self, gene_id, gene_name, transcript_id, feature, seqname, strand, tpm_WTC11, tpm_EC, exonsdict):
        self.gene_id = gene_id
        self.gene_name = gene_name
        self.transcript_id = transcript_id
        self.feature = feature
        self.seqname = seqname
        self.strand = strand
        self.tpm_WTC11 = tpm_WTC11
        self.tpm_EC = tpm_EC
        self.exonsdict = exonsdict
        self.junctionString = Transcript.makeJunctionString(self, self.exonsdict)
        self.UJC = Transcript.makeUJC(self)
        self.row = Transcript.rowDict(self)
    
    def makeUJC(self):
        printstring = self.seqname + "|" + self.strand + "|" + self.transcript_id + "|" + self.junctionString
        return(printstring)

    def rowDict(self):
        row = {"gene_id":self.gene_id, "gene_name":self.gene_name, "transcript_id":self.transcript_id, "feature":self.feature, "tpm_WTC11":self.tpm_WTC11, "tpm_EC":self.tpm_EC, "UJC": self.UJC}
        row = pd.Series(row)
        return row
        
    # def makeJunctionString(self, exonsdict):
    #     # {1: [0, 10], 2: [20, 30], 3: [40, 50]}
    #     junctionString = ""
    #     # if self.strand == "+":
    #     for i in exonsdict:
    #         if i+1 in exonsdict:
    #             exon = exonsdict[i]
    #             next_exon = exonsdict[i+1]
    #             junction = str(exon[1]) + "-" + str(next_exon[0]-1)
    #             junctionString = junctionString + junction
    #             if i+2 in exonsdict:
    #                 junctionString = junctionString + ":"
    #     # elif self.strand == "-":
    #     #     exonsdict_rev = reversed(exonsdict)
    #     #     # {1: [0, 10], 2: [20, 30], 3: [40, 50]}
    #     #     # {3: [40, 50], 2: [20, 30], 1: [0, 10]}
    #     #     # goal: 40-29:20-9
    #     #     # goal: str(exon[0]-1) + "-" + next_exon[1]
    #     #     for i in exonsdict_rev:
    #     #         if i+1 in exonsdict:
    #     #             exon = exonsdict[i]
                
    #     return junctionString 
        
    def makeJunctionString(self, exonsdict):
        # {1: [0, 10], 2: [20, 30], 3: [40, 50]}
        junctionString = ""
        if self.strand == "+":
            for i in exonsdict:
                if i+1 in exonsdict:
                    exon = exonsdict[i]
                    next_exon = exonsdict[i+1]
                    junction = str(exon[1]) + "-" + str(next_exon[0]-1)
                    junctionString = junctionString + junction
                    if i+2 in exonsdict:
                        junctionString = junctionString + ":"

        elif self.strand == "-":
            exon_keylist_reversedorder = []
            for exon in reversed(sorted(exonsdict.keys())):
                exon_keylist_reversedorder.append(exon)
            #print(exon_keylist_reversedorder)
            for i in exon_keylist_reversedorder:
                if i-1 in exonsdict:
                    exon = exonsdict[i]
                    next_exon = exonsdict[i-1]
                    junction = str(exon[1]) + "-" + str(next_exon[0]-1)
                    junctionString = junctionString + junction
                    if i-2 in exon_keylist_reversedorder:
                        junctionString = junctionString + ":"
        else:
            print("something's gone wrong! :(")
        return junctionString 