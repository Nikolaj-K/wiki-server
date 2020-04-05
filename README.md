Authored by Nikolaj Kuntner
Created on 4. April 2020

Hello.
This is the README and also the main page of the wiki.
Be sure to set `ROOT_PAGES` in `server_config.py` and all the other configs.
Search for expressions in all `ROOT_PAGES` files in the search bar, e.g., by writing `map` and hitting enter.
Expressions with an `.` in it are interpreted as files to open, e.g., `presheaf.txt`.

Run via `python main.py`. Then go to `http://127.0.0.1:8080/`.
Tested on the latest MacOS. On Windows, I think some paths and file-extension handlings must be normalized for the page loading.
Requirements are only `flask` and and the `termcolor` library, but you can comment out the last one. Here's python3 from [anaconda](
https://www.anaconda.com/distribution/#download-section) and with that you go `conda install -c anaconda flask`.

The flask is used in a very minimalist way, so there's lots of room for introducing best practices.
The python plugging of the html scheme is also very hacky right now.
I also have some ideas, so ask if interested.
So I'm quite happy for PR's or hints and also feature ideas!

![readme_page](https://i.imgur.com/Yuf2NqP.png)
![a_search_page](https://i.imgur.com/KvuaHdj.png)
![a_content_page](https://i.imgur.com/33AyhnB.png)

For professional alternatives, I've previously use [dokuwiki](https://www.dokuwiki.org/dokuwiki) (PHP Apache server) and I like it, but it's a lot more bulky of course.
