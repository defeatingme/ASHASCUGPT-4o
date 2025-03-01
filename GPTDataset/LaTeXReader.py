import sympy as sp
import matplotlib.pyplot as plt
from sympy.parsing.latex import parse_latex

# Function to render LaTeX equation
def render_latex(latex_str):
    fig, ax = plt.subplots(figsize=(6, 1))  # Create a plot
    ax.text(0.5, 0.5, f"${latex_str}$", fontsize=30, ha='center', va='center')  # Render LaTeX
    ax.axis('off')  # Hide axes
    plt.show()

# Function to solve a LaTeX equation
def solve_latex(latex_str):
    try:
        # Parse LaTeX into a sympy equation
        equation = parse_latex(latex_str)
        
        # Solve the equation
        solution = sp.solve(equation)
        return solution
    except Exception as e:
        return f"Error solving the equation: {e}"

# Example LaTeX input for solving
latex_input = r"12 \times \left( \frac{3x}{4} - \frac{2x}{3} \right) = 12 \times 2"

# Render the LaTeX equation
render_latex(latex_input)

# Solve the equation
x = sp.symbols('x')
latex_eq = "12*(3*x/4 - 2*x/3) - 12*2"  # Convert LaTeX to sympy compatible equation
solution = solve_latex(latex_eq)

print("Solution:", solution)
