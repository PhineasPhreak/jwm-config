from glob import glob
import os

tmpl = """<IconPath>
%s
</IconPath>"""

print("<JWM>")

print("\n".join([tmpl % dir for dir in glob("/usr/share/icons/*/*x*/*")]))

print("</JWM>")    
