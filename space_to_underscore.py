import argparse

def replace_space_with_underscore(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            if line.startswith('>'):  # Identifying header lines
                # Splitting at the comma and taking the first part
                header_part = line.split(',', 1)[0].strip()
                # Replacing spaces with underscores
                header = header_part.replace(' ', '_')
                f_out.write(header + '\n')
            else:
                f_out.write(line)

def main():
    parser = argparse.ArgumentParser(description="Replace spaces with underscores in the headers of a FASTA file.")
    parser.add_argument('-i', '--input_file', help="Input FASTA file path")
    parser.add_argument('-o', '--output_file', help="Output FASTA file path")

    args = parser.parse_args()
    replace_space_with_underscore(args.input_file, args.output_file)

if __name__ == "__main__":
    main()

