from csvreader import CsvReader
import sys 

if __name__ == "__main__":
    filename = sys.argv[1]
    with CsvReader(filename, skip_top=0,header=True, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.name)
            print(reader.getheader(), end = "\n")
            print(reader.getdata(), end = "\n\n")
            

    with CsvReader(filename, header = True, skip_top=17, skip_bottom=0) as reader:
        if reader == None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end = "\n")
            print(reader.getdata(), end = "\n\n")

    with CsvReader('1337') as reader:
        if reader == None:
            print("File is corrupted or missing")

