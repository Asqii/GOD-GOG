import glob

for a in glob.glob("*.html"):
    print("<div class=\"game\"><a href=\"\\games\\{}\">{}</a></div>".format(a, a.split(".")[0]))
