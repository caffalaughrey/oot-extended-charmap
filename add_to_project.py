#!/usr/bin/env python3

from sys import argv

import shutil
import sys
import os

OOT_EXTENDED_CHARMAP_PATH = os.path.dirname(os.path.realpath(__file__))


def exit_if_not_exists(path):
    if not os.path.exists(path):
        sys.exit('Path does not exist: %s' % path)


def main():
    if len(sys.argv) != 2:
        print('Usage:\n\tadd_to_project.py OOT_PATH')

        exit()
    else:
        oot_path = argv[1]

        exit_if_not_exists(oot_path)

        for (dirpath, dirnames, filenames) in os.walk(OOT_EXTENDED_CHARMAP_PATH):
            if dirpath != OOT_EXTENDED_CHARMAP_PATH and '.git' not in dirpath and '.idea' not in dirpath:
                relative = dirpath.split(OOT_EXTENDED_CHARMAP_PATH + '/')[1]
                oot_dest = os.path.join(oot_path, relative)

                exit_if_not_exists(oot_dest)

                for filename in filenames:
                    if filename != '.DS_Store':
                        source = os.path.join(dirpath, filename)
                        destination = os.path.join(oot_dest, filename)

                        shutil.copy(source, destination)

                        print("Copied %s to %s" % (source, destination))



if __name__ == '__main__':
    main()
