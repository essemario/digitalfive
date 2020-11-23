import os
import sys
from simpledbf import Dbf5


def main():
    file_path = sys.argv[1]
    dbf = Dbf5(file_path)

    file_name = file_path.split('/')[-1:][0][0:-4]
    dbf.to_textsql(
        os.getcwd() + '/' + file_name + '.sql',
        os.getcwd() + '/' + file_name + '.csv',
        sqltype='sqlite'
    )


if __name__ == '__main__':
    if (len(sys.argv) > 2 or len(sys.argv) == 1):
        raise Error('Invalid number of arguments')

    main()
