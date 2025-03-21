import os
from openai import OpenAI
from pydantic import BaseModel
from typing import Optional
import json
from PySide6.QtWidgets import QMessageBox, QMainWindow
from PySide6.QtCore import QObject, Signal

client = OpenAI()

class Response_for_HAS(BaseModel):
    display_full_result_or_ask_if_asm: str
    employed_asm: bool
    only_correct_over_total_values_from_sol_formula: Optional[str]
    sol_grade_integer: Optional[float]
    fa_grade_integer: Optional[float]
    overall_grade_integer: Optional[float]


class Evaluation(QObject):  # Now inherits QObject for PySide6 compatibility
    ask_asm_signal = Signal()  # Signal to ask main thread for ASM choice
    asm_response_signal = Signal(str)  # Signal to receive ASM response
    evaluation_done_signal = Signal(object)

    def __init__(self):
        super().__init__()  
        self.conversation = [
            {"role": "system", "content": (
                """Grade Handwritten Algebraic Solution (HAS) step-by-step based strictly on the Answer Key (AK).
                Grade = Solution (SOL) % + Final Answer (FA) %. FA is the last and not a SOL step. Deduct SOL points for each missing or wrong step; accept redundancy and partial simplifications. Ignore the first line(s) in the HAS if it is also first in the AK, as it is the algebraic problem setup. Use formula: (C/T)W for SOL grading, where C = correct SOL steps from HAS aligned with AK counterpart, T = total SOL steps from AK, and W = SOL weight.
                If the HAS employs an Alternative Solution Method (ASM) different from the AK, state: 'The solution has an Alternative Method used... Do you want to allow it? (Yes/No)' and wait for user confirmation before grading. If allowed: alter T in SOL formula to total steps in the HAS instead of the AK, and C to simply correct steps. Refrain from asking again for subsequent HAS with similar ASM, or if the user forbids ASMs.
                If the HAS has no SOL or heavily deviates with the requirements of the problem, failing to contribute to the solution, state: 'There is no solution provided to justify the answer'.
                For the result, briefly state the Problem from the AK, and if a step is Correct or not. Display Grade as: 'Solution = (substituted formula) = #%,\nFinal Answer = #%,\nGrade = #%'.
                """)
            }
        ]
        self.num_of_asm = 0  # Store first ASM message permanently


    def getResponse(self):
        """ Sends conversation to GPT model and parses the structured response. """
        completion = client.beta.chat.completions.parse(
        model="ft:gpt-4o-2024-08-06:grp-4-na-batak-magcode::B4ichSCO",
        messages=self.conversation,
        temperature=0.2,
        response_format=Response_for_HAS,
        store=True
        )
        event = completion.choices[0].message.parsed
        return event

    def evaluate(self, fa_weight, ak_latex, has_latex):
        """ Evaluates HAS and ensures first ASM stays in conversation permanently. """
        sol_weight = 100 - fa_weight
        prompt = (
            f"SOL = {sol_weight}%, FA = {fa_weight}%\n\nAK: '{ak_latex}'\n\n\nHAS: '{has_latex}'"
        )

        # Add HAS input to conversation
        self.conversation.append({"role": "user", "content": prompt})

        # Get GPT response
        self.result = self.getResponse()

        self.conversation.append({"role": "assistant", "content": self.result.display_full_result_or_ask_if_asm})

        print("GPT:", self.result)

        #IF HAS has ASM:
        if self.result.employed_asm:
            self.num_of_asm += 1
            #IF FIRST ASM
            if self.num_of_asm == 1:
                print("First Alternative Solution Method (ASM) detected. Keeping conversation history permanently.")

                ##  Ask for user confirmation via QMessageBox
                #user_choice = self.ask_user_asm_choice()
                print("First ASM detected, requesting user input...")
                self.ask_asm_signal.emit()  # Emit signal to main thread
                
                # Do NOT continue evaluation until user responds
                return None
            
            #IF 2ND ONWARDS
            else:
                self.conversation = self.conversation[:5]
        
        #IF HAS FOLLOWS AK
        else:
            #  Reset conversation but keep first ASM, user choice, and its result if it exists
            print("HAS follows Answer Key method. Resetting conversation.")
            if self.num_of_asm == 0:
                self.conversation = self.conversation[:1]
            else:
                self.conversation = self.conversation[:5]  # Reset to only system message

        print(self.conversation)
        return self.result

    def handleASM1(self, user_choice):
        """ Handles user response from the main thread. """
        print(f"Received user choice from GUI: {user_choice}")

        self.conversation.append({"role": "user", "content": user_choice})

        #  Get assistant's final grading response for this HAS
        self.result = self.getResponse()
        self.conversation.append({"role": "assistant", "content": self.result.display_full_result_or_ask_if_asm})

        print(self.conversation)
        self.evaluation_done_signal.emit(self.result)  
    '''
        """Displays a QMessageBox to ask the user whether to allow ASMs."""
        response = input("The solution has an Alternative Method used. Do you want to allow it?")

        if response == 'Yes':
            return "Yes, allow it."
        else:
            return "No, forbid it."
    '''

        

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
