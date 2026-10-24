import streamlit as st

from ai_provider import get_provider
from config import settings
from prompt_builder import build_email_improvement_prompt
from ui import render_result_area
from validation import (
    validate_api_key,
    validate_email_text,
    validate_length,
    validate_recipient,
    validate_tone,
)


st.set_page_config(page_title="AI Email Improver", page_icon="✉️")


def main() -> None:
    st.title("AI Email Improver @R_Dahdal@")
    st.caption("Paste your original email, choose the recipient and tone, and refine it before sending.")

    with st.sidebar:
        st.header("Settings")
        api_key = st.text_input(
            "Google API Key",
            type="password",
            value=settings.google_api_key,
            help="Add your Gemini API key. Keep this secure and never share it.",
        )
        provider_name = st.selectbox("AI Provider", ["google"], index=0)
        model_name = st.text_input("Model", value=settings.gemini_model)

    recipient = st.selectbox(
        "Select recipient",
        ["Client", "Colleague", "Manager", "Recruiter", "Professor", "Friend", "General"],
        index=6,
    )
    tone = st.selectbox(
        "Select tone",
        ["Professional", "Friendly", "Formal", "Persuasive", "Concise"],
        index=0,
    )
    length = st.selectbox(
        "Choose length",
        ["Short", "Balanced", "Detailed"],
        index=1,
    )

    original_email = st.text_area(
        "Paste original email",
        height=260,
        placeholder="Write or paste your email here...",
    )

    if st.button("Improve My Email", use_container_width=True):
        try:
            cleaned_email = validate_email_text(original_email)
            cleaned_api_key = validate_api_key(api_key or settings.google_api_key)
            cleaned_recipient = validate_recipient(recipient)
            cleaned_tone = validate_tone(tone)
            cleaned_length = validate_length(length)

            prompt = build_email_improvement_prompt(
                cleaned_email,
                cleaned_recipient,
                cleaned_tone,
                cleaned_length,
            )
            provider = get_provider(provider_name, cleaned_api_key, model_name)
            improved_email = provider.generate(prompt).strip()

            if not improved_email:
                raise ValueError("The AI model did not return any improved email text.")

            st.session_state["improved_email"] = improved_email
        except ValueError as exc:
            st.error(str(exc))
        except Exception as exc:
            st.error(f"Something went wrong while generating the email. Please verify your API key and model. Error: {exc}")

    if "improved_email" in st.session_state:
        render_result_area(st.session_state["improved_email"])


if __name__ == "__main__":
    main()
