#!/usr/bin/env python3

# TODO: formatter for rofi
# TODO: vim - colors_name

import subprocess
import yaml
import utils.formatters

SCHEMEPATH = '/home/flo/i3flow/schemes/tonerlow.yaml'

CONFIG_FILES = {
    'xresources': '/home/flo/.Xresources',
    'termite': '/home/flo/.config/termite/config',
    'vim': '/home/flo/.vim/colors/tonerlow.vim',
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


# reload stuff to update configs
subprocess.run(['xrdb', '-merge', '/home/flo/.Xresources'])
subprocess.run(['i3-msg', 'restart'])
subprocess.run(['killall', '-USR1', 'termite'])
