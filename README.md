# Python Scripting Template

Christopher Todd's Python Project Base (For Scripting Efforts)

## Table of Contents

- [Dependencies](#dependencies)
- [Bin Scripts](#bin-scripts)
- [Classes](#classes)
- [Tests](#tests)

## Dependencies

### Python Packages

- Add Python (PIP/Anaconda Installed) Libraries

### Other Packages

- Add Peronsal Libraries (Cross-Dependencies)

## Bin Scripts

Executable scripts to run functionality. Will call libraries and classes
to acomplish a goal

### [bin_template.py](https://github.com/ChristopherHaydenTodd/ctodd_python_scripting_template/blob/master/bin_template.py)

Script Skeleton to be used for bin scripts

Steps:
- N/A

Usage:
```sh
./bin_template.py --necessary_param {{--optional_param}}
```

## Classes

Classes to hold reusable code and OOP coding methodologies

### [class_template.py](https://github.com/ChristopherHaydenTodd/ctodd_python_scripting_template/blob/master/classes/class_template.py)

Purpose:

Template Class to Build on when building a Python Project

Usage:
``` python
class_template_object = ClassTemplate('some_param')
class_template_object =\
    ClassTemplate('some_param', 'not_needed')	
```

Tests:

Unittesting for Classes and Python Libraries

### [test_template.py](https://github.com/ChristopherHaydenTodd/ctodd_python_scripting_template/blob/master/tests/test_template.py)

Purpose:

Test File Can be used as a basis for unittesting classes
and other Python constructs

Usage:

``` sh
python3 -m pytest test_template.py
```