from os import scandir as scanDir, access, W_OK;
from os.path import abspath as absolutePath, isdir as isDir, expanduser as expandUser;
from rhythmic.general import faultReturnHandler;

@faultReturnHandler
def scanFolder(folder_to_scan = "~", show_started_with_dot = False):
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

    for item in sorted(the_folder_scan, key = lambda the_item: the_item.name):

        if item.name.startswith("."):
            inclusion = show_started_with_dot;
        else:
            inclusion = True;

        if ( inclusion and access(item.path, W_OK) ):
            folder_contents.append(
                {
                    "absolute_path": item.path,
                    "base_name": item.name,
                    "is_dir": item.is_dir()
                }
            );

    return folder_contents;