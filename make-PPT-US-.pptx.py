print("Note:Before make a PPT(.pptx) file,please write the info.xlsx file first.")
from pptx import Presentation
import pandas as pd
import time
from tqdm import tqdm
import numpy as np

exda = {
    'pagenumbers(num)':1,
    'style(1 - 11)':1,
    'PPT\'s name(string)':None,
    'title(string)':None,
    'subtitle(string)':None,
        }
write_nobugs = pd.ExcelWriter("info.xlsx")
d_s_e_f = pd.DataFrame(exda,index = [0])
d_s_e_f.to_excel(write_nobugs,sheet_name = 'read',index = False)
d_s_e_f['style(1 - 11)'].astype(dtype = int)
write_nobugs.save()
write_nobugs.close()
class wait(object):
    def to_wait(self):
        try:
            self.wait_time = int(input("Please input your wait time for write info.xlsx(s):"))
            for i in tqdm(range(self.wait_time)):
                time.sleep(1)
        except:
            pass

def make_PPT(style,name,title_input,subtitle_input):
    ppt =Presentation()
    to_int_style = np.array(style).item()
    title_slide = ppt.slides.add_slide(ppt.slide_layouts[to_int_style - 1])
    title = title_slide.shapes.title
    title.text = str(title_input)
    subtitle = title_slide.placeholders[1]
    subtitle.text = str(subtitle_input)
    ppt.save(str(name) + ".pptx")
wait().to_wait()
incase_OK = input("Are you write info.xlsx yet? (y/n):")
if incase_OK == "y" or incase_OK  == "Y":
    make_PPT(style = pd.read_excel("./info.xlsx",sheet_name = "read",usecols = ['style(1 - 11)'],dtype = int),name = pd.read_excel("./info.xlsx",sheet_name = "read",usecols = ['PPT\'s name(string)'],dtype = str),title_input=pd.read_excel("./info.xlsx",sheet_name = "read",usecols = ['title(string)']),subtitle_input=pd.read_excel("./info.xlsx",sheet_name = "read",usecols=['subtitle(string)']))
elif incase_OK == "n" or incase_OK == "N":
    wait().to_wait()
    incase_OK_1 = input("Have you written info.xlsx?(y/n):")
    if incase_OK_1 == "y" or incase_OK_1 == "Y":
        make_PPT(style = pd.read_excel("./info.xlsx",sheet_name = "read",usecols = ['style(1 - 11)'], dtype = int),name = pd.read_excel("./info.xlsx",sheet_name = "read",usecols = ['PPT\'s name(string)']),title_input=pd.read_excel("./info.xlsx",sheet_name = "read",usecols = ['title(string)']),subtitle_input=pd.read_excel("./info.xlsx",sheet_name = "read",usecols=['subtitle(string)']))
    else:
        pass
else:
    print("Only y or n.")
    wait().to_wait()
    incase_OK_1 = input("Are you write info.xlsx OK? (y/n):")
    if incase_OK_1 == "y" or incase_OK_1 == "Y":
        make_PPT(style = pd.read_excel("./info.xlsx",sheet_name = "read",usecols = ['style(1 - 11)'],dtype = int),name = pd.read_excel("./info.xlsx",sheet_name = "read",usecols = ['PPT\'s name(string)']),title_input=pd.read_excel("./info.xlsx",sheet_name = "read",usecols = ['title(string)']),subtitle_input=pd.read_excel("./info.xlsx",sheet_name = "read",usecols=['subtitle(string)']))
    else:
        pass
