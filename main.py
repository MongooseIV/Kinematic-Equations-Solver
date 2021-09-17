# Vf=Vi+at
# CX = ((Vi+Vf)/2)t
# CX=Vi+0.5at^2
# Vf^2=Vi^2+2aCX
import math

varDict = {"Vi": input("Vi: "), "Vf": input("Vf: "), "a": input("a: "), "t": input("t: "), "CX": input("CX: ")}
for i in varDict:
    try:
        varDict[i] = float(varDict[i])
    except:
        varDict[i] = False
# solve for t
if not varDict["t"]:
    if type(varDict["Vi"]) == float:
        if type(varDict["Vf"]) == float:
            if type(varDict["a"]) == float:
                varDict["t"] = (varDict["Vf"] - varDict["Vi"]) / varDict["a"]
            elif type(varDict["CX"] == float):
                varDict["t"] = varDict["CX"] / ((varDict["Vf"] + varDict["Vi"]) / 2)
        elif type(varDict["a"]) == float and type(varDict["CX"]) == float:
            varDict["t"] = math.sqrt((varDict["CX"] - varDict["Vi"]) / (0.5 * varDict["a"]))
    elif type(varDict["Vf"]) == float and type(varDict["a"]) == float and type(varDict["CX"]) == float:
        varDict["Vi"] = math.sqrt((varDict["Vf"] ** 2) - (2 * varDict["a"] * varDict["CX"]))
        varDict["t"] = (varDict["Vf"] - varDict["Vi"]) / varDict["a"]

# solve for delta X
if not varDict["CX"]:
    if type(varDict["Vi"]) == float:
        if type(varDict["Vf"]) == float:
            if type(varDict["a"]) == float:
                varDict["CX"] = ((varDict["Vf"] ** 2) - (varDict["Vi"] ** 2)) / (2 * varDict["a"])
            elif type(varDict["t"]) == float:
                varDict["CX"] = ((varDict["Vf"] + varDict["Vi"]) / 2) * varDict["t"]
        elif type(varDict["a"]) == float and type(varDict["t"]) == float:
            varDict["CX"] = varDict["Vi"] + (0.5 * varDict["a"] * (varDict("t")))
    elif type(varDict["t"]) == float and type(varDict["a"]) == float and type(varDict["Vf"]) == float:
        varDict["Vi"] = varDict["Vf"] - (varDict["a"] * varDict["t"])
        varDict["CX"] = varDict["Vi"] + (0.5 * varDict["a"] * (varDict("t")))

if not varDict["Vf"]:
    if type(varDict["Vi"]) == float:
        if type(varDict["a"]) == float:
            if type(varDict["t"]) == float:
                varDict["Vf"] = varDict["Vi"] - (varDict["a"] * varDict["t"])
            elif type(varDict["CX"]) == float:
                varDict["Vf"] = math.sqrt((varDict["Vi"] ** 2) - (2 * varDict["a"] * varDict["CX"]))
        elif type(varDict["t"]) == float and type(varDict["CX"]) == float:
            varDict["Vf"] = (2 * (varDict["CX"] / varDict["t"])) - varDict["Vi"]
    elif type(varDict["t"]) == float and type(varDict["CX"]) == float and type(varDict["a"]) == float:
        varDict["Vi"] = varDict["CX"] - (0.5 * (varDict["a"] * (varDict["t"] ** 2)))

print(varDict)
