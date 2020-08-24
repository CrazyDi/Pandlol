import os
import sys
sys.path.insert(1, os.getcwd())


from pandlol.upload.version import Version


if __name__ == "__main__":
    # Если последняя версия не загружена
    if not Version.check_version():
        pass
        # Version.upload()
