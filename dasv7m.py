# coding:utf-8
# dasv7m.py 2012.11.23
import v7m
import Bitfield
from daslib import *

def rep_null(value):
    return ""

def rep_s(value):
    if value == 1:
        return "S"
    return ""

def rep_L(value):
    if value == 1:
        return "L"
    return ""

class dasv7m(object):
    def __init__(self, code=0,pc=0):
        self.code = code
        self.pc = pc

        self.name_table = {
# name: func
"R":                REG,
"I":                str,
"S":                rep_s,
"L":                rep_L,
"cond":             COND,
"c":                rep_null,
"const":            self.const,
"const_imm12":      self.const_imm12,
"label32":          self.label32,
"label32_ADR":      self.label32_ADR,
"label_Uimm12":     self.label_Uimm12,
"label_PUimm8":     self.label_PUimm8,
"registers32":      self.registers32,
"imm5_imm3imm2":    self.imm5_imm3imm2,
"imm32_imm8":       self.imm32_imm8,
"const32_imm16":    self.const32_imm16,
"lsb":              self.lsb,
"width":            self.width,
"width2":           self.width2,
'coproc':           str,
'opc1':             str,
'opc2':             str,
'spec_reg':         str,
'option':           str,

# 16bit
"D_Rd":             self.D_Rd,
"DM_Rdm":           self.D_Rd,
"DN_Rdn":           self.D_Rd,
"label16":          self.label16,
"registers":        self.registers,
}

    def lsb(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("imm3:3 xxxx imm2:2 x msb:5")
        lsbit = cf.imm3<<2 | cf.imm2
        return str(lsbit)

    def width(self, value): # BFC BFI
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("imm3:3 xxxx imm2:2 x msb:5")
        lsbit = cf.imm3<<2 | cf.imm2
        return str(cf.msb - lsbit + 1)

    def width2(self, value): # SBFX UBFX
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("imm3:3 xxxx imm2:2 x widthm1:5")
        return str(cf.widthm1 + 1)

    def D_Rd(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("N:1 xxxx Rn:3")
        n = (cf.N<<3) | cf.Rn
        return REG(n)

    def registers(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("opA:4 L:1 opB:2 PM:1 register_list:8")
        registers = cf.register_list # STM LDM PUSH POP
        if cf.opA == 0xb and cf.opB == 2:
            if cf.L == 0: # PUSH
                registers |= (cf.PM<<14)
            else:         # POP
                registers |= (cf.PM<<15)
        return REGISTERS(registers)

    def registers32(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("L:1 Rn:4 P:1 M:1 x register_list:13")
        registers = cf.register_list | (cf.M<<14)
        if cf.L == 1:
            registers |= cf.P<<15
        return REGISTERS(registers)

    def label(self, imm32, add=True):
        a = self.pc & 0xfffffffc
        if add == False:
            imm32 *= -1
        a += imm32
        a &= 0xffffffff
        return "%08X" % a

    def label16(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("opA:4 xx i:1 x imm5:5 xxx") # CBZ CBNZ
        if cf.opA == 0xb: # "1011" 
            imm32 = ZeroExtend([(cf.i,1),(cf.imm5,5),(0,1)])
        elif cf.opA == 0xe: # "1110"
            cf.fields = Bitfield.field_compile("imm11:11") # B
            imm32 = SignExtend([(cf.imm11,11),(0,1)])
        else:
            cf.fields = Bitfield.field_compile("opA:4 xxxx imm8:8") #  B<cond>
            if cf.opA == 0xd: 
                imm32 = SignExtend([(cf.imm8,8),(0,1)])
            else: # ADR LDR
                imm32 = ZeroExtend([(cf.imm8,8),(0,2)])
                return self.label(imm32)
        return "%08X" % ((self.pc + imm32)&0xffffffff)

    def label32(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("S:1 imm10:10 xx J1:1 opA:1 J2:1 imm11:11")
        i1 = 1-(cf.J1 ^ cf.S)
        i2 = 1-(cf.J2 ^ cf.S)
        if cf.opA == 1: # B or BL
            imm32 = SignExtend([(cf.S,1),(i1,1),(i2,1),(cf.imm10,10),(cf.imm11,11),(0,1)])
        else: # B<cond>
            cf.fields = Bitfield.field_compile("S:1 xxxx imm6:6 xx J1:1 opA:1 J2:1 imm11:11")
            imm32 = SignExtend([(cf.S,1),(i1,1),(i2,1),(cf.imm6,6),(cf.imm11,11),(0,1)])
        return "%08X" % ((self.pc + imm32)&0xffffffff)

    def label32_ADR(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("i:1 opA:5 xxxxxx imm3:3 xxxx imm8:8")
        imm32 = ZeroExtend([(cf.i,1),(cf.imm3,3),(cf.imm8,8)])
        return self.label(imm32, cf.opA == 0x10)

    def label_Uimm12(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("U:1 op:3 Rn:4 Rt:4 imm12:12")
        imm32 = ZeroExtend([(cf.imm12,12)])
        return self.label(imm32, cf.U == 1)

    def label_PUimm8(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("P:1 U:1 xxxxxxx xxxxxxxx imm8:8")
        imm32 = ZeroExtend([(cf.imm8,8),(0,2)])
        return self.label(imm32, cf.U == 1)

    def const(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("i:1 xxxxxxxxxx imm3:3 xxxx imm8:8")
        imm32 = ThumbExpandImm(cf.i, cf.imm3, cf.imm8)
        return str(imm32)

    def const_imm12(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("i:1 xxxxxxxxxx imm3:3 xxxx imm8:8")
        imm32 = ZeroExtend([(cf.i,1),(cf.imm3,3),(cf.imm8,8)])
        return str(imm32)

    def const32_imm16(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("i:1 xxxxxx imm4:4 x imm3:3 xxxx imm8:8")
        imm32 = ZeroExtend([(cf.imm4,4),(cf.i,1),(cf.imm3,3),(cf.imm8,8)])
        return str(imm32)

    def imm5_imm3imm2(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("imm3:3 xxxx imm2:2 xxxxxx")
        imm32 = ZeroExtend([(cf.imm3,3),(cf.imm2,2)])
        return str(imm32)

    def imm32_imm8(self, value):
        cf = Bitfield.Bitfield(value)
        cf.fields = Bitfield.field_compile("imm8:8")
        imm32 = ZeroExtend([(cf.imm8,8),(0,2)])
        return str(imm32)

    def sub_callback(self, match):
        name = match.group(1)
        g = re.match(r"(\w+)\((\d+),(\d+)\)", name)
        if g:
            name = g.group(1)
            size = int(g.group(2))
            pos = int(g.group(3))
            value = (self.code >> pos) & ((1<<size)-1)
            if name in self.name_table:
                func = self.name_table[name]
                return func(value)
            raise ValueError("table error name: <%s> code: %08X" % (name, self.code))

        if name in self.name_table:
            func = self.name_table[name]
            return func(self.code)
        raise ValueError("table error name: <%s> code: %08X" % (name, self.code))

    def replace(self, string):
        p = re.compile(r'<([\w,\(\)]+)>')
        r = p.sub(self.sub_callback, string)
        return r

    def decode(self, code, pc=0):
        self.code = code
        self.pc = pc

        if code > 0xffff:
            code_table = v7m.thumb32
            code_size = 32
        else:
            code_table = v7m.thumb16
            code_size = 16
        
        for fmt1,fmt2,pat,mask in code_table:
            if (code&mask) == pat:
                return map(self.replace, [fmt1, fmt2])
        return ["=", "%08X" % code] # UNDEFINED
        #raise ValueError("UNDEFINED: %08X" % code)

if __name__=="__main__":
    d = dasv7m()

    # 32bit
    for fmt1,fmt2,pat,mask in v7m.thumb32:
        code = pat
        d.decode(code)

    # 16bit
    for code in range(0x10000):
        d.decode(code)
    print "%04X" % code
    
    # 32bit
    for code1 in [0xe8000000, 0xf0000000, 0xf8000000]:
        for code2 in range(0, 0x8000000, 0x10000):
            for code3 in range(0,0x10000,512):
                code = code1 | code2 | code3
                d.decode(code)
            print "%08X" % code
