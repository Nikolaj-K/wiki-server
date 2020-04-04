HOW_TO_USE_FROM_COMMAND_LINE_MESSAGE = """
Wrong usage! Proper usage looks like so:
    python finder.py --find myword[--open myindex] [--base myfolder]
e.g.,
    python finder.py --find foobar
"""

import os
import subprocess

import server_config as config
import server_utils as utils


class WordFinder:
    """
    docs
    """

    def run(self, search_words, index_to_open=-1, base_directory=config.ROOT):
        """
        docs
        """

        self._search_words = search_words
        self._index_to_open = index_to_open
        self._counter = 0
        self._num_files = 0
        self._num_lines = 0

        utils.log("yellow", "\n" + 80 * "#" + "\n") # start run

        all_search_results = []
        for rootpath, dirnames, filenames in os.walk(base_directory):
            for filename in filenames:
                if any(list(map(filename.endswith, config.WORD_FINDER_IGNORE_EXTENSIONS))):
                    utils.log("red", "Skipping {}".format(filename))
                else:
                    all_search_results += self.__scan_for_file(rootpath, filename)

        EXIT_MSG_SCHEME = "Searched {} files and {} lines. Instances of the words in {}: {}<br>Home is at {}"
        path_scheme_to_home = "localhost/" +  config.FILEPATH_HTML_HOME.split("/")[-1].split(".")[0] + "/" # hacky
        exist_msg = EXIT_MSG_SCHEME.format(self._num_files, self._num_lines, self._search_words, self._counter, path_scheme_to_home)
        all_search_results += ['<font color={color_meta}>{exist_msg}</font>'.format(exist_msg=exist_msg, color_meta=config.COLORS["grey_blue"])]
        utils.log("yellow", exist_msg)

        return all_search_results


    def __scan_for_file(self, rootpath, filename):
        """
        docs
        """

        self._num_files += 1

        search_results = []

        filepath = os.path.join(rootpath, filename)

        with open(filepath, "r") as in_file:
            try:
                for idx_line, line in enumerate(in_file):
                    self._num_lines += 1
                    for word in self._search_words:
                        if word in line:
                            if "trash" not in filepath:
                                try:
                                    # Hacky! fix
                                    GOTO_LINK_ELEMENT_SCHEME = '<a href="http://127.0.0.1:8080/{filename}/"><font color={color}><u>goto</u></font></a>'
                                    REFERENCE_SCHEME = '<font color={color_meta}>#{counter}:</font> {link_element} <a style="background-color:{color_background};"><font color={color_text}>{filepath}</font></a> <font color={color_text}> line {idx_line}</font>'
                                    FOUND_LINE_SCHEME = '<font color={color}>{line}</font><br>'
                                    link_element = GOTO_LINK_ELEMENT_SCHEME.format(
                                        filename=filename.split(".")[0],
                                        color=config.COLORS["red"],
                                    )
                                    reference = REFERENCE_SCHEME.format(
                                        counter=self._counter,
                                        link_element=link_element,
                                        filepath=utils.filepath_short(filepath),
                                        color_meta=config.COLORS["grey_blue"],
                                        color_text=config.COLORS["grey_blue"],
                                        color_background=config.COLORS["light_blue_darker"],
                                        idx_line=idx_line,
                                    )
                                    found_line = FOUND_LINE_SCHEME.format(
                                        line=line.replace("\n", ""),
                                        color="#809f38",
                                    )
                                    utils.log("cyan", reference)
                                    utils.log("grey", found_line)

                                    search_results += [reference, found_line]

                                except Exception as e:
                                    search_results += [e]

                                if self._index_to_open==self._counter:
                                    utils.log("green" , "Opening file {}".format(filepath))

                                    subprocess.run(["open", filepath])
                                self._counter += 1
                            else:
                                trash_message = "Path contains 'trash'. Skipping file:\t{}.\n".format(utils.filepath_short(filepath))
                                search_results += ['<font color="red">#{}:</font>'.format(trash_message)]
                                utils.log("red" , trash_message)

            except UnicodeDecodeError as _e:
                error_msg = "UnicodeDecodeError. Skipping file:\t<{}>\n".format(filepath)
                utils.log("red", error_msg)

        #utils.log("blue", search_results)

        return search_results


if __name__=="__main__":
    """
    docs
    """

    import argparse

    parser = argparse.ArgumentParser(description='Find words and open docs.')
    parser.add_argument('--find', type=str)
    parser.add_argument('--base', type=str, default=config.DEFAULT_BASE_DIRECTORY)
    parser.add_argument('--open', type=int, default=-1)

    args = parser.parse_args()

    if args.find:
        WordFinder().run([args.find], args.open, args.base)
    else:
        utils.log("red", HOW_TO_USE_FROM_COMMAND_LINE_MESSAGE)
