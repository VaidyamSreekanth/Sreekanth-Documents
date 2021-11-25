'''
 datefmt='%m/%d/%Y %I:%M:%S %p'
'''
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s %(asctime)s %(message)s ',
                    datefmt='%m:%d:%Y %H::%M',
                    filename='debug.log',
                    filemode='w')

logging.info(' :: TEST 1 ')
logging.debug(' :: TEST 2 ')
logging.warning(' :: TEST 3 ')
logging.error(' :: TEST 4 ')
logging.critical(" :: TEST 5 ")
