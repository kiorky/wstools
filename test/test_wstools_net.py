#!/usr/bin/env python
import unittest, tarfile, os, ConfigParser
import test_t1

CONFIG_FILE = 'config.py'

def main():
    config = ConfigParser.ConfigParser()
    config.read(CONFIG_FILE)
    test_t1.CONFIG = config 
    unittest.TestProgram(defaultTest='test_t1.makeNetworkSuite')


if __name__ == "__main__" : main()
