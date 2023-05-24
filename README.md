# latex_doi2bib.py
This script fetches bibtex entries of all valid DOIs in citations marked with `\cite{}` in a TeX file and writes them to a given bibtex file.
The DOI must be specified as full links starting with `https://doi.org/`.
## Usage
The `requests` library is a prerequisite for the script.
Install it with
```bash
pip install requests
```
Then, run the python script in the following way to append the new bibtex entries to the given bibtex file.
```bash
python latex_doi2bib.py <PATH TO LATEX FILE> <PATH TO BIBTEX FILE>
```
Running the script does not overwrite or update already present entries in the bibtex file.
