import os
import re

totalFileCnt = 0
##파일 열기(<->닫기)
f2 = open('C:/BACK/FilePile/resultGo.csv', 'w')
# nia = open('C:/BACK/FilePile/fileList.csv', 'w')

def print_files_in_dir(root_dir, prefix):
    files = os.listdir(root_dir)
    exceptFileExt = ['.js', '.jsp', '.java', '.xml']
    global totalFileCnt
    for file in files:
        path = os.path.join(root_dir, file)
        fileName, fileExt = os.path.splitext(path)
        if os.path.isdir(path):
            print_files_in_dir(path, prefix + '\t')
        else:
            if fileExt in exceptFileExt:
                totalFileCnt = totalFileCnt+1
                #print(prefix + path)
                fileRead(path)


def fileRead(path):
    print(path)
    f = open(path, 'r', encoding="UTF-8")
    # fResult = open(result_dir, 'a')
    ##파일명 입력
    # f2.write(f'{path}\n')
    # nia.write(f'{path}\n')
    # fResult.write(f'{path}\n')
    try:
        lines = f.readlines()
    except:
        lines = ['error']
        print('!!에러 발생!!')
        collectError = open(colE_dir, 'a')
        collectError.write(f'{path}\n')
        collectError.close()

    lineNo = 0
    for line in lines:
        lineNo = lineNo + 1
        afterStr = line.lstrip().rstrip().strip('\n')
        if afterStr.startswith('*'):continue
        if afterStr.startswith('//'):continue
        if afterStr.startswith('<!--'):continue
        if afterStr.startswith('<%--'):continue
        if afterStr.startswith('/*'):continue
        if afterStr.startswith('/**'):continue

        ## 주석이 없으면, 문자열 그대로 반환
        slNo1 = afterStr.find('//')
        if slNo1 == -1:
            tempLine1 = afterStr
        else :
            tempLine1 = afterStr[:slNo1]
        slNo2 = tempLine1.find('/*')
        if slNo2 == -1:
            tempLine2 = tempLine1
        else :
           tempLine2 = tempLine1[:slNo2]
        slNo3 = tempLine2.find('<!-')
        if slNo3 == -1:
            coreLine = tempLine2
        else :
            coreLine = tempLine2[:slNo3]

        result = hangul.search(coreLine)
        if result is not None:
            lineStr = afterStr.replace(',','^').replace('•','@').replace('₩','$')
            result2 = notHangul.sub('', coreLine).lstrip().rstrip()
            pureKorean = result2.replace(' ','').replace('+','')

                # print(f'NIA {lineNo}: {lineStr} -> {result2} ')
                # nia.write(f'{lineNo},{lineStr},{result2}\n')

            ##결과 입력
            print(f'{lineNo}: {lineStr} -> {result2} << {coreLine}||{tempLine2}||{tempLine1}~{slNo1},{slNo2},{slNo3}')
            f2.write(f'{result2}, {pureKorean}, {lineStr}, {path}, {lineNo}\n')
            # f2.write(f'{lineNo},{lineStr},{result2}\n')
            # fResult.write(f'{lineNo}, {result2}\n')
            #todo 파일에 쓰기
    f.close()
    # fResult.close()

if __name__ == "__main__":
    #root_dir = 'E:\\webproject-site\\NetisWeb_last\\netis\\src\\main\\webapp\WEB-INF'
    # root_dir = 'C:\\hamon\\trunk' #불러올 파일 경로
    root_dir = 'C:\\hamon\\trunk\\netis\\src\\main\\webapp\\WEB-INF\\view' #불러올 파일 경로
    colE_dir = 'C:/BACK/FilePile/error.csv'
    # result_dir = 'C:/BACK/FilePile/result.csv'
    hangul = re.compile('[ㄱ-ㅣ가-힣]')
    notHangul = re.compile('[^ ㄱ-ㅣ가-힣 +]')

    ## 호중과장님Ver
    # hangul = re.compile('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*')
    # notHangul = re.compile('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*')

    print_files_in_dir(root_dir, "")

    ##파일 닫기(<->열기)
    f2.close()
    # nia.close()