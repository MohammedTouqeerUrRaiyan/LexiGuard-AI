import streamlit as st
import requests

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="LexiGuard AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# Header
# ==========================================================

st.title("⚖️ LexiGuard AI")
st.caption("AI-Powered Contract Intelligence Platform")

st.markdown(
    """
Analyze legal contracts using AI.

Features:
- OCR Extraction
- Clause Detection
- Risk Assessment
- Semantic Search
- Named Entity Recognition
- Contract Health Score
"""
)

st.divider()

# ==========================================================
# Upload Contract
# ==========================================================

uploaded_file = st.file_uploader(
    label="Upload Contract",
    type=["pdf", "txt", "png", "jpg", "jpeg"],
    help="Supported formats: PDF, TXT, PNG, JPG, JPEG"
)

if uploaded_file:

    st.success("File uploaded successfully.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Filename",
            uploaded_file.name
        )

    with col2:
        st.metric(
            "Size",
            f"{uploaded_file.size / 1024:.2f} KB"
        )

    with col3:
        st.metric(
            "File Type",
            uploaded_file.type
        )

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

st.divider()

# ==========================================================
# Analyze Button
# ==========================================================

st.write("")

if st.button(
    "🚀 Analyze Contract",
    use_container_width=True
):

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
            
            # Check if backend gracefully failed (e.g. blank document)
            if result.get("status") == "Failed":
                st.error(result.get("message", "Analysis failed."))
                st.stop()

        except Exception as e:
            st.error(e)
            st.stop()

    # ==========================================================
    # Alignment with Secure Backend Data Model
    # ==========================================================
    analysis_results = result.get("analysis_results", {})
    detected_clauses = analysis_results.get("detected_clauses", [])
    missing_count = analysis_results.get("missing_clauses", 0)
    risk_score = analysis_results.get("risk_score", "Low")
    
    # Safely extract missing metadata details if provided, fallback safely
    missing_clauses = analysis_results.get("missing_clauses_details", [])

    st.success("Analysis Complete!")
    st.markdown("---")

    # ==========================================================
    # Executive Dashboard
    # ==========================================================
    st.subheader("📈 Executive Dashboard")

    score_col, risk_col = st.columns(2)

    # Calculate an automated score metrics based on structural gaps
    total_clauses = len(detected_clauses) + missing_count
    health_percentage = int((len(detected_clauses) / total_clauses) * 100) if total_clauses > 0 else 100

    score_col.metric(
        "📊 Structural Integrity",
        f'{health_percentage}/100'
    )

    if risk_score == "High":
        risk_col.error(f"🔴 Risk Level: {risk_score}")
    elif risk_score == "Medium":
        risk_col.warning(f"🟠 Risk Level: {risk_score}")
    else:
        risk_col.success(f"🟢 Risk Level: {risk_score}")

    st.progress(
        health_percentage / 100,
        text=f'Overall Contract Health Profile: {health_percentage}%'
    )

    st.markdown("---")

    # ==========================================================
    # Document Overview Metrics
    # ==========================================================
    st.subheader("📊 Document Overview")

    stats1, stats2 = st.columns(2)

    stats1.metric(
        "✅ Clauses Found",
        len(detected_clauses)
    )

    stats2.metric(
        "❌ Missing Segments",
        missing_count
    )

    st.markdown("---")

    # ==========================================================
    # Clause Analysis Display (Sprint 1 Refactored Layout)
    # ==========================================================
    left, right = st.columns(2)

    with left:
        st.subheader("✅ Detected Clauses")
        st.write("")

        if detected_clauses:
            for clause in detected_clauses:
                clause_title = clause.get("clause", "Unknown Clause")
                
                # Using custom headers and sub-metrics for Step 2 Target Layout
                st.markdown(f"#### {clause_title}")
                
                c_col1, c_col2 = st.columns(2)
                with c_col1:
                    st.caption("Confidence")
                    st.markdown(f"**{clause.get('confidence', 0)}%**")
                with c_col2:
                    st.caption("Matched Keywords")
                    keywords = clause.get("matched_keywords", [])
                    if keywords:
                        st.markdown(" ".join([f"`{kw}`" for kw in keywords]))
                    else:
                        st.markdown("*None*")
                
                st.caption("Matched Text")
                st.info(f'"{clause.get("matched_text", "No specific clause snippet matched.")}"')
                
                st.caption("Description")
                st.write(clause.get("description", "No summary text provided."))
                
                st.caption("Recommendation")
                st.write(clause.get("recommendation", "None"))
                
                st.markdown("---")
        else:
            st.info("No explicit structural clauses detected.")

    with right:
        st.subheader("❌ Missing Clauses")
        st.write("")

        if missing_clauses:
            for clause in missing_clauses:
                # Step 1 Target Layout matching markdown specifications
                st.markdown(f"#### ⚠ {clause.get('clause', 'Required Element')}")
                
                st.caption("Importance")
                imp = clause.get("importance", "High")
                if imp == "High":
                    st.markdown(f"🔴 **{imp}**")
                else:
                    st.markdown(f"🟡 **{imp}**")
                    
                st.caption("Description")
                st.write(clause.get("description", "Omitted requirement."))
                
                st.caption("Recommendation")
                st.write(clause.get("recommendation", "Incorporate this missing term."))
                
                st.markdown("---")
        elif missing_count > 0:
            st.warning(f"⚠️ {missing_count} essential legal protections are absent from this text.")
        else:
            st.success("All crucial structural terms are present.")

    # ==========================================================
    # Brain Search Matches
    # ==========================================================
    st.markdown("---")
    st.subheader("🧠 Semantic Clause Matches")

    semantic_matches = result.get("semantic_matches", [])
    if semantic_matches:
        for match in semantic_matches:
            clause_name = match.get('metadata', {}).get('clause', 'Clause Match')
            score = match.get('similarity', match.get('score', 0))
            
            # Format similarity score if presented as a float
            if isinstance(score, float) and score <= 1.0:
                score = round(score * 100, 2)

            with st.expander(f"🔍 {clause_name} (Match: {score}%)"):
                st.write(match.get("text", match.get("document", "Context text missing.")))
    else:
        st.info("No contextually relevant vector embedding matches found.")