#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse

from inflammation import models, views


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    in_files = args.infiles
    if not isinstance(in_files, list):
        in_files = [args.infiles]


    for filename in in_files:
        inflammation_data = models.load_csv(filename)

        view_data = {
            'average': models.daily_mean(inflammation_data),
            'max': models.daily_max(inflammation_data),
            'min': models.daily_min(inflammation_data),
            'std_dev': models.daily_std_dev(inflammation_data)
            }

        views.visualize(view_data)

        if args.text:
            print(f"\
                  Summary of statistics:             \n\
                  Average   : {view_data['average']} \n\
                  Max       : {view_data['max']}     \n\
                  Min       : {view_data['min']}     \n\
                  Std dev   : {view_data['std_dev']} \n\
                  ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')
    
    parser.add_argument(
        '--text',
        dest='text',
        action='store_true',
        help='Show statistics in text on command line')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    args = parser.parse_args()

    main(args)
