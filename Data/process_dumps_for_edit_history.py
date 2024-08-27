import xml.etree.ElementTree as etree
from bz2 import BZ2File
import pandas as pd
import codecs
import csv
import os
import logging
import concurrent.futures
import tracemalloc




def parse_dump(filename):

    prefix = '{http://www.mediawiki.org/xml/export-0.10/}'
    p_timestamp = prefix + 'timestamp'
    p_username = prefix + 'username'
    p_ip=prefix + 'ip'
    c_timestamp=None
    c_username=None
    c_ip=None

    # open the file to save discussions' text
    hfile = codecs.open(str(file_save)+str(filename[:-4])+'.csv', 'w', encoding='utf-8')
    hfilecsv = csv.writer(hfile)
    hfilecsv.writerow(['username','timestamp'])


    with BZ2File(str(file_read)+str(filename), "r") as xml_file:
        parser = etree.iterparse(xml_file, events=('end',))
        for events, elem in parser:

            if elem.tag == p_timestamp:
                c_timestamp=elem.text
            if elem.tag == p_username:
                c_username=elem.text
                hfilecsv.writerow([c_username, c_timestamp])
            if elem.tag == p_ip:
                c_username=elem.text
                hfilecsv.writerow([c_username, c_timestamp])
            ## Do some cleaning
            # Get rid of that element
            elem.clear()



#================= RUN ======================



file_read='/mnt/data/elisavetk/A1_PROCESS_DUMPS_END_2022/download_dumps/Dumps_20230301_4/'
file_save='/mnt/data/elisavetk/A1_PROCESS_DUMPS_END_2022/process_dumps/TXT_20230301_edit_history/TXT_1443_1626/'
start_file=1443
end_file=1627



if not os.path.exists(file_save):
        os.mkdir(file_save)


def thread_function(name):
    logging.info("Thread %s: starting", name)
    parse_dump(name)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        executor.map(thread_function, [f'dump_{i}.bz2' for i in range(start_file,end_file)])
