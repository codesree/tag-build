import unittest
from HtmlTestRunner import HTMLTestRunner
import logging



class awscert(unittest.TestCase):


    def test_aws_csa(self):
        """ test case 1 """
        print("this is the aws csa test case")
        unittest.TestResult("Executing currently........")

    #@unittest.skip('done')
    def test_aws_cda(self):
        """ test case 2 """
        print("this is the aws cda test case")

        raise ValueError

    @unittest.skip('test completed')
    def test_aws_cda2(self):
        """ test case 2 """
        print("this is the aws cda test case")


"""
if __name__ == '__main__':

    runner = HTMLTestRunner(output='example_suite')
    runner.run(unittest.makeSuite(awscert))

"""