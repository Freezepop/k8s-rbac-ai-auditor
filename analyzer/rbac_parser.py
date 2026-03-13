def parse_roles(raw_roles):

    parsed_roles = []

    for role in raw_roles:

        role_name = role.get("name")

        rules = role.get("rules", [])

        parsed_rules = []

        for rule in rules:

            parsed_rules.append({
                "verbs": rule.get("verbs", []),
                "resources": rule.get("resources", []),
                "apiGroups": rule.get("apiGroups", [])
            })

        parsed_roles.append({
            "name": role_name,
            "rules": parsed_rules
        })

    return parsed_roles