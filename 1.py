from my_functions import *

# File paths
input_file = "final-002.csv"
output_file = "final-003.csv"

# Sort the CSV file based on the 7th and 5th columns
sort_columns = [6, 4]
sort_csv(input_file, output_file, sort_columns)

print_seating("final-003.csv","aaa", "bbb")
summarise("final-003.csv")
print_summary("aaa","bbbb")
