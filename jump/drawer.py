from pyx import canvas, path, deco, style, color, text


c = canvas.canvas()
#axis
c.stroke(path.line(0, 0, 23, 0), [deco.earrow(size=0.5)])
c.stroke(path.line(0, 0, 0, 11), [deco.earrow(size=0.5)])
#dashed lines
c.stroke(path.line(0, 10, 20, 10), [style.linestyle.dashed])
c.stroke(path.line(20, 0, 20, 10), [style.linestyle.dashed])
c.stroke(path.line(0, 0, 20, 10), [style.linestyle.dashed])

c.stroke(path.line(0, 6.5, 13, 6.5), [style.linestyle.dashed])
c.stroke(path.line(13, 0, 13, 6.5), [style.linestyle.dashed])

c.stroke(path.line(0, 3.5, 7, 3.5), [style.linestyle.dashed])
c.stroke(path.line(7, 0, 7, 3.5), [style.linestyle.dashed])

#plot
c.stroke(path.line(0, 0, 7, 0), [style.linewidth.THICK])
c.stroke(path.line(7, 3.5, 13, 6.5), [style.linewidth.THICK])
c.stroke(path.line(13, 0, 20, 0), [style.linewidth.THICK])
c.stroke(path.circle(20, 10, 0.1), [style.linewidth.THICK])
c.stroke(path.circle(13, 6.5, 0.1), [style.linewidth.THICK])
c.stroke(path.circle(7, 3.5, 0.1), [style.linewidth.THICK])
c.stroke(path.circle(13, 0, 0.18))
c.stroke(path.circle(7, 0, 0.18))
c.stroke(path.circle(20, 0, 0.18))
c.fill(path.circle(13, 0, 0.18), [color.rgb.white])
c.fill(path.circle(7, 0, 0.18), [color.rgb.white])
c.fill(path.circle(20, 0, 0.18), [color.rgb.white])

#text
c.text(-0.2, 11, r"Jump$(x)$", [text.halign.boxright, text.valign.top, text.size.Huge])
c.text(23, -0.2, r"OneMax$(x)$", [text.halign.boxcenter, text.valign.top, text.size.Huge])

c.text(0, 10, r"$n$", [text.halign.boxright, text.valign.top, text.size.Huge])
c.text(0, 6.5, r"$n - l - 1$", [text.halign.boxright, text.valign.middle, text.size.Huge])
c.text(0, 3.5, r"$l + 1$", [text.halign.boxright, text.valign.middle, text.size.Huge])

c.text(0, 0, r"$0$", [text.halign.boxright, text.valign.top, text.size.Huge])

c.text(7, -0.2, r"$l + 1$", [text.halign.boxcenter, text.valign.top, text.size.Huge])
c.text(13, -0.2, r"$n - l - 1$", [text.halign.boxcenter, text.valign.top, text.size.Huge])
c.text(20, -0.2, r"$n$", [text.halign.boxcenter, text.valign.top, text.size.Huge])

c.stroke(path.line(0, 0, 0, -2), [style.linestyle.dashed])
c.stroke(path.line(7, -1.0, 7, -2), [style.linestyle.dashed])
c.stroke(path.line(13, -1.0, 13, -2), [style.linestyle.dashed])
c.stroke(path.line(20, -1.0, 20, -2), [style.linestyle.dashed])

c.text(3.5, -1.5, r"$s = 0$", [text.halign.boxcenter, text.valign.middle, text.size.Huge])
c.text(10, -1.5, r"$s =$OneMax$(x)$", [text.halign.boxcenter, text.valign.middle, text.size.Huge])
c.text(16.5, -1.5, r"$s = 0$", [text.halign.boxcenter, text.valign.middle, text.size.Huge])
c.text(20, -1.5, r"$s = n$", [text.halign.boxleft, text.valign.middle, text.size.Huge])

#leftbridge
#axis
c.stroke(path.line(27, 5.5, 27, 11), [deco.earrow(size=0.5)])
c.stroke(path.line(27, 5.5, 38, 5.5), [deco.earrow(size=0.5)])
#dashed_lines
c.stroke(path.line(27, 5.5 +1.75, 30.5, 5.5 + 1.75), [style.linestyle.dashed])
c.stroke(path.line(30.5, 5.5, 30.5, 5.5 + 1.75), [style.linestyle.dashed])
#plot
c.stroke(path.line(27, 5.5, 30.5, 5.5 + 1.75), [style.linewidth.THICK])
c.stroke(path.line(30.5, 5.5, 37, 5.5), [style.linewidth.THICK])
c.stroke(path.circle(30.5, 5.5, 0.1), [style.linewidth.THICK])
c.stroke(path.circle(30.5, 5.5 + 1.75, 0.18))
c.fill(path.circle(30.5, 5.5 + 1.75, 0.18), [color.rgb.white])

#text
c.text(27 - 0.2, 11, r"LeftBridge$(x)$", [text.halign.boxright, text.valign.top, text.size.huge])
c.text(38, 5.5 + 0.2, r"OneMax$(x)$", [text.halign.boxcenter, text.valign.bottom, text.size.huge])

c.text(27, 5.5 + 1.75, r"$l + 1$", [text.halign.boxright, text.valign.middle, text.size.huge])

c.text(27, 5.5, r"$0$", [text.halign.boxright, text.valign.top, text.size.huge])

c.text(30.5, 5.5 - 0.2, r"$l + 1$", [text.halign.boxcenter, text.valign.top, text.size.huge])
c.text(37, 5.5 -0.2, r"$n$", [text.halign.boxcenter, text.valign.top, text.size.huge])

#rightbridge
#axis
c.stroke(path.line(27, -1, 27, 4.5), [deco.earrow(size=0.5)])
c.stroke(path.line(27, -1, 38, -1), [deco.earrow(size=0.5)])
#dashed_lines
c.stroke(path.line(27, -1, 37, 4), [style.linestyle.dashed])
c.stroke(path.line(27, 4, 37, 4), [style.linestyle.dashed])
c.stroke(path.line(37, -1, 37, 4), [style.linestyle.dashed])
c.stroke(path.line(27, 2.25, 33.5, 2.25), [style.linestyle.dashed])
c.stroke(path.line(33.5, -1, 33.5, 2.25), [style.linestyle.dashed])
#plot
c.stroke(path.line(33.5, 2.25, 37, 4), [style.linewidth.THICK])
c.stroke(path.line(27, -1, 33.5, -1), [style.linewidth.THICK])
c.stroke(path.circle(33.5, -1, 0.1), [style.linewidth.THICK])
c.stroke(path.circle(33.5, 2.25, 0.18))
c.fill(path.circle(33.5, 2.25, 0.18), [color.rgb.white])

#text
c.text(27 - 0.2, 4.5, r"RightBridge$(x)$", [text.halign.boxright, text.valign.top, text.size.huge])
c.text(38, -1 + 0.2, r"OneMax$(x)$", [text.halign.boxcenter, text.valign.bottom, text.size.huge])

c.text(27, 2.25, r"$n - l - 1$", [text.halign.boxright, text.valign.middle, text.size.huge])

c.text(27, -1, r"$0$", [text.halign.boxright, text.valign.top, text.size.huge])

c.text(33.5, -1.2, r"$n - l - 1$", [text.halign.boxcenter, text.valign.top, text.size.huge])
c.text(37, -1.2, r"$n$", [text.halign.boxcenter, text.valign.top, text.size.huge])

c.writePDFfile("states_illustration.pdf")