import sublime
import sublime_plugin

class PassCodeCommand(sublime_plugin.WindowCommand):
	def run(self, text_command):
		self.window.run_command("send_code", {
            "code": text_command,
            })

	def input(self,args):
		if 'text_command' not in args:
			return TextCommandInputHandler()
	def input_description(self):
		return 'SendCode: Pass:'

class TextCommandInputHandler(sublime_plugin.TextInputHandler):
	
	def initial_text(self):
		return