import os
import shutil
import re

## current pathpy
path = os.getcwd()
print(path)
##number of files

number_of_f = len(list(filter(os.path.isfile, os.listdir(path))))
print('CWD: ' + str(path) + '\n # vids:' + str(number_of_f))

#gets file names
filenames = os.listdir(path)
included_extensions = ['mpg','mp4', 'avi', 'mov', 'mp5']
file_name = [fn for fn in os.listdir(path)
              if any(fn.endswith(ext) for ext in included_extensions)]

#files = ' '.join(file_name)

#print(file_name)
#print(type(file_name))
#print(type(filenames))


for i in file_name:
    newstr =  re.sub('[^a-zA-Z0-9 \n\.]', '', i) 
    
    # cfilename = re.sub('[^A-Za-z0-9.]','', str(file_name) )## changes files names to normal char
   
#    print(type(cfilename))
#    print(cfilename)
 #   print(type(newstr))
 #   print(newstr)    
    
    loc= os.path.abspath(i)
   
    #print(type(loc))
    #print(loc)    
    new=newstr.replace(" ", "_")  # removes all spaces

    os.rename(loc, new)

  
                                  ## all strange shit to space
                                
#print(cfilename)


#dir = 'modelname'

#for file in  os.walk('./'):
#included_extensions = ['mpg','mp4', 'avi', 'mov', 'mp5']
nfilename = [fn for fn in os.listdir(path)
              if any(fn.endswith(ext) for ext in included_extensions)]


for file in nfilename:
    
    dir_name = file[:-4]
    clean = re.sub('[^A-Za-z0-9 ]+', '', dir_name)
   # print(f'dir_name: {clean}')
    # get all but the last 8 characters to remove
    # the index number and extension
  
     
#    dir_path = path + clean
    dir_path = os.path.join(path, clean,)
    dir_path2 = os.path.join(path, clean,)+'/source'
    print(dir_path2)
 #   print(f'dir_path: {dir_path}')
    
     # check if directory exists or not yet

    if not os.path.exists(dir_path):
         os.makedirs(dir_path)
         os.makedirs(dir_path2)

    if os.path.exists(dir_path):
        file_path = path  + file
#        print(f'file_path: {file_path}')
        
        # move files into created directory

    source = file
    destination = os.path.abspath(dir_path2)

    shutil.move(source, destination)

