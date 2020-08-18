#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of 
the web_static folder of your AirBnB Clone repo, using the function do_pack"""


def do_pack():
    """
    
    The function do_pack must return the archive path 
    if the archive has been correctly generated. 
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
