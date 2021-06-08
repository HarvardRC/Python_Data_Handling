### Large Data Handling in Python Class

#### How to create the environment?

1. Clone or download the Github repository. 
2. Install Miniconda or Anaconda on your [Linux or Windows](https://docs.conda.io/en/latest/miniconda.html) machine or use FASRC Cannon cluster. 
3. Create a Conda environment for this course using the following command,

```bash
conda env create -f py_course.yml
```

4. Activate the newly create Conda environment (`py_course`) by,

```bash
conda activate pycourse
```

5. Install Jupyter Notebook (or Jupyter Lab) on your machine or use [FASRC Open OnDemand](http://vdi.rc.fas.harvard.edu/) interface.

```bash
pip install jupyter
```

6. Run the Jupyter Notebook and open the `PyDataCourse.ipynb` file.


7. On FASRC Cluster Terminal:

```
module load Anaconda3  (skip on your laptop)
conda create --name pycourse python=3.7
source activate pycourse
pip install jupyter vprof snakeviz numpy perfplot pandas
conda install pytables
```
