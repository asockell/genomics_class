import sys
import gzip
import re

pileup = sys.argv[1]
chr_position = sys.argv[2]
A_dict = {}
T_dict = {}
C_dict = {}
G_dict = {}



with gzip.open(pileup, "rt") as pileup_file:
	for line in pileup_file:
		chr, pos, ref, cov, reads, qual = line.rstrip('\n\r').split('\t')		
		list = [str(chr), str(pos)]
		chr_pos = '_'.join(list)
		no_indels = re.sub((r"+"\d\w | r"-"\d\w), "", reads)
		count_ref = float(len(re.findall((r"\." | r","), reads)))
		countA = float(len(re.findall((r"A" | r"t"), reads)))
		countT = float(len(re.findall((r"T" | r"a"), reads)))
		countC = float(len(re.findall((r"C" | r"g"), reads)))
		countG = float(len(re.findall((r"G" | r"c"), reads)))
		if ref == "A":
			countA = count_ref
		elif ref == "T":
			countT = count_ref
		elif ref == "C":
			countC = count_ref
		elif ref == "G":
			countG = count_ref
		A_dict.update({chr_pos:countA})
		T_dict.update({chr_pos:countT})
		C_dict.update({chr_pos:countC})
		G_dict.update({chr_pos:countG})
		

def get_nucleotides(pos):
	A = A_dict[pos]
	T = T_dict[pos]
	C = C_dict[pos]
	G = G_dict[pos]
	return list(A, T, C, G)
	
print(get_nucleotides(chr_position))
		
		
			
