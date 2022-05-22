# synchronizer
### Description
This script performs scheduled synchronization of two folders: from source to destination. Program gets pathes from the user to a source directory, destination directory, synchronization interval (in seconds) and a path to a log file. It deletes files in the destination folder if the corresponding files were removed in the source folder.
### Installation
```powershell
pip install dirsync
pip install schedule
```
### Usage
```powershell
python sync.py C:/Users/My_documents/source_dir destination_dir 60 C:/my_log_file.log
```
