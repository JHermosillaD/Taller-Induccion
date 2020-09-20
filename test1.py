import bokeh.plotting as bpl
b = bpl.figure()
b.circle(x=[10,20,40],y=[800,400,650],radius=[10,20,10],color=["red","purple","orange"], line_color="black",line_width=5)

output_file('circulo.html')
bpl.show(b)
