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

from IPython.display import Math, display, Markdown


def divide_mixed_fractions(
    first_whole_number, first_numerator, first_denominator, second_whole_number, second_numerator, second_denominator
):
    display(
        Math(
            "{"
            + str(first_whole_number)
            + r"}{\frac{"
            + str(first_numerator)
            + "}{"
            + str(first_denominator)
            + "}}"
            + r"\div"
            + "{"
            + str(second_whole_number)
            + r"}{\frac{"
            + str(second_numerator)
            + "}{"
            + str(second_denominator)
            + "}}"
        )
    )

    display(Markdown("**Rewrite**"))

    display(
        Math(
            r"{\frac{"
            + str(first_whole_number * first_denominator + first_numerator)
            + "}{"
            + str(first_denominator)
            + "}}"
            + r"\div"
            + r"{\frac{"
            + str(second_whole_number * second_denominator + second_numerator)
            + "}{"
            + str(second_denominator)
            + "}}"
        )
    )

    display(Markdown("**Invert**"))

    display(
        Math(
            r"{\frac{"
            + str(first_whole_number * first_denominator + first_numerator)
            + "}{"
            + str(first_denominator)
            + "}}"
            + r"\times"
            + r"{\frac{"
            + str(second_denominator)
            + "}{"
            + str(second_whole_number * second_denominator + second_numerator)
            + "}}"
        )
    )

    display(Markdown("**Multiply**"))

    display(
        Math(
            r"{\frac{"
            + str((first_whole_number * first_denominator + first_numerator) * second_denominator)
            + "}{"
            + str(first_denominator * (second_whole_number * second_denominator + second_numerator))
            + "}}"
        )
    )
