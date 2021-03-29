# Build the Colab notebooks

# copy the notebooks with solutions
cp solutions/[01]*.ipynb .

# remove solutions
python remove_soln.py

# pip install pytest nbmake

# run nbmake
pytest --nbmake [01]*.ipynb

# push to GitHub
git add [01]*.ipynb utils.py
git commit -m "Updating notebooks"
git push
