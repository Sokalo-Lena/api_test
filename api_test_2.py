#!/usr/bin/env python

import requests
import unittest
import json

class ApiTests(unittest.TestCase):
    def test_request1(self):
        r = requests.get('http://services.groupkt.com/state/get/IND/UP')
        print r.status_code
        self.assertEqual(r.status_code, 200)
        print 'Assert status code: 200 OK'
        param = r.json()
        self.assertEqual(param['RestResponse']['result']['id'],82)
        self.assertEqual(param['RestResponse']['result']['country'],'IND')
        self.assertEqual(param['RestResponse']['result']['name'],'Uttar Pradesh')
        self.assertEqual(param['RestResponse']['result']['abbr'],'UP')
        self.assertEqual(param['RestResponse']['result']['largest_city'],'Lucknow')
        self.assertEqual(param['RestResponse']['result']['capital'],'Lucknow')
        print 'response json test OK'

if __name__ == '__main__':
    unittest.main()