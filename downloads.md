---
layout: other
---
# Download Montilang


To install and use MontiLang, you can either download from binaries, or build from source with the instructions listed below.

| Release Version       | Download                                                                                                           | MD5 Hash                         |
|-----------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Monti 2.0 for Windows | [MontiLang2-0Win.tar.gz](https://github.com/lduck11007/MontiLang/releases/download/2.0/MontiLang2-0Win.tar.gz)     | 2db56111f81541509c5894587f18074c |
| Monti 2.0 for Linux   | [MontiLang2-0Linux.tar.gz](https://github.com/lduck11007/MontiLang/releases/download/2.0/MontiLang2-0Linux.tar.gz) | 55ef6d2004147ce34d9c7566d8b099ee |
| Monti 2.0 Source code | [Source code](https://github.com/lduck11007/MontiLang/archive/2.0.tar.gz)                                          | e2a7912d17da663b080dea4064cdd6b8 |
| Monti 1.0 for Windows | [MontiLang1-0Win.tar.gz](https://github.com/lduck11007/MontiLang/releases/download/1.0/MontiLang1-0Win.tar.gz)     | 393edb03835a91df96316f73927d112a |
| Monti 1.0 for Linux   | [MontiLang1-0Linux.tar.gz](https://github.com/lduck11007/MontiLang/releases/download/1.0/MontiLang1-0Linux.tar.gz) | c83ded4b2affe4ec4a25912698e62ff3 |
| Monti 1.0 Source code | [Source code](https://github.com/lduck11007/MontiLang/archive/1.0.tar.gz)                                          | f1f4035d47e9ed41ea3313fe0f636d75 |

## Installation

The easiest way to install and use MontiLang is to download the appropriate files for your system from above. After this is done, add the binaries to the system path. On windows, this is done by modifying the environment variables for your system. On Linux-based machines, this could be done by modifying `/etc/profile`, `/etc/environment` or any other page. Follow the appropriate instructions for your distro.

## Building from source code

For more control over MontiLang and support over a wider range of systems, MontiLang can easily be built from source code with the tool [PyInstaller](https://pypi.python.org/pypi/PyInstaller/3.3) from the Python Package Index. Ensure that you have Python and Pip installed.

This is the recomended way to install MontiLang, as it gives a greater control over the language and provides features that may not be in a release yet.

```
python -m pip install pyinstaller
git clone https://github.com/lduck11007/MontiLang.git
cd MontiLang/src
pyinstaller --icon=../icon.ico main.py -n monti
```

The appropriate binaries will be located in `/MontiLang/src/dist/monti/`.


### Extras

#### Why MontiLang is better than Python

##### Better floating point accuracy

**Python:**
```python
>>>0.1 + 0.2
0.30000000000000004
```

**MontiLang:**
```nginx
>>>0.1 0.2 + PRINT .
0.3
```

##### Easier use of system commands

**Python:**
```python
from os import system
command = raw_input()
system(command)
```

**MontiLang:**
```nginx
INPUT CMD
```

##### Automatic int/float conversion

**Python:**
```python
>>>print 1 / 2
0
# Or:
>>>from __future__ import division
>>>print 1 / 2
0.5
```

**MontiLang:**
```nginx
>>>1 2 / PRINT .
0.5
```
