#!/usr/bin/env python3

# TODO: formatter for polybar
# TODO: formatter for termite
# TODO: formatter for vim
# TODO: formatter for rofi
# TODO: injector for i3
# TODO: injector for polybar
# TODO: injector for termite
# TODO: injector for vim
# TODO: injector for rofi

import yaml
import utils.formatters

SCHEMEPATH = '/home/flo/i3flow/schemes/tonerlow.yaml'

XRESOURCES = '/home/flo/i3flow/testing/.Xresources'
I3CONFIG = '/home/flo/i3flow/testing/i3.config'

with open(SCHEMEPATH, 'r') as f:
    scheme = yaml.full_load(f) 
    # print(scheme)

with open(I3CONFIG, 'r') as config:
    config_lines = config.readlines()

formatted_colors = utils.formatters.formati3(scheme)

color_open, color_close = utils.formatters.find_color_indices(config_lines)

# overwrite part between color tags
config_lines[color_open:color_close] = formatted_colors

for line in config_lines:
    print(line, end='')
