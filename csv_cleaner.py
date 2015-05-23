#!/usr/bin/env python


import csv
import os
import argparse

descripton = """Iterate through csv file, write each row of given length to corresponding out_<row_length>.csv file
NOTE: if you have many different row lenghts, you will create many differnt out_<row_length>.csv files"""


parser = argparse.ArgumentParser(description=descripton)
parser.add_argument('-i', '--input_path',
                    help='path to csv file to parse', required=True)

parser.add_argument('-o', '--output_path',
                    help='path to directory where csv output is saved', default='.')

args = parser.parse_args()

OUT_PATH = args.output_path
INPUT_FILE = args.input_path


with open(INPUT_FILE) as input_file:
    writers = {}
    reader = csv.reader(input_file)
    header = next(reader)
    for row in reader:
        row_len = len(row)
        if row_len in writers:
            writer = writers[row_len]['writer']
        else:
            fhandle = open(os.path.join(OUT_PATH, 'out_{}.csv'.format(row_len)), 'w')
            writer = csv.writer(fhandle)
            writers[row_len] = {'writer': writer, 'fhandle': fhandle}
        writer.writerow(row)
    #csv writer won't write all rows until the file handle is closed
    else:
        for k, v in writers.items():
            v['fhandle'].close()
