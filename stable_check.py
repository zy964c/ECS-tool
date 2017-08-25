from functions import inch_to_mm
from APIE_Tool2v10_json import sta_value

plug = 456
stable_zone = [[465, 656], [1137, 1328], [1293, 2200]]
l = [list ((xrange(x[0], x[1]))) for x in stable_zone]
flat_list = [item for sublist in l for item in sublist]
mm_sta = map(lambda x: inch_to_mm(x), flat_list)
sta_to_exclude = map(lambda x: sta_value(x, plug), mm_sta)

print sta_to_exclude
