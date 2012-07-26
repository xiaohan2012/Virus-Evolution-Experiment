__author__ = 'xiaohan'
from schrodinger import structure
from complex_splitter import ATOM_as_binder,split_complex,has_atom_or_hetatm

import os
import glob

from fp_gen1 import gen_fp
from avg_sift import gen_avg_sift


def prepare_dirs(dirs = []):
    for d_ in dirs:
        if not os.path.exists(d_):
            os.mkdir(d_)

def load_structure(path):
    return structure.StructureReader(path).next()

if __name__ == "__main__":
    #define data path
    data_root_fp = "2012-7-26"
    pdb_fp = "%s/pdb" %data_root_fp
    fp_fp = "%s/fp" %data_root_fp
    avg_sift_fp = "%s/avg_sift" %data_root_fp
    ligand_fp = "%s/ligand" %data_root_fp
    binder_fp= "%s/binder" %data_root_fp
    
    #create them
    prepare_dirs([fp_fp  , avg_sift_fp , ligand_fp , binder_fp])
    
    #calculation start
    for complex_fp in glob.glob(os.path.join(pdb_fp,'*')):
        name_with_pdb = os.path.split(complex_fp)[-1]
        complex_id = os.path.split(complex_fp)[-1].split('.')[0]
    
        #init paths
        cur_binder_fp = os.path.join(binder_fp , name_with_pdb)
        cur_ligand_fp = os.path.join(ligand_fp , name_with_pdb)
        cur_avg_sift_fp = os.path.join(avg_sift_fp , "%s.sift" %complex_id)
        cur_fp_fp = os.path.join(fp_fp , "%s.fp" %complex_id)
    
        #split complex into ligand and binder
        split_complex(complex_fp , cur_binder_fp , cur_ligand_fp , has_atom_or_hetatm, ATOM_as_binder)

        
        antibody , antigen = load_structure(cur_binder_fp) , load_structure(cur_ligand_fp)
        
        #generate finger print
        fp_gen_path = gen_fp(receptor=antibody,binder = antigen,fp_path= cur_fp_fp)#get the finger print

        #generate sift
        gen_avg_sift(cur_fp_fp,cur_avg_sift_fp)#generate average sift
