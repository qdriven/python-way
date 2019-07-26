# -*- coding:utf-8 -*-
import json
import os

QV_NOTE_LOCATION = "/Users/patrick/Library/Containers/com.happenapps.Quiver/Data/Library/Application Support/Quiver/Quiver.qvlibrary"

FILTERED_QV_NB = [
    "Inbox.qvnotebook", "Trash.qvnotebook", "Tutorial.qvnotebook"
]

QV_FOLDER_SUFFIX = 'qvnotebook'
QV_NB_META = "meta.json"
QV_NB_CONTENT = "content.json"


def get_all_nv_nb_folders():
    # result = []
    # for item in os.listdir(QV_NOTE_LOCATION):
    #     if item not in FILTERED_QV_NB:
    #         result.append(item)
    # return result
    # list comprehensions
    return [item for item in os.listdir(QV_NOTE_LOCATION)
            if item not in FILTERED_QV_NB]


def get_qv_notes(notebook_folder):
    qv_notes = []
    with open(os.path.join(QV_NOTE_LOCATION, notebook_folder, QV_NB_META), "r") as meta:
        notebook_meta = json.load(meta)
    qv_notebook_name = notebook_meta.get("name", "NA")
    for note_folder in os.listdir(
            os.path.join(QV_NOTE_LOCATION, notebook_folder)):
        if os.path.isdir(os.path.join(QV_NOTE_LOCATION,
                                      notebook_folder,
                                      note_folder)):
            qv_notes.append(get_qv_note(notebook_folder, note_folder))
    return {"nb": qv_notebook_name, "notes": qv_notes}


def get_qv_note(notebook_folder, note_folder):

    result = {}
    with open(os.path.join(QV_NOTE_LOCATION,
                           notebook_folder,
                           note_folder, QV_NB_CONTENT), "r") as content:
        note_content = json.load(content)
    result['title'] = note_content.get("title")
    result['data'] = []
    for item in note_content.get("cells", []):
        if item.get("type", "NA") == "markdown":
            result['data'].append(item.get('data'))

    return result


if __name__ == '__main__':
    # todo: create directory and convert to md file in a git repo
    # then push them
    nbs = get_all_nv_nb_folders()
    for nb in nbs:
        print(get_qv_notes(nb))
