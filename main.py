"""
	Main file composing the main screen and initializing the app 
"""
from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.containers import HorizontalGroup, VerticalGroup, Vertical, Horizontal
from textual.widget import Widget
from textual.reactive import reactive


from textual import events
from rich.text import Text


import time
import asyncio


class ClockWidget(Widget):
	"""A widget that displays a live clock"""

	current_time = reactive("")

	async def on_mount(self):
		"""Start a timer when the widget mounts"""
		self.set_interval(1, self.update_time)
		self.update_time()

	def update_time(self):
		self.current_time = time.strftime("%H:%M:%S")
		self.refresh()

	def render(self):
		text = Text(self.current_time, style="bold cyan", justify="center")
		return text

class Header(Horizontal):

	"""The Header of the app"""

	def compose(self) -> ComposeResult:
		yield ClockWidget(id="clock")
		yield Button("test", id="test-button")

class ratesoftApp(App):
	"""The Textual App making the interface"""

	CSS_PATH = "main.tcss"

	def compose(self) -> ComposeResult:
		"""Creation of child widgets for the app displayed"""
		yield Header()




if __name__ == "__main__":
	app = ratesoftApp()
	app.run()