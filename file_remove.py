import os

try:
   folder_path = input('Enter file dir where you want to delete a files:\n')

   for root , dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pdf'):
               os.remove(os.path.join(root, file))
            else:
                continue
    
except:
    print('Ops something has went wrong.')




            




