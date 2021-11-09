import sublime
import sublime_plugin

class TerminusOpenDirectionPromptedCommand(sublime_plugin.WindowCommand):
	def run(self, direction):
		self.window.run_command("terminus_open",
			{ 
				"title": "Terminus",
				#"tag": "Terminus",
				"cwd": "${file_path:${folder}}",
				"pre_window_hooks": [
					["window_focus", { "store": True }]
				],
				"post_window_hooks": [
					["carry_file_to_pane", {"direction": direction}],
					["window_focus", { "store": False }]
				],
			}
		)

	def input(self,args):
		if 'direction' not in args:
			return DirectionInputHandler()
	def input_description(self):
		return 'Terminus: Open'

class DirectionInputHandler(sublime_plugin.ListInputHandler):
	def list_items(self):
		return [
			("right"),
			("down"),
			("left"),
			("up"),
			("self"),
		]
	def placeholder(self):
		return 'direction'


