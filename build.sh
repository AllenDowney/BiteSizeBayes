# Build the Colab notebooks

# copy the notebooks with solutions
cp solutions/[01]*.ipynb solutions/bandit.ipynb solutions/monty.ipynb .

# remove solutions
python remove_soln.py

# pip install pytest nbmake

# run nbmake
pytest --nbmake [01]*.ipynb bandit.ipynb monty.ipynb

# push to GitHub
git add [01]*.ipynb bandit.ipynb monty.ipynb utils.py
git commit -m "Updating notebooks"
git push
