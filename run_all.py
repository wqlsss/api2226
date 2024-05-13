# import logging
import pickle
import time
import unittest
from lib.HTMLTestRunner import HTMLTestRunner
from lib.send_email import send_email
from config.config import *
from test.suit.test_suit import *

# class MyTestCase(unittest.TestCase):
#     def test_all(self):
#         logging.info('======================运行所有的case======================')
#         suit = unittest.defaultTestLoader.discover(test_path,'test*.py')
#         # t = time.strftime('%Y_%m_%d_%H_%M_%S')
#         with open(report_file, 'wb') as f:
#             HTMLTestRunner(
#                 stream=f,
#                 title='xzs测试用例',
#                 description='xzs登录和注册用例集',
#                 verbosity=2
#             ).run(suit)
#
#         send_email(report_file)
#         logging.info('===================测试结束===================')
# if __name__ == '__main__':
#     unittest.main()

def discover():
    return unittest.defaultTestLoader.discover(test_case_path)
def run(suite):
    logging.info('==== 测试开始 ====')
    with open(report_file,'wb') as f:
        result = HTMLTestRunner(
                stream=f,
                title='接口测试',
                description='测试描述',
                verbosity=2,
                # tester='smart'
            ).run(suite)
        if result.failures:
            save_failures(result,last_fails_file)
    logging.info('==== 测试结束 ====')
def run_all():
    run(discover())
def run_suite(suite_name):
    suite = get_suite(suite_name)
    if isinstance(suite,unittest.TestSuite):
        run(suite)
    else:
        print('TestSuite不存在')

def collect():
    suite = unittest.TestSuite()
    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)
    _collect(discover())
    return suite

def collect_only():
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i),case.id()))
    print("-----------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i),time.time() - t0))

# def makesuite_by_testlist(test_list_file):
#     with open(test_list_file,encoding='utf-8') as f:
#         testlist = f.readlines()
#     print(testlist)
#     testlist = [i.strip() for i in testlist if not i.startswith("#")]
#     suite = unittest.TestSuite()
#     all_cases =collect()
#     for case in all_cases:
#         case_name = case.id().split('.')[-1]
#         if case_name in testlist:
#             suite.addTest(case)
#     return suite
def make_suit_list(list_file):
    with open(list_file,'r') as f:
        suit_list = f.readlines()
    suit_list = [x.strip() for x in suit_list if not x.startswith("#")]
    suite = unittest.TestSuite()
    all_cases =collect()
    for case in all_cases:
        if case.id().split('.')[-1] in suit_list:
            suite.addTest(case)
    return suite

def makesuit_by_tag(tag):
    suit = unittest.TestSuite()
    for case in collect():
        if case._testMethodDoc and tag in case._testMethodDoc:
            suit.addTest(case)
    return suit

def save_failures(result,file):
    suite = unittest.TestSuite()
    for case_result in result.failures:
        suite.addTest(case_result[0])
        with open(file,'wb') as f:
            pickle.dump(suite,f)

def rerun_fails():
    sys.path.append(test_case_path)
    with open(last_fails_file,'rb') as f:
        suite = pickle.load(f)
    run(suite)


if __name__ == '__main__':
   # suit = makesuite_by_testlist(test_list_file)
   # run(suit)
   # print(makesuit_by_tag('level1'))
   suit = make_suit_list(test_list_file)
   r = run(suit)
   # save_failures(r,last_fails_file)
   rerun_fails()