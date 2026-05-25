import json

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