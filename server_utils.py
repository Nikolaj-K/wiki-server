import os
import re
import subprocess
from termcolor import colored

import server_config as config
from server_finder import WordFinder


HTML_BAR = '<hr style="border:solid .5px black;">'


def get_file_content(filepath):
    """
    docs
    """

    content = open(filepath).read()

    content = content.replace('\n', '<br>')
    content = content.replace('\t', 8 * '&nbsp;')
    content = content.replace('----', HTML_BAR)
    content = re.sub(r'\$(.*?)\$', r'&nbsp;\(\1\)', content) # &nbsp; is an invisible character

    """
    src = r'\[\[(.*?)\|(.*?)\]\]' # Wikipedia type EXTERNAL link
    url = r'\1' # this means the name must be exact
    trg = make_href_element(url, r'(ext) \2') # (ext )\1 is the regex group 1
    content = re.sub(src, trg, content)
    """

    src = r'\[\[(.*?)\]\]' # Wikipedia type INTERNAL link
    url = make_internal_url(r'\1')
    trg = make_href_element(url, r' \1') # (int) \1 is the regex group 1
    content = re.sub(src, trg, content)

    for j in range(80, 3, -1):
        content = content.replace(j * ' ', 2 * j * '&nbsp;')
    for j in [3, 4, 5]:
        src = r'{k}(.*?){k}'.format(k=(8-j)*"=")
        trg = r'<h{j}>\1</h{j}>'.format(j=j)
        content = re.sub(src, trg, content)

    return content


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


def all_filepaths():
    counter = 0
    filepaths = dict()
    for root, _dirs, files in os.walk(config.ROOT): # TODO: Don't call os.walk in so many different functions
        skip_dir = any([dirname in root for dirname in config.WORD_FINDER_IGNORE_DIRS])
        if skip_dir:
            log("red", "[all_filepaths] Skipping rootpath {}".format(root))
        else:
            for file in files:
                filepaths[counter] = os.path.join(root, file)
                counter += 1
    return filepaths


def find_filepath(filename):
    """
    Try to find filepath of the file(s) ending in 'filename'.
    If there's more than one, take the one with the shortest filename.
    If not successful, return the empty string.
    """

    log("yellow", "Trying to find: {}".format(filename))

    filepath_matches = []
    for root, _dirs, files in os.walk(config.ROOT): # TODO: Don't call os.walk in so many different functions
        for file in files:
            for file_extension in config.SEARCH_FILEPATH_LEGAL_EXTENSIONS:
                filepath_ending = '{}.{}'.format(filename, file_extension)
                if file.endswith(filepath_ending):
                    filepath = os.path.join(root, file)
                    filepath_matches.append(filepath)

    log("yellow", "Matches:\n{}".format(filepath_matches))

    if filepath_matches:
        def len_of_filename(filepath):
            filename = filepath.split("/")[-1]
            return len(filename)
        return min(filepath_matches, key=len_of_filename)
    else:
        return str()


def write_search_results_file(textbox_content):
    """
    docs
    """

    with open(config.FILEPATH_SEARCH_RESULTS, "w") as out_file:
        log("yellow", "Creating file as <{}>.".format(config.FILEPATH_SEARCH_RESULTS))

        res = WordFinder().run([textbox_content], base_directory=config.ROOT)
        log("red", res)
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

    LENGTH = 3

    lst = filepath.split("/")
    if len(lst) < LENGTH:
        filepath_short = filepath
    else:
        last_three = filepath.split("/")[-LENGTH:]
        filepath_short = "/" + "/".join(last_three)

    return filepath_short


def filename_from_filepath(filepath):
    return filepath.split("/")[-1].split(".")[0]


def make_internal_url(filename):
    return r'http://{host}:{port}/{filename}/'.format(host=config.HOST, port=config.PORT, filename=filename)


def make_href_element(url, link_description):
    link_text_element = r'<font color={goto_color}><u>goto</u></font>'.format(goto_color=config.COLORS["red"])
    href_element = r'<a href="{url}">{link_text_element}</a>'.format(url=url, link_text_element=link_text_element)
    link_description_element = '<a style="background-color:{color_background};"><font color={color_text}>{link_description}</font></a>'.format(
        color_background=config.COLORS["light_blue_darker"], color_text=config.COLORS["black"], link_description=link_description
    )
    return r'{} {}'.format(href_element, link_description_element)


def goto_list_entry(counter, filepath):
    counter_element = '<font color={color_meta}>#{counter}:</font>'.format(color_meta=config.COLORS["grey_blue"], counter=counter)
    filename = filename_from_filepath(filepath)
    url = make_internal_url(filename)
    href_element = make_href_element(url, filepath_short(filepath))
    return "{} {}".format(counter_element, href_element)
