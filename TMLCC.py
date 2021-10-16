import pandas as pd
import math
radia_cal = {
    'O': 152*pow(10, -12),
    'C': 170*pow(10, -12),
    'Zn': 139*pow(10, -12),
    'H': 120*pow(10, -12),
    'N': 155*pow(10, -12),
    'P': 180*pow(10, -12),
    'Ba': 268*pow(10, -12),
    'F': 147*pow(10, -12),
    'Cu': 140*pow(10, -12),
    'V': 205*pow(10, -12),
    'S': 180*pow(10, -12),
    'Br': 185*pow(10, -12),
    'Cr': 200*pow(10, -12),
    'Cl': 175*pow(10, -12),
    'Ni': 163*pow(10, -12),
    'I': 198*pow(10, -12)}


def calculateMass(path):
    f = open(path, 'r').readlines()
    count = 0
    state = False
    cell = []
    volume = 0.0
    for x in f:
        if count > 5 and count < 9:
            cell_temp = str(x).split(" ")
            cell.append((float(cell_temp[len(cell_temp)-1]))*pow(10, -10))              
        if count > 21:
            # print(x)
            if x != '\n':
                aa = str(x).split(" ")
                # print(aa)
                temp = False
                for i in aa:
                    if temp and i != '':
                        a = float(aa[len(aa)-4])
                        b = float(aa[len(aa)-3])
                        c = float(aa[len(aa)-2])
                        volume_out = [0, 0, 0]
                        # print(i)
                        if (a > 0.5):
                            if ((1-a)*cell[0] < radia_cal[i]):
                                x = (1-a)*cell[0]
                                R = radia_cal[i]
                                h = R - x
                                r = pow((pow(R, 2)-pow(x, 2)), 1.0/2.0)
                                volume_out[0] = (math.pi*pow(h, 2)/3)*((3*r)-h)
                                # print(volume_out[0])
                        else:
                            if ((a)*cell[0] < radia_cal[i]):
                                x = (a)*cell[0]
                                R = radia_cal[i]
                                h = R - x
                                r = pow((pow(R, 2)-pow(x, 2)), 1.0/2.0)
                                volume_out[0] = (math.pi*pow(h, 2)/3)*((3*r)-h)
                                # print(volume_out[0])
                        if (b > 0.5):
                            if ((1-b)*cell[1] < radia_cal[i]):
                                x = (1-b)*cell[1]
                                R = radia_cal[i]
                                h = R - x
                                r = pow((pow(R, 2)-pow(x, 2)), 1.0/2.0)
                                volume_out[1] = (math.pi*pow(h, 2)/3)*((3*r)-h)
                                # print(x)
                                # print(R)
                                # print(h)
                                # print(r)
                                # print(volume_out[1])
                        else:
                            if ((b)*cell[1] < radia_cal[i]):
                                x = (b)*cell[1]
                                R = radia_cal[i]
                                h = R - x
                                r = pow((pow(R, 2)-pow(x, 2)), 1.0/2.0)
                                volume_out[1] = (math.pi*pow(h, 2)/3)*((3*r)-h)
                                # print(volume_out[1])
                        if (c > 0.5):
                            if ((1-c)*cell[2] < radia_cal[i]):
                                x = (1-c)*cell[2]
                                R = radia_cal[i]
                                h = R - x
                                r = pow((pow(R, 2)-pow(x, 2)), 1.0/2.0)
                                volume_out[2] = (math.pi*pow(h, 2)/3)*((3*r)-h)
                                # print(volume_out[2])
                        else:
                            if ((c)*cell[2] < radia_cal[i]):
                                x = (c)*cell[2]
                                R = radia_cal[i]
                                h = R - x
                                r = pow((pow(R, 2)-pow(x, 2)), 1.0/2.0)
                                volume_out[2] = (math.pi*pow(h, 2)/3)*((3*r)-h)
                                # print(volume_out[2])
                            volume += ((4/3)*math.pi*pow(radia_cal[i], 3))-max(volume_out)
                            # print(a)
                            # print(b)
                            # print(c)
                        break
                    temp = True
            if x == "\n":
                state = True
            if state:
                break
        count += 1
    return volume


mofname = []
mofVolume = []

for a in range(1, 10001, 1):
    
# for a in range(1, 2, 1):
    mofname.append('mof_unit_'+str(a))
    mofVolume.append(calculateMass(
        '../mof_cif_train/mof_cif_train/mof_unit_'+str(a)+'.cif'))
# for a in range(10001,20001,1):
#     mofname.append('mof_unit_'+str(a))
#     mofVolume.append(calculateMass('./mof_cif_train/mof_cif_train/mof_unit_'+str(a)+'.cif'))
# for a in range(20001,30001,1):
#     mofname.append('mof_unit_'+str(a))
#     mofVolume.append(calculateMass('./mof_cif_train/mof_cif_train/mof_unit_'+str(a)+'.cif'))
# for a in range(30001,40001,1):
#     mofname.append('mof_unit_'+str(a))
#     mofVolume.append(calculateMass('./mof_cif_train/mof_cif_train/mof_unit_'+str(a)+'.cif'))
for a in range(40001,50001,1):
    mofname.append('mof_unit_'+str(a))
    mofVolume.append(calculateMass('../mof_cif_train/mof_cif_train/mof_unit_'+str(a)+'.cif'))
for a in range(50001,60001,1):
    mofname.append('mof_unit_'+str(a))
    mofVolume.append(calculateMass('../mof_cif_train/mof_cif_train/mof_unit_'+str(a)+'.cif'))
for a in range(60001,68614,1):
    mofname.append('mof_unit_'+str(a))
    mofVolume.append(calculateMass('../mof_cif_train/mof_cif_train/mof_unit_'+str(a)+'.cif'))
re = {
    'MOFname': mofname,
    'Mof_volume': mofVolume
}
result = pd.DataFrame(data=re)
result.to_csv("Mof_volumeAtom.csv", index=False)
