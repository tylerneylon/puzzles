import sys

all_pieces = [
    (32, 11),
    (32, 10),
    (28, 14),
    (17, 14),
    (28,  7),
    (14,  4),
    (10,  7),
    (28,  6),
    (21, 18),
    (21, 18),
    (21, 14),
    (21, 14)
]

class Grid(object):
    """A grid is a collection of pieces that fill in left-to-right, top-to-bottom, thinking of the
       origin at the upper-left corner. Pieces can be added or removed in a stack-like manner."""

    def __init__(self, w, h):
        self.size = (w, h)
        self._grid = [[0] * h for i in range(w)]
        self.pt = (0, 0)
        self.num_pieces = 0

        # Data to support piece pop operations.
        self._pts = [(0, 0)]

    def can_add_piece(self, piece):
        """Try to add the piece at the next available space; only works if it fits in the grid.

           This returns True if and only if `piece` was able to fit into the grid."""

        # Return False if the piece won't fit with it's upper-left corner at self.pt.
        for i in range(2):
            if self.pt[i] + piece[i] > self.size[i]:
                return False
        x0, y0 = self.pt
        for x in range(x0, x0 + piece[0]):
            if self._grid[x][y0]:
                return False

        # It can fit; add it to self._grid.
        for y in range(y0, y0 + piece[1]):
            self._grid[x0][y] = (piece[0], piece[1], id(piece))

        # Update self.pt and self.num_pieces.
        while y0 < self.size[1] and self._grid[x0][y0]:
            x0 += self._grid[x0][y0][0]
            if x0 == self.size[0]:
                x0, y0 = 0, y0 + 1
        self.pt = (x0, y0)
        self._pts.append(self.pt)
        self.num_pieces += 1

        return True

    def pop(self):
        """Remove the last-added piece from the grid."""

        self._pts.pop()
        self.pt = self._pts[-1]
        x0, y0 = self.pt

        pw, ph = self._grid[x0][y0][:2]
        for y in range(y0, y0 + ph):
            self._grid[x0][y] = 0

        self.num_pieces -= 1

    def print_grid(self):
        """Print out the current pieces within the grid in an ascii-artish sort of style."""

        # Set up the outline.
        w, h = self.size
        lines = [list('|' + ' ' * (2 * w - 1) + '|' if i not in [0, h] else
                      '+' + '-' * (2 * w - 1) + '+') for i in range(h + 1)]

        # Draw the individual pieces.
        pieces_seen = set()
        for x in range(w):
            for y in range(h):
                p = self._grid[x][y]
                if p in pieces_seen:
                    continue
                pieces_seen.add(p)
                self._draw_piece_at(p, x, y, lines)

        print '\n'.join(''.join(line) for line in lines)

    def _draw_piece_at(self, p, x0, y0, lines):

        if p == 0:
            return

        pw, ph = p[0], p[1]
        x0 *= 2
        pw *= 2

        for x in range(x0, x0 + pw + 1):
            lines[y0][x] = lines[y0 + ph][x] = '-'

        for y in range(y0, y0 + ph + 1):
            ch = '+' if y in [y0, y0 + ph] else '|'
            lines[y][x0] = lines[y][x0 + pw] = ch

        label = '%dx%d' % (p[0], p[1])
        lines[y0 + 1][x0 + 1:x0 + 1 + len(label)] = list(label)

def spin_of(piece, spin):
    """Return the appropriate rotation of `piece` based on 0/1 value `spin`."""
    return (piece[1], piece[0]) if spin else piece

def print_solutions_of_size(w, h, pieces, grid=None, exit_on_soln=False):
    """Print all solutions with the given pieces in the given width w and height h.

       This will exit the program once the first solution is found if exit_on_soln is True."""

    grid = grid or Grid(w, h)

    for i, piece in enumerate(pieces):
        for spin in range(2):
            p = spin_of(piece, spin)
            if grid.can_add_piece(p):
                if grid.num_pieces == len(all_pieces):
                    print 'Found a solution!'
                    grid.print_grid()
                    if exit_on_soln:
                        sys.exit(0)
                else:
                    print_solutions_of_size(w, h, pieces[:i] + pieces[i + 1:], grid, exit_on_soln)
                grid.pop()


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print 'Usage: python %s [width] [height]' % sys.argv[0]
        sys.exit(2)

    w, h = int(sys.argv[1]), int(sys.argv[2])
    print_solutions_of_size(w, h, all_pieces[:], exit_on_soln=True)
