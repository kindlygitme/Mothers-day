import re
import streamlit as st
from PIL import Image
import base64

# Configure full screen layout and theme
st.set_page_config(page_title="YouTube Timestamp Extractor", layout="wide")

# Custom CSS for full blue background
st.markdown("""
    <style>
    .stApp {
        background-color: #003366;
    }
    .big-title {
        font-size: 40px;
        text-align: center;
        color: white;
        margin-top: 20px;
        font-weight: bold;
    }
    .header-text {
        font-size: 30px;
        text-align: center;
        color: white;
        margin-top: 30px;
        font-weight: bold;
    }
    .upload-button button {
        background-color: red !important;
        color: white !important;
        font-weight: bold;
        font-size: 18px !important;
    }
    .output-box {
        background-color: white;
        color: black;
        padding: 10px;
        border-radius: 10px;
        height: 400px;
        overflow-y: auto;
        font-family: Courier;
    }
    .matched-word {
        color: red;
        font-weight: bold;
    }
    .transcript-text {
        color: white;
        font-weight: bold;
    }
    .quote-text {
        color: white;
        font-size: 24px;
        text-align: center;
        font-style: italic;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="big-title">HELLO RAVI</div>', unsafe_allow_html=True)

# Mother's Day Special Heading
st.markdown('<div class="header-text">🌸 Mother\'s Day Special 🌸</div>', unsafe_allow_html=True)

# Mother's Day Quote
st.markdown('<div class="quote-text">"A mother is she who can take the place of all others, but whose place no one else can take." - Cardinal Mermillod</div>', unsafe_allow_html=True)

# Layout: 2 columns
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="header-text">### ✍️ Paste Transcript Here:</div>', unsafe_allow_html=True)
    transcript = st.text_area("Paste transcript here...", height=400, label_visibility="collapsed")

with col2:
    st.markdown('<div class="header-text">### 📄 Matched Output:</div>', unsafe_allow_html=True)
    output_container = st.empty()

# Improved regex pattern
regex_pattern = r"\b(maa|mummy|parents|mother)\b"

# Function to extract matches
def extract_matches(text, pattern):
    regex = re.compile(pattern, re.IGNORECASE)
    # Split by line breaks, then filter out lines with no matches
    lines = text.strip().split('\n')
    results = []
    
    # Process each line to match against the pattern
    for i in range(0, len(lines), 2):  # Assuming each timestamp is followed by the text
        timestamp = lines[i].strip()
        sentence = lines[i+1].strip() if i + 1 < len(lines) else ""
        
        # Check for a match with the regex
        match = regex.search(sentence)
        if match:
            matched = match.group(0)
            results.append(f"{timestamp} → {sentence} ⟶ [Matched: {matched}]")
            
    return results

# Upload Button
upload_button = st.button("UPLOAD", type="primary")

# Clear Button
clear_button = st.button("CLEAR Transcript")

# Clear action
if clear_button:
    transcript = ""  # Clear the transcript field
    output_container.empty()  # Clear the output container

if upload_button:
    if transcript.strip():
        result_lines = extract_matches(transcript, regex_pattern)
        if result_lines:
            formatted_result = "\n".join(result_lines)
            output_container.markdown(f'<div class="output-box">{formatted_result.replace("\n", "<br>")}</div>', unsafe_allow_html=True)

            # Save for download
            b64 = base64.b64encode(formatted_result.encode()).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="regex_matches.txt">📥 <b style="color:white;">Download Output</b></a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            output_container.markdown('<div class="output-box">❌ <b>No matches found.</b></div>', unsafe_allow_html=True)
    else:
        output_container.markdown('<div class="output-box">⚠️ Please paste a transcript first.</div>', unsafe_allow_html=True)
