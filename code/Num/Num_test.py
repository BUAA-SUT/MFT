import random
from Num import *
from publicFun import *
import json
import sys
import string


def random_number(num2):
    list2 = []
    for number in range(num2):
        str2 = str(random.randint(1, 9))
        list2.append(str2)
    b = " ".join(list2).replace(" ", "")
    return b


def random_number2(num2):
    list2 = []
    for number in range(num2):
        str2 = str(random.randint(1, 7))
        list2.append(str2)
    b = " ".join(list2).replace(" ", "")
    return b


def copyFile(fileDir, tarDir, picknumber):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    for i in range(len(sample)):
            shutil.copy(fileDir + sample[i], tarDir + "input{}.txt".format(i))
    return


def getOriginalInput():
    source_case_set = []
    while 1:
        a = random.randint(0, 2)  # 0--生成16进制，1--十进制，2--八进制
        # 判断末尾标识符
        typeb = ['f', 'F', 'd', 'D', 'l', 'L']
        typeb1 = ['f', 'F', 'd', 'D']
        if a == 0:
            # 生成十六进制
            typea = ["0x", "0X", "-0x", "-0X", "#", "-#"]

            a2 = random.randint(0, 2)  # 0--大于16位，1--8位-16位，2--小于8位
            if a2 == 0:
                a11 = random.choice(typeb1)
                s1 = random.randint(17, 20)
                num = random_number(s1)
                num = random.choice(typea)+num
                a5 = random.randint(0, 1)
                if a5 == 0:
                    pass
                else:
                    num = num + a11
                source_case_set.append(num)
            elif a2 == 1:
                a12 = random.choice(typeb1)
                s1 = random.randint(10, 13)
                num = random_number(s1)
                num = random.choice(typea)+num
                a5 = random.randint(0, 1)
                if a5 == 0:
                    pass
                else:
                    num = num + a12
                source_case_set.append(num)
            else:
                a13 = random.choice(typeb1)
                s1 = random.randint(1, 6)
                num = random_number(s1)
                num = random.choice(typea)+num
                a5 = random.randint(0, 1)
                if a5 == 0:
                    pass
                else:
                    num = num + a13
                source_case_set.append(num)
        elif a == 1:
            # 生成十进制
            # 是否有点，是否有e/E
            a1 = random.choice(typeb)
            a2 = random.randint(0, 2)  # 0--大于16位，1--8位-16位，2--小于8位
            a3 = random.randint(0, 1)  # 0--有点，1--没点
            a4 = random.randint(0, 1)  # 0--有e，1--没e
            if a2 == 0:
                s1 = random.randint(17, 20)
                num = random_number(s1)
                # if a3 == 0:
                #     index = random.randint(1, len(num)-2)
                #     split_strings = list(num)
                #     split_strings.insert(index, '.')
                #     num = ''.join(split_strings)
                # else:
                #     pass
                # if a4 == 0:
                #     if num[-2] == '.':
                #         pass
                #     else:
                #         index = -1
                #         split_strings = list(num)
                #         split_strings.insert(index, 'e')
                #         num = ''.join(split_strings)
                # else:
                #     pass
                source_case_set.append(num)
            elif a2 == 1:
                s1 = random.randint(10, 13)
                num = random_number(s1)
                # if a3 == 0:
                #     index = random.randint(1, len(num)-2)
                #     split_strings = list(num)
                #     split_strings.insert(index, '.')
                #     num = ''.join(split_strings)
                # else:
                #     pass
                # if a4 == 0:
                #     if num[-2] == '.':
                #         pass
                #     else:
                #         index = -1
                #         split_strings = list(num)
                #         split_strings.insert(index, 'e')
                #         num = ''.join(split_strings)
                # else:
                #     pass
                source_case_set.append(num)
            else:
                s1 = random.randint(1, 6)
                num = random_number(s1)
                # if a3 == 0:
                #     if len(num) < 3:
                #         pass
                #     else:
                #         index = random.randint(1, len(num)-2)
                #         split_strings = list(num)
                #         split_strings.insert(index, '.')
                #         num = ''.join(split_strings)
                # else:
                #     pass
                # if a4 == 0:
                #     if len(num) < 3:
                #         pass
                #     else:
                #         if num[-2] == '.':
                #             pass
                #         else:
                #             index = -1
                #             split_strings = list(num)
                #             split_strings.insert(index, 'e')
                #             num = ''.join(split_strings)
                # else:
                #     pass
                source_case_set.append(num)

        else:

            a2 = random.randint(0, 2)  # 0--大于16位，1--8位-16位，2--小于8位
            if a2 == 0:
                a11 = random.choice(typeb)
                s1 = random.randint(17, 20)
                num = random_number2(s1)
                num = '0'+num
                a5 = random.randint(0, 1)
                if a5 == 0:
                    pass
                else:
                    num = num + a11
                source_case_set.append(num)
            elif a2 == 1:
                a12 = random.choice(typeb)
                s1 = random.randint(10, 13)
                num = random_number2(s1)
                num = '0'+num
                a5 = random.randint(0, 1)
                if a5 == 0:
                    pass
                else:
                    num = num + a12
                source_case_set.append(num)
            else:
                a13 = random.choice(typeb)
                s1 = random.randint(1, 6)
                num = random_number2(s1)
                num = '0'+num
                a5 = random.randint(0, 1)
                if a5 == 0:
                    pass
                else:
                    num = num + a13
                source_case_set.append(num)

        if len(source_case_set) >= 1000:
            break

    tarDir1 = '/Applications/work/data/MT/MFT/'+string+'/input/'  # 移动到新的文件夹路径
    fileDir2 = '/Applications/work/data/MT/MFT/'+string+'/input/'  # 源文件夹路径
    tarDir2 = '/Applications/work/data/MT/MFT/'+string+'/RandomInput/'  # 移动到新的文件夹路径
    shutil.rmtree(tarDir1)
    os.mkdir(tarDir1)
    for i in range(len(source_case_set)):
        with open(tarDir1 + "input{}.txt".format(i), "w") as f:
            f.writelines(source_case_set[i])
    shutil.rmtree(tarDir2)
    os.mkdir(tarDir2)
    copyFile(fileDir2, tarDir2, 100)

    # # 随机取100个测试用例
    # random_input = random.sample(source_case_set, 100)
    # data = {
    #         'source_case_set': source_case_set,
    #         'random_input': random_input
    # }
    # json_str = json.dumps(data)
    # with open('/Applications/work/data/MT/MFT/'+string+'/OriginalInput.json', 'w') as f:
    #     json.dump(json_str, f)
    #
    # return source_case_set, random_input


def FailureRate(dynamic):
    # 把SourceCases读出来
    Result = []
    for i in range(1000):
        file_a = open('/Applications/work/data/MT/MFT/'+string+'/output/output{}_{}.txt'.format(0, i), 'r')
        file_m = open('/Applications/work/data/MT/MFT/'+string+'/output/output{}_{}.txt'.format(mu, i), 'r')
        result_s_a = file_a.readlines()[0]
        result_s_m = file_m.readlines()[0]
        if result_s_a == result_s_m:
            Result.append(0)
        else:
            Result.append(1)
    FR = round(Result.count(1) / len(Result) * 100, 2)
    return FR


def getTestcase(mr_list, test_case, num_of_samples):
    # for i in range(num_of_samples):
    #     test_case.setInputOutput("infile_{}".format(i), "outfile_{}".format(i), "outtree_{}".format(i))
    #     test_case.generateRandomTestcase()
    # for i in range(num_of_samples):
    #     for j in range(len(mr_list)):
    #         mr = mr_list[j]
    #         mr.setTestCase(test_case)
    #         mr.original_ts.setInputOutput("input{}.fa".format(i), "reference{}.fa".format(i), "e{}.fa".format(i), "output{}.txt".format(i))
    #         mr.getFollowInput(j)
    for i in range(num_of_samples):
        # test_case.setInputOutput("input{}.txt".format(i), "output{}.txt".format(i))
        # test_case.generateInput()  # 生成原始测试用例
        for j in range(len(mr_list)):
            mr = mr_list[j]
            mr.setTestCase(test_case)
            mr.original_ts.setInputOutput("input{}.txt".format(i), "output0_{}.txt".format(i))
            mr.getFollowInput(j)
            for k in range(len(mr_list)):
                mr = mr_list[k]
                mr.setTestCase(test_case)
                mr.original_ts.setInputOutput("input{}_{}.txt".format(i, j), "output0_{}_{}.txt".format(i, j))
                mr.getFollowInput(k)


def getMG(mu, ts, num_of_samples, mr_list, PFS):
    MGS = []
    SMGS = []
    for i in range(42, num_of_samples):
        MGs = []
        MG = [0] * len(mr_list)
        ts.setInputOutput("input{}.txt".format(i), "output{}_{}.txt".format(mu, i))
        original_output = getResults(ts)
        followup_ts = ts
        for j in range(len(mr_list)):
            followup_ts.setInputOutput("input{}_{}.txt".format(i, j), "output{}_{}_{}.txt".format(mu, i, j))
            mr = mr_list[j]
            followup_output = mr.getResults(followup_ts)
            expected_output = mr.getExpectedOutput(original_output)
            isViolate = mr.assertViolation(expected_output, followup_output)
            if isViolate:
                MG[j] = 1
        MGs.append(MG)
        for m in range(len(mr_list)):
            MG = [0] * len(mr_list)
            ts.setInputOutput("input{}_{}.txt".format(i, m), "output{}_{}_{}.txt".format(mu, i, m))
            original_output = getResults(ts)
            followup_ts = ts
            for n in range(len(mr_list)):
                followup_ts.setInputOutput("input{}_{}_{}.txt".format(i, m, n), "output{}_{}_{}_{}.txt".format(mu, i, m, n))
                mr = mr_list[n]
                followup_output = mr.getResults(followup_ts)
                expected_output = mr.getExpectedOutput(original_output)
                isViolate = mr.assertViolation(expected_output, followup_output)
                if isViolate:
                    MG[n] = 1
            MGs.append(MG)
        # 去掉巧合满足性
        for i1 in range(len(MGs)):
            for j1 in range(len(MGs[i1])):
                if MGs[i1][j1] == 0 and (PFS[i][i1] or PFS[i][i1 * len(MGs[0]) + j1 + 1]):  # 如果satisfied
                    MGs[i1][j1] = 3

        SMGs = copy.deepcopy(MGs)
        # 随机去除一些MG
        for i2 in range(1, len(MGs)):  # 第一组不变
            t = random.randint(1, len(MGs[i2]) - 1)  # 去几个
            a = [n for n in range(len(MGs[i2]))]
            random.shuffle(a)
            b = a[:t]
            for j2 in b:
                MGs[i2][j2] = 4

        MGS.append(MGs)
        SMGS.append(SMGs)

    return MGS, SMGS


def change(output):
    if '.' in output.lines[0] or 'e' in output.lines[0] or 'E' in output.lines[0]:
        num1 = float(output.lines[0])
        st = str(num1)
        if 'e' in st or 'E' in st:
            num1 = int(num1)
    else:
        num1 = int(output.lines[0])
    return num1


def getpf(mu, ts, num_of_samples, mr_list):
    pf = []
    Output = []
    for i in range(num_of_samples):
        output = []
        result = [0] * (len(mr_list) * (len(mr_list) + 1) + 1)
        ts.setInputOutput("input{}.txt".format(i), "output{}_{}.txt".format(0, i))
        original_output = getResults(ts)
        program_ts = ts
        program_ts.setInputOutput("input{}.txt".format(i), "output{}_{}.txt".format(mu, i))
        program_output = getResults(program_ts)
        isViolate = MR().assertViolation(original_output, program_output)
        output.append(change(original_output))
        output.append(change(program_output))
        if isViolate:
            result[0] = 1

        for j in range(len(mr_list)):
            ts.setInputOutput("input{}_{}.txt".format(i, j), "output{}_{}_{}.txt".format(0, i, j))
            original_output = getResults(ts)
            program_ts = ts
            program_ts.setInputOutput("input{}_{}.txt".format(i, j), "output{}_{}_{}.txt".format(mu, i, j))
            program_output = getResults(program_ts)
            isViolate = MR().assertViolation(original_output, program_output)
            a = change(program_output)
            if j == 0:
                a = a - 1
            if j == 1:
                a = a + 1
            if j == 2:
                if not isViolate:
                    a = output[1]
                else:
                    a = int(a / 2)
            if j == 3:
                if not isViolate:
                    a = output[1]
                else:
                    a = a * 2
            output.append(a)
            if isViolate:
                result[j + 1] = 1

        Output.append(output)

        for m in range(len(mr_list)):
            for n in range(len(mr_list)):
                ts.setInputOutput("input{}_{}_{}.txt".format(i, m, n),
                                           "output{}_{}_{}_{}.txt".format(0, i, m, n))
                original_output = getResults(ts)
                program_ts = ts
                program_ts.setInputOutput("input{}_{}_{}.txt".format(i, m, n), "output{}_{}_{}_{}.txt".format(mu, i, m, n))
                program_output = getResults(program_ts)
                isViolate = MR().assertViolation(original_output, program_output)
                if isViolate:
                    result[len(mr_list) + 1 + m * len(mr_list) + n] = 1
        pf.append(result)
    return pf, Output


if __name__ == "__main__":
    # myenv = MyEnv()
    # myenv.CreateWorkingDirs()
    string = 'Num'
    # getOriginalInput()
    row = 1
    path = '/Applications/work/data/MT/MFT/Result/result'+sys.argv[1]+'.xlsx'  # '+sys.argv[1][:-1]+' '+sys.argv[1]+'
    wb = load_workbook(path)
    del wb[string]
    ws = wb.create_sheet(string)
    # ts = TestCase()
    # mr_list = [MR1(), MR2(), MR3(), MR4(), MR5(), MR6(), MR7()]
    # # mr_list = [MR1()]
    # # getTestcase(mr_list, ts, 100)
    # PFS, Output = getpf(0, ts, 100, mr_list)
    # MGS, SMGS = getMG(0, ts, 100, mr_list, PFS)
    # for i in range(len(SMGS)):
    #     for j in range(len(SMGS[i])):
    #         if 1 in SMGS[i][j]:
    #             print(i)
    #             break
    FR = []
    MG_set = []
    PF_set = []
    SMG_set = []  # 不去除
    Group = []
    EMR = [0, 1, 2, 3, 4, 5, 6]
    for mu in [10, 11, 14, 15]:  # [10, 11, 14, 15]
        a = FailureRate(mu)
        FR.append(a)  # original = 1-failure rate
        # PFS, Output = getpf(mu, ts, 100, mr_list)
        # MGS, SMGS = getMG(mu, ts, 100, mr_list, PFS)
        # MG_set.append(MGS)
        # PF_set.append(PFS)
        # SMG_set.append(SMGS)
        # data = {
        #          'PF': PFS, 'MG': MGS, 'SMG': SMGS, 'Output': Output
        # }
        # # 将数据存下来
        # json_str = json.dumps(data)
        # with open('/Applications/work/data/MT/MFT/' + string + '/mutant' + str(mu) + '.json', 'w') as f:
        #     json.dump(json_str, f)

        if 0 < a < 30:
            with open('/Applications/work/data/MT/MFT/' + string + '/mutant' + str(mu) + '.json', 'r') as load_f:
                data = json.load(load_f)
            data = json.loads(data)
            pf = data['PF']
            MG = data['SMG']
            Output = data['Output']
            PF_set.append(pf)
            MG_set.append(MG)
            count = []
            for i in range(len(Output)):
                c = group(Output[i])
                count.append(c)
            Group.append(count)
            row = eval('getMetrics_v14')(row, ws, mu, MG, pf, Output, EMR)   # +sys.argv[1][-1]

    wb.save(path)


