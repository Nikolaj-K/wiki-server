from flask import Flask, request
import os

import server_config as config
import server_utils as utils


app = Flask(__name__)


@app.route('/')
@app.route('/<string:filename>/')
@app.route('/<string:filename>/<string:action>/')
def make_page(filename=None, action=None):
    """
    docs
    """

    utils.log("yellow", "make_page {}".format(filename))

    filepath = utils.find_filepath(filename)
    if not filepath:
        utils.log("red", "Returning default file. Could not find <{}>.".format(filename))
        filepath = config.FILEPATH_HTML_HOME
        filename = filepath.split(".")[-1].split(".")[0]
    utils.log("yellow", "Returning <{}>".format(utils.filepath_short(filepath)))

    utils.run_action_command(action, filepath)

    page = open(config.FILEPATH_HTML_SCHEME).read().format(
        filepath=utils.filepath_short(filepath),
        filename=filename,
        file_content=utils.get_file_content(filepath)
    )

    open(config.FILEPATH_HTML_DEBUG, 'w').write(page) # Creates the page being used - this is merely for debug purposes

    return page


@app.route('/', methods=['POST'])
@app.route('/<string:filename>/', methods=['POST'])
@app.route('/<string:filename>/<string:action>/', methods=['POST'])
def goto_post(filename=None, action=None):
    """
    docs
    """

    textbox_content = request.form['textbox_content']

    if utils.interpret_as_filename(textbox_content):
        filename = textbox_content
    else:
        utils.write_search_results_file(textbox_content)
        filename = config.FILEPATH_SEARCH_RESULTS.split("/")[-1]
    just_filename = filename.split(".")[0] # "foo.bar" => "foo"

    return make_page(just_filename, None)


if __name__ == '__main__':
    """
    docs
    """

    utils.log("green", "Starting server.")

    app.run(host=config.HOST, port=config.PORT, debug=True)
