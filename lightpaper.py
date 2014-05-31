import os
import sys
import subprocess
import sublime
import sublime_plugin

class LightpaperCommand(sublime_plugin.WindowCommand):
    def run(self):
        filename = self.window.active_view().file_name()
        if filename is None:
            return

        proc_env = os.environ.copy()
        encoding = sys.getfilesystemencoding()
        for k, v in proc_env.items():
            proc_env[k] = os.path.expandvars(v).encode(encoding)

        subprocess.call(['open', '-a', 'LightPaper', filename], env=proc_env)

    def is_enabled(self):
        return True

    def is_visible(self):
        view = sublime.active_window().active_view()
        if view:
            return view.settings().get('syntax') == 'Packages/Markdown/Markdown.tmLanguage'
