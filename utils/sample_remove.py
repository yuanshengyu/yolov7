import os 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source', default='coco/labels',type=str, help="input source directory")
arg = parser.parse_args()
keep_clz = {
    15: 0,
    16: 1
}
count = 0
dir_train = os.path.join(arg.source, 'train2017')
dir_train_new = os.path.join(arg.source, 'train2018')
dir_val = os.path.join(arg.source, 'train2017')
dir_val_new = os.path.join(arg.source, 'train2018')
if not os.path.exists(dir_train_new):
    os.mkdir(dir_train_new)
if not os.path.exists(dir_val_new):
    os.mkdir(dir_val_new)
    
for filename in os.listdir(dir_train):
    keep_lines = []
    with open(os.path.join(dir_train, filename)) as fr:
        lines = fr.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5:
                continue
            clz = int(parts[0])
            if clz in keep_clz:
                keep_lines.append(f'{keep_clz[clz]} {parts[1]} {parts[2]} {parts[3]} {parts[4]}')
    if len(keep_lines) == 0:
        continue
    with open(os.path.join(dir_train_new, filename), 'w') as fw:
        fw.writelines(keep_lines)
        
for filename in os.listdir(dir_val):
    keep_lines = []
    with open(os.path.join(dir_val, filename)) as fr:
        lines = fr.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5:
                continue
            clz = int(parts[0])
            if clz in keep_clz:
                keep_lines.append(f'{keep_clz[clz]} {parts[1]} {parts[2]} {parts[3]} {parts[4]}')
    if len(keep_lines) == 0:
        continue
    with open(os.path.join(dir_val_new, filename), 'w') as fw:
        fw.writelines(keep_lines)

