"""Bitdaan Dataset Preparation.

For dataset preparation, pass args like this:
    bitdaan --collect dataset --start-page 1 --end-page 2407

For just collect latest news which are not in dataset and did not analyze by bitdaan, pass args like this:
    bitdaan --collect latest

Usage:
    bitdaan [--collect=TYPE] [--start-page=NUMBER] [--end-page=NUMBER]
    
"""

import docopt
from collectors.news import *


def main():
    args = docopt.docopt(__doc__)
    if args['--collect'] == "dataset":
        if args['--start-page'] != None and args['--end-page'] != None:
            createDataset(int(args['--start-page']), int(args['--end-page']))
        else:
            exit('Error !\n\trun " bitdaan -h " for more help.')
    elif args['--collect'] == "continue":
        continueCreateDataset()
    elif args['--collect'] == "latest":
        print("latest")
    else:
        exit('Error !\n\trun " bitdaan -h " for more help.')


if __name__ == '__main__':
    main()
