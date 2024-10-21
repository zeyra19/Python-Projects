import os
# import sys
path = "C:\\Users\\zeyrabilgecartcurt\\Desktop\\zeyra_workspace\\dojo\\folders"
# sys.setrecursionlimit(2) Belirli bir sayıda çağırır

def scan_folder(folder_path):
    result = {}
    # is_error = False
    for entry in os.scandir(folder_path):
        if entry.is_dir():
            size = os.path.getsize(entry.path)
            name = entry.name
            child_folders = scan_folder(entry.path)
            result[name] = {"size": size, "child_folders": child_folders}
    return result

print(scan_folder(folder_path=path))