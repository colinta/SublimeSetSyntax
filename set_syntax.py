# import sublime
import sublime_plugin


class SetSyntaxCommand(sublime_plugin.WindowCommand):
    def run(self, matches=None):
        if matches is None:
            self.window.run_command('show_overlay', {"overlay": "command_palette", "text": "Set Syntax: "})
        else:
            self.window.run_command('show_overlay', {"overlay": "command_palette", "text": "Set Syntax: " + matches})
