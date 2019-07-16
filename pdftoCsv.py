import os
import camelot


def create_folder(file_name):
    """Will create output folder if it doesn't exist output folder will
        be created and inside that a new folder will be created acording
        to the pdf file name"""

    if os.path.exists('output'):
        if os.getcwd().split('/')[-1] == 'output':
            try:
                os.mkdir(file_name)
            except:
                print(f'{file_name} already exists.')
            os.chdir(file_name)
        else:
            os.chdir('output')
            try:
                os.mkdir(file_name)
            except:
                print(f'{file_name} already exists.')
            os.chdir(file_name)
    else:
        os.mkdir('output')
        os.chdir('output')
        try:
            os.mkdir(file_name)
        except:
            print(f'{file_name} already exists.')
        os.chdir(file_name)


def data_cleaning():
    pass


def main():
    """Main Function which is responsible for pdf parsing and exporting it into csv."""

    for pdf in os.listdir():
        file_name, file_extension = os.path.splitext(pdf)
        if file_extension == '.pdf':
            print(pdf)
            tables = camelot.read_pdf(
                pdf, flavor='stream', pages='4,5,6,7,8,9,10,11,12,13', )
            create_folder(file_name)
            tables.export('tables.csv', f='csv')


if __name__ == "__main__":
    main()
