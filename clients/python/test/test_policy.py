"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import lakefs_client
from lakefs_client.model.statement import Statement
globals()['Statement'] = Statement
from lakefs_client.model.policy import Policy


class TestPolicy(unittest.TestCase):
    """Policy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPolicy(self):
        """Test Policy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Policy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()