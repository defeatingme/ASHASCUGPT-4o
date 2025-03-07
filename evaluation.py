from openai import OpenAI
from pydantic import BaseModel
from typing import Optional
import numpy as np
from enum import Enum
from collections import defaultdict
import json
from database import engine
from ocr import GeminiOCR

client = OpenAI()

class Evaluation(BaseModel):
    display_result_or_ask_if_asm: str
    employed_asm: bool
    sol_grade_integer: Optional[float]
    fa_grade_integer: Optional[float]
    overall_grade_integer: Optional[float]

conversation = [
    # Define the system prompt
    {"role": "system", "content": (
        """Grade Handwritten Algebraic Solution (HAS) step-by-step based strictly on the Answer Key (AK).
        Grade = Solution (SOL) % + Final Answer (FA) %. FA is the last and not a SOL step. Deduct SOL points for each missing or wrong step; accept redundancy and partial simplifications. Ignore the first line(s) in the HAS if it is also first in the AK, as it is the algebraic problem setup. Use formula: (C/T)W for SOL grading, where C = correct SOL steps from HAS aligned with AK counterpart, T = total SOL steps from AK, and W = SOL weight.
        If the HAS employs an Alternative Solution Method (ASM) different from the AK, state: 'The solution has an Alternative Method used... Do you want to allow it? (Yes/No)' and wait for user confirmation before grading. If allowed: alter T in SOL formula to total steps in the HAS instead of the AK, and C to simply correct steps. Refrain from asking again for subsequent HAS with similar ASM, or if the user forbid ASMs.
        If the HAS has no SOL , state: 'There is no solution provided to justify the answer'.
        For the result, briefly state the Problem from the AK, and if a step is Correct or not. Display Grade as: 'Solution = (substituted formula) = #%,\nFinal Answer = #%,\nGrade = #%'.
        Make sure to apply delimiters '$$...$$' before and after latex format texts.
        """)
    }
]

def get_response():
    completion = client.beta.chat.completions.parse(
        model="ft:gpt-4o-2024-08-06:grp-4-na-batak-magcode::B4ichSCO",
        messages=conversation,
        temperature=0.2,  # Lower temperature for more deterministic responses
        response_format=e,
        store=True
    )
    event = completion.choices[0].message.parsed
    return event

def add_message(role: str, content: str):
    conversation.append({"role": role, "content": str(content)})

def input_HAS(sol_weight, fa_weight, ak_latex, has_count, has_count):
    #has = input("Input Handwritten Algebraic Solution:\n")
    
    prompt = (
        f"SOL = {sol_weight}%, FA = {fa_weight}%\n\n"
        f"AK 1: '{ak_latex}'\n"
        f"HAS {has_count}: '{has_latex}'"
    )

    add_message("user", prompt)
    return prompt

#Grading Input
fa_weight = int(input("Input Final Answer Weight %: "))
sol_weight = 100 - fa_weight
print(f"Solution = {sol_weight}% | Final Answer = {fa_weight}%")
ak_latex = input("Input Answer Key:\n")

print(input_HAS())

result = get_response()
print("GPT:", result)
# Append the assistant's response for context in future turns
add_message("assistant", result)

# Simulate a live chat session (this can be replaced by WebSocket integration)
while True:
    if "solution has an Alternative Method used" not in result.display_result_or_ask_if_asm:
        #HAS Input
        has = input("Input Handwritten Algebraic Solution:\n")

        # Every 8th prompt (except the first), repeat the first prompt header to refresh context.
        if (has_count % 8 == 0):
            print(input_HAS())
        else:
            prompt = f"HAS {has_count}: {has}"
            add_message("user",prompt)
            print(prompt)
        
        has_count += 1
    else:
        prompt = input("yes or no: ")
        add_message("user",prompt)
        
    result = get_response()
    print("GPT:", result)
    add_message("assistant", result)