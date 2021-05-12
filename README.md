# DBImport
[![CircleCI](https://circleci.com/gh/FHDA/DBImport.svg?style=svg)](https://circleci.com/gh/FHDA/DBImport)

## Information

The purpose of this tool/prject is to store course information which are fetched from De Anza College / Foothill College portal into MongoDB database.

## Requirements

Python v3.6
node v10.16.0
npm v6.9.0 or above

## Install

Suggestion: use virtual environment such as conda, virtualenv...etc

do the following:

```script
pip install -r requirements.txt
```

## Usage(@todo)

Activate virtual environment if you have one. Usually the command is `activate virtural_name`

## Development (@todo)

Suggestion: use virtual environment such as conda, virtualenv...etc

do the following:

```py
npm install
pip install -r requirements.txt
```

We require all contributors to write docstring so the codes are easy to follow for other contributors. 
One of the software development processes is Test-driven Development(TDD). We highly recommended you *write at least one test before code*  
However, the test is recommended but not required.  
The philosophy is **you must know exactly the detailed behavior of your code does**.  

We use [pytest](https://docs.pytest.org/) to test our code.  
We use [pydocstring](http://pydocstyle.org/) to test our docstring.  
We use [autopep8](https://github.com/hhatto/autopep8) to format our code.  
We use [pylint](https://pylint.org) as Python linter.  

## Coding Style

In general, we follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) Python coding style and [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html).
However, when [PEP 8](https://www.python.org/dev/peps/pep-0008/) is in conflict with [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html), [PEP 8](https://www.python.org/dev/peps/pep-0008/) should be given precedence.

Some special rules:

1. max-line-length: 100

Please also write docstring so the codes are easy to follow for other contributors.
We follow [Google docstring style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

## Project Structure

    .
    DBImport/  
    │  
    ├── bin/  
    │  
    ├── docs/  
    │   └── docs.md  
    │  
    ├── DBImport/  
    │   ├── __init__.py  
    │   ├── runner.py  
    │   └── DBImport/  
    │       ├── __init__.py  
    │       ├── helpers.py  
    │       └── DBImport.py  
    │  
    ├── data/  
    │   └── input.json  
    │  
    ├── scripts/  
    │   ├── pre-commit.sh  
    │   └── pre-push.sh  
    ├── tests/  
    │   ├── 00_empty_test.py  
    │   └── DBImport  
    │       ├── helpers_tests.py  
    │       └── DBImport_tests.py 
    │  
    ├── .gittattributes
    ├── .gitignore
    ├── package.json
    ├── pylintrc
    ├── requirements.txt
    ├── setup.cfg  
    ├── LICENSE  
    └── README.md  

## Git Commit message

In general, we use "Semantic Commit Messages"

Reference:

1. https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716
2. https://github.com/joelparkerhenderson/git_commit_message#begin-with-a-short-summary-line

## .env or System Environment Variables Setting Instruction

    log_path = /Users/username/Personal_Workflow/dbworkflow/log/
    data_path = /Users/username/Personal_Workflow/dbworkflow/course-data/
    Mongo_User = <username of Mongodb login>
    Mongo_Password = <password of Mongodb login>
    Mongo_Postfix = <db connection string>(e.g. @something.mongodb.net/test?retryWrites=true&w=majority)
    start_year = <the first year you want to start with>(e.g. 2020)
    <year_1> = <year_1>_<quarter>_<schoole>_courseData.json,...
    <year_2> = <year_2>_<quarter>_<schoole>_courseData.json,...
    .
    .
    .
    <year_n> = <year_n>_<quarter>_<schoole>_courseData.json,...

Note: <year_1>...<year_n> should be consecutive and start_year should be between <year_1> and <year_n>