# coding:utf-8
# setupv7m.py 2012.11.24
#
# ARMv7-Mの命令セット
#
register_name = [
    "R0","R1","R2","R3","R4","R5","R6","R7",
    "R8","R9","R10","R11","R12","SP","LR","PC"]

cond_name = [
    "EQ","NE","CS","CC","MI","PL","VS","VC",
    "HI","LS","GE","LT","GT","LE","",""]

shift_name = ["LSL", "LSR", "ASR", "ROR"]

# 16ビット命令
thumb16sub = [
("<iflags>", "", "xxxxxxxx_xxxxxx00"), # CPS
("<iflags>", "f","xxxxxxxx_xxxxxx01"), # CPS
("<iflags>","i", "xxxxxxxx_xxxxxx10"), # CPS
("<iflags>","if","xxxxxxxx_xxxxxx11"), # CPS
]

thumb16 = [
("ADD","<Rd>,SP,#<imm8>",       "10101_Rd:3_imm8:8"),
("ADD","SP,SP,#<imm7>",         "101100000_imm7:7"),
("ADD","SP,<Rm>",               "010001001_Rm:4_101"),
("ADD","<DM_Rdm>,SP,<DM_Rdm>",  "01000100_DM:1_1101_Rdm:3"),
("ADD","<DN_Rdn>,<Rm>",         "01000100_DN:1_Rm:4_Rdn:3"),
("ADDS","<Rd>,<Rn>,<Rm>",       "0001100_Rm:3_Rn:3_Rd:3"),
("ADDS","<Rd>,#<imm8>",         "00110_Rd:3_imm8:8"),
("ADDS","<Rd>,<Rn>,#<imm3>",    "0001110_imm3:3_Rn:3_Rd:3"),
("ADR","<Rd>,<label16>",        "10100_Rd:3_imm8:8"),
("ANDS","<Rdn>,<Rm>",           "0100000000_Rm:3_Rdn:3"),

("B","<label16>",               "11100_imm11:11"),
("B<cond>","<label16>",         "1101_cond:4_imm8:8"),
("BLX","<Rm>",                  "010001111_Rm:4_xxx"),
("BX","<Rm>",                   "010001110_Rm:4_xxx"),

("CBZ","<Rn>,<label16>", "101100_i:1_1_imm5:5_Rn:3"),
("CBNZ","<Rn>,<label16>","101110_i:1_1_imm5:5_Rn:3"),
("CMP","<Rd>,#<imm8>",          "00101_Rd:3_imm8:8"),
("CPSIE","<iflags>",            "10110110011_0_xx_xx"),    # CPS
("CPSID","<iflags>",            "10110110011_1_xx_xx"),    # CPS

("LDR","<Rt>,<label16>","01001_Rt:3_imm8:8"),

("SUBS","<Rd>,<Rn>,<Rm>","0001101_Rm:3_Rn:3_Rd:3"),
("SUBS","<Rd>,<Rn>,#<imm3>","0001111_imm3:3_Rn:3_Rd:3"),
("MOVS","<Rd>,#<imm8>","00100_Rd:3_imm8:8"),
("NOP","","1011111100000000"),
("YIELD","","1011111100010000"),
("WFE","","1011111100100000"),
("WFI","","1011111100110000"),
("SEV","","1011111101000000"),
("MOVS","<Rd>,<Rm>","0000000000_Rm:3_Rd:3"),
("EORS","<Rdn>,<Rm>","0100000001_Rm:3_Rdn:3"),
("LSLS","<Rdn>,<Rm>","0100000010_Rm:3_Rdn:3"),
("LSRS","<Rdn>,<Rm>","0100000011_Rm:3_Rdn:3"),
("ASRS","<Rdn>,<Rm>","0100000100_Rm:3_Rdn:3"),
("ADCS","<Rdn>,<Rm>","0100000101_Rm:3_Rdn:3"),
("SBCS","<Rdn>,<Rm>","0100000110_Rm:3_Rdn:3"),
("RORS","<Rdn>,<Rm>","0100000111_Rm:3_Rdn:3"),
("TST","<Rn>,<Rm>","0100001000_Rm:3_Rn:3"),
("RSBS","<Rd>,<Rn>,#0","0100001001_Rn:3_Rd:3"),
("CMP","<Rn>,<Rm>","0100001010_Rm:3_Rn:3"),
("CMN","<Rn>,<Rm>","0100001011_Rm:3_Rn:3"),
("ORRS","<Rdn>,<Rm>","0100001100_Rm:3_Rdn:3"),
("MULS","<Rdm>,<Rn>,<Rdm>","0100001101_Rn:3_Rdm:3"),
("BICS","<Rdn>,<Rm>","0100001110_Rm:3_Rdn:3"),
("MVNS","<Rd>,<Rm>","0100001111_Rm:3_Rd:3"),
("SXTH","<Rd>,<Rm>","1011001000_Rm:3_Rd:3"),
("SXTB","<Rd>,<Rm>","1011001001_Rm:3_Rd:3"),
("UXTH","<Rd>,<Rm>","1011001010_Rm:3_Rd:3"),
("UXTB","<Rd>,<Rm>","1011001011_Rm:3_Rd:3"),
("REV","<Rd>,<Rm>","1011101000_Rm:3_Rd:3"),
("REV16","<Rd>,<Rm>","1011101001_Rm:3_Rd:3"),
("REVSH","<Rd>,<Rm>","1011101011_Rm:3_Rd:3"),
("SUB","SP,SP,#<imm7>","101100001_imm7:7"),
("CMP","<Rn4>,<Rm>","010000101_N:1_Rm:3_Rn:3"),
("MOV","<D_Rd>,<Rm>",       "01000110_D:1_Rm:4_Rd:3"),
("BKPT","#<imm8>","10111110_imm8:8"),
("IT","<cond>","10111111_cond:4_mask:4"),
("SVC","#<imm8>","11011111_imm8:8"),
("SUBS","<Rd>,#<imm8>","00111_Rd:3_imm8:8"),
("LSLS","<Rd>,<Rm>,#<imm5>","00000_imm5:5_Rm:3_Rd:3"),
("LSRS","<Rd>,<Rm>,#<imm5>","00001_imm5:5_Rm:3_Rd:3"),
("ASRS","<Rd>,<Rm>,#<imm5>","00010_imm5:5_Rm:3_Rd:3"),
("STR","<Rt>,[<Rn>,<Rm>]","0101000_Rm:3_Rn:3_Rt:3"),
("STRH","<Rt>,[<Rn>,<Rm>]","0101001_Rm:3_Rn:3_Rt:3"),
("STRB","<Rt>,[<Rn>,<Rm>]","0101010_Rm:3_Rn:3_Rt:3"),
("LDRSB","<Rt>,[<Rn>,<Rm>]","0101011_Rm:3_Rn:3_Rt:3"),
("LDR","<Rt>,[<Rn>,<Rm>]","0101100_Rm:3_Rn:3_Rt:3"),
("LDRH","<Rt>,[<Rn>,<Rm>]","0101101_Rm:3_Rn:3_Rt:3"),
("LDRB","<Rt>,[<Rn>,<Rm>]","0101110_Rm:3_Rn:3_Rt:3"),
("LDRSH","<Rt>,[<Rn>,<Rm>]","0101111_Rm:3_Rn:3_Rt:3"),
("PUSH","<registers>","1011010_M:1_registerlist:8"),
("POP","<registers>","1011110_P:1_registerlist:8"),
("STR","<Rt>,[<Rn>,#<imm5>]","01100_imm5:5_Rn:3_Rt:3"),
("LDR","<Rt>,[<Rn>,#<imm5>]","01101_imm5:5_Rn:3_Rt:3"),
("STRB","<Rt>,[<Rn>,#<imm5>]","01110_imm5:5_Rn:3_Rt:3"),
("LDRB","<Rt>,[<Rn>,#<imm5>]","01111_imm5:5_Rn:3_Rt:3"),
("STRH","<Rt>,[<Rn>,#<imm5>]","10000_imm5:5_Rn:3_Rt:3"),
("LDRH","<Rt>,[<Rn>,#<imm5>]","10001_imm5:5_Rn:3_Rt:3"),
("STR","<Rt>,[SP,#<imm8>]","10010_Rt:3_imm8:8"),
("LDR","<Rt>,[SP,#<imm8>]","10011_Rt:3_imm8:8"),
("STM","<Rn>!,<registers>","11000_Rn:3_registerlist:8"),
("LDM","<Rn>!,<registers>","11001_Rn:3_registerlist:8"),
]

# 32ビット命令

thumb32sub = [
#                                                                P U W 
("<index32>","[<Rn>,#-<imm8>]",         "xxxxxxxx_xxxx_Rn:4_xxxx_x_1_0_0_imm8:8"),      # STRB
("<index32>","[<Rn>,#+<imm8>]",         "xxxxxxxx_xxxx_Rn:4_xxxx_x_1_1_0_imm8:8"),      # STRB
("<index32>","[<Rn>,#-<imm8>]!",        "xxxxxxxx_xxxx_Rn:4_xxxx_x_1_0_1_imm8:8"),      # STRB
("<index32>","[<Rn>,#+<imm8>]!",        "xxxxxxxx_xxxx_Rn:4_xxxx_x_1_1_1_imm8:8"),      # STRB
("<index32>","[<Rn>],#-<imm8>",         "xxxxxxxx_xxxx_Rn:4_xxxx_x_0_0_1_imm8:8"),      # STRB
("<index32>","[<Rn>],#+<imm8>",         "xxxxxxxx_xxxx_Rn:4_xxxx_x_0_1_1_imm8:8"),      # STRB
#                                               P U   W
("<index_RD>","[<Rn>,#-<imm32_imm8>]",        "xxxxxxx_1_0_x_0_x_Rn:4_xxxxxxxx_imm8:8"), # LDRD
("<index_RD>","[<Rn>,#+<imm32_imm8>]",        "xxxxxxx_1_1_x_0_x_Rn:4_xxxxxxxx_imm8:8"),
("<index_RD>","[<Rn>,#-<imm32_imm8>]!",       "xxxxxxx_1_0_x_1_x_Rn:4_xxxxxxxx_imm8:8"),
("<index_RD>","[<Rn>,#+<imm32_imm8>]!",       "xxxxxxx_1_1_x_1_x_Rn:4_xxxxxxxx_imm8:8"),
("<index_RD>","[<Rn>],#-<imm32_imm8>",        "xxxxxxx_0_0_x_1_x_Rn:4_xxxxxxxx_imm8:8"),
("<index_RD>","[<Rn>],#+<imm32_imm8>",        "xxxxxxx_0_1_x_1_x_Rn:4_xxxxxxxx_imm8:8"),

("<shift>","",                          "xxxxxxxx_xxxxxxxx_x_000_xxxx_00_00_xxxx"),
("<shift>",",LSL #<imm5_imm3imm2>",     "xxxxxxxx_xxxxxxxx_x_imm3:3_xxxx_imm2:2_00_xxxx"),
("<shift>",",LSR #<imm5_imm3imm2>",     "xxxxxxxx_xxxxxxxx_x_imm3:3_xxxx_imm2:2_01_xxxx"),
("<shift>",",ASR #<imm5_imm3imm2>",     "xxxxxxxx_xxxxxxxx_x_imm3:3_xxxx_imm2:2_10_xxxx"),
("<shift>",",ROR #<imm5_imm3imm2>",     "xxxxxxxx_xxxxxxxx_x_imm3:3_xxxx_imm2:2_11_xxxx"),
# SXTH,UXTH,SXTB,UXTB
("<rotation>",  "",             "xxxxxxxx_xxxxxxxx_xxxxxxxx_xx_00_xxxx"),
("<rotation>",  ",ROR #8",      "xxxxxxxx_xxxxxxxx_xxxxxxxx_xx_01_xxxx"),
("<rotation>",  ",ROR #16",     "xxxxxxxx_xxxxxxxx_xxxxxxxx_xx_10_xxxx"),
("<rotation>",  ",ROR #24",     "xxxxxxxx_xxxxxxxx_xxxxxxxx_xx_11_xxxx"),

]

thumb32 = [
("ADDW<c>",       "<Rd>,SP,#<const_imm12>",   "11100_i:1_100001_1101_0_imm3:3_Rd:4_imm8:8"),
("ADDW<S><c>",  "<Rd>,<Rn>,#<const_imm12>",   "11110_i:1_10000_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),
("ADD<S><c>.W", "<Rd>,SP,#<const>",           "11110_i:1_01000_S:1_11010_imm3:3_Rd:4_imm8:8"),
("ADD<S>.W",      "<Rd>,<Rn>,#<const>",       "11110_i:1_01000_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),
("ADD<S>,<c>",  "<Rd>,SP,<Rm><shift>",  "11101011000_S:1_1101_0_xxx_Rd:4_xxxx_Rm:4"),
("ADD<S>",     "<Rd>,<Rn>,<Rm><shift>", "11101011000_S:1_Rn:4_x_xxx_Rd:4_xxxx_Rm:4"),

("ADR<c>.W",      "<Rd>,<label32_ADR>",           "11110_i:1_10000011110_imm3:3_Rd:4_imm8:8"), # add=True
("ADR<c>.W",      "<Rd>,<label32_ADR>",           "11110_i:1_10101011110_imm3:3_Rd:4_imm8:8"), # add=False

("WFE<c>.W",      "",                                 "1111001110101111_10000000_00000010"),
("WFI<c>.W",      "",                                 "1111001110101111_10000000_00000011"),
("YIELD<c>.W",    "",                                 "1111001110101111_10000000_00000001"),
("NOP<c>.W",      "",                                 "111100111010xxxx_10x0x000_00000000"),
("SEV<c>.W",      "",                                 "1111001110101111_10000000_00000100"),

("DBG<c>",        "#<option>",                      "111100111010xxxx_10xxx0001111_option:4"),
("DMB<c>",        "#<option>",                      "1111001110111111_100011110101_option:4"),
("DSB<c>",        "#<option>",                      "1111001110111111_100011110100_option:4"),
("ISB<c>",        "#<option>",                      "1111001110111111_100011110110_option:4"),

("SXTH<c>.W",     "<Rd>,<Rm><rotation>",       "1111101000001111_1111_Rd:4_1x_xx_Rm:4"),
("UXTH<c>.W",     "<Rd>,<Rm><rotation>",       "1111101000011111_1111_Rd:4_1x_xx_Rm:4"),
("SXTB<c>.W",     "<Rd>,<Rm><rotation>",       "1111101001001111_1111_Rd:4_1x_xx_Rm:4"),
("UXTB<c>.W",     "<Rd>,<Rm><rotation>",       "1111101001011111_1111_Rd:4_1x_xx_Rm:4"),



("SUBW<c>",       "<Rd>,<Rn>,#<const_imm12>", "11110_i:1_101010_Rn:4_0_imm3:3_Rd:4_imm8:8"),

("MOV<S>.W",      "<Rd>,#<const>",            "11110_i:1_00010_S:1_11110_imm3:3_Rd:4_imm8:8"),
("MVN<S><c>",   "<Rd>,#<const>",              "11110_i:1_00011_S:1_11110_imm3:3_Rd:4_imm8:8"),

("TST<c>",         "<Rn>,#<const>",           "11110_i:1_000001_Rn:4_0_imm3:3_1111_imm8:8"),
("TEQ<c>",        "<Rn>,#<const>",            "11110_i:1_001001_Rn:4_0_imm3:3_1111_imm8:8"),
("CMN<c>",        "<Rn>,#<const>",            "11110_i:1_010001_Rn:4_0_imm3:3_1111_imm8:8"),
("CMP<c>.W",      "<Rn>,#<const>",            "11110_i:1_011011_Rn:4_0_imm3:3_1111_imm8:8"),

("SUB<S><c>.W", "<Rd>,SP,#<const>",           "11110_i:1_01101_S:1_11010_imm3:3_Rd:4_imm8:8"),
("AND<S><c>",   "<Rd>,<Rn>,#<const>",         "11110_i:1_00000_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),
("BIC<S><c>",   "<Rd>,<Rn>,#<const>",         "11110_i:1_00001_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),
("ORR<S><c>",   "<Rd>,<Rn>,#<const>",         "11110_i:1_00010_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),
("ORN<S><c>",   "<Rd>,<Rn>,#<const>",         "11110_i:1_00011_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),
("EOR<S><c>",   "<Rd>,<Rn>,#<const>",         "11110_i:1_00100_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),
("ADC<S>",        "<Rd>,<Rn>,#<const>",       "11110_i:1_01010_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),
("SBC<S><c>",   "<Rd>,<Rn>,#<const>",         "11110_i:1_01011_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),
("SUB<S><c>.W", "<Rd>,<Rn>,#<const>",         "11110_i:1_01101_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),
("RSB<S><c>.W", "<Rd>,<Rn>,#<const>",         "11110_i:1_01110_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),

("SUB<S><c>.W", "<Rd>,<Rn>,#<const>",         "11110_i:1_01101_S:1_Rn:4_0_imm3:3_Rd:4_imm8:8"),

("CMN<c>.W",      "<Rn>,<Rm><shift>",         "111010110001_Rn:4_x_xxx_1111_xxxx_Rm:4"),
("CMP<c>.W",      "<Rn>,<Rm><shift>",         "111010111011_Rn:4_x_xxx_1111_xxxx_Rm:4"),

("ASR<c>",        "<Rd>,<Rm>,#<imm5_imm3imm2>", "11101010010_S:1_11110_imm3:3_Rd:4_imm2:2_10_Rm:4"),


("AND<S><c>.W","<Rd>,<Rn>,<Rm><shift>", "11101010000_S:1_Rn:4_x_xxx_Rd:4_xxxx_Rm:4"),
("BIC<S>,<c>", "<Rd>,<Rn>,<Rm><shift>", "11101010001_S:1_Rn:4_x_xxx_Rd:4_xxxx_Rm:4"),
("EOR<S><c>.W","<Rd>,<Rn>,<Rm><shift>", "11101010100_S:1_Rn:4_x_xxx_Rd:4_xxxx_Rm:4"),
("ADC<S>.W",   "<Rd>,<Rn>,<Rm><shift>", "11101011010_S:1_Rn:4_x_xxx_Rd:4_xxxx_Rm:4"),

("UDIV<c>",       "<Rd>,<Rn>,<Rm>",      "111110111011_Rn:4_1111_Rd:4_1111_Rm:4"),
("ASR<S><c>.W", "<Rd>,<Rn>,<Rm>",        "11111010010_S:1_Rn:4_1111_Rd:4_0000_Rm:4"),

("B<c>.W",        "<label32>",                        "11110_S:1_cond:4_imm6:6_10_J1:1_0_J2:1_imm11:11"),

("B<c>.W",        "<label32>",                        "11110_S:1_imm10:10_10_J1:1_1_J2:1_imm11:11"),
("BL<c>",         "<label32>",                        "11110_S:1_imm10:10_11_J1:1_1_J2:1_imm11:11"),

("BFC<c>",        "<Rd>,#<lsb>,#<width>",       "11110011011011110_imm3:3_Rd:4_imm2:2_0_msb:5"),
("BFI<c>",        "<Rd>,<Rn>,#<lsb>,#<width>",  "111100110110_Rn:4_0_imm3:3_Rd:4_imm2:2_0_msb:5"),
("SBFX<c>",       "<Rd>,<Rn>,#<lsb>,#<width2>",  "11110x110100_Rn:4_0_imm3:3_Rd:4_imm2:2_x_widthm1:5"),
("UBFX<c>",       "<Rd>,<Rn>,#<lsb>,#<width2>",  "11110x111100_Rn:4_0_imm3:3_Rd:4_imm2:2_x_widthm1:5"),

("CDP<c>","<coproc>,<opc1>,<CRd>,<Rn>,<Rm>,<opc2>", "1110_1110_opc1:4_Rn:4_CRd:4_coproc:4_opc2:3_0_Rm:4"),
("CDP2<c>","<coproc>,<opc1>,<CRd>,<Rn>,<Rm>,<opc2>","1111_1110_opc1:4_Rn:4_CRd:4_coproc:4_opc2:3_0_Rm:4"),
("CLREX<c>",      "",                           "11110_0_111_01_1_1111_10_0_0_1111_0010_1111"),

("CLZ<c>",        "<Rd>,<Rm>",                    "111110101011_Rn:4_1111_Rd:4_1000_Rm:4"),

("LDC<L><c>",   "p<coproc>,<CRd>,<index_RD>", "1110110_P:1_U:1_L:1_W:1_1_Rn:4_CRd:4_coproc:4_imm8:8"),
("LDC2<L><c>",  "p<coproc>,<CRd>,<index_RD>", "1111110_P:1_U:1_L:1_W:1_1_Rn:4_CRd:4_coproc:4_imm8:8"),

("LDC<L><c>",   "p<coproc>,<CRd>,[PC,#-0]",   "1110110_P:1_U:1_L:1_W:1_11111_CRd:4_coproc:4_imm8:8"),
("LDC2<L><c>",  "p<coproc>,<CRd>,[PC,#-0]",   "1111110_P:1_U:1_L:1_W:1_11111_CRd:4_coproc:4_imm8:8"),

("LDREX<c>",      "<Rt>,[<Rn>,#<imm8>]",        "111010000101_Rn:4_Rt:4_1111_imm8:8"),
("LDRBT<c>",      "<Rt>,[<Rn>,#<imm8>]",        "111110000001_Rn:4_Rt:4_1110_imm8:8"),
("LDRHT<c>",      "<Rt>,[<Rn>,#<imm8>]",        "111110000011_Rn:4_Rt:4_1110_imm8:8"),
("LDRSHT<c>",     "<Rt>,[<Rn>,#<imm8>]",        "111110010011_Rn:4_Rt:4_1110_imm8:8"),
("LDRT<c>",       "<Rt>,[<Rn>,#<imm8>]",        "111110000101_Rn:4_Rt:4_1110_imm8:8"),
("LDRSBT<c>",     "<Rt>,[<Rn>,#<imm8>]",        "111110010001_Rn:4_Rt:4_1110_imm8:8"),
("STRBT<c>",      "<Rt>,[<Rn>,#<imm8>]",        "111110000000_Rn:4_Rt:4_1110_imm8:8"),
("STRHT<c>",      "<Rt>,[<Rn>,#<imm8>]",        "111110000010_Rn:4_Rt:4_1110_imm8:8"),
("STRT<c>",       "<Rt>,[<Rn>,#<imm8>]",        "111110000100_Rn:4_Rt:4_1110_imm8:8"),

("PLD<c>", "<label_Uimm12>",                    "11111000_U:1_0011111_1111_imm12:12"),
("PLD<c>",   "[<Rn>,#<imm12>]",                 "111110001001_Rn:4_1111_imm12:12"),
("PLD<c>",   "[<Rn>,#-<imm8>]",                 "111110000001_Rn:4_11111100_imm8:8"),
("PLD<c>",        "[<Rn>,<Rm>,LSL #<imm2>]",    "111110000001_Rn:4_1111000000_imm2:2_Rm:4"),
("PLI<c>", "<label_Uimm12>",                    "11111001_U:1_0011111_1111_imm12:12"),
("PLI<c>",        "[<Rn>,<Rm>,LSL #<imm2>]",    "111110010001_Rn:4_1111000000_imm2:2_Rm:4"),
("PLI<c>",        "[<Rn>,#-<imm8>]",            "111110010001_Rn:4_11111100_imm8:8"),
("PLI<c>",        "[<Rn>,#<imm12>]",            "111110011001_Rn:4_1111_imm12:12"),

("STRB<c>",       "<Rt>,<index32>",             "111110000000xxxx_Rt:4_1_xxx_xxxxxxxx"),
("LDRB<c>",       "<Rt>,<index32>",             "111110000001xxxx_Rt:4_1_xxx_xxxxxxxx"),
("LDRH<c>",       "<Rt>,<index32>",             "111110000011xxxx_Rt:4_1_xxx_xxxxxxxx"),
("LDR<c>",        "<Rt>,<index32>",             "111110000101xxxx_Rt:4_1_xxx_xxxxxxxx"),
("LDRSH<c>",      "<Rt>,<index32>",             "111110010011xxxx_Rt:4_1_xxx_xxxxxxxx"),
("LDRSB<c>",      "<Rt>,<index32>",             "111110010001xxxx_Rt:4_1_xxx_xxxxxxxx"),
("STR<c>",        "<Rt>,<index32>",             "111110000100xxxx_Rt:4_1_xxx_xxxxxxxx"),
("STRH<c>",       "<Rt>,<index32>",             "111110000010xxxx_Rt:4_1_xxx_xxxxxxxx"),

("POP<c>.W",      "<registers32>",              "1110100010_111101_P:1_M:1_x_registerlist:13"),
("PUSH<c>.W",     "<registers32>",              "1110100100_101101_x_M:1_x_registerlist:13"),

("LDM<c>.W",      "<Rn>!,<registers32>",        "1110100010_W:1_1_Rn:4_P:1_M:1_0_registerlist:13"),
("LDMDB<c>",      "<Rn>!,<registers32>",        "1110100100_W:1_1_Rn:4_P:1_M:1_0_registerlist:13"),

("STM<c>.W",      "<Rn>!,<registers32>",       "1110100010_W:1_0_Rn:4_x_M:1_x_registerlist:13"), #
("STMDB<c>",      "<Rn>!,<registers32>",       "1110100100_W:1_0_Rn:4_x_M:1_x_registerlist:13"), #

("LDR<c>.W",      "<Rt>,<label_Uimm12>",       "11111000_U:1_1011111_Rt:4_imm12:12"),
("LDRB<c>",       "<Rt>,<label_Uimm12>",       "11111000_U:1_0011111_Rt:4_imm12:12"),
("LDRSB<c>",      "<Rt>,<label_Uimm12>",       "11111001_U:1_0011111_Rt:4_imm12:12"),
("LDRH<c>",       "<Rt>,<label_Uimm12>",       "11111000_U:1_0111111_Rt:4_imm12:12"),
("LDRSH<c>",      "<Rt>,<label_Uimm12>",       "11111001_U:1_0111111_Rt:4_imm12:12"),

("LDRB<c>.W",     "<Rt>,[<Rn>,<Rm>]", "111110000001_Rn:4_Rt:4_000000_00_Rm:4"),
("LDRH<c>.W",     "<Rt>,[<Rn>,<Rm>]", "111110000011_Rn:4_Rt:4_000000_00_Rm:4"),
("STR<c>.W",      "<Rt>,[<Rn>,<Rm>]", "111110000100_Rn:4_Rt:4_000000_00_Rm:4"),
("LDR<c>.W",      "<Rt>,[<Rn>,<Rm>]", "111110000101_Rn:4_Rt:4_000000_00_Rm:4"),
("STRB<c>.W",     "<Rt>,[<Rn>,<Rm>]", "111110000000_Rn:4_Rt:4_000000_00_Rm:4"),
("STRH<c>.W",     "<Rt>,[<Rn>,<Rm>]", "111110000010_Rn:4_Rt:4_000000_00_Rm:4"),
("LDRSB<c>.W",    "<Rt>,[<Rn>,<Rm>]", "111110010001_Rn:4_Rt:4_000000_00_Rm:4"),
("LDRSH<c>.W",    "<Rt>,[<Rn>,<Rm>]", "111110010011_Rn:4_Rt:4_000000_00_Rm:4"),

("LDRB<c>.W",     "<Rt>,[<Rn>,<Rm>,LSL #<imm2>]", "111110000001_Rn:4_Rt:4_000000_imm2:2_Rm:4"),
("LDRH<c>.W",     "<Rt>,[<Rn>,<Rm>,LSL #<imm2>]", "111110000011_Rn:4_Rt:4_000000_imm2:2_Rm:4"),
("STR<c>.W",      "<Rt>,[<Rn>,<Rm>,LSL #<imm2>]", "111110000100_Rn:4_Rt:4_000000_imm2:2_Rm:4"),
("LDR<c>.W",      "<Rt>,[<Rn>,<Rm>,LSL #<imm2>]", "111110000101_Rn:4_Rt:4_000000_imm2:2_Rm:4"),
("STRB<c>.W",     "<Rt>,[<Rn>,<Rm>,LSL #<imm2>]", "111110000000_Rn:4_Rt:4_000000_imm2:2_Rm:4"),
("STRH<c>.W",     "<Rt>,[<Rn>,<Rm>,LSL #<imm2>]", "111110000010_Rn:4_Rt:4_000000_imm2:2_Rm:4"),
("LDRSB<c>.W",    "<Rt>,[<Rn>,<Rm>,LSL #<imm2>]", "111110010001_Rn:4_Rt:4_000000_imm2:2_Rm:4"),
("LDRSH<c>.W",    "<Rt>,[<Rn>,<Rm>,LSL #<imm2>]", "111110010011_Rn:4_Rt:4_000000_imm2:2_Rm:4"),



("LDREXB<c>",     "<Rt>,[<Rn>]",                  "111010001101_Rn:4_Rt:4_1111_0100_1111"),
("LDREXH<c>",     "<Rt>,[<Rn>]",                  "111010001101_Rn:4_Rt:4_1111_0101_1111"),

("LDRB<c>.W",     "<Rt>,[<Rn>,#<imm12>]",       "111110001001_Rn:4_Rt:4_imm12:12"),
("LDRH<c>.W",     "<Rt>,[<Rn>,#<imm12>]",       "111110001011_Rn:4_Rt:4_imm12:12"),
("LDR<c>.W",      "<Rt>,[<Rn>,#<imm12>]",       "111110001101_Rn:4_Rt:4_imm12:12"),
("LDRSB<c>",      "<Rt>,[<Rn>,#<imm12>]",       "111110011001_Rn:4_Rt:4_imm12:12"),
("LDRSH<c>",      "<Rt>,[<Rn>,#<imm12>]",       "111110011011_Rn:4_Rt:4_imm12:12"),

("MOV<S><c>",   "<Rd>,<Rm>",                   "11101010010_S:1_1111_x000_Rd:4_0000_Rm:4"),

("SDIV<c>",       "<Rd>,<Rn>,<Rm>",             "111110111001_Rn:4_1111_Rd:4_1111_Rm:4"),

("LSL<S><c>.W", "<Rd>,<Rn>,<Rm>",             "11111010000_S:1_Rn:4_1111_Rd:4_0000_Rm:4"),
("LSR<S><c>.W", "<Rd>,<Rn>,<Rm>",             "11111010001_S:1_Rn:4_1111_Rd:4_0000_Rm:4"),
("ROR<S><c>",   "<Rd>,<Rn>,<Rm>",             "11111010011_S:1_Rn:4_1111_Rd:4_0000_Rm:4"),

("LSL<S><c>.W", "<Rd>,<Rm>,#<imm5_imm3imm2>",          "11101010010_S:1_11110_imm3:3_Rd:4_imm2:2_00_Rm:4"),
("LSR<S><c>.W", "<Rd>,<Rm>,#<imm5_imm3imm2>",          "11101010010_S:1_11110_imm3:3_Rd:4_imm2:2_01_Rm:4"),

("MCR<c>",  "p<coproc>,<opc1>,<Rt>,<Rn>,<Rm>,<opc2>", "11101110_opc1:3_0_Rn:4_Rt:4_coproc:4_opc2:3_1_Rm:4"),
("MCR2<c>", "p<coproc>,<opc1>,<Rt>,<Rn>,<Rm>,<opc2>", "11111110_opc1:3_0_Rn:4_Rt:4_coproc:4_opc2:3_1_Rm:4"),
("MCRR<c>", "p<coproc>,<opc1>,<Rt>,<Rt2>,<Rm>", "111011000100_Rt2:4_Rt:4_coproc:4_opc1:4_Rm:4"),
("MCRR2<c>","p<coproc>,<opc1>,<Rt>,<Rt2>,<Rm>", "111111000100_Rt2:4_Rt:4_coproc:4_opc1:4_Rm:4"),

("MLA<c>",        "<Rd>,<Rn>,<Rm>,<Ra>",      "111110110000_Rn:4_Ra:4_Rd:4_0000_Rm:4"),
("MLS<c>",        "<Rd>,<Rn>,<Rm>,<Ra>",      "111110110000_Rn:4_Ra:4_Rd:4_0001_Rm:4"),

("MOVW<c>", "<Rd>,#<const32_imm16>",                "11110_i:1_100100_imm4:4_0_imm3:3_Rd:4_imm8:8"),
("MOVT<c>", "<Rd>,#<const32_imm16>",                "11110_i:1_101100_imm4:4_0_imm3:3_Rd:4_imm8:8"),

("MRC<c>","p<coproc>,<opc1>,<Rt>,<Rn>,<Rm>,<opc2>","11101110_opc1:3_1_Rn:4_Rt:4_coproc:4_opc2:3_1_Rm:4"),
("MRC2<c>","p<coproc>,<opc1>,<Rt>,<Rn>,<Rm>,<opc2>","11111110_opc1:3_1_Rn:4_Rt:4_coproc:4_opc2:3_1_Rm:4"),
("MRRC<c>", "p<coproc>,<opc1>,<Rt>,<Rt2>,<Rm>", "111011000101_Rt2:4_Rt:4_coproc:4_opc1:4_Rm:4"),
("MRRC2<c>","p<coproc>,<opc1>,<Rt>,<Rt2>,<Rm>", "111111000101_Rt2:4_Rt:4_coproc:4_opc1:4_Rm:4"),
("MRS<c>",        "<Rd>,<spec_reg>",              "11110011111xxxxx_10x0_Rd:4_SYSm:8"),
("MSR<c>",        "<spec_reg>,<Rn>",              "11110011100x_Rn:4_10x0xxxx_SYSm:8"),
("MUL<c>",        "<Rd>,<Rn>,<Rm>",             "111110110000_Rn:4_1111_Rd:4_0000_Rm:4"),

("MVN<S)<c>.W",  "<Rd>,<Rm><shift>",          "11101010011_S:1_11110_xxx_Rd:4_xxxx_Rm:4"),

("ORR<S><c>.W", "<Rd>,<Rn>,<Rm><shift>",   "11101010010_S:1_Rn:4_0_xxx_Rd:4_xxxx_Rm:4"),
("ORN<S><c>",   "<Rd>,<Rn>,<Rm><shift>",   "11101010011_S:1_Rn:4_0_xxx_Rd:4_xxxx_Rm:4"),


("RRX<S><c>",   "<Rd>,<Rm>",                    "11101010010_S:1_11110000_Rd:4_0011_Rm:4"),


("RBIT<c>",       "<Rd>,<Rm>",                    "111110101001_Rn:4_1111_Rd:4_1010_Rm:4"),
("REV<c>.W",      "<Rd>,<Rm>",                    "111110101001_Rn:4_1111_Rd:4_1000_Rm:4"),
("REV16(%c>.W",    "<Rd>,<Rm>",                    "111110101001_Rn:4_1111_Rd:4_1001_Rm:4"),
("REVSH(%c>.W",    "<Rd>,<Rm>",                    "111110101001_Rn:4_1111_Rd:4_1011_Rm:4"),

("ROR<S><c>", "<Rd>,<Rm>,#<imm5_imm3imm2>","11101010010_S:1_11110_imm3:3_Rd:4_imm2:2_11_Rm:4"),
("RSB<S><c>",   "<Rd>,<Rn>,<Rm><shift>",   "11101011110_S:1_Rn:4_0_xxx_Rd:4_xxxx_Rm:4"),
("SBC<S><c>.W", "<Rd>,<Rn>,<Rm><shift>",   "11101011011_S:1_Rn:4_0_xxx_Rd:4_xxxx_Rm:4"),


("SMALL<c>",      "<RdLo>,<RdHi>,<Rn>,<Rm>",  "111110111100_Rn:4_RdLo:4_RdHi:4_0000_Rm:4"),
("SMULL<c>",      "<RdLo>,<RdHi>,<Rn>,<Rm>",  "111110111000_Rn:4_RdLo:4_RdHi:4_0000_Rm:4"),

("SSAT<c>",       "<Rd>,#<imm5>,<Rn><shift>","11110x1100_sh:1_0_Rn:4_0_xxx_Rd:4_imm2:2_x_imm5:5"),
("USAT<c>",       "<Rd>,#<imm5>,<Rd><shift>","11110x1110_sh:1_0_Rn:4_0_xxx_Rd:4_imm2:2_x_imm5:5"),

("STC<L><c>",   "p<coproc>,<CRd>,<index_RD>", "1110110_P:1_U:1_L:1_W:1_0_Rn:4_CRd:4_coproc:4_imm8:8"),
("STC2<L><c>",  "p<coproc>,<CRd>,<index_RD>", "1111110_P:1_U:1_L:1_W:1_0_Rn:4_CRd:4_coproc:4_imm8:8"),

("STR<c>.W",      "<Rt>,[<Rn>,#<imm12>]",       "111110001100_Rn:4_Rt:4_imm12:12"),
("STRB<c>.W",     "<Rt>,[<Rn>,#<imm12>]",       "111110001000_Rn:4_Rt:4_imm12:12"),
("STRH<c>.W",     "<Rt>,[<Rn>,#<imm12>]",       "111110001010_Rn:4_Rt:4_imm12:12"),

("STREX<c>",      "<Rd>,<Rt>,[<Rn>,#<imm8>]", "111010000100_Rn:4_Rt:4_Rd:4_imm8:8"),
("STREXB<c>",     "<Rd>,<Rt>,[<Rn>]",           "111010001100_Rn:4_Rt:4_1111_0100_Rd:4"),
("STREXH<c>",     "<Rd>,<Rt>,[<Rn>]",           "111010001100_Rn:4_Rt:4_1111_0101_Rd:4"),

("SUBW<c>", "<Rd>,SP,#<const_imm12>", "11110_i:1_10101011010_imm3:3_Rd:4_imm8:8"),

("SUB<S><c>",   "<Rd>,SP,<Rm><shift>",      "11101011101_S:1_11010_xxx_Rd:4_xxxx_Rm:4"),
("SUB<S><c>.W", "<Rd>,<Rn>,<Rm><shift>",    "11101011101_S:1_Rn:4_0_xxx_Rd:4_xxxx_Rm:4"),

("TBB<c>",        "[<Rn>,<Rm>]",                      "111010001101_Rn:4_11110000000_0_Rm:4"),
("TBB<c>",        "[<Rn>,<Rm>,LSL #1]",               "111010001101_Rn:4_11110000000_1_Rm:4"),

("TEQ<c>",        "<Rn>,<Rm><shift>",          "111010101001_Rn:4_0_xxx_1111_xxxx_Rm:4"),
("TST<c>.W",      "<Rn>,<Rm><shift>",          "111010100001_Rn:4_0_xxx_1111_xxxx_Rm:4"),

("UMLAL<c>",      "<RdLo>,<RdHi>,<Rn>,<Rm>",  "111110111110_Rn:4_RdLo:4_RdHi:4_0000_Rm:4"),
("UMULL<c>",      "<RdLo>,<RdHi>,<Rn>,<Rm>",  "111110111010_Rn:4_RdLo:4_RdHi:4_0000_Rm:4"),

("STRD<c>", "<Rt>,<Rt2>,<index_RD>",        "1110100_P:1_U:1_1_W:1_0_Rn:4_Rt:4_Rt2:4_imm8:8"),
("LDRD<c>", "<Rt>,<Rt2>,<label_PUimm8>",    "1110100_P:1_U:1_1_011111_Rt:4_Rt2:4_imm8:8"),
("LDRD<c>", "<Rt>,<Rt2>,<index_RD>",        "1110100_P:1_U:1_1_W:1_1_Rn:4_Rt:4_Rt2:4_imm8:8"),

]

class CodeInfo(object):
    def __init__(self, string=None, code_size=32):
        self.code_size = code_size
        self.field = {}
        self.pat  = 0
        self.mask = 0
        self.mask_count = 0
        if string == None:
            return

        csize = self.code_size
        for s in string.split("_"):
            if re.match(r"[01xX]+", s):
                for c in s:
                    self.pat  <<= 1
                    self.mask <<= 1
                    if c in "01":
                        self.pat  |= int(c)
                        self.mask |= 1
                        self.mask_count += 1
                csize -= len(s)
            else:
                g = re.match(r"(\w+):(\d+)", s)
                if g:
                    size = int(g.group(2))
                    self.pat  <<= size
                    self.mask <<= size
                    csize -= size
                else:
                    raise ValueError("%s %s" % (s, string))
        if csize > 0:
            self.pat  <<= csize
            self.mask <<= csize

        temp = string.split("_")
        temp.reverse()
        pos = 0
        for s in temp:
            if re.match(r"[01x]+", s):
                pos += len(s)
            else:
                g = re.match(r"(\w+):(\d+)", s)
                if g:
                    name = g.group(1)
                    size = int(g.group(2))
                    self.field[name] = (size, pos)
                    pos += size
                else:
                    raise ValueError("%s %s" % (s, string))

class setup(object):
    def __init__(self, table, sub_table, code_size=16):
        self.output_string = ""
        self.code_size = code_size
        self.index = {}
        for name,fmt,info in sub_table:
            if name in self.index:
                self.index[name].append((fmt, CodeInfo(info, self.code_size)))
            else:
                self.index[name] = [(fmt, CodeInfo(info, self.code_size))]
        
        self.table = []
        for (fmt1,fmt2,info) in table:
            self.table.append([fmt1,fmt2, CodeInfo(info, self.code_size)])

    def output(self, s):
        self.output_string += s + "\n"

    def key_sort(self, obj):
        (fmt1,fmt2,info) = obj
        mask = info.mask
        count = 0
        while mask != 0:
            if mask&1:
                count += 1
            mask >>= 1
        return count

    def conv(self):
        result = []
        for base_fmt1, base_fmt2, base_info in self.table:
            result2 = []
            for name in self.index:
                if name in base_fmt2:
                    for sub_fmt,sub_info in self.index[name]:
                        fmt1 = base_fmt1
                        fmt2 = base_fmt2.replace(name, sub_fmt)
                        info = CodeInfo(code_size=self.code_size)
                        info.field = base_info.field
                        info.field.update(sub_info.field)
                        info.pat = base_info.pat | sub_info.pat
                        info.mask = base_info.mask | sub_info.mask
                        result2.append([fmt1, fmt2, info])
                        rflag = True
            if len(result2) == 0:
                result.append([base_fmt1, base_fmt2, base_info])
            result.extend(result2)

        # sort
        table = sorted(result, key=self.key_sort, reverse=True)

        result = []
        self.undef_name = set([])
        for fmt1,fmt2,info in table:
            self.field = info.field
            p = re.compile(r'<(\w+)>')
            d_fmt1 = p.sub(self.sub_callback, fmt1)
            d_fmt2 = p.sub(self.sub_callback, fmt2)
            result.append((d_fmt1, d_fmt2, info))

        table = result

        self.output("thumb%d = [" % self.code_size)
        for fmt1,fmt2,info in table:
            if self.code_size == 32:
                self.output("(\"%s\",\"%s\",0x%08x,0x%08x)," % (fmt1, fmt2, info.pat, info.mask))
            else: # 16bit
                self.output("(\"%s\",\"%s\",0x%04x,0x%04x)," % (fmt1, fmt2, info.pat, info.mask))
        self.output("]")
        self.output("# table size = %d" % len(table))

        for name in self.undef_name:
            self.output("# %s" % name)

    def sub_callback(self, match):
        name = match.group(1)
        if name in self.field:
            size,pos = self.field[name]
            if re.match(r"R|CR", name):
                r = "<R(%d,%d)>" % (size, pos)
            elif re.match(r"imm", name):
                r = "<I(%d,%d)>" % (size, pos)
            else:
                r = "<%s(%d,%d)>" % (name, size, pos)
                self.undef_name.add(r)
        else:
            r = match.group(0)
            self.undef_name.add(r)
        return r

    def BitCount(self, string):
        count = 0
        for s in string.split("_"):
            if re.match(r"[01x]+", s):
                count += len(s)
            else:
                g = re.match(r"\w+:(\d+)", s)
                if g:
                    count += int(g.group(1))
                else:
                    raise ValueError(s)
        return count

    def BitField(self, string):
        field = {}
        temp = string.split("_")
        temp.reverse()
        pos = 0
        for s in temp:
            if re.match(r"[01x]+", s):
                pos += len(s)
            else:
                g = re.match(r"(\w+):(\d+)", s)
                if g:
                    name = g.group(1)
                    size = int(g.group(2))
                    field[name] = (size, pos)
                    pos += size
                else:
                    raise ValueError("%s %s" % (s, string))
        return field

if __name__=="__main__":
    import argparse
    import copy
    import re

    class py16_Action(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setup16 = setup(thumb16, thumb16sub, 16)
            setup16.conv()
            print setup16.output_string

    class py32_Action(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setup32 = setup(thumb32, thumb32sub, 32)
            setup32.conv()
            print setup32.output_string

    class test_Action(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            table_sub = [
("<index32>","[<Rn>,#-<imm8>]",       "Rn:4_xxxx_x_1_0_0_imm8:8"),
("<index32>","[<Rn>,#+<imm8>]",       "Rn:4_xxxx_x_1_1_0_imm8:8"),
]

            table = [
("STRB<c>",       "<Rt>,<index32>",             "111110000000xxxx_Rt:4_1_xxx_xxxxxxxx"),
("STR<c>.W",      "<Rt>,[<Rn>,#<imm12>]",       "111110001100_Rn:4_Rt:4_imm12:12"),
]
            setup32 = setup(table, table_sub, 32)
            setup32.conv()
            print setup32.output_string

    parser = argparse.ArgumentParser()
    parser.add_argument('--py32', nargs=0, action=py32_Action, help=u"32bit命令のテスト")
    parser.add_argument('--py16', nargs=0, action=py16_Action, help=u"16bit命令のテスト")
    parser.add_argument('--test', nargs=0, action=test_Action, help=u"テスト")
    parser.add_argument('--setup', action='store_true', help=u"v7m.pyの作成")
    parser.add_argument('--output', nargs=1, help=u"出力ファイルの設定", default=["v7m.py"])
    args = parser.parse_args()

    if args.setup:
        output_filename = args.output[0]
        print "output file: %s" % output_filename

        setup16 = setup(thumb16, thumb16sub, 16)
        setup16.conv()
        setup32 = setup(thumb32, thumb32sub, 32)
        setup32.conv()
        output_data = setup16.output_string + setup32.output_string
        with open(output_filename, "wb") as f:
            f.write(output_data)

        print "done"
