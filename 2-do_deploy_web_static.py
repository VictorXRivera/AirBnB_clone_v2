#!/usr/bin/python3
"""Fabric script using the function do_deploy"""
from fabric.api import env, run, put
web01, web02 = '34.75.43.80', '34.73.48.81'
env.hosts = [web01, web02]


def do_deploy(archive_path):
    """do_deploy function"""
    from os.path import isfile

    # First, check if file exists
    if not isfile(archive_path):
        return False

    try:
        # Try extracting file name from var 'archive_path'
        archive = archive_path.split('/')[-1]

        # Upload, uncompress and delete the archive from the web servers
        put(archive_path, '/tmp/')
        out = '/data/web_static/releases/{}/'.format(archive.split('.')[0])
        run('mkdir -p {}'.format(out))
        run('tar -xzf /tmp/{} -C {}'.format(archive, out))
        run('rm -rf /tmp/{}'.format(archive))
        run('mv {}* {}'.format(out + 'web_static/', out))
        run('rm -rf {}'.format(out + 'web_static/'))

        # Delete symlink 'current' and link extracted folder to current
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(out))

        # On success, return True
        print('New version deployed!')
        return True

    except:
        return False
