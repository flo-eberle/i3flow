#!/usr/bin/env python3

SESSION_FILE = '/home/flo/i3flow/.i3flow.session'

def get(parm):
    with open(SESSION_FILE, 'r') as f:
        for line in f:
            if line.startswith(parm):
                return line.strip('\n').split(' ')[1]

def set(parm, value):
    with open(SESSION_FILE, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith(parm):
            lines[i] = f'{parm} {value}\n'
        break

    with open(SESSION_FILE, 'w') as f:
        f.writelines(lines)
