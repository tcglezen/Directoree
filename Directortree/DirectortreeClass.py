#!/usr/bin/env python

# Internal class for easily managing classes.
import os
from typing import List


class Directortree:
    """Represents node within the tree. Represents a directory
    """

    def __init__(self,
                 dir_path=None,
                 path_width=2,
                 file_spacing=' ',
                 dir_signal='/*',
                 prefix='',
                 suffix='/*',
                 max_depth=99):
        """ Constructor for Directortree

        :param dir_path:
        :type dir_path:
        """
        # Populates tree given dir_path
        self.dir_path = dir_path
        if self.dir_path is None:
            self.dir_path = os.getcwd()

        # Obtain name of folder
        self.name = os.path.split(os.path.abspath(self.dir_path))[-1]

        # Configurations
        self.path_width = path_width
        self.file_spacing = file_spacing
        self.dir_signal = dir_signal

        # Other Information
        self.prefix = prefix
        self.suffix = suffix
        self.max_depth = max_depth

        # Init files and folders
        self.folders: List[Directortree] = []
        self.files: List[FileLeaf] = []

        # Populating Tree and creating subtree/files
        dir_contents = os.listdir(self.dir_path)
        # Populating folders and files
        for content in dir_contents:
            content_path = os.path.join(self.dir_path, content)

            if os.path.isdir(content_path):  # Dir
                new_directortree = Directortree(content_path,
                                                path_width,
                                                file_spacing,
                                                dir_signal,
                                                prefix+self.folder_prefix(),
                                                self.suffix,
                                                max_depth)
                self.folders.append(new_directortree)
            else:  # File
                new_fileleaf = FileLeaf(content,
                                        path_width,
                                        file_spacing,
                                        prefix+self.file_prefix())
                self.files.append(new_fileleaf)

            self.folders = sorted(self.folders)
            self.files = sorted(self.files)

    def display_tree(self):
        """Prints tree in string format"""
        print(self.get_str())

    def get_str(self):
        result = ''
        # Print string for folder
        result += self.prefix + '_' * self.path_width + self.file_spacing + self.name + self.suffix + '\n'

        # Find the string for each of the folders and files
        for folder in self.folders:
            result += folder.get_str()

        for file in self.files:
            result += file.get_str()

        return result

    def folder_prefix(self):
        """What the tree appends to the prefix for its children"""
        return ' ' * self.path_width + '|'

    def file_prefix(self):
        return ' ' * self.path_width + '|'

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return str(self) < str(other)


class Directoroot(Directortree):
    """Root of tree
    """

    def __init__(self,
                 dir_path=None,
                 path_width=2,
                 file_spacing=' ',
                 dir_signal='/*',
                 prefix='',
                 max_depth=99):
        super().__init__(dir_path=dir_path,
                         path_width=path_width,
                         file_spacing=file_spacing,
                         dir_signal=dir_signal,
                         prefix=prefix,
                         max_depth=max_depth, )


class FileLeaf:
    """Leaf of directory. Represents a file"""

    def __init__(self,
                 file_name: str,
                 path_width: int = 2,
                 file_spacing: str = ' ',
                 prefix=''):
        self.name = file_name
        self.path_width = path_width
        self.file_spacing = file_spacing
        self.prefix = prefix

    def get_str(self):
        return self.prefix + '_' * self.path_width + self.file_spacing + self.name + '\n'

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return str(self) < str(other)
