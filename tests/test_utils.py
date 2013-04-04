from datetime import datetime
import testtools

import falcon


class TestFalconUtils(testtools.TestCase):

    def test_dt_to_http(self):
        self.assertEquals(
            falcon.dt_to_http(datetime(2013, 4, 4)),
            'Thu, 04 Apr 2013 00:00:00 GMT')

        self.assertEquals(
            falcon.dt_to_http(datetime(2013, 4, 4, 10, 28, 54)),
            'Thu, 04 Apr 2013 10:28:54 GMT')

    def test_pack_query_params_none(self):
        self.assertEquals(
            falcon.to_query_str({}),
            '')

    def test_pack_query_params_one(self):
        self.assertEquals(
            falcon.to_query_str({'limit': 10}),
            '?limit=10')

    def test_pack_query_params_several(self):
        garbage_in = {
            'limit': 17,
            'echo': True,
            'doit': False,
            'x': 'val',
            'y': 0.2
        }

        query_str = falcon.to_query_str(garbage_in)
        fields = query_str[1:].split('&')

        garbage_out = {}
        for field in fields:
            k, v = field.split('=')
            garbage_out[k] = v

        expected = {
            'echo': 'true',
            'limit': '17',
            'x': 'val',
            'y': '0.2',
            'doit': 'false'}

        self.assertEquals(expected, garbage_out)
