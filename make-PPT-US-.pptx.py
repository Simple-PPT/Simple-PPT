print("Note:Before make a PPT(.pptx) file,please write the info.xlsx file first.")
from pptx import Presentation as PreS
from pptx.util import Pt
import pandas as pd
import time
from alive_progress import alive_bar

exda = {
    'excel(Yes/None)':None,
    'pictrue(Yes/None)':None,
    'pagenum(num)':None,
        }
d_s_e_f = pd.DataFrame(exda,index=[0])
d_s_e_f.to_excel('info.xlsx')
wait_time = int(input("Please input your wait time for write info.xlsx:"))
with alive_bar(len(range(wait_time))) as bar:
    for i in range(wait_time):
        time.sleep(1)
        bar()
incase_OK = input("Are you write info.xlsx OK? (y/n):")
