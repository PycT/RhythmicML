from rhythmic.general import faultReturnHandler;
from zipfile import ZipFile, ZIP_DEFLATED;

@faultReturnHandler
def packFiles(folder_path, archive_absolute_path, files_list_dictionary):
    """
    packFiles(folder_path, archive_absolute_path, files_list_dictionary)

    folder_path - a folder scanned with folder_scan.scanModelFolder to get files_list;
    files_list_dictionary - dictionaries, containing "file_path" items: {"file-path": path [,... ]}
    (see helpers/folder_scan.py)
    """
    relative_index = len(folder_path) + 1;

    with ZipFile(archive_absolute_path, mode = 'w', compression = ZIP_DEFLATED) as version_zip:

        for item_path in files_list_dictionary:
            item = files_list_dictionary[item_path];
            version_zip.write(item["absolute_path"], item["absolute_path"][relative_index:]);

    return "[ {} ] packed to [ {} ]".format(folder_path, archive_absolute_path);