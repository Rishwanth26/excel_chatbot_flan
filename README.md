# Excel-Based Insights Chatbot

A Streamlit web app that lets users upload an Excel file and ask natural-language questions. Uses an open-source Flan-T5 model to interpret queries and renders answers as text or charts.

## Features
- No paid APIs: uses HuggingFace `transformers` and a free open-source model.
- Schema-agnostic: normalizes column names and infers data types.
- Structured JSON responses for reliable chart generation.

## Setup & Run
1. Clone the repo.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the app:
   ```bash
   streamlit run app/main.py
   ```

## Files
- `app/utils.py`: Excel loading & cleaning.
- `app/llm_chain.py`: Prompt engineering & Flan-T5 integration.
- `app/main.py`: Streamlit interface & chart rendering.
- `presentation.pptx`: Slide deck on approach and challenges.
