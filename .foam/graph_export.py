import networkx as nx
import pathlib
import re

SAFE_NODE_RE = re.compile(r'^[\w\-]+$')  # Only allow letters, numbers, _, -

def _extract_wikilinks(text) -> list[str]:
    return re.findall(r"\[\[(.*?)\]\]", text)

def _extract_hashtags(text) -> list[str]:
    return re.findall(r"#(\w{2,})", text)

def sanitize_node_id(s: str) -> str:
    # Remove problematic characters and strip whitespace
    s = re.sub(r'[|<>]', '', s).strip().replace(' ', '_')
    # Only allow safe characters
    s = re.sub(r'[^\w\-]', '', s)
    return s

g = nx.DiGraph()
files = list(pathlib.Path("./content").glob("**/*.md"))[:20]  # Only first 20 files in ./content
for file in files:
    fname_slug = sanitize_node_id(file.stem)
    if not fname_slug or not SAFE_NODE_RE.match(fname_slug):
        continue
    g.add_node(fname_slug, __labels__="File")
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
        wikilinks = _extract_wikilinks(text)
        for link in wikilinks:
            link = sanitize_node_id(link.split("#")[0])
            if link and SAFE_NODE_RE.match(link):
                g.add_node(link)
                g.add_edge(fname_slug, link)
        hashtags = _extract_hashtags(text)
        for tag in hashtags:
            tag = sanitize_node_id(tag)
            if tag and SAFE_NODE_RE.match(tag):
                g.add_node(tag, __labels__="Tag")
                g.add_edge(fname_slug, tag, __labels__="Tagged")

nx.write_graphml(g, "graph.graphml")