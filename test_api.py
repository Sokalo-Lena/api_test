#!/usr/bin/env python

import requests
import unittest
import json

class ApiTests(unittest.TestCase):
    def test_request1(self):

        print 'first test'
        r = requests.get('http://services.groupkt.com/country/search?text=un')
        print r.status_code
        self.assertEqual(r.status_code, 200)
        print 'Assert status code: 200 OK'
        data = r.json()

        country_list ={
                    "name" : "Israel",
                    "alpha2_code" : "IL",
                    "alpha3_code" : "ISR",
                    "name" : "United Arab Emirates",
                    "alpha2_code" : "AE",
                    "alpha3_code" : "ARE",
                    }

        for value in country_list:
            print value, country_list[value]

        print 'response json test OK'




        d = {'x': 1, 'y': 2, 'z': 3}
        for key, value in d.iteritems():
            print key, value




if __name__ == '__main__':
    unittest.main()