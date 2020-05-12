'''
Function which takes as first argument the directory with compressed
and unordered data files and as second argument the out directory
Example
$python extract_data.py ./DATA_for_projects ./data_extracted

Version: 12-05-20
Author: Leonardo Salicari
'''
import os
import sys
import shutil
import gzip


src_dir = sys.argv[1] # directory with compressed data
out_dir = sys.argv[2] # output directory

# Collecting all files
files = os.listdir(src_dir)
files.sort()

# printing all files found
print(f'\n################ All files found in {src_dir} #################\n')
for f in files:
    print(f)

# Selecting already uncompressed data
filtered = [f for f in files if (f.endswith('.dat') or f.endswith('.dat.ent'))]
# removing already uncompressed files
for f in filtered:
    files.remove(f)
# removing non essential files
files.remove('status_list10000polyg_N400_be0.400_3d_ooo.dat.gz')

# Selecting files to uncompress, note choise in file
gz_files = [f for f in files if (f.endswith('ooo.dat.gz') or f.endswith('hhh.dat.ent.gz'))]
# All seq after 46 (included) aren't classified, hence they have to be removed
seq_to_remove = ['46','47','48','49','50','51','52']
for seq in seq_to_remove:
    str0 = 'list10000polyg_N400_seq00' + seq + '_be0.400_3d_ooo.dat.gz'
    gz_files.remove(str0)

print(f'\n#################### Files to be uncompressed and copied in {out_dir} ###################\n')
for g in gz_files:
    print(g)

# Uncompressing and copying in new dir
for g in gz_files:

    path_file_in = src_dir + '/' + g
    path_file_out = out_dir + '/' + g[:-3]

    with gzip.open(path_file_in, 'rb') as f_in:
        with open(path_file_out, 'wb') as f_out: # output file has the same name without '.gz'

            shutil.copyfileobj(f_in, f_out) # copying
