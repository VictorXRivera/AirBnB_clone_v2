#!/usr/bin/python3
"""
Python script that generates a .tgz archive from the contents of 
the web_static folder of my AirBnB Clone repo, 
using the function do_pack
"""


def do_pack():
    """
    ---------------
    Method: do_pack
    ---------------
    do_pack will generate a .tgz archive from the
    contents of the web_static folder.

    Requirements:
    - All files in the folder web_static must be added to the final archive
    - All archives must be stored in the folder versions
    (the function should create this folder if it doesnt exist)
    - The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz
    -The function do_pack must return the archive
     path if the archive has been correctly generated. 
    Otherwise, it should return None
    """
    from fabric.api import local
    from datetime import datetime as time

    file = "web_static_" + time.now().strftime("%Y%m%d%H%M%S") + ".tgz"

    local('mkdir -p versions')

    try:
        local('tar -cvzf versions/{} web_static/'.format(file))
        path = "versions/" + file
        return path
    except Exception:
        return None
