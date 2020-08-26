import os
import sys
sys.path.insert(1, os.getcwd())


from pandlol.upload.version import VersionUploader


if __name__ == "__main__":
    # Если последняя версия не загружена
    print(VersionUploader.check_version())
    if not VersionUploader.check_version():
        # pass
        VersionUploader.upload()
