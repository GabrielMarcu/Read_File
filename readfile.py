# Scrie o aplicatie care sa poata fi executata din linie de comanda (terminal), care sa primeasca
# argumente fisiere text si/sau csv si sa returneze continutul fisierelor in terminal

import csv
import os.path
import sys


def read_file_csv(path: str) -> list:
    """Reads a csv file
    :return : a list of rows of a csv file"""
    with open(path, 'r') as fr:
        reader = csv.reader(fr)
        rows = [row for row in reader]
    return rows


def read_file_txt(path: str) -> list[str]:
    """Reads a text file
    :return : a list of rows of a text file"""
    with open(path, 'r') as fr:
        lines = fr.readlines()
    return lines


if __name__ == "__main__":
    file_path = ''.join(sys.argv[1::])
    if os.path.splitext(file_path)[1] == '.csv':
        file = ''.join(read_file_csv(file_path))
        print(file)
    elif os.path.splitext(file_path)[1] == '.txt':
        file = ''.join(read_file_txt(file_path))
        print(file)
    else:
        ext = os.path.splitext(file_path)[1]
        print(f'Not implemented for files {ext}')
