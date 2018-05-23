input_char="abcdefghijklmnopqrstuvwxyz"
output_char="cdefghijklmnopqrstuvwxyzab"
change = str.maketrans(output_char,input_char)
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
test=input("enter something: ")
print(test.translate(change))

