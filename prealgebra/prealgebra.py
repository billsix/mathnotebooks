# Copyright (c) 2023 William Emerison Six

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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
