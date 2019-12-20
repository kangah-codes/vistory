__author__ = "Joshua Akangah"

import guizero
from guizero import Window
import matplotlib as plot
import browserhistory as bh

box = None
history = None
labels = None

app = guizero.App(title="Vistory", width=500, height=600)
hist_window = Window(app, title="History")
hist_window.hide()

def main():
	guizero.Text(app, text=" ")
	guizero.Text(app, text="Visualize browser history")
	guizero.Text(app, text=" ")

	global box
	box = guizero.Box(app, width="fill")
	guizero.PushButton(box, text="Read HIstory from Browsers", command=findHistory)

def findHistory():
	global history
	history = bh.get_browserhistory()
	guizero.Text(box, text="Available browsers")
	guizero.Text(box, text=" ")
	for i in history.keys():
		guizero.Text(box, text=" ")
		guizero.PushButton(box, text=f"Read data from {i}", command=readData, args=[i])

def getHistory(browser):
	hist = []
	hist.append(f"{_[0]}//{_[2]}" for _ in history[browser].split('/'))
	print(hist)


if __name__ == '__main__':
	main()
	app.display()