from analyzer.rules import DANGEROUS_PERMISSIONS, CRITICAL_RESOURCES


def analyze_roles(roles):

    findings = []

    for role in roles:

        role_name = role["name"]

        for rule in role["rules"]:

            verbs = rule.get("verbs", [])
            resources = rule.get("resources", [])

            if "*" in verbs:
                findings.append({
                    "role": role_name,
                    "issue": "Wildcard permissions",
                    "details": rule
                })

            for verb in verbs:
                if verb in DANGEROUS_PERMISSIONS:
                    findings.append({
                        "role": role_name,
                        "issue": "Dangerous permission",
                        "permission": verb
                    })

            for resource in resources:
                if resource in CRITICAL_RESOURCES:
                    findings.append({
                        "role": role_name,
                        "issue": "Access to critical resource",
                        "resource": resource
                    })

    return findings