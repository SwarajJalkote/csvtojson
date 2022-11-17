import os, sys

PROJECT_PATH = os.getcwd()
PROJECT_PATH = PROJECT_PATH.split('\\')
PROJECT_PATH = "\\".join(i for i in PROJECT_PATH[0:-1])
SOURCE_PATH = os.path.join(PROJECT_PATH, "src")


sys.path.append(SOURCE_PATH)