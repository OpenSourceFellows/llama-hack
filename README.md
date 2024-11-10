# llama-hack

This project integrates the LLaMA LLM, TogetherAI, MindsDB, and Good Grant APIs.
- User Story
- Moqup


## Setup

1. Clone the repository.
2. Create and activate a virtual environment:
    ```bash
    python -m venv llama_env
    source llama_env/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a `.env` file with your API keys:
    ```
    TOGETHERAI_API_KEY=your_togetherai_api_key
    GOODGRANT_API_KEY=your_goodgrant_api_key
    MINDSDB_API_KEY=your_mindsdb_api_key
    ```

## Usage

Run the main script:
```bash
python main.py
