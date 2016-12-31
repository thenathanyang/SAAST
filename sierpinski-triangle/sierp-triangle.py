from drawingpanel import *

def create_s_triangle(canvas, x1, y1, x2, y2, x3, y3, n):
    if n == 0:
        canvas.create_polygon(x1, y1, x2, y2, x3, y3)
    else:
        hx1 = (x1 + x2) / 2
        hy1 = (y1 + y2) / 2
        hx2 = (x2 + x3) / 2
        hy2 = (y2 + y3) / 2
        hx3 = (x1 + x3) / 2
        hy3 = (y1 + y3) / 2
        create_s_triangle(canvas, x1, y1, hx1, hy1, hx3, hy3, n - 1)
        create_s_triangle(canvas, hx1, hy1, x2, y2, hx2, hy2, n - 1)
        create_s_triangle(canvas, hx3, hy3, hx2, hy2, x3, y3, n - 1)

def main():
    panel = DrawingPanel(200,200)
    canvas = panel.canvas
    create_s_triangle(canvas, 0, 200, 100, 0, 200, 200, 4)

if __name__ == "__main__":
    print main()