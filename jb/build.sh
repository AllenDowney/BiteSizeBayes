# pip install jupyter-book
# pip install ghp-import

# Build the Jupyter book version

# copy the chapter notebooks
cp ../solutions/[01]*.ipynb .

# remove solutions
python prep_notebooks.py

# build the HTML version
jb build .

# push it to GitHub
ghp-import -n -p -f _build/html
