class Stationery:
    title = "title"
    draw = "draw"

    def runDraw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def runDraw(self):
        print("Это Pen")


class Pencil(Stationery):
    def runDraw(self):
        print("Это Pencil")


class Handle(Stationery):
    def runDraw(self):
        print("Это Handle")


pen = Pen()
pen.runDraw()

pencil = Pencil()
pencil.runDraw()

handle = Handle()
handle.runDraw()
