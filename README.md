# PDF-Markdown-VisionParse
A simple Streamlit UI wrapper for [vision-parse](https://github.com/iamarunbrahma/vision-parse) to convert PDFs to Markdown using AI vision models.

## UI
![PDF to Markdown Conversion Interface](https://github.com/lesteroliver911/pdf-markdown-visionparse/blob/main/pdf-markdown-vision-parse-one.png)

## The Story
I was looking for an open-source PDF to Markdown library and came across [vision-parse](https://github.com/iamarunbrahma/vision-parse) by [iamarunbrahma](https://github.com/iamarunbrahma). The library did such a good job converting tables and getting text into LLM-friendly .md format that I decided to give it a simple Streamlit UI. Keeping it open source so people can do what they like with it!

## What it does
- Provides a simple web interface to convert PDFs to Markdown
- Supports multiple AI vision models:
  - OpenAI (GPT-4V)
  - Google Gemini
  - Meta's Llama & LLaVA
- Shows real-time conversion progress
- Displays markdown output page by page

## Getting Started
1. Clone this repo
   ```bash
   git clone https://github.com/lesteroliver911/pdf-markdown-visionparse.git
   cd pdf-markdown-visionparse
   ```

2. Install requirements
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app
   ```bash
   streamlit run app.py
   ```

4. Get your API key
   - OpenAI API key from: https://platform.openai.com/api-keys
   - Google Gemini API key from: https://aistudio.google.com/app/apikey
   - For Meta Llama & LLaVA: Use Ollama API endpoint (default: http://localhost:11434)

5. Upload a PDF and convert!

## Results
![PDF to Markdown Conversion Interface](https://raw.githubusercontent.com/lesteroliver911/pdf-markdown-visionparse/main/pdf-markdown-vision-parse.png)

## Credits
This project wouldn't exist without [vision-parse](https://github.com/iamarunbrahma/vision-parse) by [iamarunbrahma](https://github.com/iamarunbrahma). All the heavy lifting of PDF processing and AI model integration is handled by their excellent library.

## License
MIT - Do whatever you want with it! 😊
