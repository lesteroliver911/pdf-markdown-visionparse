import streamlit as st
from vision_parse import VisionParser, PDFPageConfig
import os
from typing import Dict

# Define model configurations
MODEL_CONFIGS: Dict[str, Dict[str, str]] = {
    "OpenAI": {
        "gpt-4o": "GPT-4o",
        "gpt-4o-mini": "GPT-4o Mini"
    },
    "Google Gemini": {
        "gemini-1.5-flash": "Gemini 1.5 Flash",
        "gemini-2.0-flash-exp": "Gemini 2.0 Flash Exp",
        "gemini-1.5-pro": "Gemini 1.5 Pro"
    },
    "Meta Llama & LLaVA": {
        "llava:13b": "LLaVA 13B",
        "llava:34b": "LLaVA 34B",
        "llama3.2-vision:11b": "Llama 3.2 Vision 11B",
        "llama3.2-vision:70b": "Llama 3.2 Vision 70B"
    }
}

def initialize_parser(provider: str, model_name: str, api_key: str):
    # Configure PDF processing settings
    page_config = PDFPageConfig(
        dpi=400,
        color_space="RGB",
        include_annotations=True,
        preserve_transparency=False
    )
    
    # Initialize parser with selected model
    parser = VisionParser(
        model_name=model_name,
        api_key=api_key,
        temperature=0.7,
        top_p=0.4,
        extraction_complexity=True
    )
    return parser

# Streamlit UI
st.title("PDF to Markdown Converter")

# Provider selection
provider = st.selectbox(
    "Select Provider",
    options=list(MODEL_CONFIGS.keys())
)

# Model selection based on provider
model_name = st.selectbox(
    "Select Model",
    options=list(MODEL_CONFIGS[provider].keys()),
    format_func=lambda x: MODEL_CONFIGS[provider][x]
)

# API key input with provider-specific help
api_key_help = {
    "OpenAI": "Get OpenAI API key from https://platform.openai.com/api-keys",
    "Google Gemini": "Get Gemini API key from https://aistudio.google.com/app/apikey",
    "Meta Llama & LLaVA": "Enter Ollama API endpoint (default: http://localhost:11434)"
}

api_key = st.text_input(
    f"Enter {provider} {'API Key' if provider != 'Meta Llama & LLaVA' else 'Endpoint'}",
    type="password" if provider != "Meta Llama & LLaVA" else "default",
    help=api_key_help[provider]
)

# File uploader
uploaded_file = st.file_uploader("Upload PDF file", type=['pdf'])

if uploaded_file and api_key:
    if st.button("Convert to Markdown"):
        try:
            with st.spinner(f"Processing with {MODEL_CONFIGS[provider][model_name]}..."):
                # Save uploaded file temporarily
                temp_path = f"temp_{uploaded_file.name}"
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Initialize parser and convert
                parser = initialize_parser(provider, model_name, api_key)
                markdown_pages = parser.convert_pdf(temp_path)
                
                # Display results
                st.success("Conversion completed!")
                for i, page_content in enumerate(markdown_pages):
                    with st.expander(f"Page {i+1}"):
                        st.markdown(page_content)
                
                # Cleanup
                os.remove(temp_path)
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
