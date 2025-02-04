#özet: Python'da çizim yapmamızı sağlayan bir modüldü
import turtle

# daire çiz ve bu daire ekranda kalsın
t = turtle.Turtle(shape="turtle")
t.circle(100)
t.getscreen()._root.mainloop()
