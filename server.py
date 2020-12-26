from flask import Flask, request
import os

import server_config as config
import server_utils as utils
import server_pages_validator as validator


app = Flask(__name__)


@app.route('/')
@app.route('/<string:filename>/')
@app.route('/<string:filename>/<string:action>/')
def make_page(filename=None, action=None):
    """
    docs
    """

    filepath = utils.find_filepath(filename)
    if not filepath:
        utils.log("red", "Returning default file. Could not find <{}>.".format(filename))
        filepath = config.FILEPATH_HTML_HOME
        filename = filepath.split(".")[-1].split(".")[0]
    utils.log("yellow", "Returning {}. Make page".format(utils.filepath_short(filepath), filename))

    validator_success = validator.PagesValidator.run()
    #if validator_success:
    pages_validator_message = "Pages validator run() command is not implemented yet.<br>"

    fps = utils.all_filepaths()

    def filter_work(fp):
        ACCEPT = ["pred_working_on", "todo_"]
        return any([w in fp for w in ACCEPT]) and not fp.endswith(".DS_Store")
    def filter_sim(fp):
        ACCEPT = ["sim/"]
        return any([w in fp for w in ACCEPT]) and not fp.endswith(".DS_Store")
    def filter_pred(fp):
        ACCEPT = ["pred/"]
        return any([w in fp for w in ACCEPT]) and not fp.endswith(".DS_Store")
    def filter_guide(fp):
        ACCEPT = ["guide_"]
        return any([w in fp for w in ACCEPT])
    def tmp_guide(fp):
        ACCEPT = ["tmp_"]
        return any([w in fp for w in ACCEPT])
    def filter_video(fp):
        ACCEPT = ["pages_video"]
        REJECT = [".pyc"]
        return any([w in fp for w in ACCEPT]) and not any([w in fp for w in REJECT])

    sim_entries : list = [utils.goto_list_entry(counter, fp)
        for counter, fp in fps.items() if filter_sim(fp)]
    work_entries : list = [utils.goto_list_entry(counter, fp)
        for counter, fp in fps.items() if filter_work(fp)]
    pred_entries : list = [utils.goto_list_entry(counter, fp)
        for counter, fp in fps.items() if filter_pred(fp)]
    pred_entries : list = [utils.goto_list_entry(counter, fp)
        for counter, fp in fps.items() if filter_pred(fp)]
    tmp_entries : list = [utils.goto_list_entry(counter, fp)
        for counter, fp in fps.items() if tmp_guide(fp)]
    video_entries : list = [utils.goto_list_entry(counter, fp)
        for counter, fp in fps.items() if filter_video(fp) and not filter_guide(fp)]
    guide_entries : list = [utils.goto_list_entry(counter, fp)
        for counter, fp in fps.items() if filter_guide(fp) and not filter_video(fp)]

    all_goto_entries : list = [utils.goto_list_entry(counter, fp) for counter, fp in fps.items()]

    work_entries_string : str = "<br><b>working-on and todo:</b><br>" + "<br>".join(work_entries)
    sim_entries_string : str = "<br><b>simulations:</b><br>" + "<br>".join(sim_entries)
    pred_entries_string : str = "<br><b>pred:</b><br>" + "<br>".join(pred_entries)
    guide_entries_string : str = "<br><b>guide:</b><br>" + "<br>".join(guide_entries)
    tmp_entries_string : str = "<br><b>tmp:</b><br>" + "<br>".join(tmp_entries)
    video_entries_string : str = "<br><b>video pages:</b><br>" + "<br>".join(video_entries)
    all_goto_entries_string : str = "<br><b>All pages:</b><br>" + "<br>".join(all_goto_entries)

    file_content = utils.get_file_content(filepath) + utils.HTML_BAR + utils.HTML_BAR + \
        pages_validator_message + \
        work_entries_string + guide_entries_string + sim_entries_string + \
        pred_entries_string + tmp_entries_string + video_entries_string + \
        all_goto_entries_string

    utils.run_action_command(action, filepath)

    with open(config.FILEPATH_HTML_SCHEME) as html_page_scheme_file:
        html_page_scheme = html_page_scheme_file.read()
        html_page = html_page_scheme.format(
            filepath=utils.filepath_short(filepath),
            filename=filename,
            file_content=file_content,
        )

    with open(config.FILEPATH_HTML_DEBUG, 'w') as html_page_debug_file:
        html_page_debug_file.write(html_page) # merely for debug purposes

    return html_page


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
