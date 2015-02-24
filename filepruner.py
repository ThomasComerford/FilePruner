__author__ = 'Thomas'

import hashlib
import sys


def main(argv):
    olddir = ''
    newdir = ''
    mode = ''

    try:
        opts, args = getopt.getopt(argv, "ac", ["old=", "new="])
    except getopt.GetoptError:
        print 'usage: filepruner.py -a|-c --old=olddir --new=newldir'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-a':
            mode = "analyse"
        elif opt == '-c':
            mode = "clean"
        elif opt == '--old':
            olddir = arg
        elif opt == '--new':
            newdir = arg


def generate_md5_hash(f, block_size=2 ** 20):
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()


if __name__ == '__main__':
    main(sys.argv[1:])
