# coding:utf-8
# Bitfield.py 2012.11.23
#
import re

class Bitfield(object):
    def __init__(self,value=0):
        self.value = value
        self.fields = []

    def __str__(self):
        return self._str()

    def __getattr__(self, name):
        return self._getattr(name)

    def _str(self):
        s = ""
        v = self.value
        for i in range(64):
            s = str(v&1) + s
            v >>= 1
            if v == 0:
                break
        return "0b" + s

    def _getattr(self, name):
        offset = 0
        for fname,size in self.fields:
            if fname == name:
                mask = (1<<size)-1
                return (self.value>>offset) & mask
            offset += size
        raise ValueError("not found name: %s" % name)

def field_compile(record, sep=None):
    result = []
    temp = record.split(sep)
    temp.reverse()
    dummy_count = 0
    pos = 0
    for name in temp:
        size = len(name)
        if re.match("[x01]+", name):
            name = "_%d" % dummy_count
            dummy_count += 1
        elif re.match("([\w]+):(\d+)", name):
            g = re.match("([\w]+):(\d+)", name)
            size = int(g.group(2))
            name = g.group(1)
        elif re.match("(imm)(\d+)", name):
            g = re.match("(imm)(\d+)", name)
            size = int(g.group(2))
        elif name in ['J1', 'J2', 'imm']:
            size = 1
        elif name in ['rotate', 'type']:
            size = 2
        elif name in ['option', 'coproc']:
            size = 4
        elif re.match("R\w+", name):
            size = 4
        elif re.match("CR\w+", name):
            size = 4
        else:
            pass
        result.append((name, size))
        pos += size
        if pos > 32:
            raise ValueError("field_comile error1: %s" % record)
    return result

def format_find(string):
    r = []
    for m in re.finditer(r"%\((\w+)\)s", string):
        r.append(m.group(1))
    return r

if __name__=="__main__":
    import unittest
    class TestBitfield(unittest.TestCase):
        def setUp(self):
            self.cf = Bitfield()

        def test_1(self):
            self.assertEqual(self.cf.foo, None)

        def test_2(self):
            self.cf.value = 0x1234
            self.cf.fields = [
                ('Rn', 4),
                ('_dummy1', 4),
                ('Rd',8)
            ]
            self.assertEqual(self.cf.Rn, 4)
            self.assertEqual(self.cf.Rd, 0x12)

        def test_field_compile_1(self):
            self.cf.value = 0x1234
            self.cf.fields = field_compile("Rd:8 xxxx Rn")
            self.assertEqual(self.cf.Rn, 4)
            self.assertEqual(self.cf.Rd, 0x12)

        def test_format_find_1(self):
            r = format_find("")
            self.assertEqual(r, [])
            
        def test_format_find_2(self):
            r = format_find("%(abc)s")
            self.assertEqual(r, ['abc'])

        def test_format_find_3(self):
            r = format_find("%(Rt)s,[%(Rn)s,#-%(imm8)s]!")
            self.assertEqual(r, ['Rt','Rn','imm8'])

    unittest.main()
