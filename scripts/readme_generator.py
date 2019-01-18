# -*- coding: utf-8 -*-
"""
This script generates Readme.md (markdown file) from the docstrings and other info from the files present in the '/scripts'.
"""

__script_name__ = "Readme.md Generator"
__version__ = "0.1.0"
__author__ = "Mayank Thakur"
__date__ = "17-01-2019"

import os
import importlib


root = "/scripts"
base_template = """# My Python Scripts ![](https://img.shields.io/github/repo-size/irotect/My-Python-Scripts.svg)

This Repository is a collection of my python scripts.


# Scripts

{entry}

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## License [![GitHub license](https://img.shields.io/github/license/irotect/My-Python-scripts.svg?style=plastic)](https://github.com/irotect/My-Python-Scripts/blob/master/LICENSE)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
"""

single_template = """
## <a href='scripts/{fname}'>{sname}</a> <sub>({ver})</sub> ![](https://img.shields.io/github/size/irotect/My-Python-Scripts/scripts/{fname}.svg)

Author: **{author}**

Date Updated: **{date}**

```Bash
{docstring}
```
"""


def list_files():
    file_list = []
    try:
        for entry in os.listdir("."):
            if os.path.isfile(entry) and entry.__contains__(".py") and not entry.__contains__("__init__"):
                file_list.append(entry)
                print("Found python script {}".format(entry))
    except FileNotFoundError:
        exit("Error: cant access the directory.")
    return file_list


if __name__ == "__main__":
    files = list_files()
    if not files:
        exit("No script Found, Exiting...")
    doc_data = []
    for file in files:
        blob = importlib.import_module(file.replace(".py", ""))
        doc_data.append(single_template.format(fname=file, sname=blob.__script_name__, ver=blob.__version__, author = blob.__author__, date=blob.__date__, docstring=blob.__doc__))

    with open("../README.md", "w") as readme:
        readme.write(base_template.format(entry = " ".join(doc_data)))
