# Python Code Reviewer Streamlit App

Welcome to the Python Code Reviewer Streamlit App! This application uses OpenAI's GPT-3.5-turbo model to review and improve your Python code. Simply enter your code, and the AI will provide feedback and suggest improvements.

## Features

- **Code Review:** Get feedback on your Python code from GPT-3.5-turbo.
- **Error Detection:** Find bugs and errors in your code.
- **Code Improvement:** Receive suggestions for enhancing your code.

## Installation

1.Clone the repository:
    ```bash
    git clone [https://github.com/fouzia0523/python-code-reviewer-genAI.git](https://github.com/fouzia2305/python-code-reviewer-genAI.git)
    cd python-code-reviewer-genAI
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a file named `keys/.openai_api_key.txt` and add your OpenAI API key.

## Configuration

- **OpenAI API Key:** Ensure your OpenAI API key is placed in the `keys/.openai_api_key.txt` file.

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the Streamlit app in your web browser. You will see an interface where you can:
   - **Enter Your Python Code:** Paste your code into the input field.
   - **Review Code:** Click on "Review code" to get feedback and suggestions.
