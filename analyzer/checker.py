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

test_clause = Clause("Data retention period", "Data handling", ["data retention", "keep your data"])
print(test_clause.name, "-", test_clause.status)

legalbasis_clause = Clause("Legal basis", "Transparency", ["legal basis", "lawful basis", "legitimate interest", "consent", "contractual necessity", "Article 6","grounds for processing"])
print(legalbasis_clause.name, "-", legalbasis_clause.status)

datasharing_clause = Clause("Data sharing", "Transparency", ["share your data", "third parties", "service providers", "affiliates", "legal disclosure", "recipients", "with whom we share"])
print(datasharing_clause.name, "-", datasharing_clause.status)

sample_policy = "We have a data retention period of 24 months. We will keep your data for that long."
test_clause.check_against(sample_policy)
print(test_clause.name, "-", test_clause.status)