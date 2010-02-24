import unittest
from nose.tools import *
import panda

class PropertiesTest(unittest.TestCase):
    def setUp(self):
        self.i = panda.Panda(cloud_id='my-cloud-id', access_key='my-access-key', secret_key='my-secret-key')

    def test_cloud_id(self):
        eq_(self.i.cloud_id, 'my-cloud-id')

    def test_access_key(self):
        eq_(self.i.access_key, 'my-access-key')

    def test_secret_key(self):
        eq_(self.i.secret_key, 'my-secret-key')

    def test_api_host(self):
        eq_(self.i.api_host, 'api.pandastream.com')

    def test_api_port(self):
        eq_(self.i.api_port, 80)

class SignatureTest(unittest.TestCase):
    def setUp(self):
        self.i = panda.Panda(access_key='my_access_key', secret_key='my_secret_key', api_host='myapihost', api_port=85, cloud_id='my_cloud_id')

    def test_simple_signed_params(self):
        result = self.i.signed_params('POST', '/videos.json', {}, '2009-11-04T17:54:11+00:00')
        expectation = {
            'access_key': "my_access_key",
            'timestamp': "2009-11-04T17:54:11+00:00",
            'cloud_id': 'my_cloud_id',
            'signature': 'TI2n/dsSllxFhxcEShRGKWtDSqxu+kuJUPs335NavMo=',
        }
        eq_(result, expectation)

    def test_signed_params_with_arguments(self):
        result = self.i.signed_params('POST', '/videos.json', {'param1': 'one', 'param2': 'two'}, '2009-11-04T17:54:11+00:00')
        expectation = {
            'access_key': "my_access_key",
            'timestamp': "2009-11-04T17:54:11+00:00",
            'cloud_id': 'my_cloud_id',
            'signature': 'w66goW6Ve5CT9Ibbx3ryvq4XM8OfIfSZe5oapgZBaUs=',
            'param1': 'one',
            'param2': 'two',
        }
        eq_(result, expectation)
