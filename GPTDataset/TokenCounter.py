from openai import OpenAI
import json
import tiktoken # for token counting
import numpy as np
from collections import defaultdict
import os

client = OpenAI()

# Open and load the JSON file

dataset = "SystemsofLinearEquationMULTI-TURNDATASET.json"

count = 0

# Load the dataset
with open(dataset, 'r', encoding='utf-8') as f:
    dataset = [json.loads(line) for line in f]

# Initial dataset stats
print("Num examples:", len(dataset))
print("First example:")

sample = dataset[17]["messages"]

for message in sample:
    print(message)
    

def num_tokens_from_messages(messages, model="gpt-4o"):
    """Return the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using o200k_base encoding.")
        encoding = tiktoken.get_encoding("o200k_base")
    if "gpt-4o" in model:
        print("Warning: gpt-4o and gpt-4o-mini may update over time. Returning num tokens assuming gpt-4o-2024-08-06.")
        return num_tokens_from_messages(messages, model="gpt-4o-2024-08-06")
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens

for i in range:
    for model in ["gpt-4o"]:
        print(model)
        # example token count from the function defined above
        print(f"{num_tokens_from_messages(sample, model)} prompt tokens counted by num_tokens_from_messages().")
        # example token count from the OpenAI API
        response = client.chat.completions.create(model=model,
        messages=sample,
        temperature=0,
        max_tokens=1)
        print(f'{response.usage.prompt_tokens} prompt tokens counted by the OpenAI API.')
        print()
    i += 1


    
#1. HAS is perfectly similar to the Answer Key
#2. HAS has an excess step, but still perfectly similar to the Answer Key
#3. HAS has steps whose values are in different arrangement, but still perfectly similar to the Answer Key
#4. SOL has a step with an Incorrect value, but FA is Correct
#5. SOL has a Incomplete/Missing step compared to the Answer Key, but FA is Correct
#6. SOL is all Correct, but FA is Incorrect/Incomplete/Missing
#7. SOL has both an Incorrect and an Incomplete/Missing step, but FA is Correct
#8. Half number of steps of SOL are Incorrect/Incomplete/Missing, and FA is Incorrect/Incomplete/Missing. 
#9. All steps of SOL are Incorrect/Incomplete/Missing, but FA is Correct.  
#10. All layers of HAS is either Incorrect or Missing.
