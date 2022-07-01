#
# Prepare data for machine learning challenge. Written for Python 3.
#
# This script assumes two columns in the input Excel file. The first column is the topic of a post, the second column
# is the text from the post.
#
# Generate TSV outputs to console. To run this script without filtering for topics:
#
#   python3 preprocess.py.py machine_learning_challenge.xlsx
#
# To run this script with filtering for topics:
#
#   python3 preprocess.py.py machine_learning_challenge.xlsx "low blood pressure"
#
# Only simple string matching is implemented for filtering. Topic posts are converted to lower case.
# Generate TSV format to console.
#

import re
import sys
from xlrd import open_workbook

if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print(('\nGenerate TSV outputs to console. To run this script without filtering for topic:\n\n  python3 preprocess.py.py machine_learning_challenge.xlsx\n\n'
               'To run this script with filtering for topics:\n\n  python3 preprocess.py.py machine_learning_challenge.xlsx "low blood pressure"\n\n'
               'Only simple string matching is implemented for filtering. Topic posts are converted to lower case.\n'))
    else:
        topic = None if len(sys.argv) != 3 else sys.argv[2].lower()
        
        for sheet in open_workbook(sys.argv[1]).sheets():
            for row in range(sheet.nrows):
                for col in range(sheet.ncols):
                    # Use lower cases (e.g. 'Life' == 'life)
                    x = sheet.cell(row,col).value.lower().strip()
                    
                    # Ignore if not the topic we're looking for
                    if col == 0 and topic is not None and not topic in x:
                        break
                        
                    # Remove unnecessary spaces/new lines
                    x = x.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')

                    # Remove common punctuation marks (e.g. "degree" == "degree.")
                    x = x.replace('.', '').replace('?', '').replace('!', '').replace(',', '')

                    # Remove excessive spaces
                    x = re.sub(' +', ' ', x)

                    print(x, end='')

                    # Convert output to TSV format
                    if col == 0:
                        print('\t', end='')
                    else:
                        print()
