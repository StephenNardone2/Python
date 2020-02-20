import zipfile
import optparse
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
            ''' filecmp.cmp(f1, f2[, shallow] need an if statment to compare
                the files extracted with the files in the zip
            '''
            print '[+] Found password: ' + password + '\n'
    except:
        pass

def main():
    parser = optparse.OptionParser("usage%prog "+"-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='secify zip file')
    parser.add_option('-d', dest='dname', type='string', help='secify dictionary file')
    (options, args) = parser.parse_args()
    if(options.zname == None) | (options.dname == None):
        print parser.print_usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == "__main__":
    main()