# Analysis of registered Dutch cars

Jupyter notebook(s) to analyze the CC0 data about the 16.2 million registered cars in The Netherlands
The analysis is done by collecting data in a streaming fashion over the 16 mio rows.

# Install

```bash
python3 -m venv py-env

source py-env/bin/activate

# install dependencies
pip install -r requirements.txt

# make the virtual environment available to the jupyter notebook
python -m ipykernel install --user --name=py-env
```

The data needed for the analysis can be downloaded here: https://opendata.rdw.nl/Voertuigen/Open-Data-RDW-Gekentekende_voertuigen/m9d7-ebf2/about_data

# Tests

The unit tests can be executed with `python -m unittest discover -s test test_utils.py`
