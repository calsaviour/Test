import os
import sys
import getopt


inputfile = ''
numberOfFiles = ''
texttoreplace = '1000'
texttoinsert = 'I am change'


def find_last_occurence_of_text(filetosearch):
    s = open(filetosearch, 'r')
    lines = s.read()
    print lines.find('Header')


def create_file(inputfile, filetosave):
    s = open(inputfile).read()
    s = s.replace(texttoreplace, texttoinsert)
    f = open(filetosave, 'w')
    f.write(s)
    f.close()


def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        # Reduce the argument list by copying it starting from index 1.
        argv = argv[1:]
    return opts


def check_for_argument(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:c:", ["ifile=", "numberOfFiles="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -c <numberOfFiles>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -c <numberOfFiles>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-c", "--numberOfFiles"):
            numberOfFiles = arg
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Starting process"
    print 'Input file is "', inputfile
    print 'Number of files to be created', numberOfFiles
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
    return inputfile, numberOfFiles

if __name__ == '__main__':
    # find_last_occurence_of_text(filetosearch)
    inputfile, numberOfFiles = check_for_argument(sys.argv[1:])
    cwd = os.getcwd()
    for count in range(0, int(numberOfFiles)):
        filetosave = str(cwd) + '/data' + str(count) + ".txt"
        create_file(inputfile, filetosave)
