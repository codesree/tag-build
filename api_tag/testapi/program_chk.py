import datetime
import logging
import os


def processlog():
    global curr_time
    curr_time = datetime.datetime.now().isoformat()

    print("Current time as per python datetime module is .",
          curr_time)
    global dof
    dof = {"formtime": "%(asctime)s - %(name)s - %(levelname)s - %(message)s", 'noform': ''}

    set_log('test_chamber','INFO',dof['formtime'])
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

    data = {"name": "srekanth",
            "age": 29,
            }

    set_log('test_chamber','INFO',dof['noform'])


    logger.info('')

def set_log(logdata,loglevl,format):

    if logdata == 'test_chamber':
        tfilename = 'log_asset_homecont_'+curr_time
        print(tfilename)
        tfilename = tfilename + '.json'
    elif logdata == 'test_chamber_2':
        tfilename = 'log_asset_vehicle_'+curr_time
        print(tfilename)
        tfilename = tfilename + '.json'


    global logger
    logger = logging.getLogger(logdata)
    if loglevl == 'DEBUG':
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
    elif loglevl == 'INFO':
        logger.setLevel(logging.INFO)
        ch = logging.FileHandler(os.path.join('test_chamber',tfilename),"a")
        ch.setLevel(logging.INFO)
    elif loglevl == 'WARNING':
        logger.setLevel(logging.WARNING)
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)
    elif loglevl == 'ERROR':
        logger.setLevel(logging.ERROR)
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

    formatter = logging.Formatter(format)

    ch.setFormatter(formatter)

    logger.addHandler(ch)

if __name__ == '__main__':
    processlog()

"""
print(type(leni))
print(len(leni))

datak = leni.keys()
print(datak)
datal = list(datak)

kcount = 0
print("length of datal",len(datal))

while kcount < len(datal):
      print("key count is",kcount)
      if datal[kcount] == 'Alarm':
         print("found!!!!")
         print(datal[kcount])

         testkey = datal[kcount]

         print(leni[testkey])

         testfact = leni[testkey]
         precount = len(testfact)

         print(precount)

         for factnum in testfact.values():
               print(factnum)


         break
      kcount = kcount + 1
else:
      print("Test_Rating_factor Key does not exist in test DB..Test case failed")
"""