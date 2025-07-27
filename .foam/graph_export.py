import numpy as np
import networkx as nx
import pathlib
import re
files = list(pathlib.Path("./content").glob("**/*.md"))
def _extract_wikilinks(text) -> list[str]:
    return re.findall(r"\[\[(.*?)\]\]", text)

def _extract_hashtags(text) -> list[str]:
    # hash with more than two chars
    return re.findall(r"#(\w{2,})", text)
# can be visualized with https://gephi.org/gephi-lite/
#   yEd does not work
g = nx.DiGraph()
for file in files:
    fname_slug = file.stem
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
        wikilinks = _extract_wikilinks(text)
        for link in wikilinks:
            link = link.split("#")[0]
            g.add_edge(fname_slug, link)

        g.add_node(fname_slug, __labels__="File", filename=fname_slug)

        hashtags = _extract_hashtags(text)
        for tag in hashtags:
            g.add_edge(fname_slug, tag, __labels__="Tagged")
            g.add_node(tag, __labels__="Tag", filename=fname_slug)

nx.write_graphml(g, "graph.graphml")
