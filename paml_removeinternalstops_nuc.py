######removes internal stop codons from files which have their end stop codons already removed 

input_file = "/Users/rhianah/Documents/Dissertation/nucleotide_nostop_go7.fa"
output_file = "/Users/rhianah/Documents/Dissertation/nucleotide_nostop2_go7.fa"
processed_sequences = []

with open(input_file, "r") as file:
    lines = file.readlines()
    header = ""
    sequence = ""
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            if sequence != "":
                processed_sequence = ""
                for i in range(0, len(sequence), 3):
                    codon = sequence[i:i+3]
                    if codon in ["TAA", "TAG", "TGA"]:
                        processed_sequence += "---"
                    else:
                        processed_sequence += codon
                processed_sequences.append((header, processed_sequence))
            header = line
            sequence = ""
        else:
            sequence += line
    if sequence != "":
        processed_sequence = ""
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i+3]
            if codon in ["TAA", "TAG", "TGA"]:
                processed_sequence += "---"
            else:
                processed_sequence += codon
        processed_sequences.append((header, processed_sequence))

with open(output_file, "w") as file:
    for header, sequence in processed_sequences:
        file.write(f"{header}\n{sequence}\n")
