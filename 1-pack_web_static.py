#!/usr/bin/python3
"""Python script that generates a .tgz archive"""


def do_pack():
    """do_pack function"""
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
