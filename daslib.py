# coding:utf-8
# daslib.py 2012.11.23
#
import re

reg_name = ["R0","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11","R12","SP","LR","PC"]
cond_name = ["EQ","NE","CS","CC","MI","PL","VS","VC","HI","LS","GE","LT","GT","LE","",""]
shift_name = ["LSL", "LSR", "ASR", "ROR"]

def REG(r):
    return reg_name[r]

def COND(n):
    return cond_name[n]

def REGISTERS(register_list):
    r = []
    v = register_list
    for i in range(16):
        if v&1:
            r.append(REG(i))
        v >>= 1
    return "{%s}" % ",".join(r)

def SET_DATA(code, size=16):
    r = ["="]
    for n in range(size-8,-1,-8):
        r.append("&%02X" % ((code >>n)&0xff))
    return r

def check_32bit_code(code):
    return (code & 0xf800) in [0xe800, 0xf000, 0xf800]  # 32bit

def SignExtend(value_list):
    imm32 = 0
    total_size = 0
    for value,size in value_list:
        imm32 <<= size
        imm32 |= value
        total_size += size
    msb_mask = 1<<(total_size-1)
    if imm32 & msb_mask:
        imm32 -= (1<<total_size)
    return imm32

def ZeroExtend(value_list):
    imm32 = 0
    for value,size in value_list:
        imm32 <<= size
        imm32 |= value
    return imm32

def ThumbExpandImm(i, imm3, imm8):
    imm32 = imm8
    return imm32

def DecodeImmShift(type, imm):
    return type, imm

def BitCount(value):
    v = value
    count = 0
    while v != 0:
         v>>= 1
         count += 1
    return count

class BitMask(object):
    def __init__(self, string, size=0):
        self._pat = 0
        self._mask = 0
        for c in string:
            if c in "01xX":
                self._pat <<= 1
                self._mask <<= 1
                if c in "01":
                    self._pat |= int(c)
                    self._mask |= 1
                size -= 1
        if size > 0:
            self._pat <<= size
            self._mask <<= size

    def __cmp__(self, other):
        if (other & self._mask) == self._pat:
            return 0
        return 1

class MEMMAP(object):
    def __init__(self):
        self._mmap ={}

    def load(self, data, offset=0):
        for i,c in enumerate(data):
            self._mmap[i+offset] = c

    def LE(self, ad, size=1):
        pass

    def mem(self, ad, size=1):
        value = 0
        pos = 0
        for i in range(size):
            if ad+i in self._mmap:
                value |= self._mmap[ad+i]<<pos
            pos += 8
        return value

if __name__=="__main__":
    pass
