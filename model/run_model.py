#!/usr/bin/env python3
"""Reproduce your result by your saved model.

This is a script that helps reproduce your prediction results using your saved
model. This script is unfinished and you need to fill in to make this script
work. If you are using R, please use the R script template instead.

The script needs to work by typing the following commandline (file names can be
different):

python3 run_model.py -i unlabelled_sample.txt -m model.pkl -o output.txt

"""

# author: Egor Galkin
# date: 18.05.2022

import argparse
import sys
# Start your coding
import pandas as pd
from joblib import load


# End your coding


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Reproduce the prediction')
    parser.add_argument('-i', '--input', required=True, dest='input_file',
                        metavar='unlabelled_sample.txt', type=str,
                        help='Path of the input file')
    parser.add_argument('-m', '--model', required=True, dest='model_file',
                        metavar='model.pkl', type=str,
                        help='Path of the model file')
    parser.add_argument('-o', '--output', required=True,
                        dest='output_file', metavar='output.txt', type=str,
                        help='Path of the output file')
    # Parse options
    args = parser.parse_args()

    if args.input_file is None:
        sys.exit('Input is missing!')

    if args.model_file is None:
        sys.exit('Model file is missing!')

    if args.output_file is None:
        sys.exit('Output is not designated!')

    # Start your coding
    call = pd.read_csv(args.input_file, sep='\t')

    HER2_chr = 17
    HER2_start = 35076296

    HER2_status = call[(call['Chromosome'] == HER2_chr) & (call['Start'] == HER2_start)]\
                      .drop(columns=['Chromosome', 'Start', 'End', 'Nclone']).squeeze(axis=0) == 2

    X = call[HER2_status[~HER2_status].index].T
    model = load(args.model_file)
    y_pred = model.predict(X).astype(bool)

    prediction_HR = pd.Series('HR+', index=X.index[y_pred])
    prediction_TN = pd.Series('Triple Neg', index=X.index[~y_pred])
    prediction_HER2 = pd.Series('HER2+', index=HER2_status[HER2_status].index)

    predictions_all = pd.concat([prediction_HR, prediction_TN, prediction_HER2])[call.columns[4:]]

    predictions_all.to_csv(args.output_file, sep='\t', index_label='Sample', header=['Subgroup'], quoting=1)

    # End your coding


if __name__ == '__main__':
    main()
