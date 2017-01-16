#!/usr/bin/env python
# This is VERY much still in progress. Not ready to be used!
import visa, time

class Oscilloscope(object):
    delay = 0.01
    #def __init__(self):

    def connect(self, instrument_id=0):
        self.rm = visa.ResourceManager()
        siglent_list = [instrument for instrument in self.rm.list_resources() if instrument.split('::')[1] == '0xF4EC']
        if len(siglent_list) >= instrument_id+1:
            print("Available oscilloscopes:")
            for idx, instrument in enumerate(siglent_list):
                print("ID:{0} (Oscilloscope Serial No. {1})".format(str(idx),instrument.split('::')[3]))
            print("")
            print("Connecting to oscilloscope (ID {}).".format(str(instrument_id)))
            self.osc = self.rm.open_resource(siglent_list[instrument_id])
            print("")
            print("Connected.")
            return
        else:
            print("No Siglent oscilloscopes found, or you've selected a nonexistent oscilloscope ID")
            return
            
    def disconnect(self):
        self.rm.close()
        
    def measure_vpp(self, channel):
        query_results = self.osc.query('C{}:PAVA? PKPK'.format(str(channel)))
        time.sleep(Oscilloscope.delay)
        print(query_results)
        
##    def measure_vpp(self, channel):
##        query_results = self.osc.query('C{}:PAVA? PKPK'.format(str(channel)))
##        time.sleep(Oscilloscope.delay)
##        print(query_results)
