import sys

from curriculum import Curriculum

language = sys.argv[1]

pdf = Curriculum()

pdf.set_margins(10, 0, 10)
pdf.set_language(language)
pdf.add_page()

pdf.experience_section()
pdf.knowledges()
pdf.others()

pdf.output(f'Pedro_Santos_Arruda_{language}.pdf')
