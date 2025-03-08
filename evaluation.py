from openai import OpenAI
from pydantic import BaseModel
from typing import Optional
import json
from PySide6.QtWidgets import QMessageBox

client = OpenAI()

class Response_for_HAS(BaseModel):
    display_result_or_ask_if_asm: str
    employed_asm: bool
    sol_substituted_formula: Optional[str]
    sol_grade_integer: Optional[float]
    fa_grade_integer: Optional[float]
    overall_grade_integer: Optional[float]


class Evaluation(object):  # Now inherits QObject for PySide6 compatibility
    def __init__(self):
        self.conversation = [
            {"role": "system", "content": (
                """Grade Handwritten Algebraic Solution (HAS) step-by-step based strictly on the Answer Key (AK).
                Grade = Solution (SOL) % + Final Answer (FA) %. FA is the last and not a SOL step. Deduct SOL points for each missing or wrong step; accept redundancy and partial simplifications. Ignore the first line(s) in the HAS if it is also first in the AK, as it is the algebraic problem setup. Use formula: (C/T)W for SOL grading, where C = correct SOL steps from HAS aligned with AK counterpart, T = total SOL steps from AK, and W = SOL weight.
                If the HAS employs an Alternative Solution Method (ASM) different from the AK, state: 'The solution has an Alternative Method used... Do you want to allow it? (Yes/No)' and wait for user confirmation before grading. If allowed: alter T in SOL formula to total steps in the HAS instead of the AK, and C to simply correct steps. Refrain from asking again for subsequent HAS with similar ASM, or if the user forbids ASMs.
                If the HAS has no SOL, state: 'There is no solution provided to justify the answer'.
                For the result, briefly state the Problem from the AK, and if a step is Correct or not. Display Grade as: 'Solution = (substituted formula) = #%,\nFinal Answer = #%,\nGrade = #%'.
                Make sure to apply delimiters '$$...$$' before and after LaTeX format texts.
                """)
            }
        ]
        self.first_asm_message = None  # Store first ASM message permanently
        self.asm_decision = None  # Store user ASM choice


    def get_response(self):
        """ Sends conversation to GPT model and parses the structured response. """
        completion = client.beta.chat.completions.parse(
        model="ft:gpt-4o-2024-08-06:grp-4-na-batak-magcode::B4ichSCO",
        messages=self.conversation,
        temperature=0.2,  # Lower temperature for more deterministic responses
        response_format=Response_for_HAS,
        store=True
        )
        event = completion.choices[0].message.parsed
        return event

    def evaluate(self, fa_weight, ak_latex, has_latex):
        """ Evaluates HAS and ensures first ASM stays in conversation permanently. """
        sol_weight = 100 - fa_weight
        prompt = (
            f"SOL = {sol_weight}%, FA = {fa_weight}%\n\n"
            f"AK: '{ak_latex}'\n\n\n"
            f"HAS: '{has_latex}'"
        )

        # Add HAS input to conversation
        self.conversation.append({"role": "user", "content": prompt})

        # Get GPT response
        result = self.get_response()

        print("GPT:", result)

        if result.employed_asm:
            if not self.first_asm_message:
                #  First ASM detected → Store this conversation permanently
                self.first_asm_message = self.conversation[:]  # Store user HAS + assistant's ASM detection prompt
                print("First Alternative Solution Method (ASM) detected. Keeping conversation history permanently.")

                #  Ask for user confirmation via QMessageBox
                user_choice = self.ask_user_asm_choice()

                #  Store user choice
                self.conversation.append({"role": "user", "content": user_choice})
                self.asm_decision = user_choice  # Store decision permanently

                #  Get assistant's final grading response for this HAS
                result = self.get_response()
                self.conversation.append({"role": "assistant", "content": result})

                #  Now store the full conversation (including grading result)
                self.first_asm_message = self.conversation[:]
            else:
                #  Reset the conversation but keep first ASM detection + grading result
                print("ASM detected again. Resetting conversation, but keeping first ASM and user decision.")
                self.conversation = self.first_asm_message[:]
        else:
            #  Reset conversation but keep first ASM, user choice, and its result if it exists
            print("HAS follows Answer Key method. Resetting conversation.")
            if self.first_asm_message:
                self.conversation = self.first_asm_message[:]
            else:
                self.conversation = self.conversation[:1]  # Reset to only system message

        #  Append new HAS input (Fresh grading)
        self.conversation.append({"role": "user", "content": prompt})

        #  Get fresh grading result
        result = self.get_response()

        #  Append the assistant’s fresh grading result (but NOT to first_asm_message)
        self.conversation.append({"role": "assistant", "content": result})

        return result


    def ask_user_asm_choice(self):
        """ Displays a QMessageBox to ask the user whether to allow ASMs. """
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Alternative Solution Method Detected")
        msg_box.setText("The solution has an Alternative Method used. Do you want to allow it?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)

        response = msg_box.exec()

        if response == QMessageBox.Yes:
            return "Yes, allow it."
        else:
            return "No, forbid it."
        

if __name__ == "__main__":
    # Example Use Case
    grader = Evaluation()

    # Simulated HAS Inputs
    fa_weight = 40
    ak_latex = open("GPTDataset/testAK.txt", "r").read()
    has_latex = open("GPTDataset/testHAS.txt", "r").read()  # Regular HAS following AK

    ## Evaluate first HAS (complies with AK → resets conversation)
    result1 = grader.evaluate(fa_weight, ak_latex, has_latex)

    ## Evaluate second HAS (triggers ASM → conversation is kept)
    #result2 = grader.evaluate(sol_weight, fa_weight, ak_latex, has_latex_2)

    ## Evaluate third HAS (also ASM, but now resets like a normal HAS)
    #result3 = grader.evaluate(sol_weight, fa_weight, ak_latex, has_latex_2)
