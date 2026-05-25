from analyzer.checker import Clause


def test_clause_starts_as_not_checked():
    clause = Clause("Test clause", "Test category", ["keyword1", "keyword2"])
    assert clause.status == "not checked"

def test_status_found_with_two_matches():
    clause = Clause("Test", "Test", ["cookies", "tracking"])
    clause.check_against("We use cookies and tracking technologies.")
    assert clause.status == "found"


def test_status_partial_with_one_match():
    clause = Clause("Test", "Test", ["cookies", "tracking"])
    clause.check_against("We use cookies to improve your experience.")
    assert clause.status == "partial"


def test_status_missing_with_no_matches():
    clause = Clause("Test", "Test", ["cookies", "tracking"])
    clause.check_against("This text is about something completely different.")
    assert clause.status == "missing"