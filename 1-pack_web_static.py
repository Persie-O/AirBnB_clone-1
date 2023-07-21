#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from fabric.api import local
from datetime import datetime

def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder."""

    # Get the current date and time
    now = datetime.now()
    formatted_date = now.strftime("%Y%m%d%H%M%S")

    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Name of the archive
    archive_name = "web_static_" + formatted_date + ".tgz"

    # Compress web_static folder into the archive
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    # Check if the archive was created successfully
    if result.succeeded:
        return "versions/" + archive_name
    else:
        return None

