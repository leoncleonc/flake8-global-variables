# flake8-global-variables

[flake8](https://flake8.pycqa.org/en/latest/index.html) plugin to prevent from global
variables using.

## Installation

```bash
pip install flake8-global-variables
```

## Code example

Things checked with this plugin:

```python
# Global variable declaration
global_hello = 'Hello'


def fun_a():
    return 2


def fun_b(var=5):
    result = fun_a() + var
    return result


# And here global variable again 
global_var = 3

fun_b(global_var)

```

## Error codes

| Error code |      Description       |
|:----------:|:----------------------:|
|   GV400    | Found global variable  |

## License

MIT.
