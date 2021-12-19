from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import easyocr
from PIL import Image
import os
from os import listdir
from subprocess import Popen, PIPE
from os.path import isfile, join
import sys
ImageFile.LOAD_TRUNCATED_IMAGES = True

job_count = 20
job_id = int(sys.argv[1])

read_id_index = int(open("workspace/current_job" + str(job_id), "r").read().strip())
target_id_index = int(open("workspace/current_job" + str(job_id), "r").read().strip()) * job_count + job_id

ids = open("ids.txt", "r").read().split(',')
target_id = ids[len(ids) - target_id_index - 1].strip()

os.environ["CURRENTID"] = target_id
os.putenv("CURRENTID", target_id)

process = Popen(['./hdownloader-bin', '-d', target_id])
process.wait()

if not os.path.isdir(target_id):
    open("workspace/current_job" + str(job_id), "w").write(str(read_id_index + 1))
    exit()

onlyfiles = [f for f in listdir(target_id) if isfile(join(target_id, f))]
onlyfiles = sorted(onlyfiles)

page_count = 0
outputs = target_id + "\n" + str(len(onlyfiles)) + "\n"

if len(onlyfiles) > 300:
    open("workspace/current_job" + str(job_id), "w").write(str(read_id_index + 1))
    exit()

for file in onlyfiles:
    fs = join (target_id, file)

    im = Image.open(fs).convert("RGB")
    im.save(fs + '.jpg', "jpeg")

    reader = easyocr.Reader(['ko'], gpu = False)
    result = reader.readtext(fs + '.jpg')
    
    page_count += 1
    outputs += str(result)
    outputs += "\n"
    
    print ("progress: " + str(page_count) + "/" + str(len(onlyfiles)))
    
if not os.path.exists('result'):
    os.makedirs('result')

f = open('result/' + target_id + ".txt", "w")
f.write(outputs)
f.close()
 
open("workspace/current_job" + str(job_id), "w").write(str(read_id_index + 1))
