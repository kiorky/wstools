#!/usr/bin/env python
import unittest, tarfile, os, ConfigParser
import test_t1

SECTION='files'
CONFIG_FILE = 'config.py'

def main():
    config = ConfigParser.ConfigParser()
    config.read(CONFIG_FILE)
    archives = config.get(SECTION, 'archives')
    archives = eval(archives)
    test_t1.CONFIG = config 
    for file in archives:
        tar = tarfile.open(file)
        if not os.access(tar.membernames[0], os.R_OK):
            for i in tar.getnames(): 
                tar.extract(i)

    unittest.TestProgram(defaultTest='test_t1.makeStandAloneSuite')


if __name__ == "__main__" : main()
