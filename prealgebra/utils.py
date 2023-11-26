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
