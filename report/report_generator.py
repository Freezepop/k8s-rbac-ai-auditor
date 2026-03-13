from datetime import datetime
from config import REPORT_FILE


def generate_report(findings, recommendations):

    with open(REPORT_FILE, "w", encoding="utf-8") as f:

        f.write("RBAC SECURITY AUDIT REPORT\n")
        f.write("=" * 40 + "\n")
        f.write(f"Generated: {datetime.now()}\n\n")

        f.write("FINDINGS\n")
        f.write("-" * 40 + "\n")

        for i, finding in enumerate(findings, 1):

            f.write(f"Finding {i}\n")
            f.write(f"Role: {finding.get('role')}\n")
            f.write(f"Issue: {finding.get('issue')}\n")

            if "permission" in finding:
                f.write(f"Permission: {finding['permission']}\n")

            if "resource" in finding:
                f.write(f"Resource: {finding['resource']}\n")

            f.write("\n")

        f.write("\nRECOMMENDATIONS\n")
        f.write("-" * 40 + "\n")

        for rec in recommendations:

            f.write(f"Issue: {rec['issue']['issue']}\n")
            f.write("Recommendation:\n")
            f.write(rec["recommendation"])
            f.write("\n\n")