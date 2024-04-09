from hitmotop import search_in_hitmotop
import csv
import os


# https://eu.hitmotop.com/

def write_csv_file(data):
    dirs = 'data'
    if not os.path.exists(dirs):
        os.mkdir(dirs)

    result = data
    for row in result:
        with open(dirs + "/" + "musics.csv", 'a+', encoding = 'utf-8') as f:
            csvwriter = csv.writer(f, lineterminator = '\n')
            csvwriter.writerow(row)


def main():
    input_part = input("Search-->")
    data = search_in_hitmotop(input_part)

    write_csv_file(data)

    print("Successfully saved data")


if __name__ == '__main__':
    main()
