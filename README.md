# llama-hack

This project integrates the LLaMA LLM, TogetherAI, MindsDB, and Good Grant APIs.
- [User Story](https://docs.google.com/document/d/1DNubRJbQVePpBDWAgUaSkvNMG6MHsrJU_3-_Ixdrzfk/edit?usp=sharing)
- [Moqup]([url](https://app.visily.ai/projects/c9f1e068-4ed6-48b9-aff0-ff1cd3f093ee/boards/1409436/presenter?play-mode=Prototype))

We are creating an AI agent that can followup with smaller nonprofits to increase bandwidth by: 
- Identifying grants that they’d be great fits for through NLP 
- Drafting potential proposals based on past grantees and pointing out the considerations they should add 
- Creating any followup tasks as an internal project board that sends notification as an sms interface 


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
