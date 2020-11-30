import lectureJson as lj
import codage as cod

cheminTEXT = "text.json"
cheminTEXTOUT = "out-text.json"

x = lj.read(cheminTEXT, "text")
print(x)

table = cod.build_Frequency_Table(x)
print(table)

#lj.write(cheminTEXTOUT, "textEncode", x)