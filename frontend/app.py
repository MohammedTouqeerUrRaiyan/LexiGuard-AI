import streamlit as st
import requests

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="LexiGuard AI",
    page_icon="📄",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("📄 LexiGuard AI")
st.write("AI-Powered Contract Intelligence Platform")

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a contract",
    type=["txt"]
)

uploaded_text = ""

if uploaded_file is not None:
    try:
        uploaded_text = uploaded_file.read().decode("utf-8")

        st.subheader("📄 Uploaded Contract")
        st.write(uploaded_text)

    except Exception as e:
        st.error(f"Error reading file: {e}")

# -----------------------------
# Manual Input
# -----------------------------
contract_text = st.text_area(
    "Paste your contract here:",
    height=300
)

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("Analyze Contract"):

    # Choose input source
    text_to_analyze = uploaded_text if uploaded_text.strip() else contract_text

    # Validate input
    if not text_to_analyze.strip():
        st.error("Please upload or enter a contract.")

    else:
        try:
            # Send request to FastAPI
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={"text": text_to_analyze},
                timeout=10
            )

            if response.status_code != 200:
                st.error(f"API Error: {response.status_code}")
                st.stop()

            result = response.json()

            # -----------------------------
            # Display Results
            # -----------------------------
            st.success("Analysis Complete!")

            st.subheader("📊 Statistics")
            st.write(f"Word Count: {result.get('word_count', 0)}")
            st.write(f"Character Count: {result.get('character_count', 0)}")

            # -----------------------------
            # Keywords
            # -----------------------------
            st.subheader("🔑 Keywords Found")

            keywords = result.get("keywords_found", [])

            if keywords:
                for keyword in keywords:
                    st.write(f"✅ {keyword}")
            else:
                st.write("No keywords detected.")

            # -----------------------------
            # Clauses
            # -----------------------------
            st.subheader("📑 Clauses Detected")

            clauses = result.get("clauses_detected", [])

            if clauses:
                for clause in clauses:
                    st.write(f"📌 {clause}")
            else:
                st.write("No clauses detected.")

            # -----------------------------
            # Risk Level
            # -----------------------------
            st.subheader("⚠️ Risk Level")
            st.write(result.get("risk_level", "Unknown"))

            # -----------------------------
            # Status
            # -----------------------------
            st.subheader("✅ Status")
            st.write(result.get("status", "No status returned"))

        except requests.exceptions.RequestException as e:
            st.error(f"Failed to connect to backend: {e}")

        except Exception as e:
            st.error(f"Unexpected error: {e}")