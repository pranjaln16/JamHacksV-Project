def solubility(ion1, ion2):
    #print(ion1, ion2)
    if ion1 == nitrate:
        return "aq"
    if ion1 == chloride:
        if ion2 == copper_ion or ion2 == silver_ion or ion2 == mercury_ion or ion2 == lead_ion: 
            return "s"
        else: 
            return "aq"
    if ion1 == sulfate: 
        if ion2 == calcium or ion2 == barium_ion or ion2 == strontium_ion or ion2 == mercury_ion or ion2 == lead_ion or ion2 == silver_ion:
            return "s"
        else: 
            return "aq"
    if ion1 == sodium_ion:
        return "aq"
    if ion1 == ammonium:
        return "aq"
    if ion1 == potassium_ion: 
        return "aq"
    if ion1 == carbonate:
        if ion2 in Group1 or ion2 == ammonium:
            return "aq"
        else:
            return "s"
    if ion1 == phosphate:
        if ion2 in Group1 or ion2 == ammonium:
            return "aq"
        else:
            return "s"
    if ion1 == hydroxide:
        if ion2 in Group1 or ion2 == calcium:
            return "aq"
        else:
            return "s"
    if ion1 == acetate:
        if ion2 == silver_ion:
          return "s"
        else:
          return "aq"
    if ion1 == sulfide:
        if ion2 in Group1 or ion2 in Group2 or ion2 == ammonium: 
            return "aq"
        else:
            return "s"

for i in IONS:
  for j in all_ions:
    print(solubility(i, j))

HOFBRINCL = [hydrogen, oxygen, fluorine, bromine, iodine, nitrogen, chlorine]
