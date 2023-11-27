# Function to input a DNA sequence from the user
def input_dna_sequence():
    dna_sequence = input("Enter a DNA sequence: ").upper()
    return dna_sequence

# Function to calculate the length of a DNA sequence
def calculate_sequence_length(dna_sequence):
    return len(dna_sequence)

# Function to calculate the GC content of a DNA sequence
def calculate_gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_bases = len(dna_sequence)
    gc_content = (gc_count / total_bases) * 100
    return gc_content

# Main function
def main():
    print("DNA Sequence Analyzer - Part 1")
    
    # Input DNA sequence
    dna_sequence = input_dna_sequence()
    
    # Calculate and display sequence length
    sequence_length = calculate_sequence_length(dna_sequence)
    print(f"Sequence Length: {sequence_length} base pairs")
    
    # Calculate and display GC content
    gc_content = calculate_gc_content(dna_sequence)
    print(f"GC Content: {gc_content:.2f}%")
    
if __name__ == "__main__":
    main()
