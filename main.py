# main.py
from llama_utils import load_llama_model, generate_text
from api_clients.togetherai_client import call_togetherai
from api_clients.goodgrant_client import call_goodgrant_api
from api_clients.mindsdb_client import connect_mindsdb, query_mindsdb

def main():
    # Load the LLaMA model
    tokenizer, model = load_llama_model()

    # Define a prompt
    prompt = "Explain the recent advancements in AI."

    # Generate text with LLaMA
    llama_response = generate_text(prompt, model, tokenizer)
    print("LLaMA Model Output:", llama_response)

    # Generate text with TogetherAI
    togetherai_response = call_togetherai(prompt)
    print("TogetherAI Response:", togetherai_response)

    # Call Good Grant API (replace endpoint and params as needed)
    goodgrant_response = call_goodgrant_api("grant-details", params={"grant_id": "example_id"})
    print("Good Grant API Response:", goodgrant_response)

    # Query MindsDB (replace with your MindsDB query)
    client = connect_mindsdb()
    query = "SELECT * FROM example_table"
    mindsdb_response = query_mindsdb(client, query)
    print("MindsDB Response:", mindsdb_response)

if __name__ == "__main__":
    main()


