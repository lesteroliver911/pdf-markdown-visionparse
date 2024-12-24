# PDF-Markdown-VisionParse

A simple Streamlit UI wrapper for [vision-parse](https://github.com/iamarunbrahma/vision-parse) to convert PDFs to Markdown using AI vision models.

## Results
![PDF to Markdown Conversion Interface](https://raw.githubusercontent.com/lesteroliver911/pdf-markdown-visionparse/main/pdf-markdown-vision-parse.png)

## Vision Parse
I was looking for an open-source PDF to Markdown library and came across [vision-parse](https://github.com/iamarunbrahma/vision-parse) by [iamarunbrahma](https://github.com/iamarunbrahma). The library did such a good job converting tables and getting text into LLM-friendly .md format that I decided to give it a simple Streamlit UI. Keeping it open source so people can do what they like with it!

## What it does
- Provides a simple web interface to convert PDFs to Markdown
- Supports multiple AI vision models:
 - OpenAI (GPT-4o)
 - Google Gemini
 - Meta's Llama & LLaVA
- Shows real-time conversion progress
- Displays markdown output page by page

## Getting Started
1. Clone this repo
  ```bash
  git clone https://github.com/lesteroliver911/pdf-markdown-visionparse.git
  cd pdf-markdown-visionparse
2. Install requirements: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`
4. Add your API key for your preferred AI model
5. Upload a PDF and convert!

## Credits
This project [vision-parse](https://github.com/iamarunbrahma/vision-parse) by [iamarunbrahma](https://github.com/iamarunbrahma). All the heavy lifting of PDF processing and AI model integration is handled by their excellent library.

## License
MIT - Do whatever you want with it! 😊
