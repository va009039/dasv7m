# coding:utf-8
# mbedDisassembler.py 2012.11.25
#
import copy
import logging
import dasv7m
from daslib import *

class mbedDisassembler(object):
    def __init__(self):
        self.das = dasv7m.dasv7m()
        self.decode = self.das.decode
        self.mmap = MEMMAP()
        self.pc = 0

    def print_das(self, loop=100):
        result = []
        for n_loop in range(loop):
            line = ["%08X" % self.pc]
            code = self.mmap.mem(self.pc ,2)
            if check_32bit_code(code):
                code = (code<<16) | self.mmap.mem(self.pc+2, 2)
                line.append("%08X" % code)
                r = self.decode(code, self.pc + 4)
                self.pc += 4
            else:
                line.append("%04X" % code)
                r = self.decode(code, self.pc + 4)
                self.pc += 2
            line.append(r[0])
            line.append(",".join(r[1:]))
            result.append(line)
        return result

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    import argparse
    import mbedVector
    das = mbedDisassembler()
    parser = argparse.ArgumentParser()
    parser.add_argument('infiles', nargs='+', help=u"入力ファイル(*.bin)")
    parser.add_argument('-a', '--address', nargs=1, help=u"開始アドレス")
    parser.add_argument('--offset', nargs=1, help=u"オフセットアドレス")

    args = parser.parse_args()
    for i, filename in enumerate(args.infiles):
        with open(filename, "rb") as f:
            data = f.read()
        data = map(ord, data)
        print("input: %s size: %d byte" % (filename, len(data)))
        if args.address:
            pc = int(args.address[0], 16)
        else:
            vec = mbedVector.mbedVector(data)
            pc = vec.pc
            pc &= 0xfffffffe
            print "address: %08X" % pc
        das.mmap.load(data)
        das.pc = pc
        for n in range(50):
            r = das.print_das(1)
            for (ad,code,op1,op2) in r:
                print ad,"%-8s" % code,"%-6s" % op1,op2
            if das.pc > len(data):
                break
