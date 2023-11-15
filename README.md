# Upwork Web Crawler

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

I will use this get projects from upwork.

**I do not condone mass web scraping, this exists for personal automation reasons**

## Getting Started <a name = "getting_started"></a>


### Prerequisites

You will need poetry installed 

On Arch, you can use

```bash
yay -S python-poetry 
```

### Installing

Once you get poetry simply run the following


```bash
poetry install --no-cache
poetry shell 
```

## Usage <a name = "usage"></a>

Now you should be in your poetry shell to execute the command below.


```bash
python main.py --topic "Machine Learning" --n 10
```
