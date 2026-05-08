import json

class Clause:
    def __init__(self, name, category, keywords):
        self.name = name
        self.category = category
        self.keywords = keywords
        self.status = "not checked"
    
    def check_against(self, text):
        text = text.lower()
        match_count = 0
        for keyword in self.keywords:
            if keyword.lower() in text:
                match_count += 1
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
sample_policy = "We collect personal data and use your information for analytics purposes."
for clause in clauses:
    clause.check_against(sample_policy)

print("---")
print("After scanning:")
for clause in clauses:
    print(clause.name, "—", clause.status)