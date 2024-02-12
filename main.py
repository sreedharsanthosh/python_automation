from shutil import move
import os
import getpass
import time
import sched

scheduler = sched.scheduler(time.time,time.sleep)

user = getpass.getuser()

root_dir = 'C:/Users/{}/Downloads'.format(user)

pic_folder = "C:/Users/{}/Downloads/Pictures".format(user)
doc_folder = "C:/Users/{}/Downloads/Docs".format(user)
software_folder = "C:/Users/{}/Downloads/Software".format(user)
others_folder = "C:/Users/{}/Downloads/Others".format(user)

doc_types = ('.doc','.docx','.zip','.pdf','.pptx','.txt')
img_types = ('.jpg','.jpeg','.svg','.png','.webp','.gif')
software_types = ('.exe','.rar')

def get_non_hidden_files_except_current_file(root_dir):
#   return [f for f in os.listdir(root_dir) if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__)]
    files = []
    for f in os.listdir(root_dir):
        if os.path.isfile(os.path.join(root_dir,f)) and not f.__eq__(__file__):
            files.append(f)
    return files


def move_files(files):
    for file in files:
        file_path = os.path.join(root_dir,file)
        if file.endswith(img_types):
            move(file_path, '{}/{}'.format(pic_folder,file))
            print('file {} moved to {}'.format(file, pic_folder))
        elif file.endswith(doc_types):
            move(file_path, '{}/{}'.format(doc_folder,file))
            print('file {} moved to {}'.format(file, doc_folder))
        elif file.endswith(software_types):
            move(file_path, '{}/{}'.format(software_folder,file))
            print('file {} moved to {}'.format(file, software_folder)) 
        else:
            move(file_path,'{}/{}'.format(others_folder,file))
            print('file {} moved to {}'.format(file,others_folder))

def call_funs():
    files = get_non_hidden_files_except_current_file(root_dir)
    move_files(files)


def repeat_task():
    scheduler.enter(5,1,call_funs,())
    scheduler.enter(5,1,repeat_task,())

repeat_task()
scheduler.run()
