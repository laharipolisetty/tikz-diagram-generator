def generate_tikz_code(description):
    desc = description.lower()

    if 'circle' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) circle (1cm);\n\\end{tikzpicture}"

    elif 'rectangle' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) rectangle (2,1);\n\\end{tikzpicture}"

    elif 'triangle' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) -- (1,2) -- (2,0) -- cycle;\n\\end{tikzpicture}"

    elif 'line' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) -- (2,0);\n\\end{tikzpicture}"

    elif 'ellipse' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) ellipse (2cm and 1cm);\n\\end{tikzpicture}"

    elif 'arrow' in desc:
        return "\\begin{tikzpicture}\n\\draw[->] (0,0) -- (2,0);\n\\end{tikzpicture}"

    elif 'grid' in desc:
        return "\\begin{tikzpicture}\n\\draw[step=1cm,gray,very thin] (0,0) grid (3,3);\n\\end{tikzpicture}"

    elif 'pentagon' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) -- (1,2) -- (3,2) -- (4,0) -- (2,-2) -- cycle;\n\\end{tikzpicture}"

    elif 'hexagon' in desc:
        return "\\begin{tikzpicture}\n\\draw (1,0) -- (2,0) -- (2.5,0.87) -- (2,1.73) -- (1,1.73) -- (0.5,0.87) -- cycle;\n\\end{tikzpicture}"

    elif 'dashed line' in desc:
        return "\\begin{tikzpicture}\n\\draw[dashed] (0,0) -- (2,0);\n\\end{tikzpicture}"

    elif 'double line' in desc:
        return "\\begin{tikzpicture}\n\\draw[double] (0,0) -- (2,0);\n\\end{tikzpicture}"

    elif 'arrow loop' in desc:
        return "\\begin{tikzpicture}\n\\draw[->] (0,0) arc (180:540:1cm);\n\\end{tikzpicture}"

    elif 'labeled arrow' in desc:
        return "\\begin{tikzpicture}\n\\draw[->] (0,0) -- (2,0) node[midway, above] {Label};\n\\end{tikzpicture}"

    elif 'arc' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) arc (0:180:1cm);\n\\end{tikzpicture}"

    elif 'semi circle' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) arc (0:180:1cm);\n\\end{tikzpicture}"

    elif 'brace' in desc:
        return "\\begin{tikzpicture}\n\\draw [decorate,decoration={brace,amplitude=10pt}] (0,0) -- (2,0);\n\\end{tikzpicture}"

    elif 'node circle' in desc:
        return "\\begin{tikzpicture}\n\\node[circle, draw] {A};\n\\end{tikzpicture}"

    elif 'node rectangle' in desc:
        return "\\begin{tikzpicture}\n\\node[rectangle, draw] {B};\n\\end{tikzpicture}"

    elif 'cloud' in desc:
        return "\\begin{tikzpicture}\n\\node[cloud, draw] {Cloud};\n\\end{tikzpicture}"

    elif 'star' in desc:
        return "\\begin{tikzpicture}\n\\node[star, star points=5, draw] {Star};\n\\end{tikzpicture}"

    elif 'diamond' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,1) -- (1,2) -- (2,1) -- (1,0) -- cycle;\n\\end{tikzpicture}"

    elif 'parallelogram' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) -- (1,1) -- (3,1) -- (2,0) -- cycle;\n\\end{tikzpicture}"

    elif 'cylinder' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) ellipse (1cm and 0.3cm);\n\\draw (-1,0) -- (-1,-2);\n\\draw (1,0) -- (1,-2);\n\\draw (-1,-2) arc (180:360:1cm and 0.3cm);\n\\draw[dashed] (1,-2) arc (0:180:1cm and 0.3cm);\n\\end{tikzpicture}"

    elif 'coordinate axis' in desc:
        return "\\begin{tikzpicture}\n\\draw[->] (0,0) -- (2,0) node[right] {x};\n\\draw[->] (0,0) -- (0,2) node[above] {y};\n\\end{tikzpicture}"

    elif 'flowchart start' in desc:
        return "\\begin{tikzpicture}\n\\node[ellipse, draw] {Start};\n\\end{tikzpicture}"

    elif 'flowchart process' in desc:
        return "\\begin{tikzpicture}\n\\node[rectangle, draw] {Process};\n\\end{tikzpicture}"

    elif 'flowchart decision' in desc:
        return "\\begin{tikzpicture}\n\\node[diamond, draw] {Decision};\n\\end{tikzpicture}"

    elif 'flowchart end' in desc:
        return "\\begin{tikzpicture}\n\\node[ellipse, draw] {End};\n\\end{tikzpicture}"

    elif 'tree diagram' in desc:
        return "\\begin{tikzpicture}\n\\node {Root} child {node {Left}} child {node {Right}};\n\\end{tikzpicture}"

    elif 'mind map' in desc:
        return "\\begin{tikzpicture}[mindmap]\n\\node {Main}\n  child {node {Idea 1}}\n  child {node {Idea 2}};\n\\end{tikzpicture}"

    elif 'bar chart' in desc:
        return "\\begin{tikzpicture}\n\\filldraw (0,0) rectangle (0.5,1);\n\\filldraw (1,0) rectangle (1.5,2);\n\\filldraw (2,0) rectangle (2.5,1.5);\n\\end{tikzpicture}"

    elif 'circle sector' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) -- (2,0) arc (0:60:2) -- cycle;\n\\end{tikzpicture}"

    elif 'tikz matrix' in desc:
        return "\\begin{tikzpicture}\n\\matrix[matrix of nodes] {\nA & B & C \\\\\nD & E & F \\\\\nG & H & I \\\\\n};\n\\end{tikzpicture}"

    elif 'tikz table' in desc:
        return "\\begin{tikzpicture}\n\\matrix (m) [matrix of nodes, nodes in empty cells,row sep=1em,column sep=2em]\n{\n Header1 & Header2 & Header3 \\\\\n Row1 & Data & Data \\\\\n Row2 & Data & Data \\\\\n};\n\\end{tikzpicture}"

    elif 'tikz pie chart' in desc:
        return "\\begin{tikzpicture}\n\\foreach \\p/\\t in {30/A,60/B,90/C,180/D}\n  {\\draw[fill=blue!\\p] (0,0) -- (\\t:1) arc (\\t:\\t+\\p:1) -- cycle;}\n\\end{tikzpicture}"

    elif 'tikz sine curve' in desc:
        return "\\begin{tikzpicture}\n\\draw[domain=0:6.28,smooth,variable=\\x] plot ({\\x},{sin(\\x r)});\n\\end{tikzpicture}"

    elif 'tikz vector' in desc:
        return "\\begin{tikzpicture}\n\\draw[->] (0,0) -- (2,1);\n\\end{tikzpicture}"

    elif 'tikz brace' in desc:
        return "\\begin{tikzpicture}\n\\draw [decorate,decoration={brace,amplitude=10pt}] (0,0) -- (2,0);\n\\end{tikzpicture}"

    elif 'tikz timeline' in desc:
        return "\\begin{tikzpicture}\n\\draw (0,0) -- (5,0);\n\\foreach \\x in {0,1,2,3,4,5} \\draw (\\x,0.1) -- (\\x,-0.1);\n\\end{tikzpicture}"

    else:
        return "\\begin{tikzpicture}\n\\node {No matching diagram found};\n\\end{tikzpicture}"
