from pkg2 import File
from datetime import datetime,date



fs = File(r"C:\Users\Sai Charan\Desktop\Python\assignments")
print(fs.getMaxSizeFile(2))
print(fs.getLatestFiles(date(2025,4,16)))


#output


"""
 for fs.getMaxSizeFile(2):
['C:\\Users\\Sai Charan\\Desktop\\Python\\assignments\\day7\\day7question10.py', 'C:\\Users\\Sai Charan\\Desktop\\Python\\assignments\\day4\\__pycache__\\pkg2.cpython-312.pyc']

fs.getLatestFiles(date(2025,4,16):
['C:\\Users\\Sai Charan\\Desktop\\Python\\assignments\\day4\\question5.py', 'C:\\Users\\Sai Charan\\Desktop\\Python\\assignments\\day4\\question6.py', 'C:\\Users\\Sai Charan\\Desktop\\Python\\assignments\\day4\\__pycache__\\pkg1.cpython-312.pyc', 'C:\\Users\\Sai Charan\\Desktop\\Python\\assignments\\day4\\__pycache__\\pkg2.cpython-312.pyc']


"""