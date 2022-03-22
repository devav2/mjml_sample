
from mjml import mjml_to_html
import sys

if len(sys.argv) == 2:
    mjml_file = open(sys.argv[1])
    mjml_data=mjml_file.read()

    print(mjml_to_html(mjml_data)['html'])