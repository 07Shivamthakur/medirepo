# Ask for patient's name and age
name = input("Enter patient's name: ")
age = int(input("Enter patient's age: "))
gender= input("Enter patient's gender: ")
# Ask for blood test values
WBC_count = float(input("Enter WBC count (10^3/μL): "))
RBC_count = float(input("Enter RBC count (10^6/μL): "))
Hemoglobin = float(input("Enter Hemoglobin level (g/dL): "))
Hematocrit = float(input("Enter Hematocrit level (%): "))
MCV = float(input("Enter MCV (fL): "))
MCH = float(input("Enter MCH (pg): "))
MCHC = float(input("Enter MCHC (g/dL): "))
RDW = float(input("Enter RDW (%): "))
Platelets = float(input("Enter Platelet count (10^3/μL): "))
MPV = float(input("Enter MPV (fL): "))
PDW = float(input("Enter PDW (%): "))

# Print the patient's name and age
print(f"\nPatient Name: {name}")
print(f"Patient Age: {age}")

# Print the blood test results
print("\nBlood Test Results:")
print(f"WBC Count: {WBC_count} 10^3/μL")
print(f"RBC Count: {RBC_count} 10^6/μL")
print(f"Hemoglobin Level: {Hemoglobin} g/dL")
print(f"Hematocrit Level: {Hematocrit}%")
print(f"MCV: {MCV} fL")
print(f"MCH: {MCH} pg")
print(f"MCHC: {MCHC} g/dL")
print(f"RDW: {RDW}%")
print(f"Platelet Count: {Platelets} 10^3/μL")
print(f"MPV: {MPV} fL")
print(f"PDW: {PDW}%")

# Interpret the blood test results
if age >= 18:
    # Interpret the WBC count
    if WBC_count < 4.5:
        print("\nWBC count is low (leukopenia). This may indicate a weakened immune system or certain medical conditions.")
    elif WBC_count >= 4.5 and WBC_count <= 11:
        print("\nWBC count is normal.")
    else:
        print("\nWBC count is high (leukocytosis). This may indicate an infection or inflammation, among other things.")
        
    # Interpret the RBC count
    if RBC_count < 4.5:
        print("\nRBC count is low (anemia). This may indicate a deficiency in iron, vitamin B12, or folate.")
    elif RBC_count >= 4.5 and RBC_count <= 5.5:
        print("\nRBC count is normal.")
    else:
        print("\nRBC count is high (polycythemia). This may indicate dehydration, smoking, or certain medical conditions.")
        
    # Interpret the Hemoglobin level
    if age >= 18 and age <= 49:
        if Hemoglobin < 12.0:
            print("\nHemoglobin level is low (anemia). This may indicate a variety of medical conditions or nutritional deficiencies.")
        elif Hemoglobin >= 12.0 and Hemoglobin <= 15.5:
            print("\nHemoglobin level is normal.")
        else:
            print("\nHemoglobin level is high. This may indicate a medical condition or dehydration.")
    elif age >= 50:
        if Hemoglobin < 11.5:
            print("\nHemoglobin level is low (anemia). This may indicate a variety of medical conditions or nutritional deficiencies.")
        elif Hemoglobin >= 11.5 and Hemoglobin <= 15.5:
            print("\nHemoglobin level is normal.")
        else:
            print("\nHemoglobin level is high. This may indicate a medical condition or dehydration.")

# Interpret the hematocrit level
    if age >= 18:
        if gender == "male":
            if Hematocrit < 39:
                print("\nHematocrit level is low (anemia). This may indicate a deficiency of iron, vitamin B12, or folate, among other things.")
            elif Hematocrit >= 39 and Hematocrit <= 50:
                print("\nHematocrit level is normal.")
            else:
                print("\nHematocrit level is high. This may indicate dehydration or certain medical conditions, among other things.")
        elif gender == "female":
            if Hematocrit < 35:
                print("\nHematocrit level is low (anemia). This may indicate a deficiency of iron, vitamin B12, or folate, among other things.")
            elif Hematocrit >= 35 and Hematocrit <= 47:
                print("\nHematocrit level is normal.")
            else:
                print("\nHematocrit level is high. This may indicate dehydration or certain medical conditions, among other things.")

# Interpret the MCV value
    if MCV < 80:
        print("\nMCV is low. This may indicate iron deficiency anemia, thalassemia, or certain chronic diseases.")
    elif MCV >= 80 and MCV <= 100:
        print("\nMCV is normal.")
    else:
        print("\nMCV is high. This may indicate megaloblastic anemia, liver disease, or hypothyroidism, among other things.")

# Interpret the MCH value
    if MCH < 26:
        print("\nMCH is low. This may indicate iron deficiency anemia or thalassemia.")
    elif MCH >= 26 and MCH <= 34:
        print("\nMCH is normal.")
    else:
        print("\nMCH is high. This may indicate megaloblastic anemia or hemolysis.")

# Interpret the MCHC value
    if MCHC < 31:
        print("\nMCHC is low. This may indicate iron deficiency anemia or thalassemia.")
    elif MCHC >= 31 and MCHC <= 36:
        print("\nMCHC is normal.")
    else:
        print("\nMCHC is high. This may indicate spherocytosis or hemolysis.")

# Interpret the RDW value
    if RDW < 11.5:
        print("\nRDW is low. This may indicate microcytic anemia or hemoglobinopathies.")
    elif RDW >= 11.5 and RDW <= 14.5:
        print("\nRDW is normal.")
    else:
        print("\nRDW is high. This may indicate macrocytic anemia or hemolysis.")
# Interpret the Platelet count
    if Platelets < 150:
        print("\nPlatelet count is low (thrombocytopenia). This may indicate bleeding disorders, bone marrow disorders, or viral infections.")
    elif Platelets >= 150 and Platelets <= 450:
        print("\nPlatelet count is normal.")
    else:
        print("\nPlatelet count is high (thrombocytosis). This may indicate blood disorders, infections, or certain cancers.")

# Interpret the MPV value
    if MPV < 7:
        print("\nMPV is low. This may indicate hypoproductive thrombocytopenia or aplastic anemia.")
    elif MPV >= 7 and MPV <= 11:
        print("\nMPV is normal.")
    else:
        print("\nMPV is high. This may indicate hyperproductive thrombocytopenia or myeloproliferative disorders.")

# Interpret the PDW value
    if PDW < 15:
        print("\nPDW is low. This may indicate immune thrombocytopenia or von Willebrand disease.")
    elif PDW >= 15 and PDW <= 17:
        print("\nPDW is normal.")
    else:
        print("\nPDW is high. This may indicate thrombocytosis or platelet activation.")
