#!/usr/bin/env python3

# TODO: formatter for rofi
# TODO: vim: colors_name
# TODO: merge xrdb
# TODO: reload i3
# TODO: reload polybar
# TODO: reload termite
# TODO: reload vim

import yaml
import utils.formatters

SCHEMEPATH = '/home/flo/i3flow/schemes/tonerlow.yaml'

CONFIG_FILES = {
    'xresources': '/home/flo/i3flow/testing/.Xresources',
    'termite': '/home/flo/i3flow/testing/termite.config',
    'vim': '/home/flo/i3flow/testing/tonerlow.vim',
}

with open(SCHEMEPATH, 'r') as f:
    scheme = yaml.full_load(f) 
    # print(scheme)

def write_configs(application, config_path):
    with open(config_path, 'r') as config:
        config_lines = config.readlines()

    formatted_colors = utils.formatters.formatter(application, scheme)

    color_open, color_close = utils.formatters.find_color_indices(config_lines)

    # overwrite part between color tags
    config_lines[color_open:color_close] = formatted_colors

    with open(config_path, 'w') as output:
        output.writelines(config_lines)

for key, value in CONFIG_FILES.items():
    print(f'Writing config for "{key}" to {value}')
    write_configs(key, value)
    print('Done!')
