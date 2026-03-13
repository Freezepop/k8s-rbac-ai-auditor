from openai import OpenAI
from llm.prompts import PROMPT

client = OpenAI(api_key="*")


def generate_llm_recommendations(findings):

    recommendations = []

    for f in findings:

        prompt = PROMPT.format(
            issue=f["issue"],
            details=str(f)
        )

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        recommendations.append({
            "issue": f,
            "recommendation": response.output[0].content[0].text
        })

    return recommendations