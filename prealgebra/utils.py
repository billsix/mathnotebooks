# Copyright (c) 2023-2024 William Emerison Six

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
import itertools
from galgebra.printer import latex

# tell sympy to use our printing by default
sympy.init_printing(latex_printer=latex, use_latex="mathjax")

from IPython.display import Math, display, Markdown


def divide_mixed_fractions(first, second):
    display(
        Math(
            "{"
            + str(first[0])
            + r"}{\frac{"
            + str(first[1])
            + "}{"
            + str(first[2])
            + "}}"
            + r"\div"
            + "{"
            + str(second[0])
            + r"}{\frac{"
            + str(second[1])
            + "}{"
            + str(second[2])
            + "}}"
        )
    )

    display(Markdown("**Rewrite**"))

    display(
        Math(
            r"{\frac{"
            + str(first[0] * first[2] + first[1])
            + "}{"
            + str(first[2])
            + "}}"
            + r"\div"
            + r"{\frac{"
            + str(second[0] * second[2] + second[1])
            + "}{"
            + str(second[2])
            + "}}"
        )
    )

    display(Markdown("**Invert**"))

    display(
        Math(
            r"{\frac{"
            + str(first[0] * first[2] + first[1])
            + "}{"
            + str(first[2])
            + "}}"
            + r"\times"
            + r"{\frac{"
            + str(second[2])
            + "}{"
            + str(second[0] * second[2] + second[1])
            + "}}"
        )
    )

    display(Markdown("**Multiply**"))

    display(
        Math(
            r"{\frac{"
            + str((first[0] * first[2] + first[1]) * second[2])
            + "}{"
            + str(first[2] * (second[0] * second[2] + second[1]))
            + "}}"
        )
    )


def add_decimals(first, second):
    display(Markdown("**Align the numbers on the decimal**"))

    def _split_decimals(first, second):
        first_whole, first_dec = first.split(".")
        second_whole, second_dec = second.split(".")

        return (first_whole, first_dec), (second_whole, second_dec)

    (first_whole, first_dec), (second_whole, second_dec) = _split_decimals(first, second)

    display(
        Math(
            r"""\begin{align}
"""
            + first_whole
            + r"""&."""
            + first_dec
            + r"""\\
 +\quad """
            + second_whole
            + r"&."
            + second_dec
            + r"""\\
\hline
\end{align}"""
        )
    )

    display(Markdown("**Put zeros for placeholders**"))

    def _split_decimals(first, second):
        first_whole, first_dec = first.split(".")
        second_whole, second_dec = second.split(".")

        def _put_zeros_on_end(first_dec, second_dec):
            max_len = max(len(first_dec), len(second_dec))
            return (
                first_dec + "".join(list(itertools.repeat("0", max_len - len(first_dec)))),
                second_dec + "".join(list(itertools.repeat("0", max_len - len(second_dec)))),
            )

        first_dec_zero_padded, second_dec_zero_padded = _put_zeros_on_end(first_dec, second_dec)

        return (first_whole, first_dec_zero_padded), (second_whole, second_dec_zero_padded)

    (first_whole, first_dec), (second_whole, second_dec) = _split_decimals(first, second)

    display(
        Math(
            r"""\begin{align}
"""
            + first_whole
            + r"""&."""
            + first_dec
            + r"""\\
 +\quad """
            + second_whole
            + r"&."
            + second_dec
            + r"""\\
\hline
\end{align}"""
        )
    )

    def _actually_add_them(first_whole, first_dec, second_whole, second_dec):
        the_len = max(len(first_dec), len(second_dec))
        dec_added = str(int(first_dec) + int(second_dec))

        if len(dec_added) > the_len:
            extra_int = dec_added[:1]
            dec_to_return = dec_added[1:]
        else:
            extra_int = "0"
            dec_to_return = dec_added

        whole_added = str(int(first_whole) + int(second_whole) + int(extra_int))

        return whole_added, dec_to_return

    result_whole, result_dec = _actually_add_them(first_whole, first_dec, second_whole, second_dec)

    display(Markdown("**Add like for integers**"))

    display(
        Math(
            r"""\begin{align}
"""
            + first_whole
            + r"""&."""
            + first_dec
            + r"""\\
 +\quad """
            + second_whole
            + r"&."
            + second_dec
            + r"""\\
\hline
"""
            + result_whole
            + r""" &."""
            + result_dec
            + r"""
\end{align}"""
        )
    )
