# What To Test

### Output Is Correct

```python
def contrived_example(in_list):
    return [n * 2 for n in in_list]
```

```python
def test_contrived_example_doubles_all_values_of_input_list():
    result = contrived_example([1, 2, 3, 4, 5])
    assert result == [2, 4, 6, 8, 10]
```

### Control flow (`if`/`else`)

* Does your code go down the right branch?
* Each condition should have one or more associated tests.

```python
def contrived_example(param_1):

if param_1 > 11:
    if_block_function()

else:
    else_block_function()
```

```python
def test_contrived_example_runs_if_block_function_if_param_1_greater_than_11(mocker):
    mocker.patch.object(contrived_example, 'if_block_function')
    contrived_example(22)
    assert contrived_example.if_block_function.called is True
```

```python
def test_contrived_example_runs_if_block_function_if_param_1_less_than_11(mocker):
    mocker.patch.object(contrived_example, 'else_block_function')
    contrived_example(22)
    assert contrived_example.else_block_function.called
```

#### Also Make Sure That Things That Shouldn't Happen Don't Happen

```python
def contrived_example(string_in):
    output = string_in

    if output == 'this':
        return uncalled_function()

    return output
```

```python
def test_contrived_example_does_not_modify_non_this_strings(mocker):
    mocker.patch.object(contrived_example, 'uncalled_function')
    result = contrived_example('those')
    assert contrived_example.uncalled_function.called is False
```

#### Don't Neglect Boolean Logic

```python
def contrived_example(list_in):

    for l in list_in:
        if l:
            boolean_function(l)
```

```python
def test_contrived_example_only_calls_boolean_function_if_input_evaluates_true(mocker):
    mocker.patch.object(contrived_example, 'boolean_function')
    result = contrived_example(1, 0, [], False, 'False')

    contrived_example.boolean_function.assert_called_with(1, 'False')
```

### Loops (for/while)

* Do `while` loops terminate when they should?

```python
def contrived_example():
    counter = 0

    while counter < 5:
        while_block_function()
        counter += 1
```

```python
def test_contrived_example_runs_while_block_function_correct_amount_of_times(mocker):
    mocker.patch.object(contrived_example, 'while_block_function')
    contrived_example()
    assert len(contrived_example.while_block_function.call_args_list) == 5
```

### Exceptions Get Raised

```python
def contrived_example(dividend, divisor):
    try:
        word_to_number(dividend) / word_to_number(divisor)

    except ZeroDivisionError as e:
        '{}: Divided by zero.'.format(e)
```

```python
def test_contrived_example_raises_divide_by_zero_error():
    with pytest.raises(ZeroDivisionError):
        contrived_example('one', 'zero')
```

# What To Not Test

* Don't test the standard library
* In general, don't test third party code if the developer already wrote their own test suite

# Tests Are Important

* ``Trust me, it just works.''
    - Increase client's confidence in your product.
* Tests are as important as commenting your code.
    - Serve as another form of documentation.
* Make sure code in production behaves the same as in your development environment.
* Writing tests can reveal bugs and edge cases.
* Something for the intern or new hire to do.
    - Well written tests should not have destructive side effects.

# Test Coverage

> Perfect is the enemy of good.

I use [coverage](https://pypi.python.org/pypi/coverage).

100% coverage for everything is unrealistic.  Test coverage isn't another metric for bean counters.  Use it as a tool to see what has been tested and make intelligent decisions about what you need to test.

# Functional Test v. Unit Test

Unit tests make sure individual components of your code (functions, classes) work as they should.  These should abstract away as many layers of other code as much as is reasonable.

Functional tests make sure your code interacts with other layers of your stack (DB, web server) as it should.

The lines can get blurry when you're working with something like a web framework that is heavily tied to a database.

# Should I Bother With Test Driven Development?

Test Driven Development (TDD) only works if everyone commits to it.

In my experience, it works better in an established codebase.  In early stages of tinkering when you haven't nailed down the requirements, all the preliminary tests are going to get thrown out.

If your project has very well defined requirements, TDD is a good point to start from.

# Advanced Testing Packages

### Faker

[Faker](https://pypi.python.org/pypi/Faker) generates random garbage data for you.

### Hypothesis

[Hypothesis](https://pypi.python.org/pypi/hypothesis/3.33.0) generates categories of data and feeds them into your code.  For example, if your code takes a string as a parameter, hypothesis will check your code with empty strings, unicode strings, etc to make sure it works.

### Behave

[Behave](https://pypi.python.org/pypi/behave) tests are written in [Gherkin](https://github.com/cucumber/cucumber/wiki/Gherkin) and are designed to be human readable.

### Useful Resources

[Test-Driven Development with Python](https://www.obeythetestinggoat.com/pages/book.html#toc)

Deploy and test a Django project using unittest and selenium.

[Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest)

Useful reference for pytest.  Assumes familiarity with testing in general.