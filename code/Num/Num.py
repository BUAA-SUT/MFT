# MR
import random
import re
from Execution import *
from TestCase import *
import itertools
import copy
import math
import operator
from decimal import Decimal

random.seed(1)


def strictassertViolation(exp_output, followup_output):
    for i in range(len(exp_output.lines)):
        if not exp_output.lines[i] == followup_output.lines[i]:
            return True
    return False


def getResults(ts):
    result = Output(ts.output)
    result.parse()
    return result


class MR:
    def __init__(self):
        self.name = self.__class__.__name__

    def setExecutor(self, executor):
        self.executor = executor

    def setTestCase(self, ts):
        self.original_ts = ts

    def strictassertViolation(self, exp_output, followup_output):
        for i in range(len(exp_output.lines)):
            if not exp_output.lines[i] == followup_output.lines[i]:
                return True
        return False

    def getResults(self, ts):
        result = Output(ts.output)
        result.parse()
        return result

    def getFollowInput(self, mr):
        original_input = Input(self.original_ts.input)
        original_input.parseInfile()
        original_output = Output(self.original_ts.output)
        original_output.parse()  # load the A,B,C and matrix information
        followup_ts = self.generateFollowupTestCase(original_input, original_output, mr)

    def generateFollowupTestCase(self, original_input, original_output, mr):
        ts = TestCase()
        followup_infile = "{}_{}.txt".format(self.original_ts.input[:-4], mr)
        followup_outfile = "{}_{}.txt".format(self.original_ts.output[:-4], mr)

        ts.setInputOutput(followup_infile, followup_outfile)
        followup_input = self.getExpectedMatrix(original_input, original_output)
        followup_input.setInfile(followup_infile)
        followup_input.writeInfile()
        return ts

    def assertViolation(self, exp_output, followup_output):
        if '.' in followup_output.lines[0] or 'e' in followup_output.lines[0] or 'E' in followup_output.lines[0]:
            num1 = float(followup_output.lines[0])
            st = str(num1)
            if 'e' in st or 'E' in st:
                num1 = int(num1)
        else:
            num1 = int(followup_output.lines[0])
        if '.' in exp_output.lines[0] or 'e' in exp_output.lines[0] or 'E' in exp_output.lines[0]:
            num2 = float(exp_output.lines[0])
            st = str(num2)
            if 'e' in st or 'E' in st:
                num2 = int(num2)
        else:
            num2 = int(exp_output.lines[0])
        if num1 == num2:
            return False
        else:
            return True

    def getExpectedOutput(self, original_output):
        expected_output = Output(original_output.output_name)
        expected_output.lines = original_output.lines
        return expected_output

    def executeTestCase(self, ts):
        self.executor.setInputOutputNames(ts.infile, ts.outfile, ts.outtree)
        self.executor.executeDnapars()

    def getExpectedMatrix(self, original_input, original_output):
        return original_input

    def setKilledMutantsTable(self, table):
        self.table = table


class MR1(MR):
    # 加法
    def __init__(self):
        super(MR1, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        # 加上标识符
        typea = ["0x", "0X", "-0x", "-0X", "#", "-#"]
        typeb = ['f', 'F', 'd', 'D', 'l', 'L']
        if original_input.lines[0][0] in typea or original_input.lines[0][0:2] in typea or \
                original_input.lines[0][0:3] in typea:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = Decimal(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = hex(num1 + 1)
            # 末尾加字符
            # if original_input.lines[0][-1] in typeb:
            #     followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
            # followup_input.lines[0] = original_input.lines[0][0:2] + followup_input.lines[0]
            # followup_input.lines[0] = original_input.lines[0][0] + followup_input.lines[0]
        elif '0' == original_input.lines[0][0]:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = oct(num1 + 1)
            # 末尾加字符
            # if original_input.lines[0][-1] in typeb:
            #     followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
            # 去掉o
            if 'o' in followup_input.lines[0]:
                followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        else:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                # num = Decimal(original_output.lines[0])
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            followup_input.lines[0] = str(num + 1)
            # 末尾加字符
            # if original_input.lines[0][-1] in typeb:
            #     followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        if '.' in followup_output.lines[0] or 'e' in followup_output.lines[0] or 'E' in followup_output.lines[0]:
            num1 = float(followup_output.lines[0])
            st = str(num1)
            if 'e' in st or 'E' in st:
                num1 = int(num1)
        else:
            num1 = int(followup_output.lines[0])
        if '.' in exp_output.lines[0] or 'e' in exp_output.lines[0] or 'E' in exp_output.lines[0]:
            num2 = float(exp_output.lines[0])
            st = str(num2)
            if 'e' in st or 'E' in st:
                num2 = int(num2)
        else:
            num2 = int(exp_output.lines[0])
        if num1 == num2 + 1:
            return False
        else:
            return True


class MR2(MR):
    # 减法
    def __init__(self):
        super(MR2, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        # 加上标识符
        typea = ["0x", "0X", "-0x", "-0X", "#", "-#"]
        typeb = ['f', 'F', 'd', 'D', 'l', 'L']
        if original_input.lines[0][0] in typea or original_input.lines[0][0:2] in typea or \
                original_input.lines[0][0:3] in typea:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = Decimal(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = hex(num1 - 1)
            # followup_input.lines[0] = original_input.lines[0][0:2] + followup_input.lines[0]
        elif '0' == original_input.lines[0][0]:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = oct(num1 - 1)
            # # 末尾加字符
            # if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
            #     followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
            # 去掉o
            if 'o' in followup_input.lines[0]:
                followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        else:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                # num = Decimal(original_output.lines[0])
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            followup_input.lines[0] = str(num - 1)
            # 末尾加字符
            # if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
            #     followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        if '.' in followup_output.lines[0] or 'e' in followup_output.lines[0] or 'E' in followup_output.lines[0]:
            num1 = float(followup_output.lines[0])
            st = str(num1)
            if 'e' in st or 'E' in st:
                num1 = int(num1)
        else:
            num1 = int(followup_output.lines[0])
        if '.' in exp_output.lines[0] or 'e' in exp_output.lines[0] or 'E' in exp_output.lines[0]:
            num2 = float(exp_output.lines[0])
            st = str(num2)
            if 'e' in st or 'E' in st:
                num2 = int(num2)
        else:
            num2 = int(exp_output.lines[0])
        if num1 == num2 - 1:
            return False
        else:
            return True


class MR3(MR):
    # 乘法
    def __init__(self):
        super(MR3, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        typea = ["0x", "0X", "-0x", "-0X", "#", "-#"]
        typeb = ['f', 'F', 'd', 'D', 'l', 'L']
        if original_input.lines[0][0] in typea or original_input.lines[0][0:2] in typea or \
                original_input.lines[0][0:3] in typea:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = Decimal(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = hex(num1 * 2)
            # followup_input.lines[0] = original_input.lines[0][0:2] + followup_input.lines[0]
        elif '0' == original_input.lines[0][0]:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = oct(num1 * 2)
            # 末尾加字符
            # if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
            #     followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
            # 去掉o
            if 'o' in followup_input.lines[0]:
                followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        else:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                # num = Decimal(original_output.lines[0])
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            followup_input.lines[0] = str(num * 2)
            # # 末尾加字符
            # if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
            #     followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        if '.' in followup_output.lines[0] or 'e' in followup_output.lines[0] or 'E' in followup_output.lines[0]:
            num1 = float(followup_output.lines[0])
            st = str(num1)
            if 'e' in st or 'E' in st:
                num1 = int(num1)
        else:
            num1 = int(followup_output.lines[0])
        if '.' in exp_output.lines[0] or 'e' in exp_output.lines[0] or 'E' in exp_output.lines[0]:
            num2 = float(exp_output.lines[0])
            st = str(num2)
            if 'e' in st or 'E' in st:
                num2 = int(num2)
        else:
            num2 = int(exp_output.lines[0])
        if num1 == num2 * 2:
            return False
        else:
            return True


class MR4(MR):
    # 除法
    def __init__(self):
        super(MR4, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        # 加上标识符
        typea = ["0x", "0X", "-0x", "-0X", "#", "-#"]
        typeb = ['f', 'F', 'd', 'D', 'l', 'L']
        if original_input.lines[0][0] in typea or original_input.lines[0][0:2] in typea or \
                original_input.lines[0][0:3] in typea:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = Decimal(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = hex(int(num1 / 2))
        elif '0' == original_input.lines[0][0]:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = oct(int(num1 / 2))
            # 末尾加字符
            # if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
            #     followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
            # 去掉o
            if 'o' in followup_input.lines[0]:
                followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        else:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                # num = Decimal(original_output.lines[0])
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            followup_input.lines[0] = str(int(num / 2))
            # 末尾加字符
            # if original_input.lines[0][-1] == "L" or original_input.lines[0][-1] == "l":
            #     followup_input.lines[0] = followup_input.lines[0] + original_input.lines[0][-1]
        return followup_input

    def assertViolation(self, exp_output, followup_output):
        if '.' in followup_output.lines[0] or 'e' in followup_output.lines[0] or 'E' in followup_output.lines[0]:
            num1 = float(followup_output.lines[0])
            st = str(num1)
            if 'e' in st or 'E' in st:
                num1 = int(num1)
        else:
            num1 = int(followup_output.lines[0])
        if '.' in exp_output.lines[0] or 'e' in exp_output.lines[0] or 'E' in exp_output.lines[0]:
            num2 = float(exp_output.lines[0])
            st = str(num2)
            if 'e' in st or 'E' in st:
                num2 = int(num2)
        else:
            num2 = int(exp_output.lines[0])
        if num1 == int(num2 / 2):
            return False
        else:
            return True


class MR5(MR):
    # 转化为16进制
    def __init__(self):
        super(MR5, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        typea = ["0x", "0X", "-0x", "-0X", "#", "-#"]
        typeb = ['f', 'F', 'd', 'D', 'l', 'L']
        if original_input.lines[0][0] in typea or original_input.lines[0][0:2] in typea or \
                original_input.lines[0][0:3] in typea:
            return original_input
        elif '0' == original_input.lines[0][0]:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = hex(num1)
        else:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                # num = Decimal(original_output.lines[0])
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = hex(num1)

        return followup_input


class MR6(MR):
    # 转化为8进制
    def __init__(self):
        super(MR6, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        typea = ["0x", "0X", "-0x", "-0X", "#", "-#"]
        typeb = ['f', 'F', 'd', 'D', 'l', 'L']
        if original_input.lines[0][0] in typea or original_input.lines[0][0:2] in typea or \
                original_input.lines[0][0:3] in typea:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = Decimal(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = oct(num1)
            followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        elif '0' == original_input.lines[0][0]:
            return original_input
        else:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                # num = Decimal(original_output.lines[0])
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = oct(num1)
            followup_input.lines[0] = followup_input.lines[0].replace('o', '')
        return followup_input


class MR7(MR):
    # 转化为10进制
    def __init__(self):
        super(MR7, self).__init__()

    def getExpectedMatrix(self, original_input, original_output):
        followup_input = copy.deepcopy(original_output)
        typea = ["0x", "0X", "-0x", "-0X", "#", "-#"]
        typeb = ['f', 'F', 'd', 'D', 'l', 'L']
        if original_input.lines[0][0] in typea or original_input.lines[0][0:2] in typea or \
                original_input.lines[0][0:3] in typea:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = Decimal(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = str(num1)
        elif '0' == original_input.lines[0][0]:
            if '.' in original_output.lines[0] or 'e' in original_output.lines[0] or 'E' in original_output.lines[0]:
                num = float(original_output.lines[0])
                st = str(num)
                if 'e' in st or 'E' in st:
                    num = int(num)
            else:
                num = int(original_output.lines[0])
            num1 = int(num)
            if num1 != num:
                print('出错啦')
            followup_input.lines[0] = str(num1)
        else:
            return original_input
        return followup_input

