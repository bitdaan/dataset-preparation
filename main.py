"""Bitdaan Dataset Preparation.

For dataset preparation, pass args like this:
    python main --collect dataset --start-page 1 --end-page 2407

For continue dataset preparation, pass args like this:
    python main --collect continue

For just collect latest news which are not in dataset and did not analyze by bitdaan, pass args like this:
    python main --collect latest

Usage:
    bitdaan [--collect=TYPE] [--start-page=NUMBER] [--end-page=NUMBER]
    
"""

import docopt
import os
from collectors.news import *
from collectors.latestNews import *


def main():
    args = docopt.docopt(__doc__)
    if args['--collect'] == "dataset":
        if args['--start-page'] != None and args['--end-page'] != None:
            if os.path.exists("pickles/peak-flag.pickle"):
                os.remove("pickles/peak-flag.pickle")
            if os.path.exists("pickles/continue-date.pickle"):
                os.remove("pickles/continue-date.pickle")
            createDataset(int(args['--start-page']), int(args['--end-page']))
        else:
            exit('Error !\n\trun " bitdaan -h " for more help.')
    elif args['--collect'] == "continue":
        continueCreateDataset()
    elif args['--collect'] == "latest":
        collectLatestNews()
    else:
        exit('Error !\n\trun " bitdaan -h " for more help.')


if __name__ == '__main__':
    main()
