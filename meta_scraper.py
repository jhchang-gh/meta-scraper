import glob, os, codecs


path="/ENTER-FILEPATH-HERE"
os.chdir(path)
wf = open ('meta_output.txt','w')
for file in glob.glob("*.htm"):
    print(file)
    f = codecs.open(path+file, 'r')
    wf.write(file+'\n')
    for line in f:
        
        if '<title' in line:
            wf.write(line)
        elif '<meta name="description"' in line:
            wf.write(line)
            break;

    wf.write('\n')
    f.close()
for file in glob.glob("*.html"):
    print(file)
    f = codecs.open(path+file, 'r')
    wf.write(file+'\n')
    for line in f:
        
        if '<title' in line:
            wf.write(line)
        elif '<meta name="description"' in line:
            wf.write(line)
            break;

    wf.write('\n')
    f.close()    
wf.close()
