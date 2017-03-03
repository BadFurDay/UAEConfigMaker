import os


def check_inputdirs(inputdirs):
    """Check the Directories to scan are valid on this system.

    Args:
        inputdirs (list): list of directories to scan.
    Returns:
        list of directories.
    Raises:
        ValueError: if a directory is not valid.

    """
    for i, directory in enumerate(inputdirs):

        # Format Directory string for this OS
        directory = os.path.abspath(directory)

        # Check Directory is valid
        if not os.path.isdir(directory):
            raise ValueError('"{}" is not a valid directory on this system'.format(
                directory
            ))

        # Update Directory string in list with trailing "/" or "\" depending on OS
        inputdirs[i] = "{directory}{separator}".format(
            directory=directory,
            separator=os.sep
        )

    return inputdirs