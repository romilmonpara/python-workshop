# for UI creation use Streamlit

import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "gpt2"
# MODEL_NAME = "Llama-3.1-Nemotron-708-Instruct-HF"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)  # Fixed method call
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)  # Fixed method call
    return tokenizer, model

tokenizer, model = load_model()

def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors='pt')  # PyTorch
    output = model.generate(
        inputs,
        max_length=100,
        num_return_sequences=1,
        no_repeat_ngram_size=2
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

def main():
    st.title("AI-Powered Chatbot")

    if "messages" not in st.session_state:
        st.session_state['messages'] = []

    user_input = st.text_input("Ask me anything")
    
    if st.button('Send'):
        response = generate_response(user_input)
        st.session_state['messages'].append(("User", user_input))
        st.session_state['messages'].append(("Bot", response))

    for sender, msg in st.session_state['messages']:
        st.write(f"**{sender.capitalize()}** : {msg}")

if __name__ == "__main__":
    main()

# for output (in Terminal):
#   streamlit run 01_HuggingFace.py