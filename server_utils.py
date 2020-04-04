import os
import re
import subprocess
from termcolor import colored

import server_config as config
from finder import WordFinder


def log(color, message_string):
    """
    docs
    """

    colored_msg = colored(message_string, color)
    print(colored_msg)


def run_action_command(action, filepath):
    """
    docs
    """

    if action=='open':
        subprocess.run([config.FILE_EDITOR_COMMAND, filepath]) # alternatively 'open' instead of 'atom'
    if action=='new':
        subprocess.run([config.FILE_EDITOR_COMMAND]) # ['atom', '-e']


def find_filepath(filename):
    """
    Try to find filepath of the files 'filename'. If not successful, return the empty string.
    """

    log("yellow", "Trying to find {}.".format(filename))

    for root, _dirs, files in os.walk(config.ROOT):
        for file in files:
            for file_extension in config.SEARCH_FILEPATH_LEGAL_EXTENSIONS:
                filepath_ending = '{}.{}'.format(filename, file_extension)
                if file.endswith(filepath_ending):
                    filepath = os.path.join(root, file)
                    return filepath
    return str()


def get_file_content(filepath):
    """
    docs
    """

    content = open(filepath).read()

    content = content.replace('\n', '<br>')
    content = content.replace('\t', 8 * '&nbsp;')
    content = content.replace('----', '<hr style="border:solid .5px black;">')
    content = re.sub(r'\$(.*?)\$', r'&nbsp;\(\1\)', content) # &nbsp; is an invisible character
    for j in range(80, 3, -1):
        content = content.replace(j * ' ', 2 * j * '&nbsp;')
    for j in [3, 4, 5]:
        src = r'{k}(.*?){k}'.format(k=(8-j)*"=")
        trg = r'<h{j}>\1</h{j}>'.format(j=j)
        content = re.sub(src, trg, content)

    return content


def write_search_results_file(textbox_content):
    """
    docs
    """

    with open(config.FILEPATH_SEARCH_RESULTS, "w") as out_file:
        log("yellow", "Creating file as <{}>.".format(config.FILEPATH_SEARCH_RESULTS))

        res = WordFinder().run([textbox_content], base_directory=config.ROOT)
        res_str = "\n".join(res) if res else "No file found containing '{}'".format(res)
        out_file.write(res_str)


def interpret_as_filename(textbox_content):
    """
    docs
    """

    FILE_TAG = "."
    return FILE_TAG in textbox_content


def filepath_short(filepath):
    """
    docs
    """

    LENGTH = 2

    lst = filepath.split("/")
    if len(lst) < LENGTH:
        filepath_short = filepath
    else:
        last_three = filepath.split("/")[-LENGTH:]
        filepath_short = "/" + "/".join(last_three)

    return filepath_short
