def is_notebook():
    """
    Detect if the code is running in a Jupyter Notebook.
    """
    try:
        shell = get_ipython().__class__.__name__
        return shell == "ZMQInteractiveShell"
    except NameError:
        return False
