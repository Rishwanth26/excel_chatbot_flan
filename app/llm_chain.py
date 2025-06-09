import json
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

class ExcelChatChain:
    def __init__(self, df):
        self.df = df
        model_name = "google/flan-t5-small"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.generator = pipeline(
            "text2text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_length=512,
            do_sample=False
        )

    def build_prompt(self, question: str) -> str:
        # Convert dataframe to readable text
        rows_text = ""
        for i, row in self.df.iterrows():
            row_str = ', '.join(f"{col}: {row[col]}" for col in self.df.columns)
            rows_text += f"Row {i+1}: {row_str}\n"
        
        prompt = (
            "You are a helpful assistant. Answer the question based on the data below.\n\n"
            f"Data:\n{rows_text}\n"
            f"Question: {question}\nAnswer:"
        )
        return prompt

    def query(self, question: str) -> str:
        prompt = self.build_prompt(question)
        result = self.generator(prompt)[0]["generated_text"].strip()
        return result
