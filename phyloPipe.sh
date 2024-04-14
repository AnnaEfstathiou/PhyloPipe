#!/bin/bash

########################### LOAD FILES / DIRECTORIES & CHECKS ###########################

# Check if a directory or file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory_of_fastas_or_fasta_file>"
    exit 1
fi

# Input could be either a directory or a single fasta file
INPUT_PATH="$1"

# Load the configuration file
source phylo_parameters.cfg

# Check if the output directory assigned in the config file doesn't exist and create it
if [ ! -d "$OUTPUT_DIR" ]; then
    mkdir -p "$OUTPUT_DIR"
fi

########################### HANDLE INPUT ###########################

# Check if input is a directory or a file and set appropriate variables
if [ -d "$INPUT_PATH" ]; then
    # It's a directory
    FASTA_DIR="$INPUT_PATH"
    FASTA_DIR_NAME=$(basename "$FASTA_DIR")
    all_fasta="$OUTPUT_DIR/all_$FASTA_DIR_NAME.fa"
    > "$all_fasta" # Clear the file content before starting

    # Concatenate all FASTA files into one
    for fasta_file in "$FASTA_DIR"*.fa; do
        cat "$fasta_file" >> "$all_fasta"
    done
else
    # It's a single file
    all_fasta="$INPUT_PATH"
    FASTA_DIR_NAME=$(basename "$all_fasta" .fa)
fi

########################### MAFFT ###########################

alignment_file="$OUTPUT_DIR/aligned_$FASTA_DIR_NAME.fa" # Initialize variable to store the alignment output
mafft --auto "$all_fasta" > "$alignment_file" # Run multiple sequence alignment

########################### EDIT HEADERS (Optional) ###########################

python3 "$EDIT_HEADERS_SCRIPT" "$alignment_file" "$OUTPUT_DIR/modified_$FASTA_DIR_NAME.fa"
# e.g. >NC_0102 Homo Sapiens, complete genome >> >NC_0102_Homo_Sapiens

# Check if the modified file exists >> Making the modification optional
if [ -f "$OUTPUT_DIR/modified_$FASTA_DIR_NAME.fa" ]; then
    # If it exists, update alignment_file to point to the modified file
    alignment_file="$OUTPUT_DIR/modified_$FASTA_DIR_NAME.fa"
fi

########################### RAxML ###########################

# RAxML_COMMAND_MODIFIED="${RAxML_COMMAND/ALIGNED_FASTA/$alignment_file}" # Assign the aligned file (from mafft) to the RAxML command

# # Check if the RAxML_COMMAND variable is not empty
# if [ -z "$RAxML_COMMAND_MODIFIED" ]; then
#     echo "The RAxML command is not set in the config file."
#     exit 1
# else
#     echo "Executing RAxML command: $RAxML_COMMAND_MODIFIED"
#     eval $RAxML_COMMAND_MODIFIED # Execute the modified RAxML command
# fi

# # Optional: Remove intermediate files
# rm "$all_fasta"
# rm "$alignment_file"
