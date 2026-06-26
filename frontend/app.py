import streamlit as st
import requests

# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="LexiGuard AI",
    page_icon="⚖️",
    layout="wide"
)

# ============================================
# Header
# ============================================

st.title("⚖️ LexiGuard AI")
st.caption("AI-Powered Contract Intelligence Platform")
st.markdown("---")

# ============================================
# Upload Section
# ============================================

uploaded_file = st.file_uploader(
    "Upload Contract",
    type=["txt", "pdf", "png", "jpg", "jpeg"],
    help="Supported formats: TXT, PDF, PNG, JPG, JPEG"
)

if uploaded_file:

    st.success("File uploaded successfully.")

    col1, col2, col3 = st.columns(3)

    col1.metric("Filename", uploaded_file.name)

    col2.metric(
        "Size",
        f"{uploaded_file.size/1024:.2f} KB"
    )

    col3.metric(
        "Type",
        uploaded_file.type
    )

    if uploaded_file.type.startswith("image/"):

        st.image(
            uploaded_file,
            caption="Uploaded Contract",
            use_container_width=True
        )

    elif uploaded_file.type == "text/plain":

        preview = uploaded_file.getvalue().decode("utf-8")

        with st.expander("Preview Uploaded Text"):

            st.text(preview)

# ============================================
# Analyze Button
# ============================================

st.write("")

if st.button("🚀 Analyze Contract", use_container_width=True):

    if uploaded_file is None:

        st.error("Please upload a contract.")

        st.stop()

    with st.spinner("Running OCR and AI Analysis..."):

        try:

            files = {

                "file": (

                    uploaded_file.name,

                    uploaded_file.getvalue(),

                    uploaded_file.type

                )

            }

            response = requests.post(

                "http://127.0.0.1:8000/analyze",

                files=files,

                timeout=120

            )

            if response.status_code != 200:

                st.error(response.text)

                st.stop()

            result = response.json()

        except Exception as e:

            st.error(e)

            st.stop()

# ============================================
# Results
# ============================================

    st.success("Analysis Complete!")

    risk = result["risk_level"]

    if risk == "High":

        st.error("🔴 HIGH RISK")

    elif risk == "Medium":

        st.warning("🟠 MEDIUM RISK")

    else:

        st.success("🟢 LOW RISK")

    # ============================================
    # Statistics
    # ============================================

    st.subheader("📊 Document Statistics")

    c1, c2 = st.columns(2)

    c1.metric(
        "Word Count",
        result["word_count"]
    )

    c2.metric(
        "Character Count",
        result["character_count"]
    )

    # ============================================
    # Clauses / Keywords
    # ============================================

    left, right = st.columns(2)

    with left:

        st.subheader("📑 Clauses Detected")

        if result["clauses_detected"]:

            for clause in result["clauses_detected"]:

                st.success(clause)

        else:

            st.info("No clauses detected.")

    with right:

        st.subheader("🔑 Keywords")

        if result["keywords_found"]:

            for word in result["keywords_found"]:

                st.info(word)

        else:

            st.info("No keywords detected.")

    # ============================================
    # OCR Output
    # ============================================

    st.subheader("📄 Extracted Contract")

    with st.expander("View Extracted Text", expanded=False):

        st.text(result["extracted_text"])