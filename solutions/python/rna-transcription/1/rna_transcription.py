def to_rna(dna_strand):
    rna_strand = ''
    for value in dna_strand:
        if value == 'A':
            rna_strand += 'U'
        elif value == 'C':
            rna_strand += 'G'
        elif value == 'G':
            rna_strand += 'C'
        elif value == 'T':
            rna_strand += 'A'
    return rna_strand
        
        
            
