def generate_llm_recommendations(findings):

    recommendations = []

    for f in findings:

        if f["issue"] == "Wildcard permissions":

            text = """
Role uses wildcard permissions (*).
It is recommended to restrict verbs to the minimal required set
(get, list, watch) according to the principle of least privilege.
"""

        elif f["issue"] == "Access to critical resource":

            text = f"""
Role has access to critical resource '{f["resource"]}'.
Access should be limited only to trusted service accounts.
"""

        else:

            text = "Review RBAC permissions and apply least privilege principle."

        recommendations.append({
            "issue": f,
            "recommendation": text
        })

    return recommendations
