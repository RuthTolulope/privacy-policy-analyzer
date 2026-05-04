class Clause:
    def __init__(self, name, category, keywords):
        self.name = name
        self.category = category
        self.keywords = keywords
        self.status = "not checked"

test_clause = Clause("Data retention period", "Data handling", ["data retention", "keep your data"])
print(test_clause.name, "-", test_clause.status)

legalbasis_clause = Clause("Legal basis", "Transparency", ["legal basis", "lawful basis", "legitimate interest", "consent", "contractual necessity", "Article 6","grounds for processing"])
print(legalbasis_clause.name, "-", legalbasis_clause.status)

datasharing_clause = Clause("Data sharing", "Transparency", ["share your data", "third parties", "service providers", "affiliates", "legal disclosure", "recipients", "with whom we share"])
print(datasharing_clause.name, "-", datasharing_clause.status)
