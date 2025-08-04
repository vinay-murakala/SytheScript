import fitz
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import parse_qs

def extract_text_from_pdf(pdf_file) -> str:
    """
    Extracts and returns text from an uploaded PDF file using PyMuPDF.
    
    Args:
        pdf_file: A file-like object from Streamlit uploader.

    Returns:
        str: Cleaned extracted text from the PDF.
    """
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    full_text = ""

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        full_text += f"\n\n--- Page {page_num} ---\n{text}"

    doc.close()
    return full_text.strip()

def extract_text_from_youtube(url: str) -> str:
    # Extract video ID from URL
    parsed_url = urlparse(url)
    if 'youtube.com' in parsed_url.netloc:
        query_params = parse_qs(parsed_url.query)
        video_id = query_params.get("v", [None])[0]
    elif 'youtu.be' in parsed_url.netloc:
        video_id = parsed_url.path.strip("/")
    else:
        raise ValueError("Invalid YouTube URL format.")

    if not video_id:
        raise ValueError("Unable to extract video ID from URL.")

    # Fetch transcript
    try:
        transcript_list = YouTubeTranscriptApi().fetch(video_id)
    except Exception as e:
        raise RuntimeError(f"Error fetching transcript: {str(e)}")

    # Combine transcript text
    transcript_text = " ".join([entry.text for entry in transcript_list])

    return transcript_text

def extract_text_from_web(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove script and style tags
        for tag in soup(['script', 'style', 'noscript']):
            tag.decompose()

        # Get visible text
        text = soup.get_text(separator='\n', strip=True)

        # Optional: Trim long content
        return text[:5000]  # Limit to first 5000 characters for summary
    except Exception as e:
        raise RuntimeError(f"Error extracting web content: {str(e)}")