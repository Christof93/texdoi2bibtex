import sys
import re
import requests

tex_file = sys.argv[1]
bib_file = sys.argv[2]

def get_bibtex_from_doi(doi):
    if doi.startswith("10."):
        doi = "https://doi.org/"+doi
    print(f"doi2bib: Fetching entry for {doi}...")
    response = requests.get(doi, headers = {"Accept": "application/x-bibtex"})
    if response.status_code == 200:
        return response.text
    else:
        return None
    
def change_bibtex_name(entry, change_to):
    print(entry)
    print(change_to)
    changed_name = re.sub(r'(\@.+\{)(?:.*)?(\,)', rf'\g<1>{change_to}\2', entry)
    print(changed_name)
    return changed_name

def read_bibtex_file(fn):
    entries = []
    try:
        with open(fn, 'r') as bibtex_file:
            for line in bibtex_file:
                if line.strip().startswith('@'):
                    try:
                        entries.append(re.search(r'\@.+\{(.*?)\,', line).group(1))
                    except:
                        print(f"doi2bib: Couldn't read name of entry {line}")
    except FileNotFoundError:
        print(f"doi2bib: creating new bib file {fn}.")
    return entries

def read_latex_file(fn):
    citations = []
    with open(fn, 'r') as latex_file:
        for line in latex_file:
            raw_cites=re.findall(r'\\cite[tp]?\*?\{(.*?)\}', line)
            for raw_cite in raw_cites:
                for citation in raw_cite.split(','):
                    citation = citation.strip()
                    ## match the only possible doi starting with 10. and at least 4 numbers following
                    if re.match(r'.*10\.\d{4,}(\.\d+)*\/.*', citation):
                        citations.append(citation)
    return citations

def writeappend_to_bibtex_file(entries, bibtex_fn):
    with open(bibtex_fn, 'a') as bibtex_fh:
        for entry in entries:
            # print(f"written new entry: {entry[:entry.find(',')]}")
            bibtex_fh.write(f'{entry}\n\n')

def main():
    citations = read_latex_file(tex_file)
    print(f"doi2bib: Found {len(citations)} citations in LaTeX file.")
    bib_entries = read_bibtex_file(bib_file)
    print(f"doi2bib: Found {len(bib_entries)} entries in bibTeX file.")
    new_entries = []
    for citation in citations[:1]:
        if citation not in bib_entries:
            new_bib_entry = get_bibtex_from_doi(citation)
            if new_bib_entry is not None:
                new_bib_entry = change_bibtex_name(new_bib_entry, citation)
                new_bib_entry = new_bib_entry.replace("%", "/")
                new_entries.append(new_bib_entry)
            else:
                print(f"doi2bib warning: No bibtex found for citation: {citation}. Is it a valid DOI url?")

    writeappend_to_bibtex_file(new_entries, bib_file)


if __name__=="__main__":
    main()
