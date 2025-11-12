# Getting Started

This guide will help you set up your environment for the Plotly Dash workshop.

## Step 1: Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** installed
  ```bash
  python --version
  # or
  python3 --version
  ```

- **pip** (Python package installer)
  ```bash
  pip --version
  # or
  pip3 --version
  ```

## Step 2: Clone the Repository

If you haven't already, clone this repository:

```bash
git clone https://github.com/DustinMathia/plotly-dash-demo.git
cd plotly-dash-demo
```

## Step 3: Create a Virtual Environment

It's best practice to use a virtual environment for Python projects:

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt when the virtual environment is activated.

## Step 4: Install Dependencies

Install all required packages using pip:

```bash
pip install -r requirements.txt
```

This will install:
- **dash** - The main Dash framework
- **plotly** - Interactive plotting library
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **jupyter** - Jupyter notebook interface
- **jupyterlab** - Modern Jupyter interface

## Step 5: Launch JupyterLab

Start JupyterLab to access the workshop notebooks:

```bash
jupyter lab
```

This will open JupyterLab in your default web browser (usually at `http://localhost:8888`).

## Step 6: Navigate to the Notebooks

In JupyterLab, you'll find the workshop notebooks in the `notebooks/` directory:

1. `01_introduction_to_dash.ipynb`
2. `02_interactive_components.ipynb`
3. `03_advanced_layouts.ipynb`
4. `04_real_world_dashboard.ipynb`

Start with notebook 01 and work through them in order.

## Troubleshooting

### Issue: Python not found
**Solution:** Install Python from [python.org](https://www.python.org/downloads/) or use your system's package manager.

### Issue: pip command not found
**Solution:** Try using `python -m pip` instead of just `pip`.

### Issue: Permission errors during installation
**Solution:** Make sure you're using a virtual environment. Don't use `sudo` with pip.

### Issue: Jupyter not launching
**Solution:** 
```bash
# Try reinstalling jupyter
pip install --upgrade jupyter jupyterlab

# Or launch with explicit path
python -m jupyter lab
```

### Issue: Port 8888 already in use
**Solution:** Jupyter will automatically use a different port (8889, 8890, etc.). Check the terminal output for the correct URL.

## Verifying Your Installation

You can verify that everything is installed correctly by running:

```python
python -c "import dash; import plotly; import pandas; print('All packages installed successfully!')"
```

## Next Steps

Once your environment is set up:

1. ✅ Read the [Workshop Overview](WORKSHOP_OVERVIEW.md)
2. ✅ Open the first notebook: `notebooks/01_introduction_to_dash.ipynb`
3. ✅ Start learning!

## Alternative: Using Google Colab

If you prefer not to install anything locally, you can use Google Colab:

1. Go to [Google Colab](https://colab.research.google.com/)
2. Upload the notebook files
3. Run this in the first cell:
   ```python
   !pip install dash plotly pandas
   ```

**Note:** Some Dash features may be limited in Colab since it's designed for notebooks, not web applications.

## Need Help?

- Check the [Workshop Overview](WORKSHOP_OVERVIEW.md)
- Review the [Additional Resources](RESOURCES.md)
- Visit the [Plotly Dash Documentation](https://dash.plotly.com/)

Ready? Let's build some dashboards! 🎉
