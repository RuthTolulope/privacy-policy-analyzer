# Privacy Policy Analyzer

A Python tool that scans website privacy policies, checks them against a set of key GDPR clauses, and produces a compliance report. It helps software developers, privacy professionals and everyday users quickly see which essential clauses a policy addresses, partially addresses, or omits, without reading the whole document.

## Features

- **Two input methods**: scan a live policy directly from a URL, or read a saved policy from a local `.txt` file (useful for sites that block automated requests, draft policies, or offline review).
- **19 GDPR clauses** across four categories (Transparency, User Rights, Data Handling, Accountability), defined in a configurable JSON file.
- **Three-level status** for each clause: `found`, `partial`, or `missing`, based on how many of its keywords appear in the text.
- **HTML parsing** with BeautifulSoup to extract readable text from web pages.
- **Two report formats**: a structured `report.json` (machine-readable) and a `report.csv` (opens in Excel for human review), each including the source, a timestamp, a summary, and detailed per-clause findings.
- **Graceful error handling** for unreachable URLs, missing or empty files, and invalid input.
- **Unit tests** with pytest covering the core clause-matching logic.

## Requirements

- Python 3.10 or newer (developed on Python 3.13)
- The libraries listed in `requirements.txt` (`requests`, `beautifulsoup4`, `pytest`)

## Installation

Clone the repository:

```bash
git clone https://github.com/RuthTolulope/privacy-policy-analyzer.git
cd privacy-policy-analyzer
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate        # on macOS/Linux
# venv\Scripts\activate         # on Windows
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the tool from the project root:

```bash
python3 -m main
```

The program will ask whether you want to scan a URL or a file:

```
Scan a URL or a file? Type 'url' or 'file': url
Enter the URL: https://example.com/privacy
```

It then fetches the policy text, scans it against all clauses, prints a summary to the terminal, and saves two reports (`report.json` and `report.csv`) in the project root.

Example output:

```
Loaded 43909 characters from https://example.com/privacy
---
Data collection practices — found
Data use purposes — found
Legal basis for processing — found
Right to access — partial
Right to restrict processing — missing
...
Report saved to report.json
Report saved to report.csv
```

To scan a local file instead, choose `file` at the prompt and enter the path (e.g. `test_policy.txt`).

## How It Works

1. **Load clauses**: clause definitions (name, category, keywords) are read from `rules/clauses.json` and turned into `Clause` objects.
2. **Fetch text**: the policy is fetched from a URL (and cleaned of HTML with BeautifulSoup) or read from a local file.
3. **Scan**: each `Clause` searches the text for its keywords. The status is decided by how many match:
   - **2 or more** keywords → `found`
   - **exactly 1** keyword → `partial`
   - **0** keywords → `missing`
4. **Report**: results are written to JSON and CSV, with a summary and detailed findings.

## Project Structure

```
privacy_policy_analyzer/
├── analyzer/
│   ├── __init__.py
│   ├── checker.py        # Clause class + matching logic
│   ├── fetcher.py        # fetch from URL or file
│   └── reporter.py       # save JSON and CSV reports
├── rules/
│   └── clauses.json      # the 19 GDPR clause definitions
├── tests/
│   └── test_checker.py   # pytest unit tests
├── main.py               # interactive entry point
├── requirements.txt
└── README.md
```

## Running the Tests

```bash
python3 -m pytest -v
```

## Limitations

This tool uses keyword-based substring matching. It is designed as a fast first-pass triage, not a definitive legal assessment, and has known limitations:

- **Vocabulary drift**: a policy may fully address a clause using different wording than the configured keywords. For example, a policy that says *"changes to our privacy statement"* may be scored lower by keywords expecting the word *"policy"* rather than *"statement"*.
- **No semantic understanding**: the matcher cannot tell that *"limit the processing"* and *"limit processing"* mean the same thing; even a single extra word can break a match.
- **No negation handling**: a phrase like *"we do not share your data"* still contains the keyword *"share your data"* and may be counted as present.

These trade-offs are deliberate: keyword matching is fast, transparent, and easy to audit. A future version could add semantic matching (e.g. embeddings) as a second pass to catch wording variations, while keeping the keyword layer for explainability.

## Future Work

- A web interface (e.g. FastAPI) so policies can be scanned from a browser.
- Expanded and refined keyword sets per clause.
- Support for additional jurisdictions beyond GDPR.
- Implement keyBERT for context aware keyword identification

## Resources
- CodeAcademy
- Labex.io
- Chatgpt - explanation of concepts in easy to understand manner with examples
- Stack Overflow
