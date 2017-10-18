# File: readline-example-1.py

txtpath='Labels/004/'
kittipath='Labels/004_kitti/'
vocpath='Labels/004_voc/'
vocname='parking'
allFile='Labels/count004.txt'
count = 0
allCount = 0

fileAll=open(allFile,'r')
while 1:
    allCount = allCount + 1
    fileOne = fileAll.readline()
    txtname = fileOne.strip('\n')
    #txtname='20170831164118_121.txt'
    file = open(txtpath+txtname,'r')
    isNothing=0
    voctxt=[]
    kittitxt=[]
    while 1:
        line = file.readline()
        if not line:
            break #    print 1 # do something"")
        list2 = line.split(' ')
        #    print list2[0]
        if list2[0]=='0\n':
            print "nothing"
            isNothing=1
            break
        elif list2[0]=='empty':
            kittitxt.append(list2[0]+' 0.00 0 -0.20 '+list2[1]+' '+list2[2]+' '+list2[3]+' '+list2[4])
            voctxt.append(vocname+' '+list2[1]+' '+list2[2]+' '+list2[3]+' '+list2[4])
        elif list2[0]=='obstracle':
            kittitxt.append(list2[0]+' 0.00 0 -0.20 '+list2[1]+' '+list2[2]+' '+list2[3]+' '+list2[4])
            voctxt.append(list2[0]+' '+list2[1]+' '+list2[2]+' '+list2[3]+' '+list2[4])
    if isNothing==0:
        count = count+1
        fokitti = open(kittipath+txtname,"w")
        fokitti.writelines(kittitxt)
        fokitti.close()
        fovoc = open(vocpath+txtname,"w")
        fovoc.writelines(voctxt)
        fovoc.close()
        print "good:",count,": ",fileOne,"all:",allCount
print "all:",allCount
