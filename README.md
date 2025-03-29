SetSyntax
=========

Some generic keyboard bindings for 'Set Syntax:'

Installation
------------

Using Package Control, install "SetSyntax" or clone this repo in your packages folder.

I recommended you add key bindings for the commands. I've included my preferred bindings below.
Copy them to your key bindings file (⌘⇧,).

Commands
--------

`set_syntax`: Opens a command selector that is prefiltered with 'Set Syntax'.

If you provide a `matches` argument, the list will be filtered further, and if only one syntax matches that syntax is used.

`set_syntax_settings`: Easy access to indentation settings for the current buffer (does not change global settings).

Key Bindings
------------

Copy these to your user key bindings file.

<!-- keybindings start -->
    { "keys": ["super+ctrl+shift+s"], "command": "set_syntax_settings" },
    { "keys": ["ctrl+alt+shift+a"], "command": "set_syntax", "args": {"matches": "a"} },
    { "keys": ["ctrl+alt+shift+b"], "command": "set_syntax", "args": {"matches": "b"} },
    { "keys": ["ctrl+alt+shift+c"], "command": "set_syntax", "args": {"matches": "c"} },
    { "keys": ["ctrl+alt+shift+d"], "command": "set_syntax", "args": {"matches": "d"} },
    { "keys": ["ctrl+alt+shift+e"], "command": "set_syntax", "args": {"matches": "e"} },
    { "keys": ["ctrl+alt+shift+f"], "command": "set_syntax", "args": {"matches": "f"} },
    { "keys": ["ctrl+alt+shift+g"], "command": "set_syntax", "args": {"matches": "g"} },
    { "keys": ["ctrl+alt+shift+h"], "command": "set_syntax", "args": {"matches": "h"} },
    { "keys": ["ctrl+alt+shift+i"], "command": "set_syntax", "args": {"matches": "i"} },
    { "keys": ["ctrl+alt+shift+j"], "command": "set_syntax", "args": {"matches": "j"} },
    { "keys": ["ctrl+alt+shift+k"], "command": "set_syntax", "args": {"matches": "k"} },
    { "keys": ["ctrl+alt+shift+l"], "command": "set_syntax", "args": {"matches": "l"} },
    { "keys": ["ctrl+alt+shift+m"], "command": "set_syntax", "args": {"matches": "m"} },
    { "keys": ["ctrl+alt+shift+n"], "command": "set_syntax", "args": {"matches": "n"} },
    { "keys": ["ctrl+alt+shift+o"], "command": "set_syntax", "args": {"matches": "o"} },
    { "keys": ["ctrl+alt+shift+p"], "command": "set_syntax", "args": {"matches": "p"} },
    { "keys": ["ctrl+alt+shift+q"], "command": "set_syntax", "args": {"matches": "q"} },
    { "keys": ["ctrl+alt+shift+r"], "command": "set_syntax", "args": {"matches": "r"} },
    { "keys": ["ctrl+alt+shift+s"], "command": "set_syntax", "args": {"matches": "s"} },
    { "keys": ["ctrl+alt+shift+t"], "command": "set_syntax", "args": {"matches": "t"} },
    { "keys": ["ctrl+alt+shift+u"], "command": "set_syntax", "args": {"matches": "u"} },
    { "keys": ["ctrl+alt+shift+v"], "command": "set_syntax", "args": {"matches": "v"} },
    { "keys": ["ctrl+alt+shift+w"], "command": "set_syntax", "args": {"matches": "w"} },
    { "keys": ["ctrl+alt+shift+x"], "command": "set_syntax", "args": {"matches": "x"} },
    { "keys": ["ctrl+alt+shift+y"], "command": "set_syntax", "args": {"matches": "y"} },
    { "keys": ["ctrl+alt+shift+z"], "command": "set_syntax", "args": {"matches": "z"} },
<!-- keybindings stop -->
