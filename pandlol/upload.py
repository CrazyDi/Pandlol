import os
import sys
sys.path.insert(1, os.getcwd())


from pandlol.upload.version import Version


if __name__ == "__main__":
    print(os.getcwd())
    Version.upload()