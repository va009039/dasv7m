# coding:utf-8
# mbedVector.py 2012.11.25
#
import logging

class mbedVector(object):
    def __init__(self, data):
        self.vector = []
        for ad in range(0, 4*8, 4):
            v = data[ad+0] | data[ad+1]<<8 | data[ad+2]<<16 | data[ad+3]<<24
            self.vector.append((ad, v))
        self.pc = self.vector[1][1]
        self.sp = self.vector[0][1]

    def verify(self):
        x = 0
        for v in self.vector:
            x += v[1]
            x &= 0xffffffff
        return x == 0

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('infiles', nargs='+', help=u"入力ファイル(*.bin)")
    args = parser.parse_args()
    for i, filename in enumerate(args.infiles):
        with open(filename, "rb") as f:
            data = f.read()
        data = map(ord, data)
        print("input: %s size: %d byte" % (filename, len(data)))
        vec = mbedVector(data)
        for i,v in enumerate(vec.vector):
            print "%d %08X %08X" % (i, v[0], v[1])
        print "CHECK:", vec.verify()
