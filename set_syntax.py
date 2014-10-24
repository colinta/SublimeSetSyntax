import sublime
import sublime_plugin


class SetSyntaxCommand(sublime_plugin.WindowCommand):
    def run(self, matches=None):
        if matches is None:
            self.window.run_command('show_overlay', {"overlay": "command_palette", "text": "Set Syntax: "})
        else:
            self.window.run_command('show_overlay', {"overlay": "command_palette", "text": "Set Syntax: " + matches})


class SetSyntaxSettingsCommand(sublime_plugin.TextCommand):
    def run(self, matches=None):
        soft_tabs = self.view.settings().get('translate_tabs_to_spaces')
        tabs = self.view.settings().get('tab_size')
        settings = [
            ('{} Tab Width: 2'.format(tabs == 2 and '✓' or '  '), lambda: self.set_tab_size(2)),
            ('{} Tab Width: 4'.format(tabs == 4 and '✓' or '  '), lambda: self.set_tab_size(4)),
            ('{} Tab Width: 8'.format(tabs == 6 and '✓' or '  '), lambda: self.set_tab_size(6)),
            ('———', lambda: None),
            ('Convert indentation to {}'.format(soft_tabs and 'Tab' or 'Spaces'), lambda: self.set_soft_tabs(not soft_tabs)),
            ('Reapply indentation to {}'.format(not soft_tabs and 'Tab' or 'Spaces'), lambda: self.set_soft_tabs(soft_tabs)),
        ]
        prompts = [entry[0] for entry in settings]
        self.view.window().show_quick_panel(prompts, self.handler(settings))

    def handler(self, settings):
        def _handler(choice):
            if choice != -1:
                sublime.set_timeout(lambda: settings[choice][1](), 0)
        return _handler

    def tab_size_handler(self, settings):
        def _handler(choice):
            if choice != -1:
                sublime.set_timeout(lambda: settings[choice][1](), 0)
        return _handler

    def set_soft_tabs(self, new_setting):
        if new_setting:
            self.view.run_command('expand_tabs')
        else:
            self.view.run_command('unexpand_tabs')
        self.view.settings().set('translate_tabs_to_spaces', new_setting)

    def set_tab_size(self, new_setting):
        self.view.settings().set('tab_size', new_setting)
