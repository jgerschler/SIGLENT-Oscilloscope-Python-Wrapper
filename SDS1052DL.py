#!/usr/bin/env python
# This is VERY much still in progress. Not ready to be used!
import visa, time

class Oscilloscope(object):
    def __init__(self):
        self.delay = 0.01
        
    def connect(self, instrument_id=0):
        self.rm = visa.ResourceManager()
        siglent_list = [instrument for instrument in self.rm.list_resources() if instrument.split('::')[1] == '0xF4EC']
        if len(siglent_list) >= instrument_id+1:
            print("Available oscilloscopes:")
            for idx, instrument in enumerate(siglent_list):
                print("ID:{0} (Oscilloscope Serial No. {1})".format(str(idx),instrument.split('::')[3]))
            print("")
            print("Connecting to oscilloscope (ID {0}).".format(str(instrument_id)))
            self.osc = self.rm.open_resource(siglent_list[instrument_id])
            print("")
            print("Connected.")
            return
        else:
            print("No Siglent oscilloscopes found, or you've selected a nonexistent oscilloscope ID.")
            return
            
    def disconnect(self):
        self.rm.close()
    
    def measure_vpp(self, channel):
        query_results = self.osc.query('C{0}:PAVA? PKPK'.format(str(channel)))
        time.sleep(self.delay)
        print(Oscilloscope.format_results(query_results))
        
    def measure_vmax(self, channel):
        query_results = self.osc.query('C{0}:PAVA? MAX'.format(str(channel)))
        time.sleep(self.delay)
        print(Oscilloscope.format_results(query_results))

    def measure_rms(self, channel):
        query_results = self.osc.query('C{0}:PAVA? RMS'.format(str(channel)))
        time.sleep(self.delay)
        print(Oscilloscope.format_results(query_results))

    def measure_freq(self, channel):
        query_results = self.osc.query('C{0}:PAVA? FREQ'.format(str(channel)))
        time.sleep(self.delay)
        print(Oscilloscope.format_results(query_results))

    def measure_period(self, channel):
        query_results = self.osc.query('C{0}:PAVA? PER'.format(str(channel)))
        time.sleep(self.delay)
        print(Oscilloscope.format_results(query_results))

    def set_vdiv(self, channel, value):
        """accepted values: 2mV, 5mV, 10mV, 50mV, 100mV, 200mV, 500mV, 1V, 2V, 5V, 10V"""
        if value in ('2mV', '5mV', '10mV', '50mV', '100mV', '200mV', '500mV', '1V', '2V', '5V', '10V'):
            self.osc.write('C{0}:VDIV {1}'.format(str(channel), value.upper()))
        else:
            print("Invalid voltage division value.")

    @staticmethod# fix this
    def format_results(query_results):
        return query_results.split(',')[1]
