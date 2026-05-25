from analyzer.checker import Clause
from analyzer.fetcher import fetch_from_url, fetch_from_file
from analyzer.reporter import save_json_report, save_csv_report
import json

def load_clauses():
    with open("rules/clauses.json", "r") as file:
        clauses_data = json.load(file)

    clauses = []
    for clause_data in clauses_data:
        clause = Clause(clause_data["name"], clause_data["category"], clause_data["keywords"])
        clauses.append(clause)

    return clauses

def get_policy_text():
    choice = input("Scan a URL or a file? Type 'url' or 'file': ")

    if choice == "url":
        url = input("Enter the URL: ")
        text = fetch_from_url(url)
        return text, "url", url

    elif choice == "file":
        path = input("Enter the file path: ")
        text = fetch_from_file(path)
        return text, "file", path

    else:
        print("Invalid choice. Please type 'url' or 'file'.")
        return None, None, None
    
def main():
    # Get the policy text from the user
    text, source_type, source_value = get_policy_text()

    # Stop if fetching failed
    if text is None:
        print("Could not load the policy. Stopping.")
        return

    print(f"Loaded {len(text)} characters from {source_value}")

    # Load clauses and scan
    clauses = load_clauses()
    for clause in clauses:
        clause.check_against(text)

    # Show results
    print("---")
    for clause in clauses:
        print(clause.name, "—", clause.status)

    # Save reports
    save_json_report(clauses, source_type, source_value, "report.json")
    save_csv_report(clauses, "report.csv")


if __name__ == "__main__":
    main()