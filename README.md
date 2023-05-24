# latex_doi2bib.py
This script fetches bibtex entries of all valid DOIs in citations marked with `\cite{}`, `\citet{}` or `\citep{}` in a TeX file and writes them to a given bibtex file.
The DOI can be specified as full URL starting with `https://doi.org/` or just the DOI which is usually the rest of the URL.
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
Running the script does not overwrite or update already present entries in the bibtex file. So it is still possible to add entries manually alongside the generated ones while at the same time running the script repeatedly.

## Example
```latex
Some of the problems which were identified are publication bias\cite{10.7554/eLife.21451}, 
misaligned incentives \cite{10.1098/rsos.160384},
irreproducability of research \cite{10.1371/journal.pmed.0020124, https://doi.org/10.1038/s41562-016-0021},
inconsistent peer-reviews \cite{10.12688/f1000research.11369.2, 10.12688/f1000research.12037.1},
unreasonable delays in the publication process \cite{https://doi.org/10.1016/j.joi.2013.09.001},
lack of transparency \citep{10.1016/j.ejim.2016.04.014} 
and low quality publication outlets\cite{10.1101/2023.05.06.23289563}.
```

becomes 
```bibtex
@article{10.7554/eLife.21451,
	doi = {10.7554/elife.21451},
	url = {https://doi.org/10.7554/2Felife.21451},
	year = 2016,
	month = {dec},
	publisher = {{eLife} Sciences Publications, Ltd},
	volume = {5},
	author = {Silas Boye Nissen and Tali Magidson and Kevin Gross and Carl T Bergstrom},
	title = {Publication bias and the canonization of false facts},
	journal = {{eLife}}
}

@article{https://doi.org/10.1098/rsos.160384,
	doi = {10.1098/rsos.160384},
	url = {https://doi.org/10.1098/2Frsos.160384},
	year = 2016,
	month = {sep},
	publisher = {The Royal Society},
	volume = {3},
	number = {9},
	pages = {160384},
	author = {Paul E. Smaldino and Richard McElreath},
	title = {The natural selection of bad science},
	journal = {Royal Society Open Science}
}

@article{https://doi.org/10.1371/journal.pmed.0020124,
	doi = {10.1371/journal.pmed.0020124},
	url = {https://doi.org/10.1371/2Fjournal.pmed.0020124},
	year = 2005,
	month = {aug},
	publisher = {Public Library of Science ({PLoS})},
	volume = {2},
	number = {8},
	pages = {e124},
	author = {John P. A. Ioannidis},
	title = {Why Most Published Research Findings Are False},
	journal = {{PLoS} Medicine}
}

...
```
