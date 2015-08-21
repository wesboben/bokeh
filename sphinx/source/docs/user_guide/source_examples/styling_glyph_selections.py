from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import Circle

output_file("styling_selections.html")

p = figure(plot_width=400, plot_height=400, tools="tap", title="Select a circle")
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=50, name="mycircle")

selected_circle = Circle(fill_alpha=1, fill_color="firebrick", line_color=None)
nonselected_circle = Circle(fill_alpha=0.2, fill_color="blue", line_color="firebrick")

renderer = p.select(name="mycircle")
renderer.selection_glyph = selected_circle
renderer.nonselection_glyph = nonselected_circle

show(p)
