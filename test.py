from ete3 import Tree, TreeStyle, NodeStyle

# Example tree (replace with your tree file)
tree = Tree('/home/anna/viroids/phylogenetics/RAxML_bestTree.AllGenomes', format=1)

# Example mapping from leaf names to families
# In practice, replace this with your mapping
leaf_to_family = {

    'NC_003463.1_Apple_dimple_fruit_viroid': 'Pospiviroidae_Family',
    'NC_028132.1_Apple_hammerhead_viroid-like_circular_RNA': 'Avsunviroidae_Family',
    'NC_001340.1_Apple_scar_skin_viroid': 'Pospiviroidae_Family',
    'NC_003553.1_Australian_grapevine_viroid': 'Pospiviroidae_Family',
    'NC_001410.1_Avocado_sunblotch_viroid': 'Avsunviroidae_Family',
    'NC_003540.1_Chrysanthemum_chlorotic_mottle_viroid': 'Avsunviroidae_Family',
    'NC_002015.1_Chrysanthemum_stunt_viroid': 'Pospiviroidae_Family',
    'NC_003539.1_Citrus_viroid_IV_virus': 'Pospiviroidae_Family',
    'NC_001651.1_Citrus_bent_leaf_viroid': 'Pospiviroidae_Family',
    'NC_003264.1_Citrus_dwarfing_viroid': 'Pospiviroidae_Family',
    'NC_001464.1_Citrus_exocortis_viroid': 'Pospiviroidae_Family',
    'NC_010165.1_Citrus_viroid_V': 'Pospiviroidae_Family',
    'NC_004359.1_Citrus_viroid_VI': 'Pospiviroidae_Family',
    'NC_001462.1_Coconut_cadang-cadang_viroid': 'Pospiviroidae_Family',
    'NC_001471.1_Coconut_tinangaja_viroid': 'Pospiviroidae_Family',
    'NC_003681.1_Coleus_blumei_viroid_1': 'Pospiviroidae_Family',
    'NC_003682.1_Coleus_blumei_viroid_2': 'Pospiviroidae_Family',
    'NC_003683.1_Coleus_blumei_viroid_3': 'Pospiviroidae_Family',
    'NC_012127.1_Coleus_blumei_viroid_5': 'Pospiviroidae_Family',
    'NC_012805.1_Coleus_blumei_viroid_6': 'Pospiviroidae_Family',
    'NC_003882.1_Coleus_blumei_viroid': 'Pospiviroidae_Family',
    'NC_003538.1_Columnea_latent_viroid': 'Pospiviroidae_Family',
    'NC_020160.1_Dahlia_latent_viroid': 'Pospiviroidae_Family',
    'NC_039241.1_Eggplant_latent_viroid': 'Avsunviroidae_Family',
    'NC_028131.1_Grapevine_latent_viroid': 'Pospiviroidae_Family',
    'NC_001920.1_Grapevine_yellow_speckle_viroid_1': 'Pospiviroidae_Family',
    'NC_003612.1_Grapevine_yellow_speckle_viroid_2': 'Pospiviroidae_Family',
    'NC_003611.1_Hop_latent_viroid': 'Pospiviroidae_Family',
    'NC_001351.1_Hop_stunt_viroid': 'Pospiviroidae_Family',
    'NC_003613.1_Iresine_viroid_1': 'Pospiviroidae_Family',
    'NC_035620.1_Lychee_viroid-like_RNA_isolate_20160105': 'Pospiviroidae_Family',
    'NC_003637.1_Mexican_papita_viroid': 'Pospiviroidae_Family',
    'NC_003636.1_Peach_latent_mosaic_viroid': 'Avsunviroidae_Family',
    'NC_001830.1_Pear_blister_canker_viroid': 'Pospiviroidae_Family',
    'NC_011590.1_Pepper_chat_fruit_viroid': 'Pospiviroidae_Family',
    'NC_021720.1_Persimmon_viroid_2_genomic_RNA': 'Pospiviroidae_Family',
    'NC_010308.1_Persimmon_viroid': 'Pospiviroidae_Family',
    'NC_027432.1_Portulaca_latent_viroid_isolate_Vd21': 'Pospiviroidae_Family',
    'NC_002030.1_Potato_spindle_tuber_viroid': 'Pospiviroidae_Family',
    'NC_001553.1_Tomato_apical_stunt_viroid': 'Pospiviroidae_Family',
    'NC_000885.1_Tomato_chlorotic_dwarf_viroid': 'Pospiviroidae_Family',
    'NC_001558.1_Tomato_planta_macho_viroid': 'Pospiviroidae_Family',
}

# Define colors for each family
family_colors = {
    'Pospiviroidae_Family': 'LightPink',
    'Avsunviroidae_Family': 'LightCyan',
}

# Apply colors to nodes based on their family
for leaf in tree.iter_leaves():
    # Determine the family of the leaf
    family = leaf_to_family.get(leaf.name, None)
    if family:
        # Get the color for the family
        color = family_colors.get(family, 'gray')
        
        # Create and apply a style for the node
        nstyle = NodeStyle()
        nstyle["bgcolor"] = color
        leaf.set_style(nstyle)

# Define tree style
ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_support = True

# Show or save the tree
tree.show(tree_style=ts)
# tree.render('path_to_save_your_colored_tree.png', tree_style=ts)

