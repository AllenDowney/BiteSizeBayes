import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
filenames = glob("[01]*.ipynb")

text = '# Solution'
replacement = '# Solution goes here'

# Search through each notebook
for filename in sorted(filenames):
    print('Removing solutions from', filename)
    ntbk = nbf.read(filename, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        # remove tags
        if 'tags' in cell['metadata']:
            cell['metadata']['tags'] = []

        # remove output
        if 'outputs' in cell:
            cell['outputs'] = []

        # remove solutions
        if cell['source'].startswith(text):
            cell['source'] = replacement

    nbf.write(ntbk, filename)
