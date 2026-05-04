class Clause:
    def __init__(self, name, category, keywords):
        self.name = name
        self.category = category
        self.keywords = keywords
        self.status = "not checked"

test_clause = Clause("Data retention period", "Data handling", ["data retention", "keep your data"])
print(test_clause.name, "-", test_clause.status)