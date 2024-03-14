import os
import sys
import torch
from transformers import GPTJForCausalLM, AutoTokenizer

model_loaded_flag = False
if(len(sys.argv) > 1):
   model_path = os.path.join(sys.argv[1])
   if( os.path.exists( model_path )):
      print(model_path)
      model = GPTJForCausalLM.from_pretrained( model_path, revision="float32",  torch_dtype=torch.float32)
      model_loaded_flag = True
if(model_loaded_flag == False):
    model = GPTJForCausalLM.from_pretrained( "EleutherAI/gpt-j-6b", revision="float32",  torch_dtype=torch.float32)
    model.save_pretrained(model_path)
prompt = "To make a great scrambled egg, you must"
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6b", trust_remote_code=True)
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
gen_tokens = model.generate(input_ids, do_sample=True, temperature=0.9, max_length=400)
gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)
