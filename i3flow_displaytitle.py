#!/usr/bin/env python3

from i3ipc import Connection
from subprocess import call
import sys
import i3flow_sm

def clipboarder(text):
    # escape the colon for the string piped into clipboard
    ftext = text.replace(':', '\:').strip('\n')
    return f'%{{A3:echo {ftext} | xclip -i -selection clipboard:}}{text}%{{A}}'

i3 = Connection()

mode = i3flow_sm.get('polybar_title_mode')

# switch display title mode, save the state with i3flow_sm
if len(sys.argv) > 1 and sys.argv[1] == 'switch':
    if mode == 'advanced':
        i3flow_sm.set('polybar_title_mode', 'normal')
        mode = 'normal'
    else:
        i3flow_sm.set('polybar_title_mode', 'advanced')
        mode = 'advanced'


focused = i3.get_tree().find_focused()
if mode == 'normal':
    output = clipboarder(focused.name)
else:
    output = f'{clipboarder(focused.window_class)}   ---   {clipboarder(focused.window_instance)}'

print(f'%{{A1:polybar-msg hook titlehook 2:}}{output}%{{A}}')
