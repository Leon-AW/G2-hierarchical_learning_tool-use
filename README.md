# G2-hierarchical_learning_tool-use (p4)

This project simulates a 2D environment where robotic arm tools interact with various objects. The simulation includes elements like grip arms, sticks, magnets, and more, designed to explore intrinsic motivated learning and tool use in a controlled setting.

The original Code came from:
https://github.com/sebastien-forestier/IMGEP

## Installation

To set up and run the simulation, follow these steps:

### Dependencies

Ensure you have Python 3 installed on your system.

### Setting up a Virtual Environment (Optional)

It's recommended to use a virtual environment to manage dependencies. You can create one using the following commands:

### Step 1: Install Conda (if not already installed)

If you don't have Conda installed, you'll need to install either Anaconda or Miniconda. You can download Anaconda from the Anaconda website or Miniconda from the Miniconda website.

### Step 2: Create a New Conda Environment

Navigate to your project directory (or where you wish to create it) and create the environment with python 3.8.

```bash
conda create --name explauto-env python=3.8
```

activate the environment:

```bash
conda activate explauto-env
```

### Installing Required Libraries

Install the necessary Python packages by running:

```bash
pip3 install numpy scipy scikit-learn explauto matplotlib
```

### Verify Installation

```bash
python -c "import explauto"
```

If you don't get any errors, explauto is successfully installed in your environment, and you're ready to proceed with your work.

### Troubleshoot potential Error: Requirements should be satisfied by a PEP 517 installer.

```bash
pip3 install 'setuptools<58.0.0'
```
Then, try installing explauto again:

```bash
pip3 install explauto
```

Verify the installation again:

```bash
python -c "import explauto"
```

## Running the Simulation

Navigate to the project directory and execute the main script:

```bash
cd path/to/2D_Simulated_Tool-Use_Environment/IMGEP/2DSimulation
python3 run.py <log_dir> <seed> <distractors> <optim_explo> <end_point> <condition> <iterations>
```
```markdown
<log_dir>: Directory to write log files.
<seed>: Seed for pseudo-random number generation.
<distractors>: Type of distractors in the environment (none, random, static, or both).
<optim_explo>: Optimization exploration strategy (random, gaussian, or full).
<end_point>: Goal representation as an endpoint (True or False).
<condition>: Experimental condition (rmb, SGS, FC, FRGB, RMB, or AMB).
<iterations>: Number of iterations to run.
```

Example:

```bash
python3 run.py ./experiment_logs 42 both full True RMB 1000
```



