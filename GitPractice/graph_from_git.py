"""
Generates the commit graph from the current .git folder
"""

import os
import collections
import typing as t
import urllib.parse

def get_object_hashes():
    stdout = os.popen("git rev-list --objects --all")
    hashes_list = stdout.read().split("\n")
    for obj_hash in hashes_list:
        parts = list(filter(lambda x: x != "", obj_hash.split(" "))) # two parts for file hashes, 1 for else
        if len(parts) == 1:
            yield obj_hash

def get_refs():
    stdout = os.popen("git show-ref")
    refs_list = stdout.read().split("\n")
    for ref in refs_list:
        parts = ref.split(" ")
        if len(parts) >= 2:
            ref_hash = parts[0]
            ref_name = parts[1]
            if ref_name.startswith("refs/heads"):
                yield (f"\"{ref_name[11:]}\"", ref_hash)

def get_edge_if_exists(obj_hash: str):
    stdout = os.popen(f"git cat-file {obj_hash} -p")
    object_contents = stdout.read().split("\n")
    if object_contents[0].startswith("tree"):
        if len(object_contents) > 1 and object_contents[1].startswith("parent"):
            return (object_contents[1].split("parent ")[1], obj_hash)
    # print(object_contents)

def get_edges():
    for h in get_object_hashes():
        e = get_edge_if_exists(h)
        if e is not None:
            yield e

def get_commit_number(commit_hash: str, objects: t.List[str]) -> int:
    return len(objects) - objects.index(commit_hash)

def rename(edges: t.List[t.Tuple[str, str]], refs: t.List[t.Tuple[str, str]]):
    objects = list(get_object_hashes())
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        yield (get_commit_number(parent, objects), get_commit_number(child, objects))
    for ref in refs:
        yield (ref[0], get_commit_number(ref[1], objects))

def generate_dot(edges: t.Iterable[t.Tuple[int, int]]):
    edges = list(edges)
    nodes_set = set()
    for edge in edges:
        if type(edge[0]) != str:
            nodes_set.add(edge[0])
            nodes_set.add(edge[1])
    node_color = "\n".join(map(lambda n: f"  {n} [style=filled];", nodes_set))
    edges_dot = "\n".join(map(lambda e: f"  {e[0]}->{e[1]};", edges))
    return "digraph G {\n" + node_color + "\n" + edges_dot + "\n}"

def get_visualization_link(dot: str):
    sanitized_dot = urllib.parse.quote(dot)
    return f"https://dreampuf.github.io/GraphvizOnline/#{sanitized_dot}"

d = generate_dot(rename(get_edges(), get_refs()))
# with open("steps_dot.txt", "wb") as df:
#     df.write(d.encode("UTF-8"))
print(get_visualization_link(d))
