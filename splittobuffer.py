import sublime, sublime_plugin

class splittobufferCommand(sublime_plugin.TextCommand):
  def run(self, edit):
		sels = self.view.sel()
		self.window = sublime.active_window()
		self.make_buffer(sels)

	def make_buffer(self, sels):
		regions = []
		orv = self.window.active_view()
		for sel in sels:
			buff = self.window.new_file()
			clipboard = self.view.substr(sel)
			bedit = buff.begin_edit()
			buff.insert(bedit, 0, clipboard)
			buff.end_edit(bedit)
			regions.append(sel)
		self.window.focus_view(orv)
		regions.reverse()
		for region in regions:
			edit = self.view.begin_edit()
			self.view.erase(edit, region)
			self.view.end_edit(edit)

		
