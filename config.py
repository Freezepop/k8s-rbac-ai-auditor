# Kubernetes settings
KUBE_CONFIG_PATH = "~/.kube/config"

# LLM settings
LLM_MODEL = "gpt-4.1-mini"

# Report settings
REPORT_FILE = "security_report.txt"

# Security analysis parameters
MAX_ALLOWED_VERBS = [
    "get",
    "list",
    "watch"
]

CRITICAL_RESOURCES = [
    "secrets",
    "configmaps",
    "clusterroles",
    "clusterrolebindings",
    "pods"
]

# AI prompt settings
MAX_PROMPT_LENGTH = 2000