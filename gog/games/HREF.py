import glob

for a in glob.glob("*.html"):
    print("<li><a href=\"\\gog\games\\{}\">{}</a></li>".format(a, a.split(".")[0]))
output.txt
