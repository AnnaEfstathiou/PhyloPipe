# PhyloPipe

#### `phyloPipe.sh` (`phylo_parameters.cfg`)
The phyloPipe.sh script is a Bash shell script that automates a series of bioinformatics tasks involving the manipulation and analysis of FASTA formatted sequence files. 

The expected input file is a directory or a FASTA file.
The script checks if the output directory specified in the configuration file exists; if not, it creates the directory using mkdir -p.

- Handling Input:
The script determines if the input path is a directory or a single file.
If it's a directory, it sets FASTA_DIR to the input path, generates a name for an output file to concatenate all FASTA files in the directory, and then concatenates these files.
If it's a single file, it uses the file itself as the input for later processing.
- MAFFT Alignment:
The script initializes a variable alignment_file for storing the result of a multiple sequence alignment.
It uses the MAFFT software to perform a multiple sequence alignment on the FASTA file(s) and stores the result in alignment_file.
- Optional Header Editing:
A Python script is called to modify headers in the aligned FASTA file. This step is intended to reformat or correct sequence headers for clarity or compliance with specific formats.
- RAxML Phylogenetic Analysis:
The script constructs a command for RAxML, a tool used for phylogenetic tree construction, by replacing a placeholder in a pre-defined command template with the path to the aligned FASTA file.
It checks if the command is properly set (i.e., the template was replaced correctly) and exits with an error message if not.
Finally, it executes the RAxML command to generate a phylogenetic tree from the aligned sequences.
- Error Handling and User Feedback
The script includes error checks and user feedback at critical points, such as ensuring an input is provided, successfully creating directories, and setting up the RAxML command. This ensures that the user is informed of the script’s progress and any issues that might occur.

Overall, this script automates the workflow of concatenating FASTA files, aligning them, optionally editing sequence headers, and constructing a phylogenetic tree, making it a useful tool in genomic studies or similar bioinformatics workflows.

Suggested palettes for phyloView:
Seaborn color palettes: https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette 
