__author__ = "Joshua Akangah"

import guizero
from guizero import Window
import matplotlib.pyplot as plot
import browserhistory as bh

box = None
history = None
hist = None
times = None
parse_hist = None

app = guizero.App(title="Vistory", width=500, height=600)
hist_window = Window(app, title="History")
hist_window.hide()

def main():
	guizero.Text(app, text=" ")
	guizero.Text(app, text="Visualize browser history")
	guizero.Text(app, text=" ")

	global box
	box = guizero.Box(app, width="fill")
	guizero.PushButton(box, text="Check browsers", command=findHistory)

def findHistory():
	global history
	history = bh.get_browserhistory()
	guizero.Text(box, text="Available browsers")
	guizero.Text(box, text=" ")
	for i in history.keys():
		guizero.PushButton(box, text=f"Read data from {i}", command=getHistory, args=[i])

def getHistory(browser):
	global hist
	global times
	global parse_hist
	hist = []
	times = []
	for i in history[browser]:
		times.append(i[-1])
		hist.append(i[0].split('/'))

	parse_hist = []
	for i in hist:
		parse_hist.append(f"{i[0]}//{i[2]}")

	hist_window.show()
	guizero.Text(hist_window, text=f"History for {browser}")
	guizero.Text(hist_window, text=f" ")
	guizero.Text(hist_window, text="If no history appears, try closing the browser and restart the app.", align="bottom")
	guizero.ListBox(hist_window, items=list(zip(times, parse_hist)), width="fill", height="fill", scrollbar=True)
	guizero.PushButton(hist_window, text="Plot data", command=plotData, args=[browser], align="bottom")

def Nmaxelements(list1, N): 
	final_list = [] 
	urls = []
	for i in range(0, N):  
		max1 = 0
		for j in range(len(list1)):  
			final_list.append([list1[j][0], list1[j][1]])

	items = []
	final_list.sort()
	for i in final_list:
		if i not in items:
			items.append(i)
	items.sort(reverse=True)
	return items[0:5]

def plotData(browser):
	final_items = []
	final_item = []

	parse_hist.sort()


	for i in parse_hist[::-1][0:1000]:
		if i not in final_items:
			final_items.append([parse_hist[::-1][0:1000].count(i), i])

	for i in final_items:
		if i not in final_item:
			final_item.append(i)


	dict_of_vals = { i[1] : i[0] for i in Nmaxelements(final_item, 5) }

	names = list(dict_of_vals.keys())
	names1 = []
	names2 = []
	names3 = []
	# bad code
	for i in names:
		names1.append(i.split('.com'))
	for i in names1:
		a = i[0].split('https://')
		names2.append(a[1].split('www.'))
	for i in names2:
		try:
			if i[0] == '':
				names3.append(i[1])
			else:
				names3.append(i[0])

		except:
			pass

	vals = list(dict_of_vals.values())
	fig = plot.figure(figsize=(10, 5))
	plot.style.use('ggplot')

	x = names3
	y = vals

	x_pos = [i for i, _ in enumerate(x)]

	plot.bar(x_pos, y, color='green')
	plot.xlabel("Websites")
	plot.ylabel("Visits")
	plot.title("Most visited sites in browser history")

	plot.xticks(x_pos, names3)

	plot.show()

if __name__ == '__main__':	
	main()
	app.display()