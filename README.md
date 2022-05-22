# synchronizer
### Description
Scheduled synchronization of two folders in one direction. Program gets pathes from user to source directory, destination directory, synchronizating interval (in seconds) and a path to a log file. Deleting files in destination folder if relevant files were deleted in source folder supported.
### Installation
dirsync and schedule libraries needed to be installed previously.
### Usage
From the comand line:
`python sync.py C:/Users/My_documents/source_dir destination_dir 60 C:/my_log_file.log`
