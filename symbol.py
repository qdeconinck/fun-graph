import numpy as np

class Drawer:
    def line(self, from_pt, to_pt, dx, dy, **kwargs):
        dx += list(np.linspace(from_pt[0], to_pt[0], **kwargs))
        dy += list(np.linspace(from_pt[1], to_pt[1], **kwargs))

class ScatterDataGenerator:
    # TODO dict of list of lists of 2-tuples
    pts_between = {
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
        "i": [
            [
                (0, 0.5),
                (0, -0.5),
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
        