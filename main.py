import camelot
import os
import sys

VALID_OUTPUT_EXTENSIONS = ['.xlsl', '.csv', '.html', '.json', '.md', '.sqlite']

# getting the image path
pdf_path = sys.argv[1]
output_file = sys.argv[2]

# geting the output file extnsiom
output_file_ext = os.path.splitext(output_file)[1]

# some validation checks
assert os.path.isfile(pdf_path) , 'file does not exist'
assert os.path.splitext(pdf_path)[1] == '.pdf', 'invalid pdf file'
assert output_file_ext in VALID_OUTPUT_EXTENSIONS, 'invalid output file extension, please choos from the list' + ', '.join(VALID_OUTPUT_EXTENSIONS)

tables = camelot.read_pdf(pdf_path)
print(tables[0].parsing_report)

tables.export(output_file)
