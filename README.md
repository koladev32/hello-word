# Kolawole Hello World package

![CI](https://github.com/koladev32/hello-word/actions/workflows/ci.yml/badge.svg?branch=main)

This is a simple repository to learn how to deploy a package on PyPi.

To install the package,

```shell
pip install kolawole-hello-world 
```

## Usage

To use the package, do the following: 

```python
from hello_world import HelloWorld

a = HelloWorld("message")

a.log()
```