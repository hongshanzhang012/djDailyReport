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
    '''
    PC Name=[AU-BC-BOH-D141_F4CE46106110]
    companyid=Brightstar Australia
    adminconsoleserver=http://cmc.futuredial.com/
    siteid=Australia_Sydney
    solutionid=allinone
    productid=greent
    Caption  FreeSpace     Size          
    C:       20G           232G          
    D:       
    '''
    desFile.write('"PC Name","Company", "Site", "Solution", "Product", "availableCSpace (G)","totalCSpace (G)", "availableDSpace (G)", "totalDSpace (G)" \r\n')
    while line:
        #in this 'if' process data of a whole company
        if line.find("Checking:", 0, len(line))>=0: 
            #pc name
            textToWrite='"'+line[19:len(line)-2]+'",'
            
            #company
            tmp=srcFile.readline()
            id=tmp[10:len(tmp)]
            id=id.replace('\r','')
            id=id.replace('\n','')
            
            try:
                companyName=config.get('CompanyID',id)
            except ConfigParser.NoOptionError, err:
                companyName=id
            textToWrite=textToWrite+'"'+companyName
            textToWrite=textToWrite+'",'
            
            #server
            tmp=srcFile.readline()
            #textToWrite=textToWrite+tmp
            
            #site
            tmp=srcFile.readline()
            id=tmp[7:len(tmp)]
            id=id.replace('\r','')
            id=id.replace('\n','')
    
            try:
                siteName=config.get('SiteID',id)
            except ConfigParser.NoOptionError, err:
                siteName=id
            textToWrite=textToWrite+'"'+siteName
            textToWrite=textToWrite+'",'
            
            #solution
            tmp=srcFile.readline()
            id=tmp[11:len(tmp)]
            id=id.replace('\r','')
            id=id.replace('\n','')
            try:
                solutionName=config.get('SolutionID',id)
            except ConfigParser.NoOptionError, err:
                solutionName=id
    
            textToWrite=textToWrite+'"'+solutionName
            textToWrite=textToWrite+'",'
    
            #product
            tmp=srcFile.readline()
            id=tmp[10:len(tmp)]
            id=id.replace('\r','')
            id=id.replace('\n','')
            try:
                ProductName=config.get('ProductID',id)
            except ConfigParser.NoOptionError, err:
                ProductName=id
    
            textToWrite=textToWrite+'"'+ProductName
            textToWrite=textToWrite+'",'
    
            #FreeSpace, disk space, "file diff", Missingfiles        
            tmp=srcFile.readline()
            while tmp:
                if len(tmp)>1 and tmp.find('FreeSpace', 0, len(tmp))>=0:
                    tmp=srcFile.readline()
                    whichDrive=""
                    availableCSpace=""
                    totalCSpace=""
                    availableDSpace=""
                    totalDSpace=""
                    while tmp:#C:, D:, E:
                        if isDriveLetter(tmp):
                            pos=0
                            
                            for s in tmp.split():#
                                pos=pos+1
                                if s.isdigit()==False:
                                    whichDrive=s[0:1]
                                else:
                                    diskSpace=int(int(s)/(1073741824))
                                    if pos==2 and whichDrive=='C':
                                        availableCSpace=str(diskSpace)
                                    elif pos==2 and whichDrive=='D':
                                        availableDSpace=str(diskSpace)
                                    if pos==3 and whichDrive=='C':
                                        totalCSpace=str(diskSpace)
                                    elif pos==3 and whichDrive=='D':
                                        totalDSpace=str(diskSpace)
                            tmp=srcFile.readline()
                        elif tmp.find('Checking:', 0, len(tmp))>=0:
                            line=tmp
                            break
                        else:
                            tmp=srcFile.readline()
                    textToWrite=textToWrite+'"'+availableCSpace+'",'+'"'+totalCSpace+'",'+'"'+availableDSpace+'",'+'"'+totalCSpace+'",'                            
                    textToWrite=textToWrite+'\r\n'
                    if (availableCSpace!="" and int(availableCSpace)<=25) or  (availableDSpace!="" and int(availableDSpace)<=25) :
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
    
