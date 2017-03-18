#!/usr/bin/env bash

function extract_pot() {
    pybabel extract -s --no-wrap --project="Flex" --copyright-holder="Alexandre Vicenzi" --version="2.1.0" --mapping translations/babel.cfg --output translations/messages.pot ./
}

function new_translation() {
    pybabel init --no-wrap --input-file translations/messages.pot --output-dir translations/ --locale $1 --domain messages
}

function update_translation() {
    pybabel update --no-wrap --input-file translations/messages.pot --output-dir translations/ --domain messages
}

function compile_translations() {
    pybabel compile -f --directory translations/ --domain messages
}

function can_run() {
    if ! [ -x "$(command -v pybabel)" ]; then
        echo "Missing translation tool. Please, install Flask-Babel to continue."
        echo ""
        echo "    pip install Flask-Babel"
        echo ""
        exit 1
    fi
}

function usage {
    echo "Translate Flex theme tool"
    echo ""
    echo "Usage:"
    echo ""
    echo "    new [language]  create new translation."
    echo "    compile         compile all PO files into MO files."
    echo "    update          update all translations based on POT file."
    echo "    extract         extract all messages from templates and create the POT file."
}

case "$1" in
   "new")
        can_run

        if [ -z "$2" ]
        then
            echo "Error: missing translation code."
            echo ""
            usage
            exit 1
        else
            new_translation $2
        fi
      ;;
   "compile")
      can_run
      compile_translations
      ;;
   "update")
      can_run
      update_translation
      ;;
   "extract")
      can_run
      extract_pot
      ;;
   *)
    usage
    exit 1
    ;;
esac
