from openai import OpenAI
from pydantic import BaseModel
from typing import Optional
import json

client = OpenAI()

class Statement(BaseModel):
    display_result_or_ask_if_asm: str
    employed_asm: bool
    sol_substituted_formula: Optional[str]
    sol_grade_integer: Optional[float]
    fa_grade_integer: Optional[float]
    overall_grade_integer: Optional[float]

# System Instructions
conversation = [
    {"role": "system", "content": (
        """Grade Handwritten Algebraic Solution (HAS) step-by-step based strictly on the Answer Key (AK).
        Grade = Solution (SOL) % + Final Answer (FA) %. FA is the last and not a SOL step. Deduct SOL points for each missing or wrong step; accept redundancy and partial simplifications. Ignore the first line(s) in the HAS if it is also first in the AK, as it is the algebraic problem setup. Use formula: (C/T)W for SOL grading, where C = correct SOL steps from HAS aligned with AK counterpart, T = total SOL steps from AK, and W = SOL weight.
        If the HAS employs an Alternative Solution Method (ASM) different from the AK, state: 'The solution has an Alternative Method used... Do you want to allow it? (Yes/No)' and wait for user confirmation before grading. If allowed: alter T in SOL formula to total steps in the HAS instead of the AK, and C to simply correct steps. Refrain from asking again for subsequent HAS with similar ASM, or if the user forbid ASMs.
        If the HAS has no SOL, state: 'There is no solution provided to justify the answer'.
        For the result, briefly state the Problem from the AK, and if a step is Correct or not. Display Grade as: 'Solution = (substituted formula) = #%,\nFinal Answer = #%,\nGrade = #%'.
        Make sure to apply delimiters '$$...$$' before and after LaTeX format texts.
        """)
    }
]

def get_response():
    completion = client.beta.chat.completions.parse(
        model="ft:gpt-4o-2024-08-06:grp-4-na-batak-magcode::B4ichSCO",
        messages=conversation,
        temperature=0.2,  # Lower temperature for more deterministic responses
        response_format=Statement,
        store=True
    )
    event = completion.choices[0].message.parsed
    return event


def add_message(role: str, content: str):
    """ Adds message to the conversation history. """
    conversation.append({"role": role, "content": str(content)})

def Evaluation(sol_weight, fa_weight, ak_latex, has_latex):
    """ Evaluates HAS based on Answer Key and resets conversation if ASM is not used. """

    prompt = (
        f"SOL = {sol_weight}%, FA = {fa_weight}%\n\n"
        f"AK: '{ak_latex}'\n"
        f"HAS: '{has_latex}'"
    )
    
    # Add user input to conversation
    add_message("user", prompt)

    # Get GPT response
    result = get_response()

    print("GPT:", result.display_result_or_ask_if_asm)

    # If HAS uses an Alternative Solution Method, keep conversation history
    if result.employed_asm:
        print("Alternative Method detected. Keeping conversation history.")
    else:
        print("HAS follows Answer Key method. Resetting conversation.")
        conversation[:] = conversation[:1]  # Reset to only system message

    # Append assistant response if ASM is used
    add_message("assistant", result.display_result_or_ask_if_asm)

    # If ASM is detected, ask for confirmation
    if "Alternative Method used" in result.display_result_or_ask_if_asm:
        user_response = input("Allow alternative method? (Yes/No): ").lower()
        add_message("user", user_response)
        result = get_response()
        print("GPT:", result.display_result_or_ask_if_asm)
        add_message("assistant", result.display_result_or_ask_if_asm)

    return result

if __name__ == "__main__":
    sol_weight = 60  # Example solution weight
    fa_weight = 40   # Example final answer weight
    ak_latex = "x^2 + 3x - 4 = 0"
    has_latex = "x^2 + 3x - 4 = 0\n(x+4)(x-1) = 0"

    result = evaluation(sol_weight, fa_weight, ak_latex, has_latex)
