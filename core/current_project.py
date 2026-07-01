CURRENT_PROJECT = None


def set_project(project):

    global CURRENT_PROJECT

    CURRENT_PROJECT = project


def get_project():

    return CURRENT_PROJECT


def clear_project():

    global CURRENT_PROJECT

    CURRENT_PROJECT = None