import csv


def find_doubled_rows(input_file, output_file):
    
    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        
        first_column_index = header.index( 'Drug_ID')  
        tenth_column_index = header.index('interaction_text')  
        
        pair_occurrences = {}

        
        for row_num, row in enumerate(reader, 2):  
            
            if row[first_column_index] and row[tenth_column_index]:
                pair = (row[first_column_index], row[tenth_column_index])
                if pair in pair_occurrences:
                    pair_occurrences[pair].append(row)
                else:
                    pair_occurrences[pair] = [row]

    
    with open(output_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
       
        writer.writerow(header)
        
        for pair, rows in pair_occurrences.items():
            if len(rows) > 1:
                for row in rows:
                    writer.writerow(row)



input_file = 'DFI.csv'
output_file = 'the output.csv'
find_doubled_rows(input_file, output_file)
