# ft_package

A simple package with a function to count elements in a list.

## Usage:
### 1) building package 
```bash
python3 -m build 
```
### 2) installing package with pip (or pip3)
```bash
pip install ./dist/ft_package-0.0.1.tar.gz
``` 
  or
```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```
### 3) get info
```bash
pip show -v ft_package
```
### 4) unistall package
```bash
python3 -m pip uninstall ft_package
```

## If during building there will be message
    "No module named build"
## Run this:
```bash
python3 -m pip install --upgrade pip setuptools wheel build
```


## pyproject.toml explanation
`[build-system]` - section that tells python what to use for building the package

    `requires = ["setuptools", "wheel"]` — list of libraries for building:
    
        `setuptools` — standard tool for creating Python packages
    
        `wheel` — tool for building wheel files (.whl), installable via pip
    
    `build-backend = "setuptools.build_meta"` — Python module used for building the package (PEP 517 standard)

`[project]` - section with metedata for pip, PyPI and pip show:

    `name` — package name, shown in pip list and during installation

    `version` — package version

    `description` — short package description, shown in pip show

    `authors` — list of authors with name and email
    
    `readme` — path to README file
    
    `license` — license type
    
    `requires-python` — minimal Python version required

`[tool.setuptools.packages.find]` - this section is used by setuptools:

    `where = ["."]` — search for all folders containing __init__.py to include in the package