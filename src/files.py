"""
File handling type functions.
TODO Put into class
"""
import os
import shutil
import zipfile
import re
from datetime import datetime


class Files(object):

    def __init__(self, folder_directory=None, file_name=None):

        self.file_name = file_name
        self.folder_directory = folder_directory

        try:
            self.full_path = os.path.join(folder_directory, file_name)
        except TypeError:
            print("File name not specified.")

    def arrange_files(self, misc_folder_name="others"):
        """
        Arrange files accordingly to their extension type

        Parameters
        ----------
            Folder to arrange files.
        misc_folder_name : str
            Folder to store anything else without file extension, creates default "others" folder.

        """

        try:
            os.makedirs(os.path.join(self.folder_directory, misc_folder_name))
        except FileExistsError:
            raise FileExistsError(f"Folder {misc_folder_name} already exists, please specify different folder name for "
                                  f"misc files.")

        lst_files = os.listdir(self.folder_directory)
        lst_file_end = [x[-4:] for x in lst_files]
        lst_file_ext = [y for y in lst_file_end if re.search("^[.]", y)]

        for ext in lst_file_ext:
            if ext[1:].isalpha() is True:
                print(f"{ext} is an extension")
            else:
                lst_file_ext.remove(ext)
                print(f"{ext} is not an extension")

        # drop duplicates
        lst_file_ext = list(set(lst_file_ext))

        for folder in lst_file_ext:
            try:
                os.makedirs(os.path.join(self.folder_directory, folder))
            except FileExistsError:
                print(f"Extension {folder} already exists.")

        for file in lst_files:
            for file_ext in lst_file_ext:
                if file[-4:] == file_ext:
                    shutil.move(os.path.join(self.folder_directory, file), os.path.join(self.folder_directory, file_ext))

        lst_all_files = os.listdir(self.folder_directory)

        lst_misc_files = [x for x in lst_all_files if x not in lst_file_ext]

        for misc_file in lst_misc_files:
            shutil.move(os.path.join(self.folder_directory, misc_file), os.path.join(self.folder_directory, "others"))

    def list_file_exts(self, ext):
        """Returns a list of files of specified extension."""
        return [os.path.join(self.folder_directory, x) for x in os.listdir(self.folder_directory) if x.endswith(ext)]

    def read_zip(self, zip_file, file_name):
        """
        Opens contents of zip file without extraction, can be read using pandas if dataframe like.
        """
        zip_extraction = zipfile.ZipFile(zip_file, 'r')
        file = zip_extraction.open(file_name)
        return file

    # TODO add folder
    def check_file_exists(self, files):

        if isinstance(files, list):
            # Testing all directories
            for file in files:
                assert os.path.exists(file), f"{file} not found"

        else:
            assert os.path.exists(files), f"{files} not found"

    def check_last_modified(self, files):
        for s in files:
            print(f"{s} last modified at {datetime.utcfromtimestamp(int(os.path.getmtime(s))).strftime('%Y%m%d, %H:%S.')}")

    # TODO incorporate move files
    def copy_file(self, src, des, src_name=None, des_name=None):
        """
        Basic copy function

        Parameters
        ----------
        src : str
            Source to file to copy
        des : str
            Destination to copy file to
        src_name : str
            Specify file name if needed (for loop runs)
        des_name : str
            New file name
        """
        if src_name is not None:
            src = os.path.join(src, src_name)

        if des_name is not None:
            des = os.path.join(des, des_name)

        shutil.copy(src, des)


if __name__ == '__main__':
    Files(folder_directory="C:/Users/Dencan Gan/Downloads").arrange_files(misc_folder_name="new_others")