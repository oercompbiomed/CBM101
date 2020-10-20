# run with: python nb2sln.py <filename>

import sys, json, os, pathlib

if __name__ == "__main__":
    fn = str(sys.argv[1])

dic = json.load(open(fn, 'r', encoding='utf8'))

def is_code(cell):
    return cell['cell_type'] == 'code'

def is_solution_cell(content_list):
    kw = r"%load solutions"
    cont_str = "".join(content_list)
    return kw in cont_str

def write_py_file(fn, content):
    with open(fn, 'w', encoding='utf8') as f:
        f.write(content)
    print('wrote file ', fn)
        
def fix_fn(fn):
    ls = ['/', '\\', '.']
    for s in ls: fn = fn.replace(s,'')
    return fn


for cell in dic['cells']:
    if is_code(cell):
        content_list = cell['source'] 
        if is_solution_cell(content_list):
            out_fn = content_list[0].splitlines()[0].split('/')[-1]
            print("out_fn = ", out_fn)
            xpt = "".join(content_list[1:]) # append all but first line
            #print(xpt)
            
            dir_name = ".tmpdir_" + fix_fn(fn)
            if not pathlib.Path(dir_name).exists(): 
                os.mkdir(dir_name)
        
            write_py_file(dir_name+'/'+out_fn, xpt)