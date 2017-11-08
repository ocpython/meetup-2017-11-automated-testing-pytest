# Running The Tests

### With unittest

All tests

```python
python -m unittest discover
```

Specific directory

```python
python -m unittest discover test_dir
```

### With pytest

All tests

```python
pytest
```

Specific file

```python
pytest test_file.py
```

Specific test

```python
pytest test_file.py::test_function
```

Specific test class and method

```python
pytest test_file.py::TesClass::test_method
```

Print test output

```python
pytest -s
```

# Test Coverage

### With unittest

```python
coverage run my_program.py arg1 arg2

coverage report -m

coverage html
```

### With pytest

Install [pytest-cov](https://pypi.python.org/pypi/pytest-cov) plugin.

```python
pytest --cov=my_module

pytest --cov=my_module --cov-report html

pytest --cov-config .coveragerc --cov=my_module --cov-report html
```
