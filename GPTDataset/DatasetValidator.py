from openai import OpenAI
import json
import tiktoken # for token counting
import numpy as np
from collections import defaultdict
import os

cwd = os.getcwd()
print(cwd)

client = OpenAI()

# Open and load the JSON file

dataset = r"GPTDataset\SimplifyANDExpandMULTI-TURN-DATASET.json"

count = 0

# Load the dataset
with open(dataset, 'r', encoding='utf-8') as f:
    dataset = [json.loads(line) for line in f]

# Initial dataset stats
print("Num examples:", len(dataset))
print("Last example:")

sample = dataset[-1]["messages"]

for message in sample:
    print(message)
    
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
