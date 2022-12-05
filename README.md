# Bitdaan dataset preparation
This is a tool implemented for the Bitdaan project that gathers news about Bitcoin.

## Getting Started

After clone this repo

`pip install -r requirements.txt`

For dataset preparation

  `python main.py --collect dataset --start-page [Number] --end-page [Number] --path [PATH]` 

For continue dataset preparation,

  `python main.py --collect continue`

For just collect latest news which are not in dataset and did not analyze by bitdaan
  
  `python main.py --collect latest --path [PATH]`
