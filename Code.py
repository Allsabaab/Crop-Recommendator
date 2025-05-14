crop_file = "/home/allsabaab/Documents/VSCode/Crop Recommendation/Crops.txt"
district_file = "/home/allsabaab/Documents/VSCode/Crop Recommendation/Districts.txt"

def crop_data():
    crop_dict = {}
    with open(crop_file) as f:
        for line in f:
            line = line.strip()
            crop_name = line.split(",")[0]
            fmin = float(line.split(",")[1])
            fmax = float(line.split(",")[2])
            nitro = line.split(",")[3]
            crop_dict[crop_name] = {"pHmin":fmin, "pHmax":fmax, "Nitrogen":nitro}
    return crop_dict

def recommend1(v,p,n):
    res = []
    loop = v.keys()
    for i in loop:
        if v[i]["pHmin"]<=p<=v[i]["pHmax"] and v[i]["Nitrogen"]==n:
            res.append(i)
    suit1 = ", ".join(res)
    return suit1, res

def recommend2(res,d):
    while True:
        
        dis_dict = {}
        with open(district_file) as f:
            for line in f:
                line = line.strip()
                line_list = line.split(",")
                dis = line_list[0]
                dis_dict[dis] = line_list[1:]
        final = []
        best = []
        if d in dis_dict.keys():
            for i in dis_dict[d]:
                final.append(i)
                if i in res:
                    best.append(i)
            suit2 = ", ".join(final)
            suit3 = ", ".join(best)
            return suit2, suit3
        else:
            print("District not found in the database.")
            continue

print("""
Welcome to the Crop Recommendation System.
""")
pH = float(input("pH of the Soil: "))
while True:
    try:
       n_level = [" ","High", "Medium", "Low"]
       N = int(input("Nitrogen level (1.High 2.Medium 3.Low): "))
       if N == 1:
           N = n_level[1]
           break
       elif N == 2:
           N = n_level[2]
           break
       elif N == 3:
           N = n_level[3]
           break
       else:
            print("Invalid Input! Please enter 1, 2 or 3.")
            continue
    except ValueError:
        print("Invalid Input! Please enter 1, 2 or 3.")
        continue

district = input("Enter your District: ").strip().title()
crops = crop_data()
suitable1, result = recommend1(crops, pH, N)
suitable2, suitable3 = recommend2(result, district)

print(f"""
Suitable Crops based on the Inputs: {suitable1}
""")
print(f"""Suitable Crops for your District: {suitable2}
""")
if suitable3:
    print(f"Best Suitable Crops for your land: {suitable3}")
