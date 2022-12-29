import camelot
import os
import sys

# getting the image path
pdf_path = sys.argv[1]

# some validation checks
assert os.path.isfile(pdf_path) , 'file does not exist'
assert os.path.splitext(pdf_path)[1] == '.pdf', 'invalid pdf file'

tables = camelot.read_pdf(pdf_path)
print(tables[0].parsing_report)
tables[0].to_excel('foo.xlsx')