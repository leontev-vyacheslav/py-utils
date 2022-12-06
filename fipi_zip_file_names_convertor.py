from os import makedirs, path, walk
from zipfile import ZipFile
from shutil import copy2, rmtree

zip_name = 'Informatika'

root_dir = f'c:\\Temp\\{zip_name}'


def encode_path(root, name):
  return path.join(root, name) \
      .encode('IBM437') \
      .decode('IBM866') \
      .replace(zip_name, f'{zip_name}_encoded')


def unzip_prepare():

  try:
    rmtree(root_dir)
  except FileNotFoundError:
      pass

  try:
    rmtree(root_dir.replace(zip_name, f'{zip_name}_encoded'))
  except FileNotFoundError:
      pass

  with ZipFile(f'{root_dir}.zip', 'r') as zip_file:
    zip_file.extractall(root_dir)

def rename_items():
  for root, dirs, files in walk(root_dir):
    for name in dirs:
        makedirs(encode_path(root, name))

  for root, dirs, files in walk(root_dir):
    for name in files:
        copy2(path.join(root, name), encode_path(root, name))


def convert():
  unzip_prepare()
  rename_items()
