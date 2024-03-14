import os
import sys
import torch
from transformers import GPTJForCausalLM, AutoTokenizer

model = GPTJForCausalLM.from_pretrained( "EleutherAI/gpt-j-6b", revision="float32",  torch_dtype=torch.float32)
prompt = "To make a great taco, you must"
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6b", trust_remote_code=True)
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
gen_tokens = model.generate(input_ids, do_sample=True, temperature=0.9, max_length=400)
gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)
