#!/usr/bin/env python
# This is VERY much still in progress. Not ready to be used!
import visa, time

class Oscilloscope(object):
    #def __init__(self):

    def find_oscopes(self):
        rm = visa.ResourceManager()
        siglent_list = [instrument for instrument in rm.list_resources() if instrument.split('::')[1] == '0xF4EC']
        for instrument in siglent_list:
            print('Found a Siglent Oscilloscope. Serial:{}'.format(instrument.split('::')[3]))
                
            
        
        
