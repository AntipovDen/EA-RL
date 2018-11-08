from matplotlib import pyplot as plt
from pyx import canvas, path, deco, style, color, text

def plot():
    k = 10
    x = list(range(81))
    om = x.copy()
    zm = x.copy()
    zm.reverse()
    xdk = [[5 * ((i + 10 * j) // k) for i in range(k)] for j in range(80 // k)]


    plt.plot(x, om, 'b-', label='OneMax')
    plt.plot(x, zm, 'r-', label='ZeroMax')
    plt.plot(x[:k], xdk[0], 'g-', label='X div K')
    for i in range(1, 8):
        plt.plot(x[k * i:k * i + k], xdk[i], 'g-',)
    plt.plot([80], [40], 'go')
    plt.plot([80], [80], 'bo')
    plt.plot([0], [80], 'ro')
    plt.xlabel("Number of one-bits")

    plt.legend(loc=4)
    plt.show()

def plateau():
    c = canvas.canvas()

    c.stroke(path.line(0, 0, 12, 0), [style.linewidth.Thick, color.cmyk.Green])
    c.stroke(path.line(-3, -3, -5, -3), [style.linewidth.Thick, color.cmyk.Green])
    c.stroke(path.line(15, 3, 17, 3), [style.linewidth.Thick, color.cmyk.Green])

    c.stroke(path.curve(0, 0.5, 1, 2, 2, 2, 3, 0.5), [style.linewidth.Thick, deco.earrow.Large()])
    c.stroke(path.curve(3, 0.5, 4, 2, 5, 2, 6, 0.5), [style.linewidth.Thick, deco.earrow.Large()])
    c.stroke(path.curve(6, 0.5, 7, 2, 8, 2, 9, 0.5), [style.linewidth.Thick, deco.earrow.Large()])
    c.stroke(path.curve(9, 0.5, 10, 2, 11, 2, 12, 0.5), [style.linewidth.Thick, deco.earrow.Large()])

    #fall
    c.stroke(path.curve(0, 0.5, -1, 1, -2, -0.5, -3, -2.5), [style.linewidth.Thick, deco.earrow.Large(), color.cmyk.Red])

    #finish
    c.stroke(path.curve(12, 0.5, 13, 3, 14, 4.5, 15, 3.5), [style.linewidth.Thick, deco.earrow.Large(), color.cmyk.RoyalBlue])

    c.fill(path.circle(-3, -3, 0.5), [color.cmyk.Green])
    c.fill(path.circle(0, 0, 0.5), [color.cmyk.Green])
    c.fill(path.circle(3, 0, 0.5), [color.cmyk.Green])
    c.fill(path.circle(6, 0, 0.5), [color.cmyk.Green])
    c.fill(path.circle(9, 0, 0.5), [color.cmyk.Green])
    c.fill(path.circle(12, 0, 0.5), [color.cmyk.Green])
    c.fill(path.circle(15, 3, 0.5), [color.cmyk.Green])
    
    c.stroke(path.circle(-3, -3, 0.5), [style.linewidth.Thick])
    c.stroke(path.circle(0, 0, 0.5), [style.linewidth.Thick])
    c.stroke(path.circle(3, 0, 0.5), [style.linewidth.Thick])
    c.stroke(path.circle(6, 0, 0.5), [style.linewidth.Thick])
    c.stroke(path.circle(9, 0, 0.5), [style.linewidth.Thick])
    c.stroke(path.circle(12, 0, 0.5), [style.linewidth.Thick])
    c.stroke(path.circle(15, 3, 0.5), [style.linewidth.Thick])

    c.text(0, -1, r"\Huge{$i$}", [text.halign.boxcenter, text.valign.middle])
    c.text(12, -1, r"\Huge{$i + k - 1$}", [text.halign.boxcenter, text.valign.middle])

    c.writePDFfile("plateau.pdf")

plot()
