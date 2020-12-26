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

        utils.log("yellow", "\n" + 80 * "#" + "\n") # start run

        self._search_words = search_words
        self._index_to_open = index_to_open
        self._counter = 0
        self._num_files = 0
        self._num_lines = 0

        all_search_results = []
        for rootpath, dirnames, filenames in os.walk(base_directory): # TODO: Don't call os.walk in so many different functions
            skip_dir = any([dirname in rootpath for dirname in config.WORD_FINDER_IGNORE_DIRS])
            if skip_dir:
                pass
                #utils.log("red", "[WordFinder.run] Skipping rootpath {}".format(rootpath))
            else:
                for filename in filenames:
                    skip_file = any(list(map(filename.endswith, config.WORD_FINDER_IGNORE_EXTENSIONS)))
                    if skip_file:
                        pass
                        #utils.log("red", "[WordFinder.run] Skipping filename {}".format(filename))
                    else:
                        all_search_results += self.__scan_for_file(rootpath, filename)

        SEARCH_SUMMARY_ELEMENT_SCHEME = '<font color={}>Searched {} files and {} lines. Instances of the words in {}: {}</font><br>'
        search_summary_element = SEARCH_SUMMARY_ELEMENT_SCHEME.format(
            config.COLORS["grey_blue"],
            self._num_files,
            self._num_lines,
            self._search_words,
            self._counter,
        )
        utils.log("yellow", search_summary_element)

        return [search_summary_element] + all_search_results


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
                                    search_result = [
                                        '{goto_list_entry} <font color={color_text}>line {idx_line}</font>'.format(
                                            goto_list_entry=utils.goto_list_entry(self._counter, filepath),
                                            color_text=config.COLORS["grey_blue"],
                                            idx_line=idx_line,
                                        ),
                                        '<font color={color}>{line}</font><br>'.format(
                                            line=line.replace("\n", ""),
                                            color="#809f38",
                                        ),
                                    ]
                                    for idx, color in enumerate(["cyan", "grey"]):
                                        utils.log(color, search_result[idx])

                                    search_results += search_result
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
        #print("^ search_results")

        return search_results


if __name__=="__main__":
    """
    docs
    """

    import argparse

    parser = argparse.ArgumentParser(description='Find words and open docs.')
    parser.add_argument('--find', type=str)
    parser.add_argument('--base', type=str, default=None)
    parser.add_argument('--open', type=int, default=-1)

    args = parser.parse_args()

    if args.find:
        WordFinder().run([args.find], args.open, args.base)
    else:
        utils.log("red", HOW_TO_USE_FROM_COMMAND_LINE_MESSAGE)
