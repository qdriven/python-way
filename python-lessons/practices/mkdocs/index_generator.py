# -*- coding: utf-8 -*-

import yaml
import os


class MkdocsGenerator(object):
    """
    This file is used for generate mkdoc.yml files.
    The Convention of this project is that:
    1. folder name is subsection name, index_chapter name
    2. file_name: index_subsection_description
    """

    def __init__(self):
        self.md_files = {}
        self.yaml_setting = {}

    def read_all_notes(self):
        """
        1. read the existing files
        2. scan the folders to get the files
        3. compose the mkdocs files
        :return:
        """
        for item in os.listdir('docs'):
            if item.endswith('.md') or item.endswith('.sh') or item.startswith('.') or item =='getting_shit_done': continue
            self.md_files[item] = list()
            for root, folder, file in os.walk('docs/' + item):
                if len(file) >= 1 and root != 'docs' :
                    for f in file:
                        self.md_files[item].append({f.replace('.md', ''):
                                                        root.replace('docs/', '') + '/' + f})

    def load_yaml_setting(self, f):

        """
        load mkdocs.yml first
        :return:
        """
        self.yaml_setting = yaml.load(f)
        self.yaml_setting['pages'] = []
        self.yaml_setting['pages'].append({"Home": "index.md"})


    def generate_mkdocs_yaml(self):
        with open('mkdocs.yml', 'r') as f:
            self.read_all_notes()
            self.load_yaml_setting(f)
            for k in self.md_files:
                self.yaml_setting['pages'].append({k: self.md_files[k]})
            with open('mkdocs.yml', 'w') as new_file:
                new_file.write(yaml.dump(self.yaml_setting, default_flow_style=False))
        self.write_index()

    def write_index(self):

        title = '# Learning Testing in a hard way \n'
        content = []
        for item in self.yaml_setting['pages']:
            for k in item:
                if k not in ['Home', 'About','getting_shit_done'] and not k.startswith('.'):
                    content.append('## ' + k.capitalize().replace('_', ' '))
                    if len(item[k]) >= 1:
                        print(item[k])
                        for index_item in item[k]:
                            print(index_item)
                            print(type(index_item))
                            for key in index_item:
                                content.append(
                                '   - [' + key + '](' + index_item[key] + ')'
                                 )
        with open('docs/index.md', 'w') as index:
            document = "\n\n".join([title, '\n'.join(content)])
            index.write(document)


if __name__ == '__main__':
    MkdocsGenerator().generate_mkdocs_yaml()
