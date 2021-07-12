import numpy as np

class Drawer:
    def line(self, from_pt, to_pt, dx, dy, **kwargs):
        dx += list(np.linspace(from_pt[0], to_pt[0], **kwargs))
        dy += list(np.linspace(from_pt[1], to_pt[1], **kwargs))

class ScatterDataGenerator:
    pts_between = {
        "a": [
            [
                (-0.5, -0.5),
                (-0.5, 0.5),
                (0.5, 0.5),
                (0.5, -0.5),
            ],
            [
                (-0.5, 0),
                (0.5, 0),
            ]
        ],
        "b": [
            [
                (-0.5, 0.5),
                (0.4, 0.5),
                (0.5, 0.4),
                (0.5, 0.1),
                (0.4, 0),
                (0.5, -0.1),
                (0.5, -0.4),
                (0.4, -0.5),
                (-0.5, -0.5),
                (-0.5, 0.5),
            ],
            [
                (-0.5, 0),
                (0.4, 0),
            ],
        ],
        "c": [
            [
                (0.5, 0.5),
                (-0.5, 0.5),
                (-0.5, -0.5),
                (0.5, -0.5),
            ],
        ],
        "d": [
            [
                (-0.5, 0.5),
                (0.25, 0.5),
                (0.5, 0.25),
                (0.5, -0.25),
                (0.25, -0.5),
                (-0.5, -0.5),
                (-0.5, 0.5),
            ],
        ],
        "e": [
            [
                (0.5, 0.5),
                (-0.5, 0.5),
                (-0.5, -0.5),
                (0.5, -0.5),
            ],
            [
                (-0.5, 0),
                (0.5, 0),
            ],
        ],
        "f": [
            [
                (0.5, 0.5),
                (-0.5, 0.5),
                (-0.5, -0.5),
            ],
            [
                (-0.5, 0),
                (0.5, 0),
            ],
        ],
        "g": [
            [
                (0.5, 0.5),
                (-0.5, 0.5),
                (-0.5, -0.5),
                (0.5, -0.5),
                (0.5, 0),
                (0.25, 0),
            ],
        ],
        "h": [
            [
                (-0.5, 0.5),
                (-0.5, -0.5),
            ],
            [
                (0.5, 0.5),
                (0.5, -0.5),
            ],
            [
                (-0.5, 0),
                (0.5, 0),
            ],
        ],
        "i": [
            [
                (0, 0.5),
                (0, -0.5),
            ],
        ],
        "j": [
            [
                (-0.5, 0.5),
                (0.5, 0.5),
            ],
            [
                (0.125, 0.5),
                (0.125, -0.5),
                (-0.5, -0.5),
                (-0.5, -0.25),
            ],
        ],
        "k": [
            [
                (-0.5, 0.5),
                (-0.5, -0.5),
            ],
            [
                (-0.5, 0),
                (0.5, 0.5),
            ],
            [
                (-0.5, 0),
                (0.5, -0.5),
            ],
        ],
        "l": [
            [
                (-0.5, 0.5),
                (-0.5, -0.5),
                (0.5, -0.5),
            ],
        ],
        "m": [
            [
                (-0.5, -0.5),
                (-0.5, 0.5),
                (0, 0),
                (0.5, 0.5),
                (0.5, -0.5),
            ],
        ],
        "n": [
            [
                (-0.5, -0.5),
                (-0.5, 0.5),
                (0.5, -0.5),
                (0.5, 0.5),
            ],
        ],
        "o": [
            [
                (0.5, 0.5),
                (-0.5, 0.5),
                (-0.5, -0.5),
                (0.5, -0.5),
                (0.5, 0.5),
            ],
        ],
        "p": [
            [
                (-0.5, -0.5),
                (-0.5, 0.5),
                (0.5, 0.5),
                (0.5, 0),
                (-0.5, 0),
            ],
        ],
        "q": [
            [
                (0.5, 0.5),
                (-0.3, 0.5),
                (-0.3, -0.3),
                (0.5, -0.3),
                (0.5, 0.5),
            ],
            [
                (0, 0),
                (0.5, -0.5),
            ],
        ],
        "r": [
            [
                (-0.5, -0.5),
                (-0.5, 0.5),
                (0.25, 0.5),
                (0.25, 0.125),
                (0, 0),
                (0.5, -0.5),
            ],
            [
                (-0.5, 0),
                (0.25, 0),
            ],
        ],
        "s": [
            [
                (0.5, 0.5),
                (-0.5, 0.5),
                (-0.5, 0),
                (0.5, 0),
                (0.5, -0.5),
                (-0.5, -0.5),
            ],
        ],
        "t": [
            [
                (-0.5, 0.5),
                (0.5, 0.5),
            ],
            [
                (0, 0.5),
                (0, -0.5),
            ],
        ],
        "u": [
            [
                (-0.5, 0.5),
                (-0.5, -0.5),
                (0.5, -0.5),
                (0.5, 0.5),
            ],
        ],
        "v": [
            [
                (-0.5, 0.5),
                (0, -0.5),
                (0.5, 0.5),
            ],
        ],
        "w": [
            [
                (-0.5, 0.5),
                (-0.25, -0.5),
                (0, 0.5),
                (0.25, -0.5),
                (0.5, 0.5),
            ],
        ],
        "x": [
            [
                (-0.5, 0.5),
                (0.5, -0.5),
            ],
            [
                (-0.5, -0.5),
                (0.5, 0.5),
            ],
        ],
        "y": [
            [
                (-0.5, 0.5),
                (0, 0),
                (0.5, 0.5),
            ],
            [
                (0, 0),
                (0, -0.5),
            ],
        ],
        "z": [
            [
                (-0.5, 0.5),
                (0.5, 0.5),
                (-0.5, -0.5),
                (0.5, -0.5),
            ],
        ],
        "-": [
            [
                (-0.5, 0),
                (0.5, 0),
            ],
        ],
        "?": [
            [
                (-0.5, 0.375),
                (-0.375, 0.5),
                (0.375, 0.5),
                (0.5, 0.375),
                (0, 0),
                (0, -0.125),
            ],
            [
                (-0.075, -0.5),
                (-0.075, -0.425),
                (0.075, -0.425),
                (0.075, -0.5),
                (-0.075, -0.5),
            ],
        ],
        " ": [

        ],
    }

    def __init__(self):
        self.drawer = Drawer()
        self.dx = []
        self.dy = []

    def draw_straight_lines(self, pts, **kwargs):
        for pt in pts:
            assert(len(pt) == 2)
            self.drawer.line(pt[0], pt[1], self.dx, self.dy, **kwargs)

    def draw_straight_lines_between(self, pts_between, **kwargs):
        assert(len(pts_between) >= 2)
        pts = []
        for i in range(len(pts_between) - 1):
            assert(len(pts_between[0]) == 2)
            assert(len(pts_between[1]) == 2)
            pts.append((pts_between[i], pts_between[i + 1]))

        self.draw_straight_lines(pts, **kwargs)

    def get_pts(self, c, ct, num=50):
        if c in ScatterDataGenerator.pts_between:
            for curve in ScatterDataGenerator.pts_between[c]:
                pts_between_c = []
                for pt_x, pt_y in curve:
                    pts_between_c.append((ct[0] + pt_x, ct[1] + pt_y))

                self.draw_straight_lines_between(pts_between_c, num=50)
        else:
            raise NotImplementedError("Character {} not supported".format(c))

    def get_data_line(self, text, cy, **kwargs):
        cx = -((len(text) - 1) / 2) * 1.5
        for i in range(len(text)):
            ch = text[i]
            ct = (cx + (i * 1.5), cy) # TODO update cy
            self.get_pts(ch, ct)

        return self.dx, self.dy

    def get_data(self, text, **kwargs):
        if isinstance(text, str):
            return self.get_data_line(text, 0.0, **kwargs)
        elif isinstance(text, list):
            cy = ((len(text) - 1) / 2) * 1.5
            for i in range(len(text)):
                self.get_data_line(text[i], cy - (i * 1.5))

            return self.dx, self.dy
        else:
            raise NotImplementedError("Unsupported type")
