#!/usr/bin/env python

import requests
import unittest
import json

class ApiTests(unittest.TestCase):
    def test_request1(self):
        print 'first test'
        r = requests.get('http://services.groupkt.com/country/get/iso2code/IN')
        print r.status_code
        self.assertEqual(r.status_code, 200)
        print 'Assert status code: 200 OK'
        #print r.json['RestResponse']['result']
        data = r.json()
        self.assertEqual(data['RestResponse']['result']['name'],'India')
        self.assertEqual(data['RestResponse']['result']['alpha2_code'],'IN')
        self.assertEqual(data['RestResponse']['result']['alpha3_code'],'IND')
        print 'response json test OK'

if __name__ == '__main__':
    unittest.main()