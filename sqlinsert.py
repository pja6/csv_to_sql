#! /usr/bin/env python3

import sys
import csv

def sql_insert(csv_file, table_name, file_name="output"):
    # Open your CSV file
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
    
        # Convert CSV data into a list for easy access to both rows and columns
        data = list(csvreader)
    
    # Get the header (first row)
    header = data[0]
    
    # Get the number of rows (excluding the header)
    row_count = len(data) - 1  # Subtract 1 for the header
    column_count = len(header)

# Print the column names for reference
    print(f"Column names: {header}\n")
 
    #clears file first, in case it's already created
    with open(f'{file_name}.sql', 'w') as sqlfile:
            pass 
    
    # Open the output file to write SQL commands
    with open(f'{file_name}.sql', 'w') as sqlfile:
        
     
        sqlfile.write(f"DELETE FROM {table_name};\n")

        # Now iterate over the rows (skipping the header)
        for row_idx, row in enumerate(data[1:], start=1):  # Start at row 1 to skip header
            # Create the INSERT INTO statement
            
        # Escape apostrophes by replacing single quotes with double single quotes
            escaped_row = [
                "NULL" if value == "" else value.replace("'", "''") for value in row
            ] 
            
            # Join values for each column
            values = "', '".join(escaped_row)  
            sql = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES ('{values}');\n"
            sqlfile.write(sql)  # Write the insert statement to the file
            if row_idx==1:
                print(f"Example statement: {sql}")
            #print(f"Row {row_idx}: {sql}")  # Optional: print to screen for tracking
def main():
   
    if len(sys.argv) < 3:
        print("Insufficient Args: sudo python3 lab9.py <csv_file> <table_name>")
        sys.exit(1)
        
    if sys.argv[3]:
        file_name=sys.argv[3]
            
    elif len(ses.argv) > 4:
        print("Too many Args: python3 sqlinsert.py <csv_fil> <table_name> <output_name> ")
        sys.exit(1)
        
        
    csv_file=sys.argv[1]    
    table_name=sys.argv[2]
    print("\n*-----------------------------------------------------*")
    print("Starting...\n")
    sql_insert(csv_file, table_name, file_name)
    print("======================================================")
    print(f"output to {file_name}.sql\n")


if __name__== "__main__":
    main()