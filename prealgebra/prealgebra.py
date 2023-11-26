# %% [markdown]
# Cross Product
# -------------
# %%
import sympy
from galgebra.printer import latex

# tell sympy to use our printing by default
sympy.init_printing(latex_printer=latex, use_latex="mathjax")


from utils import divide_mixed_fractions

# %% [markdown]
# Dividing Fractions
# ------------------
# %%
first_whole_number = 7
first_numerator = 1
first_denominator = 2


second_whole_number = 8
second_numerator = 3
second_denominator = 4

divide_mixed_fractions(
    first_whole_number, first_numerator, first_denominator, second_whole_number, second_numerator, second_denominator
)

# display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))
# display(Math(r'F(k) = {3}{\frac{5}{2}}'))

# %%
