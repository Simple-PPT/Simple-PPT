print("Note:Before make a PPT(.pptx) file,please write the info.xlsx file first.")
from pptx import Presentation as PreS
from pptx.util import Pt
import pandas as pd
import time
from tqdm import tqdm

exda = {
    'excel(Yes/None)':None,
    'pictrue(Yes/None)':None,
    'pagenum(num)':None,
        }
d_s_e_f = pd.DataFrame(exda,index=[0])
d_s_e_f.to_excel('info.xlsx')
class wait(object):
    def to_wait(self):
        try:
            self.wait_time = int(input("Please input your wait time for write info.xlsx:"))
            for i in tqdm(range(self.wait_time)):
                time.sleep(1)
        except:
            pass

def make_PPT():
    print()
wait().to_wait()
incase_OK = input("Are you write info.xlsx OK? (y/n):")
if incase_OK == "y" or incase_OK  == "Y":
    make_PPT()
elif incase_OK == "n" or incase_OK == "N":
    wait().to_wait()
    incase_OK_1 = input("Are you write info.xlsx OK? (y/n):")
    if incase_OK_1 == "y" or incase_OK_1 == "Y":
        make_PPT()
    else:
        pass
else:
    print("Only y or n.")
    wait().to_wait()
    incase_OK_1 = input("Are you write info.xlsx OK? (y/n):")
    if incase_OK_1 == "y" or incase_OK_1 == "Y":
        make_PPT()
    else:
        pass
