import sys
import wget
import zipfile
import os


def main():
    url = sys.argv[1]
    filename = wget.download(url)

    dbf_data_path = os.getcwd() + '/dbf-data/' + url.split('/')[-1:][0][0:-4]

    if not os.path.exists(dbf_data_path):
        os.makedirs(dbf_data_path)

    zip = zipfile.ZipFile(filename)
    zip.extractall(dbf_data_path)
    zip.close()


if __name__ == "__main__":
    if (len(sys.argv) > 2 or len(sys.argv) == 1):
        raise Error('Invalid number of arguments')

    main()
