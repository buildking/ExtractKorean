import os
import re

totalFileCnt = 0
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
    f2 = open(csv_dir, 'a')
    nia = open(nia_dir, 'a')
    # fResult = open(result_dir, 'a')
    f2.write(f'{path}\n')
    nia.write(f'{path}\n')
    # fResult.write(f'{path}\n')
    lines = f.readlines()
    hangul = re.compile('[ㄱ-ㅣ가-힣]')
    notHangul = re.compile('[^ ㄱ-ㅣ가-힣|()+]')
    lineNo = 0
    for line in lines:
        lineNo = lineNo + 1
        afterStr = line.lstrip().rstrip().strip('\n')
        if afterStr.startswith('*'):continue
        if afterStr.startswith('//'):continue
        if afterStr.startswith('<!--'):continue
        if afterStr.startswith('/*'):continue
        if afterStr.startswith('/**'):continue

        slNo = afterStr.find('//')
        coreLine = afterStr[:slNo]
        result = hangul.search(coreLine)
        if result is not None:
            result2 = notHangul.sub('', coreLine).lstrip().rstrip()
            lineStr = afterStr.replace(',',' ').replace('•',' ').replace('₩','$')

            if afterStr.startswith('<%'):
                print(f'NIA {lineNo}: {lineStr} -> {result2} ')
                nia.write(f'{lineNo},{lineStr},{result2}\n')
                continue

            print(f'{lineNo}: {lineStr} -> {result2} ')
            f2.write(f'{lineNo},{lineStr},{result2}\n')
            # fResult.write(f'{lineNo}, {result2}\n')
            #todo 파일에 쓰기
    f.close()
    f2.close()
    # fResult.close()

if __name__ == "__main__":
    #root_dir = 'E:\\webproject-site\\NetisWeb_last\\netis\\src\\main\\webapp\WEB-INF'
    root_dir = 'D:\\hamon\\trunk\\netis\\src\\main\\webapp' #불러올 파일 경로
    csv_dir = 'C:/BACK/FilePile/korean.csv' #저장할 파일 경로
    nia_dir = 'C:/BACK/FilePile/nia.csv' #저장할 파일 경로
    # result_dir = 'C:/BACK/FilePile/result.csv'
    print_files_in_dir(root_dir, "")