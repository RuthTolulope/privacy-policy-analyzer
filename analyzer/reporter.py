import json 
import csv
from datetime import datetime

def save_json_report(clauses,source_type, source_value, output_path="report.json"):
    # Build summary count
    summary = {"found": 0, "partial": 0, "missing": 0}
    for clause in clauses:
        summary[clause.status] += 1
    
    #Build detailed findings
    findings = []
    for clause in clauses:
        findings.append({
            "name": clause.name,
            "category": clause.category,
            "status": clause.status,
            "matched_keywords": clause.matched_keywords,
        })

    # Build the full report
    report = {
        "input_source_type": source_type,
        "input_source_value": source_value,
        "scanned_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": summary,
        "findings": findings
    }

    # Write to file
    with open(output_path, "w") as file:
        json.dump(report, file, indent=2)
    
    print(f"Report saved to {output_path}")

def save_csv_report(clauses, output_path="report.csv"):
    with open(output_path, "w", newline="") as file:
        writer = csv.writer(file)
        
        # Write header row
        writer.writerow(["Name", "Category", "Status", "Matched Keywords"])
        
        # Write one row per clause
        for clause in clauses:
            matched_keywords_string = "; ".join(clause.matched_keywords)
            writer.writerow([
                clause.name,
                clause.category,
                clause.status,
                matched_keywords_string
            ])
    
    print(f"Report saved to {output_path}")