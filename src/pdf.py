from fpdf import FPDF


class PDF(FPDF):
    def _section_line(self, height, text='', align='L', width=0, ln=1):
        self.set_text_color(255, 255, 255)
        self._set_section_color()
        self.cell(width, height, text, align=align, fill=True, border=1, ln=ln)
        self.set_text_color(0, 0, 0)

    def _set_ornament_color(self):
        self.set_fill_color(41, 180, 255)
        self.set_draw_color(41, 180, 255)

    def _set_section_color(self):
        self.set_fill_color(27, 30, 38)
        self.set_draw_color(27, 30, 38)

    def _empty_line(self, quantity=1):
        self.cell(0, 2 * quantity, ln=1)

    def _set_font(self, style='', size=12):
        self.set_font('arial', style, size)

    def _full_section_header(self, text):
        self._empty_line(5)
        self._set_font('B')

        self._section_line(1)
        self._section_line(6, text, 'C')

    def _half_section_header(self, text, width):
        self._set_font('B')
        self._section_line(6, text, 'C', width=width, ln=0)

    def _footer_text(self, key, value, position):
        self._empty_line(4)
        self.cell(50, self.y, fill=True)
        self._section_line(7, value)
        self.set_text_color(255, 255, 255)
        self._set_font('B', 16)
        self.text(position, self.y - 2, key)
        self._set_font()
