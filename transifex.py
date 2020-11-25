"""
transifex.py - Tool to manage Transifex translations

    u, up, update <DIR>  Download all translations from Transifex
    l, list              List all translations available on Transifex
"""
import os
import sys

import requests

API_URL = "https://www.transifex.com/api/2"
API_KEY = os.getenv("TRANSIFEX_API_KEY")
PROJECT_SLUG = "flex-pelican"
RESOURCE_SLUG = "messagespot"


def get_languages():
    url = "{api_url}/project/{project_slug}/languages/".format(
        **{"api_url": API_URL, "project_slug": PROJECT_SLUG,}
    )

    req = requests.get(url, auth=("api", API_KEY))
    req.raise_for_status()
    languages = req.json()

    return sorted([lang["language_code"] for lang in languages])


def list_languages():
    languages = get_languages()

    print("LANG   LOCAL")

    for lang in languages:
        filename1 = os.path.join(".", lang, "LC_MESSAGES", "messages.po")
        filename2 = os.path.join(
            ".", "translations", lang, "LC_MESSAGES", "messages.po"
        )

        if os.path.exists(filename1) or os.path.exists(filename2):
            print("{0}   YES".format(lang.ljust(5)))
        else:
            print("{0}   NO".format(lang.ljust(5)))

    print("\nTotal: {}".format(len(languages)))


def download(path):
    languages = get_languages()

    for lang in languages:
        print("Downloading {}...".format(lang))

        url = "{api_url}/project/{project_slug}/resource/{resource_slug}/translation/{lang_code}/".format(
            **{
                "api_url": API_URL,
                "project_slug": PROJECT_SLUG,
                "resource_slug": RESOURCE_SLUG,
                "lang_code": lang,
            }
        )

        req = requests.get(url, auth=("api", API_KEY))
        req.raise_for_status()
        data = req.json()
        po_content = data["content"]

        filepath = os.path.join(path, lang, "LC_MESSAGES")
        os.makedirs(filepath, exist_ok=True)

        filename = os.path.join(path, lang, "LC_MESSAGES", "messages.po")

        with open(filename, "w") as f:
            f.write(po_content)

        print("{} updated".format(lang))


def usage():
    print(__doc__[1:])


def _pop(l, default=None):
    try:
        return l.pop(0)
    except IndexError:
        return default


def run():
    args = sys.argv[1:]

    cmd = _pop(args, "help")

    if cmd in ["u", "up", "update"]:
        path = _pop(args)

        if path and not args:
            download(path)
        else:
            usage()
    elif cmd in ["l", "list"]:
        if not args:
            list_languages()
        else:
            usage()
    else:
        usage()


if __name__ == "__main__":
    run()
