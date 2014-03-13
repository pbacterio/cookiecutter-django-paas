#!/usr/bin/env python
"""Post-generate hook"""

from os import walk, path
from random import choice
from string import Template


def main():
    """Generate Django SECRET_KEY setting"""
    for (dirpath, _, filenames) in walk('.'):
        if 'settings.py' in filenames:
            settings_path = path.join(dirpath, 'settings.py')
            break
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = ''.join((choice(chars) for _ in range(50)))
    with open(settings_path) as settings_file:
        tmpl = Template(settings_file.read())
    open(settings_path, 'w').write(tmpl.safe_substitute(secret_key=secret_key))

if __name__ == '__main__':
    main()
