# %%
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
# Pre-Algebra
# -----------
# %% [markdown]
# Do Imports
# ----------

# %%
import sympy
from galgebra.printer import latex

# tell sympy to use our printing by default
sympy.init_printing(latex_printer=latex, use_latex="mathjax")


from billsixmathnotebooks.prealgebra.utils import divide_mixed_fractions, add_decimals, subtract_decimals

# %% [markdown]
# Dividing Mixed Fractions
# ------------------------
# %%
divide_mixed_fractions((3, 1, 3), (1, 5, 9))

# %% [markdown]
# Adding Decimals
# ---------------

# %%
add_decimals("3.14", "5.999")

# %% [markdown]
# Subtracting Decimals
# --------------------

# %%
subtract_decimals("2.0123", "3.14")

# %% [markdown]
# Multiplying Decimals
# --------------------

# %% [markdown]
# Dividing Decimals
# -----------------

# %% [markdown]
# Converting Fractions And Decimals
# ---------------------------------

# %% [markdown]
# Ratios and Rates
# ----------------

# %% [markdown]
# Proportions
# -----------

# %%
