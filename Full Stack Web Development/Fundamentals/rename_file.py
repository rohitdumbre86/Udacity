
import os

def rename_files():
 curr_direct = os.getcwd()
 os.chdir(r"C:\Users\rdumb\OneDrive\Desktop\alphabet\alphabet\myworld")
 file_list = os.listdir(r"C:\Users\rdumb\OneDrive\Desktop\alphabet\alphabet\myworld")
 for file_name in file_list:
     print "Changing old name" + file_name
     os.rename(file_name, file_name.translate(None,"0123456789"))
 os.chdir(curr_direct) 

rename_files()
