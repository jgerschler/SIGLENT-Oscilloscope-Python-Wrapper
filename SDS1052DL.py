#!/usr/bin/env python
# This is VERY much still in progress. Not ready to be used!
import visa, time

class Oscilloscope(object):
    #def __init__(self):

    def enumerate_osc(self):
        rm = visa.ResourceManager()
        siglent_list = [instrument for instrument in rm.list_resources() if instrument.split('::')[1] == '0xF4EC']
        for idx, instrument in enumerate(siglent_list):
            print('ID:{0} (Oscilloscope Serial No. {1})'.format(str(idx),instrument.split('::')[3]))
                
            
        
        
