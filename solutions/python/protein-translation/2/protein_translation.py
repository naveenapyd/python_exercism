def proteins(strand):
    codons = [['AUG'], ['UUU', 'UUC'], ['UUA', 'UUG'], ['UCU', 'UCC', 'UCA', 'UCG'], ['UAU', 'UAC'], ['UGU', 'UGC'], ['UGG']]
    amino_acids = ['Methionine', 'Phenylalanine', 'Leucine', 'Serine', 'Tyrosine', "Cysteine", 'Tryptophan']
    protein_list = []
    for index in range(0, len(strand), 3):
        triplet = strand[index : index+3]
        if triplet in ['UAA', 'UAG', 'UGA']:
            break
        for row_index, list_of_codon in enumerate(codons):
            if triplet in list_of_codon:
                protein_list.append(amino_acids[row_index])
    return protein_list
        
