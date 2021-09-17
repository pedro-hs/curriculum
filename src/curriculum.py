from fpdf import FPDF

from page_data import PageData


class Curriculum(FPDF):
    def set_language(self, language):
        self.data = PageData(language).data

    def header(self):
        self._set_font()
        self._set_section_color()
        self.rect(0, 0, 250, 15.2, 'F')

        self._set_ornament_color()
        self.rect(0, 0, 2, 15.2, 'F')

        self._empty_line()

        self._set_font('B', 13)
        self._section_line(7, self.data.info.name)

        self._set_font()
        self._section_line(3, self.data.info.age)

        self.image('images/github.png', self.w - 80, 2, h=10)
        self._set_font('I')
        self.set_text_color(255, 255, 255)
        self.text(145, 9, self.data.info.github)

    def experience_section(self):
        self._full_section_header(self.data.section_titles.expeciences)

        for expecience in self.data.experiences:
            self._empty_line(4)

            self._set_font('B')
            self.cell(40, 7, expecience.company)
            self.cell(0, 7, expecience.position, ln=1)

            self.set_draw_color(190, 190, 190)
            self.line(10, self.get_y(), self.w - 10, self.get_y())

            top = self.y
            offset = self.x + 40

            self._empty_line()
            self._set_font(size=8)
            self.multi_cell(40, 7, expecience.period)

            self.y = top
            self.x = offset

            self._set_font(size=11)
            self.multi_cell(153, 7, expecience.description.encode('latin-1', 'replace').decode('latin-1'), align='L')
            self._empty_line(4)

    def knowledges(self):
        self._full_section_header(self.data.section_titles.knowledges)

        self._empty_line(3)

        self.set_x(15)
        self._set_font('B', 11)
        self.cell(0, 7, self.data.knowledges)

    def others(self):
        self._empty_line(12)

        self._half_section_header(self.data.section_titles.academic, width=90)
        self.cell(10, 7)
        self._half_section_header(self.data.section_titles.languages, width=0)

        self._empty_line(4)

        self._set_font(size=11)
        self.cell(102, 15, self.data.academic)
        self.cell(0, 15, self.data.languages)

    def footer(self):
        self.set_y(-60)
        self._set_font()

        self._set_section_color()
        self.rect(0, self.y, 250, 120, 'F')

        self._footer_text('Email', self.data.info.email, 24)
        self.image('images/email.png', 40, self.y - 9, h=10.5)

        self._empty_line(5)
        self.cell(50, self.y, fill=True)
        self._section_line(7, self.data.info.linkedin)
        self.image('images/linkedin.png', 10, self.y - 18, h=28)

        self._footer_text('WhatsApp', self.data.info.whatsapp, 12)
        self.image('images/whatsapp.png', 42, self.y - 8, h=9)

        self.set_y(-2)
        self._set_ornament_color()
        self.rect(0, self.y, 250, 3, 'F')

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
        self._empty_line(6)
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
