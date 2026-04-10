import csv

SAMPLE_FILE = "scan_results.csv"


# --- Helper (provided) ---
def load_findings(filename):
    """Load CSV findings (from Q1)."""
    try:
        with open(filename, "r") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please run the Q1 script first.")
        return []


# Draw horizontal bars using █ characters, scaled to max value
def bar_chart(data, title, max_width=30):
    if not data:
        return

    print(title)
    # Find the max value in data for scaling
    max_val = max(count for _, count in data)

    for label, count in data:
        # Calculate bar length relative to the max value
        # If max_val is 0, bar_length should be 0 to avoid division by zero
        bar_length = int((count / max_val) * max_width) if max_val > 0 else 0
        print(f"  {label:<15} {'█' * bar_length} {count}")


# Count findings per severity and return ordered: HIGH, MEDIUM, LOW
def severity_summary(findings):
    # Initialize counts
    counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for f in findings:
        sev = f["severity"]
        if sev in counts:
            counts[sev] += 1

    # Return as list of tuples in specific order
    return [
        ("HIGH", counts["HIGH"]),
        ("MEDIUM", counts["MEDIUM"]),
        ("LOW", counts["LOW"])
    ]


# Count findings per date and return sorted by date ascending
def timeline(findings):
    date_counts = {}
    for f in findings:
        d = f["date"]
        date_counts[d] = date_counts.get(d, 0) + 1

    # Sort items by the key (the date string) ascending
    return sorted(date_counts.items())


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: ASCII DASHBOARD")
    print("=" * 60)

    findings = load_findings(SAMPLE_FILE)

    if findings:
        print()
        sev = severity_summary(findings)
        if sev:
            bar_chart(sev, "SEVERITY BREAKDOWN")

        print()
        dates = timeline(findings)
        if dates:
            bar_chart(dates, "FINDINGS BY DATE")

        print()
        # Count by type for a third chart
        type_counts = {}
        for f in findings:
            t = f["type"]
            type_counts[t] = type_counts.get(t, 0) + 1
        type_data = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
        if type_data:
            bar_chart(type_data, "VULNERABILITY TYPES")
    else:
        print("\n  No data found to generate dashboard.")

    print("\n" + "=" * 60)
