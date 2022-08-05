# Vietnam Tax Identifier Number validator

This is simple project that helps you to validate the vietnam tax numbers.

### Base example

Given the tax identifer number string, we can check the validity

``` python

from vntin.common import validate_tin
validate_tin("0305418909")
# must be 1 - mean valid

```

### Documentation
We have got a simple documentation page here.


### Features

* no dependencies
* support Python 3.6+ version
* MIT license

### Installation

You can install this package via `pip`

``` python

pip install vietnam-tin-checker

```

It may be safer however to install via;

``` python

python -m pip install vietnam-tin-checker

```

### Contributing

Make sure you check out the issue list beforehand in order to prevent double work before you make a pull request. To get started locally, you can clone the repo and quickly get started using the `Makefile`.

``` bash

git clone git@github.com:lampts/vntinchecker.git
cd vntinchecker
make install-dev

```