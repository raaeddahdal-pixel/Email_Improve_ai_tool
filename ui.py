import streamlit as st
from streamlit.components.v1 import html


def copy_to_clipboard_js(text: str) -> None:
    escaped_text = text.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n").replace("\r", "")
    html(
        f"""
        <script>
        const text = `{escaped_text}`;
        navigator.clipboard.writeText(text).then(() => {{
            const button = document.getElementById('copy-email');
            if (button) {{
                button.textContent = 'Copied!';
                setTimeout(() => {{ button.textContent = 'Copy Improved Email'; }}, 1500);
            }}
        }}).catch(() => {{
            const button = document.getElementById('copy-email');
            if (button) {{
                button.textContent = 'Copy failed';
            }}
        }});
        </script>
        """,
        height=0,
    )


def render_result_area(improved_email: str) -> None:
    st.subheader("Improved Email")
    result = st.text_area(
        "Review and copy the improved text",
        value=improved_email,
        height=280,
        key="improved_email_area",
    )

    if st.button("Copy Improved Email", key="copy-email"):
        copy_to_clipboard_js(result)
