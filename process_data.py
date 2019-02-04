def extract_python_version(output_var):
    """Extracts python version.

    :param output_var: the value passed from ansible playbook
    :return: python version
    """
    return output_var.split(" ")[-1]
