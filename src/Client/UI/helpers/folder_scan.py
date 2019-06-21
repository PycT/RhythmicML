from os import scandir as scanDir, access, W_OK;
from os.path import abspath as absolutePath, isdir as isDir, expanduser as expandUser;
from rhythmic.general import faultReturnHandler;

@faultReturnHandler
def scanFolder(folder_to_scan = "~"):
    """
     scanFolder(folder_to_scan)

     Shows all the items in the folder the user has permission to write to.
     That includes '..' entry too.
    """

    if folder_to_scan == "~":
        the_folder = expandUser("~");
    else:
        the_folder = folder_to_scan;

    absolute_path = absolutePath(the_folder);

    folder_contents = [];

    level_above = absolute_path[0:absolute_path.rfind("/")];

    if ( (isDir(level_above)) and (access(level_above, W_OK)) ):
        folder_contents.append(
            {
                "absolute_path": level_above,
                "base_name": "< .. >",
                "is_dir": True
            }
        );

    the_folder_scan = scanDir(absolute_path);

    for item in the_folder_scan:
        if access(item.path, W_OK):
            folder_contents.append(
                {
                    "absolute_path": item.path,
                    "base_name": item.name,
                    "is_dir": item.is_dir()
                }
            );

    return folder_contents;