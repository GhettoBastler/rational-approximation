# stern_brocot.py

A script that finds the best relative approximations of an floating point number by searching the [Stern-Brocot tree](https://en.wikipedia.org/wiki/Stern%E2%80%93Brocot_tree).

## Requirements

- Python3

## Usage

```
./stern_brocot.py target_number
```

By default, the script prints three different values, the first one having an error less than 10%, the second having an error less than 5%, and the third less than 1%.

The `-a`/`--all` option prints every successive relative approximations until the target number is reached.

## Licensing

The code for this project is licensed under the terms of the GNU GPLv3 license.
