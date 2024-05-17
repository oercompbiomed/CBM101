# Setting up your system

## Video walkthrough: 
We provide a [step-by-step instruction video](https://www.youtube.com/watch?v=BF9OTam4nwk) which covers everything you need to do get started with CBM101. Also, if you are new to computer science, we *strongly* recommend you start by watching [this video](https://www.youtube.com/watch?v=4KpD-L8-uZQ) on how to navigate the command terminal.


## Anaconda:
We recommend installing Python via the [Anaconda Distribution](https://www.anaconda.com/download). Be sure to use the "Python 3.6.x" version or later. We will use the Conda Package Management System within the Anaconda Distribution. From the [documentation](https://conda.io/docs):
> Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer.

After the installation run `python --version` in a terminal window (in "Anaconda Prompt" if you are using Windows). If the output show "Python 3.6.x" or later (and "Anaconda") you are good to go.

## GitHub:
The course code is hosted on the code-sharing platform GitHub (where you now are reading this). If you do not have a GitHub account already you should make one now. We recommend that you are using the platform for you own projects during the course. https://github.com/join.

## Install and test the course environment:

After you have successfully installed Anaconda, go through the following steps (if you are using Windows, be at the "Anaconda Prompt").

### Install Git:
```bash
conda install git
```
### Download the repository:
```bash
git clone https://github.com/oercompbiomed/CBM101
cd CBM101
```

### Configure the Python-environment:
**NB!** Before executing the next command, we recommend you temporarily deactivate your antivirus (AV) software. Some software conflates python.exe with a virus (IDP.generic), and will corrupt your install. If your AV gives this warning, delete your environment (`conda remove --name cbm101 --all --yes`), deactivate the AV and run the commands below.
```bash
conda env update
```
You should now reactivate the AV.

### Activate the environment:
```bash
conda activate cbm101
```
If you are using Linux or MacOS and the command above fails, type
```bash
source ~/.bash_profile
```
and try `conda activate cbm101` again. If this fails, activate the environment by typing `source activate cbm101` instead.

### Install a Jupyter kernel:
```bash
python -m ipykernel install --user --name cbm101 --display-name "CBM101"
```

### Test you installation:
Go through the notebook `1.0-python-basics.ipynb` in the `B_Python_and_friends` directory:
```bash
cd B_Python_and_friends
jupyter notebook
```
(Tip: you can auto complete the name of a file/directory by pressing Tab, so you won't have to write out the 
full name.) Jupyter notebook only supports Firefox, Safari and Chrome. Unless you have set one of these as your default browser, 
you should do so, or alternatively you can run `jupyter notebook --no-browser` and paste the link into a supported browser.
You can also use [JupyterLab](https://github.com/jupyterlab/jupyterlab): `jupyter lab`.

## Update:
The code and environment will be updated during the course. Run the following commands regularly:
* Update code: `git pull`
* Update environment:
```bash
conda activate cbm101
conda env update
```

## Overwriting local changes
Sometimes `git pull` will throw an error message as it would overwrite any local changes you have made. This 
problem can be solved by:
i) Make a copy of the notebook (.ipynb) files before working through them.
OR 
ii) 
```bash
git fetch --all
git reset --hard origin/master
```
WARNING: option ii) *will* permanently delete any personal changes you have made to any of the original files 
(but not the copied ones).

# Jupyter notebooks using R

## Installation of libraries and necessary software

These notebooks requires an R kernel to run the R scripts. We recommend to install the latest R version (https://www.r-project.org/), open an R console and then follow the instructions in https://irkernel.github.io/installation.

### If you are on **Windows**,

at the local CBM101 root directory, and have installed R version 3.5.1 (say), type:

CBM101>`conda deactivate` <br>
CBM101>`"C:\Program Files\R\R-3.5.1\bin\R.exe"` <br>

Now you got the R command prompt `>`. Then type <br>

  \> `install.packages('IRkernel')` <br>
  \> `IRkernel::installspec()` <br>
  \> `quit()`<br>

### If you are on **Mac**,

at the local CBM101 root directory, and have installed R version 3.6.0 (say), type:

CBM101>`conda deactivate` <br>
CBM101>`/usr/local/bin/R` <br>

Now you got the R command prompt `>`. Then type <br>
  \> `install.packages('IRkernel')` <br>
  \> `IRkernel::installspec()` <br>
  \> `quit()`<br>

### If you are on **Linux**,

at the local CBM101 root directory, and have installed R version 3.6.1 (say), type:

  CBM101>`conda deactivate` <br>
  CBM101>`/usr/bin/R` <br>

Now you got the R command prompt `>`. Then type <br>
    \> `install.packages('IRkernel')` <br>
    \> `IRkernel::installspec()` <br>
    \> `quit()`<br>


**Then**: Go to the `E_Biostatistics` folder, and start the Jupyter notebook, i.e.

CBM101/E_Biostatistics>`jupyter notebook`

and you will load the `R kernel` when opening an  `.ipynb`  notebook, say `ProbsAndDistr.ipynb` in the `Probabilities-and-Distributions` folder.

Using Anaconda for the R programming language in Jupyter Notebookhttps see: https://docs.anaconda.com/anaconda/navigator/tutorials/r-lang

More features and a user-friendly environment to run R scripts outside jupyter are available through [RStudio](https://www.rstudio.com)

Install the necessary libraries (only needed once) by executing (shift-enter), e.g.`

`install.packages("MASS", repos='http://cran.us.r-project.org')`

## Edit and live-preview markdown files, e.g. `README.md`

You can use the [Markdown Live Preview](https://markdownlivepreview.com/) page to directly see the formated text.
