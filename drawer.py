from pyx import canvas, path, deco, style, color, text


c = canvas.canvas()
c.stroke(path.line(0, 0, 23, 0), [deco.earrow(size=0.5)])
c.stroke(path.line(0, 0, 0, 23), [deco.earrow(size=0.5)])
c.stroke(path.line(0, 20, 20, 20), [style.linestyle.dashed])
c.stroke(path.line(20, 0, 20, 20), [style.linestyle.dashed])
c.stroke(path.line(0, 0, 20, 20), [style.linestyle.dashed])

c.stroke(path.line(0, 13, 13, 13), [style.linestyle.dashed])
c.stroke(path.line(13, 0, 13, 13), [style.linestyle.dashed])

c.stroke(path.line(0, 7, 7, 7), [style.linestyle.dashed])
c.stroke(path.line(7, 0, 7, 7), [style.linestyle.dashed])

c.stroke(path.line(0, 0, 6, 0), [style.linewidth.THICK])
c.stroke(path.line(7, 7, 13, 13), [style.linewidth.THICK])
c.stroke(path.line(14, 0, 19, 0), [style.linewidth.THICK])
c.stroke(path.circle(20, 20, 0.001), [style.linewidth.THICK])

c.text(0, 23, r"Jump$(x)$", [text.halign.boxright, text.valign.top, text.size.Huge])
c.text(23, 0, r"OneMax$(x)$", [text.halign.boxleft, text.valign.top, text.size.Huge])

c.text(0, 20, r"$n$", [text.halign.boxright, text.valign.middle, text.size.Huge])
c.text(0, 13, r"$n - l - 1$", [text.halign.boxright, text.valign.middle, text.size.Huge])
c.text(0, 7, r"$l + 1$", [text.halign.boxright, text.valign.middle, text.size.Huge])

c.text(0, 0, r"$0$", [text.halign.boxright, text.valign.top, text.size.Huge])

c.text(7, -0.2, r"$l + 1$", [text.halign.boxcenter, text.valign.top, text.size.Huge])
c.text(13, -0.2, r"$n - l - 1$", [text.halign.boxcenter, text.valign.top, text.size.Huge])
c.text(20, -0.2, r"$n$", [text.halign.boxcenter, text.valign.top, text.size.Huge])

c.stroke(path.line(0, 0, 0, -3), [style.linestyle.dashed])
c.stroke(path.line(6.5, -1.5, 6.5, -3), [style.linestyle.dashed])
c.stroke(path.line(13.5, -1.5, 13.5, -3), [style.linestyle.dashed])
c.stroke(path.line(19.5, -1.5, 19.5, -3), [style.linestyle.dashed])

c.text(3.25, -3, r"$s = 0$", [text.halign.boxcenter, text.valign.bottom, text.size.Huge])
c.text(10, -3, r"$s =$OneMax$(x)$", [text.halign.boxcenter, text.valign.bottom, text.size.Huge])
c.text(16.5, -3, r"$s = 0$", [text.halign.boxcenter, text.valign.bottom, text.size.Huge])
c.text(19.5, -3, r"$s = n$", [text.halign.boxleft, text.valign.bottom, text.size.Huge])
c.writePDFfile("states_illustration.pdf")