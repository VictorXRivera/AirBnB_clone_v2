#!/usr/bin/python3
"""
Python script that generates a .tgz archive from the contents of 
the web_static folder of my AirBnB Clone repo, 
using the function do_pack
"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """    
    The function do_pack must return the archive path 
    if the archive has been correctly generated. 
    Otherwise, it should return None
    """
    file = "web_static_" + time.now().strftime("%Y%m%d%H%M%S") + ".tgz"

    local('mkdir -p versions')

    try:
        local('tar -cvzf versions/{} web_static/'.format(file))
        path = "versions/" + file
        return path
    except Exception:
        return None
