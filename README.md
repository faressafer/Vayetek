README: Extract and Sum Numbers from Text File

Overview

This Python script reads a text file line by line, extracts numeric characters from each line, and calculates a sum based on the first and last digit of the extracted numbers. It provides a simple utility to process and analyze numeric data embedded in text files.

Features

Extracts all digits from each line of a text file.

Combines the first and last digit of the extracted numbers to form a two-digit number.

Prints the processed line and the corresponding two-digit number.

Computes the total sum of all extracted numbers.

How It Works

File Reading: The script reads a specified file line by line.

Digit Extraction: For each line, it filters out all non-digit characters to extract numeric values.

Number Formation: It uses the first and last digit of the extracted sequence to form a two-digit number.

Summation: The two-digit numbers are added to compute a cumulative total.

Output: The script prints the original line, the extracted two-digit number, and the final sum.

Code Breakdown

extract_and_sum_from_file(file_path)

This function processes the input file and calculates the sum of extracted numbers.

Input: A file path (file_path) to the text file to be processed.

Output: The total sum of all extracted two-digit numbers.

Key Steps:

Open File: Opens the file in read mode.

Line Processing: Iterates through each line, removing whitespace.

Digit Filtering: Filters characters to retain only digits.

Two-Digit Number Formation:

If no digits are found, the line is skipped.

Combines the first and last digit to form a two-digit number.

Print Line and Number: Displays the processed line and extracted number.

Summation: Adds the two-digit number to the total sum.

Code Example:

file_path = "document.txt"  # Specify the file path
result = extract_and_sum_from_file(file_path)
print("Total sum:", result)

Example Usage

Input File (document.txt):

ckmb52fldxkseven3fkjgcbzmnr7
gckhqpb6twoqnjxqplthree2fourkspnsnzxlz1

Output:

Line: 'ckmb52fldxkseven3fkjgcbzmnr7', Extracted Number: 57
Line: 'gckhqpb6twoqnjxqplthree2fourkspnsnzxlz1', Extracted Number: 61
Total sum: 118

Requirements

Python 3.6+

How to Run

Place the script and your input file in the same directory.

Update the file_path variable with the name of your text file.

Run the script using the command:

python script_name.py

License

This project is licensed under the MIT License.

