
def build_email_improvement_prompt(email_text: str, recipient: str, tone: str, length: str) -> str:
    length_guidance = {
        "Short": "Keep it concise and to the point with a brief, clear structure.",
        "Balanced": "Keep it polished and balanced, with enough detail to sound professional and clear.",
        "Detailed": "Provide a thorough but still readable version with necessary context and detail.",
    }

    return f"""
You are an expert email editor and writing coach.
Improve the following email for clarity, grammar, tone, and structure.

Requirements:
- Fix language and formatting naturally.
- Keep the meaning intact while making it more polished.
- Adjust the email for the recipient: {recipient}
- Use a {tone} tone.
- {length_guidance.get(length, length_guidance['Balanced'])}
- Avoid adding any greeting or closing if they are not needed.
- Return only the improved email text.
- Do not include notes, explanations, or labels.

Original email:
{email_text}
""".strip()
