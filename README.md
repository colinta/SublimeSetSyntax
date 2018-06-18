SetSyntax
=========

Some generic keyboard bindings for 'Set Syntax:'

Installation
------------

1. Using Package Control, install "SetSyntax"

Or:

1. Open the Sublime Text Packages folder
    - OS X: ~/Library/Application Support/Sublime Text 3/Packages/
    - Windows: %APPDATA%/Sublime Text 3/Packages/
    - Linux: ~/.Sublime Text 3/Packages/ or ~/.config/sublime-text-3/Packages

2. clone this repo
3. Install keymaps for the commands (see Example.sublime-keymap for my preferred keys)

Commands
--------

`set_syntax`: Opens a command selector that is prefiltered with 'Set Syntax'.

If you provide a `matches` argument, the list will be filtered further, and if only one syntax matches that syntax is used.
