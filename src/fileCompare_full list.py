import ConfigParser

## Open the file with read only permit
srcFile = open('iphoneCompare.txt')
desFile = open ('resultFile.txt', 'w')

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read('cmc.futuredial.com.ini')

line = srcFile.readline()
while line:
    if line.find("Checking:", 0, len(line)-1)>=0:
        #pc name
        desFile.write('\n'+line[10:])
        
        #company
        tmp=srcFile.readline()
        desFile.write(tmp[0:10])
        id=tmp[10:len(tmp)]
        id=id.replace('\r','')
        id=id.replace('\n','')
        
        try:
            companyName=config.get('CompanyID',id)
        except ConfigParser.NoOptionError, err:
            companyName=id
        desFile.write(companyName)
        desFile.write('\n')
        
        #server
        tmp=srcFile.readline()
        desFile.write(tmp)
        
        #site
        tmp=srcFile.readline()
        desFile.write(tmp[0:7])
        id=tmp[7:len(tmp)]
        id=id.replace('\r','')
        id=id.replace('\n','')

        try:
            siteName=config.get('SiteID',id)
        except ConfigParser.NoOptionError, err:
            siteName=id
        desFile.write(siteName)
        desFile.write('\n')
        
        #solution
        tmp=srcFile.readline()
        desFile.write(tmp[0:11])
        id=tmp[11:len(tmp)]
        id=id.replace('\r','')
        id=id.replace('\n','')
        try:
            solutionName=config.get('SolutionID',id)
        except ConfigParser.NoOptionError, err:
            solutionName=id

        desFile.write(solutionName)
        desFile.write('\n')

        #product
        tmp=srcFile.readline()
        desFile.write(tmp[0:10])
        id=tmp[10:len(tmp)]
        id=id.replace('\r','')
        id=id.replace('\n','')
        try:
            ProductName=config.get('ProductID',id)
        except ConfigParser.NoOptionError, err:
            ProductName=id

        desFile.write(ProductName)
        desFile.write('\n')

        #disk space title        
        #disk space and other info until "file diff"        
        tmp=srcFile.readline()
        if len(tmp)>1 and tmp.find('FreeSpace', 0, len(tmp)-1)>=0:
            desFile.write(tmp)
            tmp=srcFile.readline()
            while tmp:
                if len(tmp)>1 and tmp.find('file diff:', 0, len(tmp)-1)<0 and tmp.find('Missing',0, len(tmp))<0:
                    for s in tmp.split():
                        if s.isdigit()==False:
                            for i in range(1,10-len(s)):
                                s=s+' '
                        else:
                            s=str(int(int(s)/(1073741824)))+'G'
                            for i in range(1,15-len(s)):
                                s=s+' '
                            
                        desFile.write(s)
                            
                    desFile.write('\n')
                    tmp=srcFile.readline()
                elif tmp.find('file diff:', 0, len(tmp)-1)>=0 or tmp.find('Missing',0, len(tmp))>=0:
                    line=tmp
                    break
        else:
            line=tmp
    else:
        line=srcFile.readline()    
srcFile.close()
desFile.close()

