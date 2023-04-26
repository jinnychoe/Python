import requests
from io import StringIO
import pymol2 as pymol

class DNA:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def count_nucleotides(self):
        counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
        for nucleotide in self.sequence:
            if nucleotide in counts:
                counts[nucleotide] += 1
        return tuple(counts.values())
    
    def to_rna(self):
        # Convert DNA sequence to RNA sequence
        rna_seq = ''
        for base in self.sequence:
            if base == 'A':
                rna_seq += 'U'
            elif base == 'T':
                rna_seq += 'A'
            elif base == 'C':
                rna_seq += 'G'
            elif base == 'G':
                rna_seq += 'C'
            else:
                raise ValueError('Invalid DNA sequence')
        return rna_seq
    
    def to_protein(self):
        # Create a dictionary of codons and their corresponding amino acids
        codon_table = {
            'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
            'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
            'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
            'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '',
            'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
            'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
            'UGU': 'C', 'UGC': 'C', 'UGA': '', 'UGG': 'W',
            'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
            'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
        }
        # Convert DNA sequence to RNA sequence
        rna_seq = self.to_rna()
        # Generate amino acid sequence
        protein_seq = ''
        for i in range(0, len(rna_seq), 3):
            codon = rna_seq[i:i+3]
            if len(codon) == 3:
                amino_acid = codon_table.get(codon, 'X')
                protein_seq += amino_acid
        return protein_seq
    
def generate_protein_model(sequence):
    
    # Send request to Swiss-Model to get PDB file
    url = 'https://swissmodel.expasy.org/interactive'
    data = {'qname': sequence, 'template': 'None'}
    response = requests.post(url, data=data)
    pdb_text = response.text

    # Parse PDB file text and load into Pymol
    pymol.cmd.gui() #opens PyMOL GUI
    pdb_file = StringIO(pdb_text)
    pymol.cmd.read_pdbstr(pdb_file.getvalue(), 'my_protein')
    pymol.cmd.show_as('cartoon', 'my_protein')
    pymol.cmd.zoom('my_protein')

# Main program loop
def main():
    dna_seq = ""
    while True:
        # Display menu options
        print('Menu Options:')
        print('1. Input DNA sequence')
        print('2. Convert to RNA sequence')
        print('3. Convert to amino acid sequence')
        print('4. Generate 3D protein model')
        print('5. Quit')
    
        # Get user input
        choice = input('Enter your choice: ')
    
        # Process user choice
        if choice == '1':
            dna_seq = input('Enter the DNA sequence: ')
            dna = DNA(dna_seq)
            count = dna.count_nucleotides()
            print("Nucleotide count: A={}, T={}, G={}, C={}".format(count[0], count[1], count[2], count[3]))
            
        elif choice == '2':
            if dna_seq:
                dna = DNA(dna_seq)
                rna_seq = dna.to_rna()
                print('RNA sequence:', rna_seq)
            else:
                print("Please input a DNA sequence first.")
                continue  # return to menu
            
        elif choice == '3':
            if dna_seq:
                dna = DNA(dna_seq)
                prot_seq = dna.to_protein()
                print('Protein sequence:', prot_seq)
            else:
                print("Please input a DNA sequence first.")
                continue  # return to menu
            
        elif choice == '4':
            while True:
                print('1. Generate 3D protein model')
                print('2. Quit')
                sub_choice = input('Enter your choice: ')
                if sub_choice == '1':
                    if dna_seq:
                        try:
                            generate_protein_model(dna.sequence)
                            print('Protein model generated successfully.')
                        except Exception as e:
                            print('Error generating protein model:', e)
                        pymol.cmd.delete('*')
                    else:
                        print('Error. Please input DNA sequence first.')
                elif sub_choice == '2':
                    pymol.cmd.quit()
                    break
                else:
                    print('Invalid choice. Please try again.')
                    continue

        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')
  
main()

    #install on terminal
    #sudo apt-get install python-pip
    #pip install requests (. )
    #sudo apt-get update
    #sudo apt-get install pymol
    
