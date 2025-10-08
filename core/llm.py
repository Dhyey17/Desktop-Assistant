import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
tokenizer = AutoTokenizer.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.1",
    token=HF_TOKEN
)
model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.1",
    token=HF_TOKEN,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)


def get_llm_response(prompt):
    messages = [
        {"role": "user", "content": prompt}
    ]

    try:
        # Prepare input tokens
        inputs = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt",
            return_dict=True,
            tokenize=True
        ).to(model.device)

        # Generate response
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.9,
            top_p=0.95,
            repetition_penalty=1.1,
            pad_token_id=tokenizer.eos_token_id
        )

        response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
        return response.strip()
    except Exception as e:
        print("LLM API Error:", e)
        print("Response:", response.text if 'response' in locals() else 'No response')
        return "Some error occurred, please try again!"
