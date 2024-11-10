# llama_utils.py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_llama_model(model_name="LLaMA_MODEL_PATH"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

def generate_text(prompt, model, tokenizer, max_length=50):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

