
conv = ["iestwjefwf", "erwerrw"]
def input_HAS():
    has = input("Input Handwritten Algebraic Solution:\n")
    prompt = (has, "hello")
    conv.append(prompt)
    return prompt

inp = input_HAS()
print(inp)
print(conv)
print(inp)
print(conv)