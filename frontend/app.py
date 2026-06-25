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
# Title & Brand
# -----------------------------
st.title("📄 LexiGuard AI")
st.caption("AI-Powered Contract Intelligence Platform | Secure Legal Analysis")
st.markdown("---")

# -----------------------------
# Input Methods (Using Tabs for Clean Layout Selection)
# -----------------------------
tab1, tab2 = st.tabs(["📤 Upload File", "📝 Paste Text"])
text_to_analyze = ""

with tab1:
    uploaded_file = st.file_uploader(
        "Upload Contract",
        type=["txt", "pdf", "png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:

        st.success(f"Uploaded: {uploaded_file.name}")

        file_type = uploaded_file.type

        if file_type == "text/plain":
            text_to_analyze = uploaded_file.read().decode("utf-8")

            with st.expander("Preview"):
                st.text(text_to_analyze)

        elif file_type == "application/pdf":

            st.info(
                "PDF uploaded successfully. OCR/PDF parsing integration coming soon."
            )

        elif file_type.startswith("image/"):

            st.image(
                uploaded_file,
                caption="Uploaded Contract Image",
                use_container_width=True
            )

            st.info(
                "Image uploaded successfully. OCR integration coming soon."
            )

with tab2:
    contract_text = st.text_area(
        "Paste your contract draft here:",
        height=250,
        placeholder="Type or paste contract clauses here..."
    )
    # If the user pasted text and didn't upload a file, use the pasted text
    if not text_to_analyze.strip():
        text_to_analyze = contract_text

# -----------------------------
# Analyze Execution Button
# -----------------------------
st.write("")
if st.button("🚀 Analyze Contract", use_container_width=True):

    # Validate input explicitly
    if not text_to_analyze.strip():
        st.error("⚠️ Please provide contract text by uploading a file or pasting content.")
    else:
        with st.spinner("Analyzing contract syntax and processing risk metrics..."):
            try:
                # Send request to FastAPI backend
                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    json={"text": text_to_analyze},
                    timeout=10
                )

                if response.status_code != 200:
                    st.error(f"Backend API Error: System returned status code {response.status_code}")
                    st.stop()

                result = response.json()

                # -----------------------------
                # Display Analysis Results
                # -----------------------------
                st.success("✨ Analysis Complete!")
                
                # Risk Metric Breakdown Display
                risk_level = result.get('risk_level', 'Unknown')
                st.subheader("⚠️ Risk Assessment")
                
                if risk_level == "High":
                    st.error("🚨 HIGH RISK: This contract contains critical liability, damages, or exposure terms.")
                elif risk_level == "Medium":
                    st.warning("⚠️ MEDIUM RISK: Termination or conditional warning clauses detected.")
                else:
                    st.info("✅ LOW RISK: Standard baseline vocabulary identified.")

                # Document Metrics Row
                st.subheader("📊 Document Statistics")
                col1, col2 = st.columns(2)
                col1.metric(label="Total Word Count", value=f"{result.get('word_count', 0):,}")
                col2.metric(label="Character Count", value=f"{result.get('character_count', 0):,}")

                # Context Alignment Split Columns
                st.markdown("---")
                col_clauses, col_keywords = st.columns(2)

                with col_clauses:
                    st.subheader("📑 Clauses Detected")
                    clauses = result.get("clauses_detected", [])
                    if clauses:
                        for clause in clauses:
                            st.markdown(f"• **`{clause}`**")
                    else:
                        st.caption("No standard legal clauses detected.")

                with col_keywords:
                    st.subheader("🔑 Risk Keywords")
                    keywords = result.get("keywords_found", [])
                    if keywords:
                        # Displaying keywords as interactive inline tags
                        st.write(", ".join([f"`{kw}`" for kw in keywords]))
                    else:
                        st.caption("No actionable risk keywords flag triggered.")

            except requests.exceptions.RequestException as e:
                st.error(f"🔌 Connection Failure: Could not connect to the FastAPI backend service. Is it running? Details: {e}")
            except Exception as e:
                st.error(f"Unexpected operational error occured: {e}")