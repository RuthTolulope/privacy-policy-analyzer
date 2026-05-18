import json
from analyzer.fetcher import fetch_from_url
from analyzer.reporter import save_json_report, save_csv_report

class Clause:
    def __init__(self, name, category, keywords):
        self.name = name
        self.category = category
        self.keywords = keywords
        self.status = "not checked"
        self.matched_keywords = []
    
    def check_against(self, text):
        text = text.lower()

        self.matched_keywords = []
        for keyword in self.keywords:
            if keyword.lower() in text:
                self.matched_keywords.append(keyword)

        match_count = len(self.matched_keywords)

        if match_count == 0:
            self.status = "missing"
        elif match_count == 1:
            self.status = "partial"
        else:
            self.status = "found"

#Load the clause definitions from JSON
with open("rules/clauses.json", "r") as file:
    clauses_data = json.load(file)

#Create a Clause object for each entry
clauses = []
for clause_data in clauses_data:
    clause = Clause(clause_data["name"], clause_data["category"], clause_data["keywords"])
    clauses.append(clause)

# Run a test scan against a sample policy
# sample_policy = "We collect personal data and use your information for analytics purposes."
test_url = "https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement"
sample_policy = fetch_from_url(test_url)

if sample_policy is None:
    print("Could not fetch policy from", test_url)
    exit()

print("Fetched", len(sample_policy), "characters from", test_url)

for clause in clauses:
    clause.check_against(sample_policy)


print("---")
print("After scanning:")
for clause in clauses:
    print(clause.name, "—", clause.status)

# Save the report to a JSON file
save_json_report(clauses, "url", test_url, "report.json")
save_csv_report(clauses, "report.csv")