import csv


def find_doubled_rows(input_file, output_file):
    # Open input file
    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # Read header
        header = next(reader)
        # Get column indices
        first_column_index = header.index(
            'Drug_ID')  # Replace 'First_Column_Header' with actual header name
        tenth_column_index = header.index(
            'interaction_text')  # Replace 'Tenth_Column_Header' with actual header name
        # Create a dictionary to store occurrences of pairs
        pair_occurrences = {}

        # Iterate through rows
        for row_num, row in enumerate(reader, 2):  # Start enumeration from row 2 (since header is row 1)
            # Check if both columns are present and not empty
            if row[first_column_index] and row[tenth_column_index]:
                pair = (row[first_column_index], row[tenth_column_index])
                if pair in pair_occurrences:
                    pair_occurrences[pair].append(row)
                else:
                    pair_occurrences[pair] = [row]

    # Write results to output file
    with open(output_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        # Write header
        writer.writerow(header)
        # Write rows containing pairs and their occurrences
        for pair, rows in pair_occurrences.items():
            if len(rows) > 1:
                for row in rows:
                    writer.writerow(row)


# Example usage:
input_file = 'DFI(new extraction)3.csv'
output_file = 'the 116.csv'
find_doubled_rows(input_file, output_file)
