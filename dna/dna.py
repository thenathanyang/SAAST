def get_info():
    resp = raw_input("What would you like as your input file? ")
    resp2 = raw_input("What would you like as your output file? ")
    in_file = open(resp)
    #list_dna = dna()
    count = 0
    out = open(resp2, "w")
    for line in in_file.readlines():
        if count % 2 == 0:
            out.write("Region name: " + line)
        else:
            out.write("Nucleotides: " + line.upper())
            nucl = str(nucl_counts(line))
            nucl_numbers = nucl_counts(line)
            out.write("Nucleotide count: ",)
            out.write(nucl + "\n")
            totmass = str(total_mass(line, nucl_numbers))
            out.write("Total mass%: ",)
            out.write(totmass + "\n")
            codon = str(codons(line))
            out.write("Codons List: ",)
            out.write(codon + "\n")
            yes_no = proteins(line)
            out.write("Is Protein?: ",)
            out.write(yes_no + "\n")
        count = count + 1
    
# Counts the number of nucleobases
def nucl_counts(line):
    line = line.lower()
    adenine = line.count("a")
    cytosine = line.count("c")
    guanine = line.count("g")
    thymine = line.count("t")
    return [adenine, cytosine, guanine, thymine]

# Calculates the mass of the 
def total_mass(line, nucl_numbers):
    J = line.count("-")
    mass_adenine = 135.128 * nucl_counts(line)[0]
    mass_cytosine = 111.103 * nucl_counts(line)[1]
    mass_guanine = 151.128 * nucl_counts(line)[2]
    mass_thymine = 125.107 * nucl_counts(line)[3]
    mass_junk = 100.000 * J
    total_mass = mass_adenine + mass_cytosine + mass_guanine + mass_thymine + mass_junk
    return [round((mass_adenine / total_mass) * 100, 1), round((mass_cytosine / total_mass) * 100, 1), round((mass_guanine / total_mass) * 100, 1), round((mass_thymine / total_mass) * 100, 1)]

# Creates a codon list
def codons(line):
    line = line.replace("-", "")
    line = line.replace("\n", "")
    line = line.upper()
    count = 0
    codon_list = []
    for letter in line:
        if count%3 == 0:
            codon_list.append(line[count:count + 3])
        count = count + 1
    return codon_list

# Determines whether or not the codon list is a protein
def proteins(line):
    codon_list = codons(line)
    total_mass_list = total_mass(line, nucl_counts(line))
    if (codon_list[0] == "ATG") and ((codon_list[len(codon_list) - 1] == "TAA") or (codon_list[len(codon_list) - 1] == "TAG") or (codon_list[len(codon_list) - 1] == "TGA")) and (len(codon_list) >= 5) and (total_mass_list[1] + total_mass_list[2] >= 30.0):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    get_info();
