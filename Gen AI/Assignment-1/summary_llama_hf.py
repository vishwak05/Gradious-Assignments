
!pip install -q transformers langchain accelerate

!huggingface-cli login

from transformers import AutoTokenizer, pipeline
from  langchain import LLMChain, HuggingFacePipeline, PromptTemplate
import torch

model_hf = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_hf)

pipeline = pipeline(
    "text-generation",
    model=model_hf,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
    max_length=3000,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id
)

llm = HuggingFacePipeline(pipeline = pipeline, model_kwargs = {'temperature':0})

template = """
              Write a summary of the following text delimited by triple backticks.
              Return your response which covers the key points of the text.
              ```{text}```
              SUMMARY:
           """

prompt = PromptTemplate(template=template, input_variables=["text"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

with open('/content/drive/MyDrive/data_files/einstein.txt', 'r') as f:
    text = f.read()

print(llm_chain.invoke(text))

