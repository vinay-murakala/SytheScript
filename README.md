# 📘 SyntheScript

**Intelligent Content Analysis & Summarization Tool**

SyntheScript is a powerful Streamlit-based web application that extracts text from PDFs, YouTube videos, and web pages, then generates intelligent summaries using Google's Gemini AI. Perfect for researchers, students, and content creators who need quick insights from various content sources.

## ✨ Features

- **📄 PDF Processing**: Extract and analyze text from uploaded PDF documents
- **🎥 YouTube Transcripts**: Get transcripts and summaries from YouTube videos
- **🌐 Web Content**: Extract and summarize content from web pages
- **🤖 AI-Powered Summaries**: Generate detailed, bullet-point summaries using Gemini 2.5 Pro
- **💬 Q&A Capability**: Ask questions about extracted content (enabled via checkbox)
- **🔄 Session Persistence**: Maintains extracted content across interactions
- **🎨 Clean Interface**: User-friendly Streamlit web interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd SyntheScript
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root:

   ```env
   GEMINI_API_KEY=your_google_gemini_api_key_here
   ```

4. **Run the application:**

   ```bash
   streamlit run SYNTHESCRIPT/main.py
   ```

5. **Open your browser:**
   Navigate to `http://localhost:8501`

## 📖 Usage Guide

### Step 1: Provide Input

Choose your input method:

- **📄 PDF Upload**: Upload a PDF file directly
- **🔗 YouTube/Web URL**: Paste a YouTube or website URL

### Step 2: Content Extraction

The application will automatically:

- Extract text from PDFs using PyMuPDF
- Fetch YouTube transcripts using YouTube Transcript API
- Scrape web content using BeautifulSoup
- Display progress indicators during extraction

### Step 3: AI Summarization

- Content is automatically summarized using Gemini 2.5 Pro
- Summaries include key points in bullet format
- Large texts are intelligently truncated for optimal processing

### Step 4: Ask Questions

- Enable Q&A mode using the checkbox
- Ask specific questions about the extracted content
- Get context-aware answers based on the extracted text

## 🏗️ Architecture

```
SYNTHESCRIPT/
├── main.py              # Streamlit web application
├── agents/
│   ├── extract.py       # Text extraction from various sources
│   ├── summarize.py     # AI-powered summarization
│   └── qa.py           # Question & Answer functionality
├── requirements.txt     # Python dependencies
└── README.md          # This file
```

## 🔧 Technical Details

### Dependencies

- **streamlit**: Web interface framework
- **pymupdf**: PDF text extraction
- **youtube-transcript-api**: YouTube transcript retrieval
- **beautifulsoup4**: Web content scraping
- **google-generativeai**: Gemini AI integration
- **google-cloud-aiplatform**: Vertex AI integration
- **requests**: HTTP requests for web scraping
- **lxml_html_clean**: HTML cleaning utilities

### API Requirements

- **Google Gemini API**: Required for AI summarization and Q&A
- **YouTube Transcript API**: For YouTube video transcript extraction

### Content Limits

- **Web Content**: Limited to 5,000 characters for optimal processing
- **PDF Processing**: No specific limit, but large files may take longer
- **YouTube Transcripts**: Full transcript extraction supported

## 🛠️ Development

### Project Structure

The application follows a modular architecture:

- **`main.py`**: Main Streamlit application with UI logic
- **`agents/`**: Core functionality modules
  - `extract.py`: Text extraction from various sources
  - `summarize.py`: AI summarization using Gemini
  - `qa.py`: Question-answering capabilities

### Adding New Features

1. **New Input Sources**: Add extraction functions to `agents/extract.py`
2. **Custom Summarization**: Modify prompts in `agents/summarize.py`
3. **Enhanced Q&A**: Extend `agents/qa.py` with new capabilities
4. **File Type Support**: Extend the file uploader in `main.py` to support more formats

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**

   - Ensure `GEMINI_API_KEY` is set in your `.env` file
   - Verify the API key is valid and has sufficient quota

2. **PDF Upload Issues**

   - Check file format (PDF only)
   - Ensure file is not corrupted or password-protected

3. **YouTube Transcript Errors**

   - Verify the video has available transcripts
   - Check if the video is public and accessible

4. **Web Scraping Issues**
   - Some websites may block automated requests
   - Check if the URL is accessible

### Error Messages

- **"Could not extract YouTube transcript"**: Video may not have transcripts or is private
- **"Could not extract web content"**: Website may be blocking requests or inaccessible
- **"Failed to summarize"**: API key issue or content too large


## 🙏 Acknowledgments

- **Google Gemini AI**: For powerful AI summarization capabilities
- **Streamlit**: For the excellent web framework
- **PyMuPDF**: For robust PDF processing
- **YouTube Transcript API**: For video transcript extraction

