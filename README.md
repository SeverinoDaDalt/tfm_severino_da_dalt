# Master Thesis

## The thesis itself
The thesis pdf can be found at `out/thesis.pdf`.
The compilable Latex code main file is `thesis.tex` and all sections can be found in `sections/`.

## Other code
As mentioned in Appendix C of the thesis, some python code is provided.

### Requirements
To run it, first clone the repository.

Next, install Python (any reasonable version should work, but it is recommended $\geq 3.12$).

Then, install the required packages by running:
```bash
pip install -r code/requirements.txt
```
from the main folder.

Everything is set up 

### $G_r$ counterexample
To compute that a given graph $G_r$ is $\frac{1}{2r-1}$-excellent but not $\frac{r-1}{2r-1}$-excellent, run
```bash
python code/non-monotonicity_counterexample.py --subset_size <R>
```
where `<R>` $=2\cdot r$.

To run the code to exhaustively check for possible counterexamples, run
```bash
python code/explore_counterexamples.py
```