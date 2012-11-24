# coding:utf-8
# das.py 2012.11.23
#
import copy
import logging
import dasv7m
from daslib import *

class das(object):
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
    das = das()
    parser = argparse.ArgumentParser()
    parser.add_argument('infiles', nargs='*')
    parser.add_argument('-a', '--address', nargs=1, help=u"開始アドレス")

    args = parser.parse_args()
    for i, filename in enumerate(args.infiles):
        with open(filename, "rb") as f:
            data = f.read()
        data = map(ord, data)
        print("input: %s size: %d byte" % (filename, len(data)))
        if args.address:
            pc = int(args.address[0], 16)
        else:
            pc = data[4] | data[5]<<8 | data[6]<<16 | data[7]<<24
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
