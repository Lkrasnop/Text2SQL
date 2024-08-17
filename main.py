import pandas as pd
from typing import Any, List, Optional
import google.generativeai as genai
from langchain.llms.base import LLM
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
import os
from dotenv import load_dotenv
import re

# Load the .env file
load_dotenv()

import os
import sys
import google.generativeai as genai

api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    print("Error: GOOGLE_API_KEY environment variable is not set.")
    api_key= 'AIzaSyB4E57nRa9eM92K938fjz7FGJ-LoU-ppfk'

genai.configure(api_key=api_key)
class GoogleAIWrapper(LLM):
    model: Any

    def __init__(self, model):
        super().__init__()
        self.model = model

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = self.model.generate_content(prompt)
        return response.text

    @property
    def _identifying_params(self) -> dict:
        return {"model": self.model}

    @property
    def _llm_type(self) -> str:
        return "google_ai"


class PandasQueryOutputParser(BaseOutputParser):
    def parse(self, text: str) -> str:
        # Remove any markdown formatting
        query = re.sub(r'```python\n?', '', text)
        query = re.sub(r'```\n?', '', query)
        # Remove any leading/trailing whitespace
        query = query.strip()
        return query


def get_db_chain():
    # Read the CSV file
    df = pd.read_csv('dataset.csv')

    # Initialize the generative AI model
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    google_model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    llm = GoogleAIWrapper(google_model)

    # Define the query prompt template
    prompt = """
    You are a pandas DataFrame expert. Given an input question, create a pandas DataFrame query to answer the question using the 'df' DataFrame.
    The DataFrame has the following columns: {columns}

    Pay attention to use only the column names you can see above. Be careful to not query for columns that do not exist.
    Provide ONLY the pandas query without any additional formatting, explanation, or markdown syntax.

    Examples:
    - For "show all records": df
    - For "show first 5 records": df.head()
    - For average age: df['age'].mean()
    - For count by gender: df['sex'].value_counts()

    Human: {question}
    Assistant: Here's the pandas query to answer your question:
    """
    prompt_template = PromptTemplate(template=prompt, input_variables=['question', 'columns'])

    # Create an LLMChain for generating pandas queries
    query_generator = LLMChain(
        llm=llm,
        prompt=prompt_template,
        output_parser=PandasQueryOutputParser()
    )

    def execute_query_and_respond(query, original_question):
        try:
            if query.strip().lower() in ['df', 'insurance']:
                result = df.head(10)  # Display first 10 rows
            else:
                # Use locals() to provide local variables to eval
                local_vars = {'df': df, 'pd': pd}
                result = eval(query, globals(), local_vars)

            if isinstance(result, pd.DataFrame):
                result_df = result.head(10)  # Limit to 10 rows for display
            elif isinstance(result, pd.Series):
                result_df = result.to_frame().head(10)
            else:
                result_df = pd.DataFrame({"Result": [result]})

            df_str = result_df.to_string(index=False)
            response_prompt = f"""
            Given the following pandas query, its result, and the original question, provide a concise answer to the question. Include relevant data from the query result to support your answer.

            Original Question: {original_question}

            Pandas Query: {query}

            Query Result:
            {df_str}

            Answer:
            """
            return llm(response_prompt), result_df
        except Exception as e:
            error_message = f"Error executing query: {str(e)}"
            return error_message, pd.DataFrame()

    def custom_chain(question):
        pandas_query = query_generator.run(question=question, columns=', '.join(df.columns))
        final_answer, result_df = execute_query_and_respond(pandas_query, question)
        return {
            "query": pandas_query,
            "result": result_df,
            "answer": final_answer
        }

    return custom_chain


if __name__ == "__main__":
    # This allows you to test the chain directly
    chain = get_db_chain()
    result = chain("Give me all records")
    print("Query:", result["query"])
    print("Result:")
    print(result["result"])
    print("Answer:", result["answer"])
