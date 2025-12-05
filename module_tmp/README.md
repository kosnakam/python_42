# 42_DSLR

## 🧙‍♂️ Project Overview — Hogwarts Magic Hat

A data science project to recreate the **Hogwarts Sorting Hat** using **logistic regression**.
You’ll analyse and visualize student data, then implement a **    multi-class logistic regression (One-vs-All)** model trained with gradient descent — all from scratch, without using built-in statistical functions.

## Setup

### Prerequisites

- Python 3.10

### Installation

1. Create a virtual environment with Python 3.10:
```bash
python3.10 -m venv venv
```

2. Activate the virtual environment:
```bash
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Freeze dependencies (when you want to update requirements.txt):
```bash
pip freeze > requirements.txt
```

## Development

### Naming Conventions

This project follows standard Python naming conventions (PEP 8):

- **Classes**: `PascalCase` (e.g., `LogisticRegression`)
- **Functions & Variables**: `snake_case` (e.g., `train_model`, `learning_rate`)
- **Constants**: `UPPER_CASE` (e.g., `MAX_ITERATIONS`)
- **Files & Directories**: `snake_case` (e.g., `data_processing.py`)

**Consistency is key**: Once a rule is decided, it must be followed strictly.
- **Verb-Noun Pattern**: Functions should follow the `verb_noun` pattern (e.g., `get_data`, `calc_mean`).

### Execution Directory & Paths

- **Execution Root**: All scripts must be executed from the **project root directory**.
- **Relative Paths**: Use relative paths starting from the project root.
    - **Command Line**: `python main.py` (Run from root)
    - **Data Access**: `pd.read_csv("data/raw/dataset_train.csv")`
    - **Saving Files**: `plt.savefig("plots/scatter_plot.png")`
    - **Bad Practice**: Avoid using `../` to go up directories or absolute paths.

### Git Workflow

#### Commit Messages (Conventional Commits)
Format: `type(scope): subject`

- **Types**:
  - `feat`: New feature
  - `fix`: Bug fix
  - `docs`: Documentation only
  - `style`: Formatting, missing semi-colons, etc.
  - `refactor`: Code change that neither fixes a bug nor adds a feature
  - `test`: Adding or correcting tests
  - `chore`: Build process or auxiliary tool changes

**Example**: `feat(model): implement gradient descent`

#### Branch Naming
Format: `type/description`

- `feat/logistic-regression`
- `fix/parsing-error`
- `docs/update-readme`

### Code Quality Tools

This project uses the following tools to maintain code quality:

#### Black (Code Formatter)
Black is used as the code formatter. To format your code:
```bash
black .
```

To check formatting without making changes:
```bash
black --check .
```

#### Flake8 (Linter)
Flake8 is used for linting. To check your code:
```bash
flake8 .
```

#### mypy (Type Checker)
mypy is used for static type checking. To run type checks:
```bash
mypy .
```

### Running All Checks
To ensure your code meets all quality standards, run:
```bash
black --check . && flake8 . && mypy .
```
