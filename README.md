SetSyntax for Sublime Text 2
==================================

Some generic keyboard bindings for 'Set Syntax:'

Installation
------------

1. Using Package Control, install "SetSyntax"

Or:

1. Open the Sublime Text 2 Packages folder

    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/

2. clone this repo
3. Install keymaps for the commands (see Example.sublime-keymap for my preferred keys)

Commands
--------

`set_syntax`: Opens a command selector that is prefiltered with 'Set Syntax'.

If you provide a `matches` argument, the list will be filtered further, and if only one syntax matches that syntax is used.
