# Setting up your system

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
```bash
conda env update
```

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
Go through the notebook `0.0-test.ipynb` in the `notebooks`-directory:
```bash
cd notebooks
jupyter notebook
```
You can also use [JupyterLab](https://github.com/jupyterlab/jupyterlab): `jupyter lab`.

## Update:
The code and environment will be updated during the course. Run the following commands regularly:
* Update code: `git pull`
* Update environment:
```bash
conda activate cbm101
conda env update
```

