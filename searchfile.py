import glob

files = glob.glob('D:/BSUIR/4_course/TVOP/lab1/*.py')

f = open('extensions.txt', 'w+')
for i in range(len(files)):
    f.write(files[i].replace('\\', '/') + '\n')
