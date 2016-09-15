#! /usr/bin/env python

import numpy as np
import pandas as pd

class NHL:
    '''
    '''

    # Make'em work like a dictionary:
    def __getitem__(self, key):
        if self.filedata.has_key(key):
            return self.filedata[key].get_value()
        elif self.data.has_key(key):
            return self.data[key]
        else:
            raise KeyError('Key not found in object.')
    def __setitem__(self, key,value):
        self.data[key]=value
        self.namevars.append(key)

    def keys(self):
        '''
        List all keys for data objects stored in the RamSat object.
        '''
        return  self.data.keys()

    def has_key(self,key):
        '''
        Checks object dictionaries for "key", returns boolean.
        '''
        if self.data.has_key(key):
            return True
        else:
            return False

    def __init__(self, filename,*args, **kwargs):
        # Filename:
        #super(PbData, self).__init__(*args, **kwargs)
        self.filename=filename

        self._read(filename)


    def close(self):
        f.close()

    def _read(self,filename):
        '''
        Load the NCDF file.  Should only be called by __init__().
        '''
        import csv
        with open(filename,'rb') as f:
            data = [row for row in csv.reader(f.read().splitlines())]
        f.close()

        self.namevars = data.pop(0)
        self.rawdata = data
        self.nVars = len(self.namevars)
        self.nPlayers = len(data[:])
        #self.Players = np.zeros(self.nPlayers,dtype=object)
        self.Players = {}
        for i,l in enumerate(data):
            self.Players[l[0]] = l[1:]




if __name__ == '__main__':
    
    fname = 'Adjusted NHL Stats 1968-2013.xlsx'
    fname = 'Career.csv'
    nhl = NHL(fname)
    #read_xlsx(fname)
