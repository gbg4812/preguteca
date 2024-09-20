import re
from io import FileIO, TextIOWrapper
import xml.dom.minidom as dom


svg = dom.parse("main_illustration_v3_Mesa de trabajo 1.svg")
comp = open("../../components/MainIllustration.vue", "r+")


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return "".join(rc)


INJAPPEND = 0
INJREPLACE = 1


def inject(oldstr: str, value: str, tag: str, mode: int):
    tags = re.search(f"<{tag}.*>", oldstr).start()
    tage = oldstr.find(f"</{tag}>")

    if mode == INJREPLACE:
        oldstr = oldstr[:tags] + f"<{tag}>" + value + oldstr[tage:]
    return oldstr


for el in svg.getElementsByTagName("image"):
    path = el.getAttribute("xlink:href")
    fpath = "../../assets/main-illustration/img/" + path
    el.setAttribute("xlink:href", fpath)
    print("modified image path to: " + fpath)

css = ""
for el in svg.getElementsByTagName("style"):
    css += getText(el.childNodes)
    el.unlink()


code = comp.read()

code = inject(
    code,
    css,
)
