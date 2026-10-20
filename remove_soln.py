import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder
filenames = glob("[01]*.ipynb") + ["bandit.ipynb", "monty.ipynb"]

text = '# Solution'
replacement = '# Solution goes here'

colab_prefix = '[Click here to run this notebook on Colab]'
colab_url = 'https://colab.research.google.com/github/AllenDowney/BiteSizeBayes/blob/master/'

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

        # point the Colab link at this version
        if cell['source'].startswith(colab_prefix):
            cell['source'] = f'{colab_prefix}({colab_url}{filename})'

    nbf.write(ntbk, filename)
