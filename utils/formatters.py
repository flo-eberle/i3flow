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


def formatter(config_type, scheme):
    if config_type == 'xresources':
        # format for .Xresources
        # #define base00 #xxxxxx
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

    elif config_type == 'termite':
        # format for termite
        colors = ['\n']
        comment = '#'
        # color mappings
        termite_colors = {
            'foreground': 'base05',
            'foreground_bold': 'base06',
            'cursor': 'base06',
            'cursor_foreground': 'base00',
            'background': 'base00',
            'color0': 'base00',
            'color8': 'base03',
            'color7': 'base05',
            'color15': 'base07',
            'color1': 'base09',
            'color9': 'base09',
            'color2': 'base0B',
            'color10': 'base0B',
            'color3': 'base0A',
            'color11': 'base0A',
            'color4': 'base0D',
            'color12': 'base0D',
            'color5': 'base0E',
            'color13': 'base0E',
            'color6': 'base0C',
            'color14': 'base0C',
            'color16': 'base07',
            'color17': 'base0F',
            'color18': 'base01',
            'color19': 'base02',
            'color20': 'base04',
            'color21': 'base06',
            }
        
        if scheme['scheme']:
            colors.append(f'{comment} scheme: {scheme["scheme"]}\n')
        if scheme['author']:
            colors.append(f'{comment} author: {scheme["author"]}\n\n')

        for key, value in termite_colors.items():
            colors.append(f'{key} = #{scheme[value]}\n')
        colors.append('\n')

    elif config_type == 'vim':
        # format for vim
        # let s:base00 = "xxxxxx"
        colors = ['\n']
        comment = '"'
        for key, value in scheme.items():
            if 'base' in key:
                if 'base00' in key:
                    colors.append('\n')
                line = (f'let s:{key} = "{value}"\n')
            else:
                line = (f'{comment} {key}: {value}\n')
            colors.append(line)
        colors.append('\n')

    return colors

