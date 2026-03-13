from kubernetes import client, config


def collect_rbac():

    config.load_kube_config()

    api = client.RbacAuthorizationV1Api()

    roles = api.list_cluster_role()

    data = []

    for role in roles.items:

        rules = []

        for rule in role.rules or []:

            rules.append({
                "verbs": rule.verbs,
                "resources": rule.resources
            })

        data.append({
            "name": role.metadata.name,
            "rules": rules
        })

    return data