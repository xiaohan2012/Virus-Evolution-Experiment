
#finer judger
def ATOM_as_binder(line):
    return line.split()[0].lower() == 'atom'

#coarser judger
def has_atom_or_hetatm(line):
    return line.split()[0].lower() in  ('atom','hetatm')

def split_complex(complex_path , binder_path , ligand_path , consider_criteria , binder_line_judger):
    with open(binder_path ,'w') as binder_f , open(ligand_path ,'w') as ligand_f, open(complex_path) as c_f:
        for line in c_f.readlines():
            if consider_criteria(line):
                if binder_line_judger(line):
                    binder_f.write(line[:60]+'\n')
                else:
                    ligand_f.write(line[:60]+'\n')

