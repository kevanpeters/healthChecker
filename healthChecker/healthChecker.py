"""
Health Checker

Usage:
    healthChecker.py <url> [-p <port>] [-i interval]

Options:
    -h --help       Show this screen.
    -i <interval>   Number of health checks per second [default: 2].
"""
from docopt import docopt
from datetime import datetime #TODO
import logging
import requests
import time

logging.basicConfig(format='%(levelname)s | %(asctime)s | %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

class Check:
  """ Checks status and given Endpoint """
  def __init__(self, url, interval):
    self.url = url
    self.interval = int(interval)
    self.seconds_per_run = 1 / self.interval

  def run(self):
    logging.info(f"Starting HealthChecker against {self.url} running {args['-i']} times a Second")
    logging.info("--------------------------")
    logging.info("STATUS | TIME TO LAST BYTE")
    logging.info("--------------------------")
    starttime=time.time()
    while True:
      self.get_health()
      time.sleep(self.seconds_per_run - ((time.time() - starttime) % self.seconds_per_run))

  def get_health(self):
      try:
        start = time.time()
        requests.get(self.url, timeout=(3, 3))
        logging.info(f"SUCCESS | {round(time.time() - start, 5)}")
      except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        logging.error("FAILED TO CONNECT")
      except requests.exceptions.ReadTimeout:
        logging.error("FAILED TO RESOLVE")
      except Exception:
        logging.error("Exception occurred", exc_info=True)

if __name__ == "__main__":
    
    args = docopt(__doc__)
    checker = Check(args['<url>'], args['-i'])
    checker.run()
