###removes protein stop codons from the file 
###replces * with x in the biopython converted files 
###biopython autamatically converts gaps into *

def replace_stop_codons(input_file, output_file):
    with open(input_file, 'r') as file:
        sequences = []
        header = ''
        sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if header != '':
                    sequences.append((header, sequence))
                header = line
                sequence = ''
            else:
                sequence += line.replace('*', 'x')
        if header != '':
            sequences.append((header, sequence))
    
    with open(output_file, 'w') as file:
        for header, sequence in sequences:
            file.write(header + '\n')
            file.write(sequence + '\n')

input_file = '/gpfs01/home/mbxrs14/paml3/protein_nostop_biopython_go7.fa'
output_file = '/gpfs01/home/mbxrs14/paml3/proteinnostopx_go7.fa'
replace_stop_codons(input_file, output_file)
