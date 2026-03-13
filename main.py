import yaml

from analyzer.rbac_parser import parse_roles
from analyzer.privilege_analyzer import analyze_roles
from llm.llm_client_mock import generate_llm_recommendations
from report.report_generator import generate_report


def load_yaml():

    with open("examples/insecure_role.yaml") as f:
        data = yaml.safe_load(f)

    return [{
        "name": data["metadata"]["name"],
        "rules": data["rules"]
    }]


def main():

    print("Loading RBAC YAML...")

    raw_roles = load_yaml()

    print("Parsing RBAC...")

    roles = parse_roles(raw_roles)

    print("Analyzing roles...")

    findings = analyze_roles(roles)

    print("Generating AI recommendations...")

    recommendations = generate_llm_recommendations(findings)

    print("Creating report...")

    generate_report(findings, recommendations)


if __name__ == "__main__":
    main()