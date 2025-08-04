import streamlit as st
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.extract import extract_text_from_pdf, extract_text_from_youtube, extract_text_from_web
from agents.summarize import summarize_text
from agents.qa import run_gemini_qa

# --- Page Config ---
st.set_page_config(page_title="Synthescript", layout="centered")

# --- Header ---
st.title("📘 Synthescript")
st.caption("Upload PDFs or paste YouTube/Web URLs to get smart summaries & ask content-aware questions.")

# --- Input Selection ---
st.header("Step 1: Provide Input")
input_type = st.radio("Choose Input Type:", ["📄 PDF Upload", "🔗 YouTube/Web URL"])
user_input = None
extracted_text = None

# PDF Upload
if input_type == "📄 PDF Upload":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file:
        st.success("✅ PDF uploaded successfully.")
        user_input = uploaded_file

# URL Input
elif input_type == "🔗 YouTube/Web URL":
    url = st.text_input("Enter the YouTube or Website URL:")
    if url:
        st.success("✅ URL submitted successfully.")
        user_input = url

# --- Text Extraction ---
st.divider()
st.header("Step 2: Content Summary")
if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = None

if user_input and input_type == "📄 PDF Upload":
    if st.session_state.extracted_text is None:
        with st.spinner("Extracting text from PDF..."):
            extracted_text = extract_text_from_pdf(user_input)
            st.session_state.extracted_text = extracted_text
    else:
        extracted_text = st.session_state.extracted_text

    st.success("✅ Text extraction complete.")
    #st.text_area("Extracted Text (preview)", extracted_text[:1000] + "..." if len(extracted_text) > 1000 else extracted_text, height=300)

elif input_type == "🔗 YouTube/Web URL" and user_input:
    if st.session_state.extracted_text is None:
        if "youtube.com" in user_input or "youtu.be" in user_input:
            with st.spinner("Extracting transcript from YouTube..."):
                try:
                    extracted_text = extract_text_from_youtube(user_input)
                    st.session_state.extracted_text = extracted_text
                    st.success("✅ Transcript extracted.")
                except Exception as e:
                    st.error(f"❌ Could not extract YouTube transcript: {str(e)}")
                    extracted_text = None
        else:
            with st.spinner("Extracting content from web page..."):
                try:
                    extracted_text = extract_text_from_web(user_input)
                    st.session_state.extracted_text = extracted_text
                    st.success("✅ Web content extracted.")
                except Exception as e:
                    st.error(f"❌ Could not extract web content: {str(e)}")
                    extracted_text = None
    else:
        extracted_text = st.session_state.extracted_text

    # if extracted_text:
        #st.text_area("Extracted Text (preview)", extracted_text[:1000] + "..." if len(extracted_text) > 1000 else extracted_text, height=300)


# --- Summary ---
if extracted_text:
    with st.spinner("Summarizing content..."):
        summary = summarize_text(extracted_text)
    st.subheader("📝 Summary")
    st.success(summary)

# --- Q&A Placeholder ---
st.divider()
st.header("Step 3: Ask Questions")

enable_qa = st.checkbox("Enable QA", value=False)

if enable_qa and extracted_text:
    question = st.text_input("Ask your question here:")
    if question:
        with st.spinner("Getting answer from Gemini 2.5 Pro..."):
            try:
                answer = run_gemini_qa(extracted_text, question)  # function you defined
                st.success("✅ Answer generated:")
                st.write(answer)
            except Exception as e:
                st.error(f"❌ Failed to get answer: {str(e)}")

