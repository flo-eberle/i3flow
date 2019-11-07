#!/usr/bin/env python3

import yaml

SCHEMEPATH = '/home/flo/i3flow/schemes/tonerlow.yaml'

XRESOURCES = '/home/flo/i3flow/testing/.Xresources'

COLOR_OPEN_TAG = '*startcolors*'
COLOR_CLOSE_TAG = '*endcolors*'

def formatXresources(scheme):
    xr_colors=[]
    comment = '!'
    for key, value in scheme.items():
        if 'base' in key:
            line = f'#define {key} #{value}\n'
        else:
            line = f'{comment} {key}: {value}\n'
        xr_colors.append(line)
    return xr_colors

with open(SCHEMEPATH, 'r') as f:
    scheme = yaml.full_load(f) 
    # print(scheme)

with open(XRESOURCES, 'r') as xr:
    xr_lines = xr.readlines()

# find indices of COLOR_TAGS
i = 0
for line in xr_lines:
    if COLOR_OPEN_TAG in line:
        color_open = i+1
    if COLOR_CLOSE_TAG in line:
        color_close = i
        break
    i += 1

fxr = formatXresources(scheme)

# overwrite part between color tags
xr_lines[color_open:color_close] = fxr

for line in xr_lines:
    print(line, end='')
