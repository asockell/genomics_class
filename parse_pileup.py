import sys
import gzip
import re

pileup = sys.argv[1]
chr_position = sys.argv[2]
nucleotides = ["A","T","C","G", "a", "t", "c", "g"]
complement = {'a':'T','g':'C','t':'A','c':'G'}
pos_count = {}



with gzip.open(pileup, "rt") as pileup_file:
	for line in pileup_file:
		chrom, pos, ref, cov, reads, qual = line.rstrip('\n\r').split('\t')		
		temp_list = [str(chrom), str(pos)]
		chr_pos = '_'.join(temp_list)
		no_indels = re.sub('[+]\w+', '', reads)
		base_dict = {}
		for base in nucleotides:
			all_forw = re.sub(str(base), str(complement[base]), no_indels)
			count = len(re.findall(base, all_forw))
			base_dict.update({base:count})
		pos_count.update({chr_pos:str(base_dict)})
		
print(pos_count)
