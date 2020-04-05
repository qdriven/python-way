# -*- coding:utf-8 -*-
import json
import subprocess
import sys

"""
Convert Juptior Notes to Git Pitch 
"""
def __load_pynotes(note_path):
    with open(note_path, 'r') as note:
        pynotes = json.load(note)
    return pynotes["cells"]


SLIDE_SEPERATOR = "---"


def before_write_to_pitchme_and_python():
    try:
        subprocess.run(["mv", "PITCHME.md", "PITCHME_BNK.md"])
    except:
        pass
    subprocess.run(["touch", "PITCHME.md"])


def write_to_pitchme_and_python(note_path):
    """
    write to pitchme.md
    :return:
    """
    note_cells = __load_pynotes(note_path)
    codes = []
    with open('PITCHME.md', 'a') as pitchme:
        for note_cell in note_cells:
            if note_cell.get("cell_type", "none") == 'markdown':
                md = note_cell['source']
                if md[0][:2] == "##":
                    pitchme.write(SLIDE_SEPERATOR + "\n")
                    pitchme.write("\n")
                pitchme.writelines(md)
                pitchme.write("\n")
            if note_cell['cell_type'] == 'code':
                if len(note_cell["source"]) >= 1:
                    pitchme.write("\n")
                    pitchme.write("```python")
                    pitchme.write("\n")
                    pitchme.writelines(note_cell["source"])
                    pitchme.write("\n")
                    pitchme.write("```\n")
                    codes.extend(note_cell["source"])
    py_path = note_path.replace("ipynb","py")
    print(py_path)
    with open(py_path,'w') as py_file:
        py_file.writelines("".join(codes))

if __name__ == '__main__':
    pitchme_path = sys.argv[1]
    python_file_path = pitchme_path
    if len(pitchme_path) < 1:
        raise Exception("Your Input python Notes is not correct!!! "
                        "Usage is python pynote2pitch.py <your_file_path>")
    before_write_to_pitchme_and_python()
    write_to_pitchme_and_python(pitchme_path)
