import ConfigParser
import string
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def isDriveLetter(tmpString):
    #string.lowercase[1:26]
    #string.uppercase[1:26]
    if len(tmpString)>=3:
        c=tmpString[0].upper()
        if c>='A' and c<='Z' and tmpString[1]==':' and tmpString[2]==' ':
            return True
    return False

def fc():
    fileCompare('iphoneCompare.txt', 'resultFile.txt')
    
def fileCompare(src, dec):
    ## Open the file with read only permit
    srcFile = open(src)
    desFile = open (dec, 'w')
    
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read(os.path.join(BASE_DIR, 'src/cmc.futuredial.com.ini'))
    
    line = srcFile.readline()
    while line:
        #in this 'if' process data of a whole company
        if line.find("Checking:", 0, len(line))>=0: 
            #pc name
            textToWrite='\r\n'+line[10:]
            
            #company
            tmp=srcFile.readline()
            textToWrite=textToWrite+tmp[0:10]
            id=tmp[10:len(tmp)]
            id=id.replace('\r','')
            id=id.replace('\n','')
            
            try:
                companyName=config.get('CompanyID',id)
            except ConfigParser.NoOptionError, err:
                companyName=id
            textToWrite=textToWrite+companyName
            textToWrite=textToWrite+'\r\n'
            
            #server
            tmp=srcFile.readline()
            textToWrite=textToWrite+tmp
            
            #site
            tmp=srcFile.readline()
            textToWrite=textToWrite+tmp[0:7]
            id=tmp[7:len(tmp)]
            id=id.replace('\r','')
            id=id.replace('\n','')
    
            try:
                siteName=config.get('SiteID',id)
            except ConfigParser.NoOptionError, err:
                siteName=id
            textToWrite=textToWrite+siteName
            textToWrite=textToWrite+'\r\n'
            
            #solution
            tmp=srcFile.readline()
            textToWrite=textToWrite+tmp[0:11]
            id=tmp[11:len(tmp)]
            id=id.replace('\r','')
            id=id.replace('\n','')
            try:
                solutionName=config.get('SolutionID',id)
            except ConfigParser.NoOptionError, err:
                solutionName=id
    
            textToWrite=textToWrite+solutionName
            textToWrite=textToWrite+'\r\n'
    
            #product
            tmp=srcFile.readline()
            textToWrite=textToWrite+tmp[0:10]
            id=tmp[10:len(tmp)]
            id=id.replace('\r','')
            id=id.replace('\n','')
            try:
                ProductName=config.get('ProductID',id)
            except ConfigParser.NoOptionError, err:
                ProductName=id
    
            textToWrite=textToWrite+ProductName
            textToWrite=textToWrite+'\r\n'
    
            #FreeSpace, disk space, "file diff", Missingfiles        
            tmp=srcFile.readline()
            while tmp:
                if len(tmp)>1 and tmp.find('FreeSpace', 0, len(tmp))>=0:
                    needToWrite=False
                    textToWrite=textToWrite+tmp
                    tmp=srcFile.readline()
                    while tmp:#C:, D:, E:
                        if isDriveLetter(tmp):
                            pos=0
                            cOrd=False
                            noEnoughSpace=False
                            for s in tmp.split():#
                                pos=pos+1
                                if s.isdigit()==False:
                                    if s.find('C:', 0, len(s))>=0 or s.find('D:',0, len(s))>=0:
                                        cOrd=True
                                    for i in range(1,10-len(s)):
                                        s=s+' '
                                else:
                                    diskSpace=int(int(s)/(1073741824))
                                    if pos==2 and diskSpace<=25:
                                        noEnoughSpace=True
                                    s=str(diskSpace)+'G'
                                    for i in range(1,15-len(s)):
                                        s=s+' '
                                    
                                textToWrite=textToWrite+s
                            
                            if cOrd==True and noEnoughSpace==True:
                                needToWrite=True        
                            textToWrite=textToWrite+'\r\n'
                            tmp=srcFile.readline()
                        elif tmp.find('Checking:', 0, len(tmp))>=0:
                            line=tmp
                            break
                        else:
                            tmp=srcFile.readline()
                    if needToWrite==True:
                        desFile.write(textToWrite)
                    
                elif tmp.find("Checking:", 0, len(line))>=0:
                    line=tmp
                    break
                else:
                    tmp=srcFile.readline()
            line=tmp
        else:
            line=srcFile.readline()    
    srcFile.close()
    desFile.close()
    
