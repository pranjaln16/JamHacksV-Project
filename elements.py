hydrogen = ["hydrogen", "H", 1, 1] #HOFBRINCL
helium = ["helium", "He", 2, 8]
lithium = ["lithium", "Li", 2, 1]
beryllium = ["beryllium", "Be", 2, 2]
boron = ["boron", "B", 2, 3]
carbon = ["carbon", "C", 2, 4]
nitrogen = ["nitrogen", "N", 2, 5] #HOFBRINCL
oxygen = ["oxygen", "O", 2, 6] #HOFBRINCL
fluorine = ["fluorine", "F", 2, 7] #HOFBRINCL
neon = ["neon","Ne", 2, 8] 
sodium = ["sodium", "Na", 3, 1]
magnesium = ["magnesium","Mg", 3, 2 ]
aluminum = ["aluminum", "Al", 3, 3]
silicon = ["silicon", "Si", 3, 4]
phosphorous = ["phosphorous", "P", 3, 5]
sulfur = ["sulfur", "S", 3, 6]
chlorine = ["chlorine", "Cl", 3, 7] #HOFBRINCL
argon = ["argon", "Ar", 3, 8]
potassium = ["potassium", "K", 4, 1]
calcium = ["calcium", "Ca", 4, 2]
bromine = ["bromine", "Br", 4, 7] #HOFBRINCL
iodine = ["iodine", "I", 5, 7] #HOFBRINCL
ELEMENTS = [hydrogen, helium, lithium, beryllium, boron, carbon, nitrogen, oxygen, fluorine, neon, sodium, magnesium, aluminum, silicon, phosphorous, sulfur, chlorine, argon, potassium, calcium]
HOFBRINCL = [hydrogen, oxygen, fluorine, bromine, iodine, nitrogen, chlorine]

nitrate = ["NO3", -1]
chloride= ["Cl", -1]
sulfate = ["SO4", -2]
acetate = ["C2H3O2", -1]
sodium_ion = ["Na", 1]
potassium_ion = ["K", 1]
ammonium = ["NH4", 1]
carbonate = ["CO3", -2]
phosphate = ["PO4", -3]
hydroxide = ["OH", -1]
sulfide = ["S", -2]
IONS = [nitrate, chloride, sulfate, acetate, sodium_ion, potassium_ion, ammonium, carbonate, phosphate, hydroxide, sulfide]

#Various metal ions
lead_ion = ["Pb", 2]
copper_ion = ["Cu", 1]
silver_ion = ["Ag", 1]
mercury_ion = ["Hg", 2]
calcium_ion = ["Ca", 2]
strontium_ion = ["Sr", 2]
barium_ion = ["Ba", 2]

metal_ions = [lead_ion , silver_ion, mercury_ion, calcium_ion, strontium_ion, barium_ion]

all_ions = metal_ions + IONS

Group1 = []
Group2 = []

#list of ions
for i in ELEMENTS:
    if i[3] == 1:
        Group1.append(i)
    if i[3] == 2:
        Group2.append(i)
