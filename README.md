# Issue_01

python -m doctest -v issue_01.py

python -m doctest -o NORMALIZE_WHITESPACE -v issue_01.py

# Issue_02

python -m pytest -v issue_02.py

# Issue_03

python -m unittest issue_03.py

# Issue_04

python -m pytest issue_04.py

# Issue_05

python -m pytest issue_05.py
python -m pytest issue_05.py --cov . --cov-report html
