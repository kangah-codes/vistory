__author__ = "Joshua Akangah"

import guizero
import matplotlib as plot
import browserhistory as bh

box = None

app = guizero.App(title="Vistory", width=500, height=600)

def main():
	guizero.Text(app, text=" ")
	guizero.Text(app, text="Visualize browser history")
	guizero.Text(app, text=" ")

	global box
	box = guizero.Box(app, width="fill")
	guizero.PushButton(box, text="Read HIstory from Browsers", command=findHistory)

def findHistory():
	history = bh.get_browserhistory()
	guizero.Text(box, text="Available browsers")
	guizero.Text(box, text=" ")
	for i in history.keys():
		guizero.Text(box, text=" ")
		guizero.PushButton(box, text=f"Read data from {i}")


if __name__ == '__main__':
	main()
	app.display()