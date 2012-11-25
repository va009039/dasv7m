# coding:utf-8
# test_dasv7m.py 2012.11.25
#
import unittest
import dasv7m

class Test_dasv7m_32bit(unittest.TestCase):
    def setUp(self):
        self.das = dasv7m.dasv7m()
        self.decode = self.das.decode
        
    def test_F0000000_AND(self):
        code = 0xf0000000
        r = self.decode(code)
        self.assertEqual(r, ["AND","R0,R0,#0"])

    def test_EA130102_ANDS(self):
        code = 0xea130102
        r = self.decode(code)
        self.assertEqual(r, ["ANDS.W","R1,R3,R2"])

    def test_F8c000FF_STR(self):
        code = 0xf8c000ff
        r = self.decode(code)
        self.assertEqual(r, ["STR.W","R0,[R0,#255]"])

    def test_F8400000_STR(self):
        code = 0xf8400000
        r = self.decode(code)
        self.assertEqual(r, ["STR.W","R0,[R0,R0]"])

    def test_F8400012_STR(self):
        code = 0xf8400012
        r = self.decode(code)
        self.assertEqual(r, ["STR.W","R0,[R0,R2,LSL #1]"])

    def test_F8800000_STRB(self):
        code = 0xf8800000
        r = self.decode(code)
        self.assertEqual(r, ["STRB.W","R0,[R0,#0]"])

    def test_F8000c01_STRB(self):
        code = 0xf8000c01
        r = self.decode(code)
        self.assertEqual(r, ["STRB","R0,[R0,#-1]"])

    def test_F8000e01_STRBT(self):
        code = 0xf8000e01
        r = self.decode(code)
        self.assertEqual(r, ["STRBT","R0,[R0,#1]"])

    def test_F8000021_STRB(self):
        code = 0xf8000021
        r = self.decode(code)
        self.assertEqual(r, ["STRB.W","R0,[R0,R1,LSL #2]"])

    def test_F890F001_PLD_imm12(self):
        code = 0xf890f001
        r = self.decode(code)
        self.assertEqual(r, ["PLD","[R0,#1]"])

    def test_F810Fc02_PLD_imm8(self):
        code = 0xf810fc02
        r = self.decode(code)
        self.assertEqual(r, ["PLD","[R0,#-2]"])

    def test_F89ff001_PLD_literal(self):
        code = 0xf89ff000
        r = self.decode(code)
        self.assertEqual(r, ["PLD","00000000"])

    def test_F815F032_PLD_register(self):
        code = 0xf815f032
        r = self.decode(code)
        self.assertEqual(r, ["PLD","[R5,R2,LSL #3]"])

    def test_F992F001_PLI_imm12(self):
        code = 0xf992f001
        r = self.decode(code)
        self.assertEqual(r, ["PLI","[R2,#1]"])

    def test_F913FC01_PLI_imm8(self):
        code = 0xf913fc01
        r = self.decode(code)
        self.assertEqual(r, ["PLI","[R3,#-1]"])

    def test_F99FF000_PLI_literal(self):
        code = 0xf99ff000
        r = self.decode(code)
        self.assertEqual(r, ["PLI","00000000"])

    def test_F99FF000_PLI_register(self):
        code = 0xf911f032
        r = self.decode(code)
        self.assertEqual(r, ["PLI","[R1,R2,LSL #3]"])

    def test_F8D12003_LDR_imm12(self):
        code = 0xf8d12003
        r = self.decode(code)
        self.assertEqual(r, ["LDR.W","R2,[R1,#3]"])

    def test_F8500E07_LDRT_imm8(self):
        code = 0xf8500e07
        r = self.decode(code)
        self.assertEqual(r, ["LDRT","R0,[R0,#7]"])

    def test_F8900001_LDRB_imm12(self):
        code = 0xf8900001
        r = self.decode(code)
        self.assertEqual(r, ["LDRB.W","R0,[R0,#1]"])

    def test_F8100c01_LDRB_imm8(self):
        code = 0xf8100c01
        r = self.decode(code)
        self.assertEqual(r, ["LDRB","R0,[R0,#-1]"])

    def test_F8100e01_LDRBT_imm8(self):
        code = 0xf8100e01
        r = self.decode(code)
        self.assertEqual(r, ["LDRBT","R0,[R0,#1]"])

    def test_F89F0000_LDRB(self):
        code = 0xf89f0000
        r = self.decode(code)
        self.assertEqual(r, ["LDRB","R0,00000000"])

    def test_F9900001_LDRSB_imm12(self):
        code = 0xf9900001
        r = self.decode(code)
        self.assertEqual(r, ["LDRSB","R0,[R0,#1]"])

class Test_dasv7m_16bit(unittest.TestCase):
    def setUp(self):
        self.das = dasv7m.dasv7m()
        self.decode = self.das.decode

    def test_1c07(self):
        code = 0x1c07
        r = self.decode(code)
        self.assertEqual(r, ["ADDS","R7,R0,#0"])

    def test_4151(self):
        code = 0x4151
        r = self.decode(code)
        self.assertEqual(r, ["ADCS","R1,R2"])

    def test_4240(self):
        code = 0x4247
        r = self.decode(code)
        self.assertEqual(r, ["RSBS","R7,R0,#0"])

    def test_4353(self):
        code = 0x4353
        r = self.decode(code)
        self.assertEqual(r, ["MULS","R3,R2,R3"])

    def test_4601(self):
        code = 0x4601
        r = self.decode(code)
        self.assertEqual(r, ["MOV","R1,R0"])

    def test_6001(self):
        code = 0x6001
        r = self.decode(code)
        self.assertEqual(r, ["STR","R1,[R0,#0]"])

    def test_e000(self):
        code = 0xe000
        r = self.decode(code)
        self.assertEqual(r, ["B","00000000"])

    def test_A000_ADR(self): # ADR
        code = 0xa000
        r = self.decode(code)
        self.assertEqual(r, ["ADR","R0,00000000"])

    def test_a800(self): # ADD
        code = 0xa800
        r = self.decode(code)
        self.assertEqual(r, ["ADD","R0,SP,#0"])

    def test_B6xx_CPS(self): # CPS
        code = 0xb600
        for i in range(256):
            r = self.decode(code + i)
            self.assertTrue(r[0] in ["CPSIE","CPSID","="])

class Test_dasv7m_32bit_B(unittest.TestCase):
    def setUp(self):
        self.das = dasv7m.dasv7m()
        self.decode = self.das.decode
        
    def test_F002FBCB_BL_00002796(self):
        code = 0xf002fbcb
        pc = 0
        r = self.decode(code, pc)
        self.assertEqual(r, ["BL","00002796"])

    def test_E8DF2301_LDRD_R2_R3_00000004(self):
        code = 0xe8df2301
        pc = 0
        r = self.decode(code, pc)
        self.assertEqual(r, ["LDRD","R2,R3,00000004"])

    def test_E85F8901_LDRD_R8_R9_FFFFFFFC(self):
        code = 0xe85f8901
        pc = 0
        r = self.decode(code, pc)
        self.assertEqual(r, ["LDRD","R8,R9,FFFFFFFC"])

    def test_F20F0000_ADR_W_R0_00000000(self):
        code = 0xf20f0000
        for pc in range(4):
            r = self.decode(code, pc)
            self.assertEqual(r, ["ADR.W","R0,00000000"])

    def test_F20F0000_ADR_W_R0_00000004_PC_4(self):
        code = 0xf20f0000
        for pc in range(4,8,1):
            r = self.decode(code, pc)
            self.assertEqual(r, ["ADR.W","R0,00000004"])

    def test_F2AF0000_SUB_R0_PC_0(self):
        code = 0xf2af0000
        pc = 0
        r = self.decode(code, pc)
        self.assertEqual(r, ["SUB","R0,PC,#0"])

    def test_F2AF0A00_SUB_R10_PC_0(self):
        code = 0xf2af0a00
        pc = 0
        r = self.decode(code, pc)
        self.assertEqual(r, ["SUB","R10,PC,#0"])

    def test_F36F0000_BFC_R0(self):
        code = 0xf36f0000
        r = self.decode(code)
        self.assertEqual(r, ["BFC","R0,#0,#1"])

    def test_F36F7CFF_BFC_R12(self):
        code = 0xf36f7cff
        r = self.decode(code)
        self.assertEqual(r, ["BFC","R12,#31,#1"])

    def test_F3610203_BFI_R2_R1(self):
        code = 0xf3610204
        r = self.decode(code)
        self.assertEqual(r, ["BFI","R2,R1,#0,#5"])

    def test_F0200000_BIC(self):
        code = 0xf0200000
        r = self.decode(code)
        self.assertEqual(r, ["BIC","R0,R0,#0"])

    def test_EA220103_BIC_R1_R2_R3(self):
        code = 0xea220103
        r = self.decode(code)
        self.assertEqual(r, ["BIC","R1,R2,R3"])

class Test_dasv7m_16bit_IT(unittest.TestCase):
    def setUp(self):
        self.das = dasv7m.dasv7m()
        self.decode = self.das.decode
        
    def test_BF08_IT_EQ(self):
        r = self.decode(0xbf08)
        self.assertEqual(r, ["IT","EQ"])

    def test_BF04_ITT_EQ(self):
        r = self.decode(0xbf04)
        self.assertEqual(r, ["ITT","EQ"])

    def test_BF18_IT_EQ(self):
        r = self.decode(0xbf18)
        self.assertEqual(r, ["IT","NE"])

    def test_BF0F_ITEEE_EQ(self):
        r = self.decode(0xbf0f)
        self.assertEqual(r, ["ITEEE","EQ"])

if __name__=="__main__":
    unittest.main()
