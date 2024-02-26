import argparse
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex
from ete3 import Tree, TreeStyle, NodeStyle, TextFace

def parse_args():
    parser = argparse.ArgumentParser(description='Color tree leaves based on their family.')
    # string parsers
    parser.add_argument('-t', '--tree_file', type=str, help='Input a tree file.')
    parser.add_argument('-f', '--mapping_file', type=str, help='Input a leaf:category mapping file.')
    parser.add_argument('-p', '--palette', type=str, help='Input a seaborn palette name or path to the palette file.')
    parser.add_argument('-title', '--tree_title', type=str, help='Title of the tree.')
    parser.add_argument('-png', '--save_png', type=str, nargs='?', default='Tree.png', help='Optional output filename for the PNG file. If -png is used without a value, uses default name.')
    parser.add_argument('-svg', '--save_svg', type=str, nargs='?', default='Tree.svg', help='Optional output filename for the SVG file. If -svg is used without a value, uses default name.')
    # action parsers
    parser.add_argument('-circ', '--circular_tree', action="store_true", help='Create a circular tree (default:rectangular).')
    parser.add_argument('-r', '--rotate_tree', action="store_true", help="Draw a rectangular tree from top to bottom")
    return parser.parse_args()

def load_mapping(mapping_file):
    leaf_to_family = {}
    with open(mapping_file, 'r') as f:
        for line in f:
            parts = line.strip().split(':')
            if len(parts) == 2:
                leaf_to_family[parts[0]] = parts[1].strip()  # Strip whitespace from family name
    return leaf_to_family

def load_palette(palette):
    if palette.endswith('.txt'):
        # Load palette from file
        with open(palette, 'r') as f:
            palette_dict = {}
            for line in f:
                key, value = line.strip().split(':')
                palette_dict[key.strip()] = value.strip()
        return palette_dict
    else:
        # Assume palette is a seaborn palette name
        return palette

def generate_colors_for_families(palette, families):
    if isinstance(palette, dict):
        # Use the colors from the palette file
        family_colors = {family: rgb2hex(palette.get(family, 'grey')) for family in families}
    else:
        # Generate colors using seaborn palette
        colors = sns.color_palette(palette, n_colors=len(families))
        family_colors = dict(zip(families, colors))
    return family_colors

def rgb_to_hex(rgb_color):
    return rgb2hex(rgb_color)

def apply_node_style(tree):

    '''
    NodeStyle for all the internal nodes 
    '''
    for node in tree.traverse():  
        instyle = NodeStyle()
        instyle["shape"] = "circle"  # Set the shape of the node
        instyle["fgcolor"] = "black"  # Set the foreground color (text color) to white for contrast, if needed
        instyle["size"] = 5  # Set the size of the node, adjust as necessary
        node.set_style(instyle)


def main():

    args = parse_args()

    # Load the tree
    tree = Tree(args.tree_file, format=1)

    # Load the leaf-to-family mapping
    leaf_to_family = load_mapping(args.mapping_file)
    families = sorted(set(leaf_to_family.values()))

    # Generate colors for each family
    if args.palette:
        palette = load_palette(args.palette)
    else:
        palette = "pastel"
    family_colors = generate_colors_for_families(palette, families)

    ## Node Style ##
    apply_node_style(tree) 
    for leaf in tree.iter_leaves():
        family = leaf_to_family.get(leaf.name, None)
        if family:
            color = family_colors.get(family, 'grey')
            hex_color = rgb_to_hex(color)
            nstyle = NodeStyle()
            nstyle["bgcolor"] = hex_color # background color
            nstyle["shape"] = "circle"
            nstyle["fgcolor"] = "black"
            nstyle["size"] = 2
            
            # nstyle["node_bgcolor"] = "black"
            # # Gray dashed branch lines
            # nstyle["hz_line_type"] = 2
            # nstyle["hz_line_color"] = "black"
            # nstyle["vt_line_color"] = "black"

            leaf.set_style(nstyle)

            # space_face = TextFace(" ", fsize=10)  # Adjust `fsize` for bigger or smaller space
            # leaf.add_face(space_face, column=0, position="branch-right")

    # Define tree style
    ts = TreeStyle()

    # Handle tree mode and related settings
    if args.circular_tree:
        ts.mode = "c"  # circular tree
    else:
        ts.mode = 'r'  # rectangular tree

    # Add title if provided
    if args.tree_title:
        # Adjust font size based on tree mode
        fsize = 50 if args.circular_tree else 30
        tree_title = TextFace(" " * 20 + args.tree_title, fsize=fsize)
        ts.title.add_face(tree_title, column=0)

    # Apply rotation for rectangular tree mode if specified
    if not args.circular_tree and args.rotate_tree:
        ts.rotation = 90

    # Adjust branch vertical margin for rectangular tree without rotation
    if not args.circular_tree and not args.rotate_tree:
        ts.branch_vertical_margin = 5

    # Set common properties
    ts.show_leaf_name = True
    ts.show_branch_length = True
    ts.show_scale = False  # Do not show the scale bar

    ts.show_leaf_name = True
    ts.show_branch_length = True
    ts.show_scale = False  # Do not show the scale bar
    ts.branch_vertical_margin = 5  # Adjust the vertical space between nodes

 
    # Save or show the tree
    # if args.save_png is None and args.save_svg is None:
    #     tree.show(tree_style=ts)
    # elif args.save_png:
    #     tree.render("mytree.png", tree_style=ts)
    # elif args.save_svg:
    #     tree.render("mytree.svg", tree_style=ts)
    # else:
    #     tree.show(tree_style=ts)
    tree.show(tree_style=ts)

if __name__ == '__main__':
    main()

