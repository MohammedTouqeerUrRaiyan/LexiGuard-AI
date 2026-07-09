import streamlit as st
import requests

# ==========================================================
# Page Configuration
#configure streamlit title
# ==========================================================
#adding application icon

st.set_page_config(
    page_title="LexiGuard AI",
    page_icon="⚖️",
    layout="wide"
)
#enabled wide layout for UI
# ==========================================================
# Header
# ==========================================================

st.title("⚖️ LexiGuard AI")
st.caption("AI-Powered Contract Intelligence Platform")
st.markdown("---")

# ==========================================================
# Upload Section
# ==========================================================
#added fileupload content
uploaded_file = st.file_uploader(
    "Upload Contract",
    type=["pdf", "txt", "png", "jpg", "jpeg"],
    help="Supported formats: PDF, TXT, PNG, JPG, JPEG"
)
#included multiple file formats
#added help option
if uploaded_file:

    st.success("File uploaded successfully.")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Filename",
        uploaded_file.name
    )

    c2.metric(
        "Size",
        f"{uploaded_file.size/1024:.2f} KB"
    )

    c3.metric(
        "Type",
        uploaded_file.type
    )#displayed file info like type and size

    if uploaded_file.type.startswith("image/"):

        st.image(
            uploaded_file,
            use_container_width=True
        )

    elif uploaded_file.type == "text/plain":

        with st.expander("Preview Uploaded Text"):

            st.text(
                uploaded_file.getvalue().decode("utf-8")
            )
#added preview file
# ==========================================================
# Analyze Button
# ==========================================================

st.write("")

if st.button(
    "🚀 Analyze Contract",
    use_container_width=True
):
#created contract analysis trigger
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
#authentication enabled for file check
#integration of backend with  API 
    # ==========================================================
    # Overall Analysis
    # ==========================================================

    analysis = result["analysis"]
    document = result["document"]
    statistics = result["statistics"]

    st.success("Analysis Complete!")

    st.markdown("---")
    # ==========================================================
    # Executive Dashboard
    # ==========================================================

    st.subheader("📈 Executive Dashboard")

    score_col, risk_col, verdict_col = st.columns(3)

    score_col.metric(
        "📊 Contract Score",
        f'{analysis["contract_score"]}/100'
    )

    risk = analysis["risk_level"]

    if risk == "High":
        risk_col.error(f"🔴 {risk}")

    elif risk == "Medium":
        risk_col.warning(f"🟠 {risk}")

    else:
        risk_col.success(f"🟢 {risk}")

    verdict_col.metric(
        "⚖ Final Verdict",
        analysis["verdict"]
    )

    st.progress(
        analysis["contract_health"] / 100,
        text=f'Overall Contract Health : {analysis["contract_health"]}%'
    )

    st.markdown("### 📝 Executive Summary")

    st.info(
        analysis["summary"]
    )

    st.markdown("---")

    # ==========================================================
    # Statistics
    # ==========================================================

    st.subheader("📊 Document Statistics")

    a, b, c, d = st.columns(4)

    a.metric(
        "Words",
        document["word_count"]
    )

    b.metric(
        "Characters",
        document["character_count"]
    )

    c.metric(
        "Detected Clauses",
        statistics["detected_clauses"]
    )

    d.metric(
        "Missing Clauses",
        statistics["missing_clauses"]
    )

    # ==========================================================
    # Clause Analysis
    # ==========================================================

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        st.subheader("✅ Detected Clauses")

        if result["clauses"]["detected"]:
            st.write(result["clauses"]["detected"])
            
            for clause in result["clauses"]["detected"]:

                with st.expander(clause["clause"]):

                    st.write(
                        f'**Importance:** {clause["importance"]}'
                    )

                    st.write(
                        f'**Description:** {clause["description"]}'
                    )

                    st.write(
                        f'**Recommendation:** {clause["recommendation"]}'
                    )

        else:

            st.info("No clauses detected.")

    with right:

        st.subheader("❌ Missing Clauses")

        if result["clauses"]["missing"]:

            for clause in result["clauses"]["missing"]:

                with st.expander(clause["clause"]):

                    st.write(
                        f'**Importance:** {clause["importance"]}'
                    )

                    st.write(
                        f'**Description:** {clause["description"]}'
                    )

                    st.write(
                        f'**Recommendation:** {clause["recommendation"]}'
                    )

        else:

            st.success("No important clauses missing.")

    # ==========================================================
    # Risk Factors
    # ==========================================================

    st.markdown("---")

    st.subheader("⚠ Risk Factors")

    if result.get("risk_factors"):

        for factor in result["risk_factors"]:

            st.warning(factor)

    else:

        st.success("No significant legal risks detected.")

    # ==========================================================
    # Legal Warnings
    # ==========================================================

    st.subheader("🚨 Legal Warnings")

    if result["warnings"]:

        for warning in result["warnings"]:

            st.warning(warning)

    else:

        st.success("No warnings generated.")

    # ==========================================================
    # Keywords
    # ==========================================================

    st.markdown("---")

    st.subheader("🔑 Keywords Found")

    if result["keywords_found"]:

        cols = st.columns(4)

        for index, word in enumerate(result["keywords_found"]):

            cols[index % 4].success(word)

    else:

        st.info("No keywords found.")

    # ==========================================================
    # Named Entities
    # ==========================================================

    st.markdown("---")

    st.subheader("🏷 Named Entities")

    entities = result.get(
        "entities_detected",
        {}
    )

    if entities:

        st.json(entities)

    else:

        st.info("No legal entities detected.")

    # ==========================================================
    # OCR Output
    # ==========================================================

    st.markdown("---")

    st.subheader("📄 Extracted Contract")

    with st.expander(
        "View OCR Extracted Text"
    ):

        st.text(
            result["extracted_text"]
        )