import os 
import json
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source', default='./datasets/coco128/labels',type=str, help="input source directory")
arg = parser.parse_args()
keep_clz = {
    15: 0,
    16: 1
}
count = 0
dir = os.path.join(arg.source, 'train2017')
new_dir = os.path.join(arg.source, 'train2018')
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    
for filename in os.listdir(dir):
    keep_lines = []
    with open(os.path.join(dir, filename)) as fr:
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
    with open(os.path.join(new_dir, filename), 'w') as fw:
        fw.writelines(keep_lines)
