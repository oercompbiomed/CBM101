
# Jupyter notebooks using R

## Installation of libraries and necessary software

These notebooks requires an R kernel to run the R scripts. We recommend to install the latest R version (https://www.r-project.org/), open an R console and then follow the instructions in https://irkernel.github.io/installation.

If you are on **Windows**, at the local CBM101 root directory, and have installed R version 3.5.1 (say), type:

CBM101>`conda deactivate` <br>
CBM101>`"C:\Program Files\R\R-3.5.1\bin\R.exe"` <br>

Now you got the R command prompt `>`. Then type <br>

  \> `IRkernel::installspec()` <br>
  \> `quit()`
  
Go to the `C_Basic-Concepts-in-Statistics` folder, and start the Jupyter notebook, i.e.

CBM101/C_Basic-Concepts-in-Statistics>`jupyter notebook`

and you will load the `R kernel` when opening an  `.ipynb`  notebook, say `ProbsAndDistr.ipynb` in the `Probabilities-and-Distributions` folder.



Using Anaconda for the R programming language in Jupyter Notebookhttps see: https://docs.anaconda.com/anaconda/navigator/tutorials/r-lang

More features and a user-friendly environment to run R scripts outside jupyter are available through [RStudio](https://www.rstudio.com)

Install the necessary libraries (only needed once) by executing (shift-enter), e.g.`

`install.packages("MASS", repos='http://cran.us.r-project.org')`

