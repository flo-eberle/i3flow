# find indices of COLOR_TAGS
def find_color_indices(lines):
    COLOR_OPEN_TAG = '*startcolors*'
    COLOR_CLOSE_TAG = '*endcolors*'
    i = 0
    for line in lines:
        if COLOR_OPEN_TAG in line:
            color_open = i+1
        if COLOR_CLOSE_TAG in line:
            color_close = i
            break
        i += 1
    return (color_open, color_close)

# format for .Xresources
# #define base00 #xxxxxx
def formatXresources(scheme):
    colors=['\n']
    comment = '!'
    for key, value in scheme.items():
        if 'base' in key:
            if 'base00' in key:
                colors.append('\n')
            line = f'#define {key} #{value}\n'
        else:
            line = f'{comment} {key}: {value}\n'
        colors.append(line)

    colors.append('\n')
    return colors

# format for i3 config
# set $base00 #xxxxxx
def formati3(scheme):
    colors=['\n']
    comment = '#'
    for key, value in scheme.items():
        if 'base' in key:
            if 'base00' in key:
                colors.append('\n')
            line = f'set ${key} #{value}\n'
        else:
            line = f'{comment} {key}: {value}\n'
        colors.append(line)

    colors.append('\n')
    return colors
