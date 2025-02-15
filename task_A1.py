import os

if os.system("uv --version") != 0:
    print("Installing uv...")
    os.system("pip install uv")

os.system("curl -O https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py")
os.system(r"C:\Users\kastu\anaconda3\python datagen.py 23f3003300@ds.study.iitm.ac.in")

