
def get_pdb_ids(pmid):
    search_dict = pypdb.make_query(pmid)
    hits = pypdb.do_search(search_dict)
    return hits

# sometimes we get multiple hits (or none!). For now, we are only concerned with the first one.

def get_ligands(pdb_id):
    ligs = pypdb.get_ligands(pdb_id)
    return [lig['@chemicalID'] for lig in ligs['ligandInfo']['ligand']]

def whole_pipeline(pmid):
    hits = get_pdb_ids(pmid)
    if len(hits)<1: return []
    try: ligands = get_ligands(hits[0])
    except: return []
    print(ligands, '\n')
    return ligands


# explanation: 
# the try and except blocks lets you first attempt (try) to execute some code.
# if that code throws an error, we will jump to the code in the except block.
# if no error occurs, it will simply execute, and ignore the except block, continuing as usual.