import pandas as pd
import numpy as np  

state_encoding_map = {
    1: 'Jammu_&_Kashmir',
    2: 'Himachal_Pradesh',
    3: 'Punjab',
    4: 'Chandigarh',
    5: 'Uttarakhand',
    6: 'Haryana',
    7: 'Delhi',
    8: 'Rajasthan',
    9: 'Uttar_Pradesh',
    10: 'Bihar',
    11: 'Sikkim',
    12: 'Arunachal_Pradesh',
    13: 'Nagaland',
    14: 'Manipur',
    15: 'Mizoram',
    16: 'Tripura',
    17: 'Meghalaya',
    18: 'Assam',
    19: 'West_Bengal',
    20: 'Jharkhand',
    21: 'Odisha',
    22: 'Chhattisgarh',
    23: 'Madhya_Pradesh',
    24: 'Gujarat',
    25: 'Daman_&_Diu',
    26: 'D_&_N_Haveli',
    27: 'Maharashtra',
    28: 'Andhra_Pradesh',
    29: 'Karnataka',
    30: 'Goa',
    31: 'Lakshadweep',
    32: 'Kerala',
    33: 'Tamil_Nadu',
    34: 'Puducherry',
    35: 'A_&_N_Islands',
    36: 'Telangana'
}

sector = {
    1: 'Rural',
    2: 'Urban'
}

district_encoding_map = {
    35: {
        1: "Nicobars", 2: "North & Middle Andaman", 3: "South Andaman"
    },
    28: {
        1: "Srikakulam", 2: "Vizianagaram", 3: "Visakhapatnam",
        4: "East Godavari", 5: "West Godavari", 6: "Krishna",
        7: "Guntur", 8: "Prakasam", 9: "Sri Potti Sriramulu Nellore",
        10: "Y.S.R. (Cuddapah)", 11: "Kurnool", 12: "Anantapur",
        13: "Chittoor"
    },
    12: {
        1: "Tawang", 2: "West Kameng", 3: "East Kameng", 4: "Papum Pare",
        5: "Upper Subansiri", 6: "West Siang", 7: "East Siang", 8: "Upper Siang",
        9: "Changlang", 10: "Tirap", 11: "Lower Subansiri", 12: "Kurung Kumey",
        13: "Dibang Valley", 14: "Lower Dibang Valley", 15: "Lohit", 16: "Anjaw"
    },
    18: {
        8: "Lakhimpur", 9: "Dhemaji", 10: "Tinsukia", 11: "Dibrugarh",
        12: "Sivasagar", 13: "Jorhat", 14: "Golaghat", 1: "Kokrajhar",
        2: "Dhubri", 3: "Goalpara", 4: "Barpeta", 20: "Bongaigaon",
        21: "Chirang", 22: "Kamrup", 23: "Kamrup Metropolitan", 24: "Nalbari",
        25: "Baksa", 15: "Karbi Anglong", 16: "Dima Hasao", 17: "Cachar",
        18: "Karimganj", 19: "Hailakandi", 5: "Morigaon", 6: "Nagaon",
        7: "Sonitpur", 26: "Darrang", 27: "Udalguri"
    },
    10: {
        1: "Pashchim Champaran", 2: "Purba Champaran", 3: "Sheohar",
        4: "Sitamarhi", 5: "Madhubani", 6: "Supaul", 7: "Araria",
        8: "Kishanganj", 9: "Purnia", 10: "Katihar", 11: "Madhepura",
        12: "Saharsa", 13: "Darbhanga", 14: "Muzaffarpur", 15: "Gopalganj",
        16: "Siwan", 17: "Saran", 18: "Vaishali", 19: "Samastipur",
        20: "Begusarai", 21: "Khagaria", 22: "Bhagalpur", 23: "Banka",
        24: "Munger", 25: "Lakhisarai", 26: "Sheikhpura", 27: "Nalanda",
        28: "Patna", 29: "Bhojpur", 30: "Buxar", 31: "Kaimur (Bhabua)",
        32: "Rohtas", 33: "Aurangabad", 34: "Gaya", 35: "Nawada",
        36: "Jamui", 37: "Jehanabad", 38: "Arwal"
    },
    4: {
        1: "Chandigarh"
    },
    22: {
        1: "Koriya", 2: "Surguja", 26: "Surajpur", 27: "Balrampur",
        3: "Jashpur", 4: "Raigarh", 5: "Korba", 6: "Janjgir-Champa",
        7: "Bilaspur", 8: "Kabeerdham", 9: "Rajnandgaon", 10: "Durg",
        11: "Raipur", 12: "Mahasamund", 13: "Dhamtari", 19: "Balodabazar",
        20: "Gariyaband", 23: "Bemetara", 24: "Balod", 25: "Mungeli",
        14: "Uttar Bastar Kanker", 15: "Bastar", 16: "Narayanpur",
        17: "Dakshin Bastar Dantewada", 18: "Bijapur", 21: "Kondagaon",
        22: "Sukama"
    },
    26: {
        1: "Dadra & Nagar Haveli"
    },
    25: {
        1: "Diu", 2: "Daman"
    },
    7: {
        1: "North West", 2: "North", 3: "North East", 4: "East",
        5: "New Delhi", 6: "Central", 7: "West", 8: "South West",
        9: "South"
    },
    30: {
        1: "North Goa", 2: "South Goa"
    },
    24: {
        17: "Panch Mahals", 18: "Dohad", 19: "Vadodara", 20: "Narmada",
        21: "Bharuch", 22: "The Dangs", 23: "Navsari", 24: "Valsad",
        25: "Surat", 26: "Tapi", 29: "Chhota Udepur", 32: "Mahisagar",
        4: "Mahesana", 5: "Sabar Kantha", 6: "Gandhinagar", 7: "Ahmadabad",
        15: "Anand", 16: "Kheda", 27: "Arvalli", 2: "Banas Kantha",
        3: "Patan", 1: "Kachchh", 8: "Surendranagar", 9: "Rajkot",
        10: "Jamnagar", 11: "Porbandar", 12: "Junagadh", 13: "Amreli",
        14: "Bhavnagar", 28: "Botad", 30: "Dev Bhumi-Dwarka", 31: "Gir Somnath",
        33: "Morbi"
    },
    6: {
        1: "Panchkula", 2: "Ambala", 3: "Yamunanagar", 4: "Kurukshetra",
        5: "Kaithal", 6: "Karnal", 7: "Panipat", 8: "Sonipat",
        14: "Rohtak", 15: "Jhajjar", 18: "Gurgaon", 19: "Mewat",
        20: "Faridabad", 21: "Palwal", 9: "Jind", 10: "Fatehabad",
        11: "Sirsa", 12: "Hisar", 13: "Bhiwani", 16: "Mahendragarh",
        17: "Rewari"
    },
    2: {
        2: "Kangra", 4: "Kullu", 5: "Mandi", 6: "Hamirpur",
        7: "Una", 1: "Chamba", 3: "Lahul & Spiti", 8: "Bilaspur",
        9: "Solan", 10: "Sirmaur", 11: "Shimla", 12: "Kinnaur"
    },
    1: {
        7: "Kathua", 21: "Jammu", 22: "Samba", 5: "Punch",
        6: "Rajouri", 16: "Doda", 17: "Ramban", 18: "Kishtwar",
        19: "Udhampur", 20: "Reasi", 1: "Kupwara", 2: "Badgam",
        8: "Baramula", 9: "Bandipore", 10: "Srinagar", 11: "Ganderbal",
        12: "Pulwama", 13: "Shupiyan", 14: "Anantnag", 15: "Kulgam",
        3: "Leh", 4: "Kargil"
    },
    20: {
        1: "Garhwa", 12: "Lohardaga", 13: "Purbi Singhbhum", 14: "Palamu",
        19: "Latehar", 20: "Ranchi", 21: "Khunti", 22: "Gumla",
        23: "Simdega", 24: "Pashchimi Singhbhum", 11: "Saraikela-Kharsawan",
        2: "Chatra", 3: "Kodarma", 4: "Giridih", 5: "Deoghar",
        6: "Godda", 7: "Sahibganj", 8: "Pakur", 9: "Dhanbad",
        10: "Bokaro", 15: "Hazaribagh", 16: "Ramgarh", 17: "Dumka",
        18: "Jamtara"
    },
    29: {
        9: "Uttara Kannada", 15: "Udupi", 21: "Dakshina Kannada", 14: "Shimoga",
        16: "Chikmagalur", 20: "Hassan", 22: "Kodagu", 17: "Tumkur",
        18: "Bangalore", 19: "Mandya", 23: "Mysore", 24: "Chamarajanagar",
        27: "Kolar", 28: "Chikkaballapura", 29: "Bangalore Rural", 30: "Ramanagara",
        1: "Belgaum", 2: "Bagalkot", 3: "Bijapur", 4: "Bidar",
        5: "Raichur", 6: "Koppal", 7: "Gadag", 8: "Dharwad",
        10: "Haveri", 11: "Bellary", 12: "Chitradurga", 13: "Davanagere",
        25: "Gulbarga", 26: "Yadgir"
    },
    32: {
        1: "Kasaragod", 2: "Kannur", 3: "Wayanad", 4: "Kozhikode",
        5: "Malappuram", 6: "Palakkad", 7: "Thrissur", 8: "Ernakulam",
        9: "Idukki", 10: "Kottayam", 11: "Alappuzha", 12: "Pathanamthitta",
        13: "Kollam", 14: "Thiruvananthapuram"
    },
    31: {
        1: "Lakshadweep"
    },
    23: {
        7: "Tikamgarh", 8: "Chhatarpur", 9: "Panna", 12: "Satna",
        13: "Rewa", 14: "Umaria", 43: "Shahdol", 44: "Anuppur",
        45: "Sidhi", 46: "Singrauli", 10: "Sagar", 11: "Damoh",
        26: "Vidisha", 27: "Bhopal", 28: "Sehore", 29: "Raisen",
        15: "Neemuch", 16: "Mandsaur", 17: "Ratlam", 18: "Ujjain",
        19: "Shajapur", 20: "Dewas", 21: "Dhar", 22: "Indore",
        25: "Rajgarh", 47: "Jhabua", 48: "Alirajpur", 33: "Katni",
        34: "Jabalpur", 35: "Narsimhapur", 36: "Dindori", 37: "Mandla",
        38: "Chhindwara", 39: "Seoni", 40: "Balaghat", 23: "Khargone (West Nimar)",
        24: "Barwani", 30: "Betul", 31: "Harda", 32: "Hoshangabad",
        49: "Khandwa (East Nimar)", 50: "Burhanpur", 1: "Sheopur",
        2: "Morena", 3: "Bhind", 4: "Gwalior", 5: "Datia",
        6: "Shivpuri", 41: "Guna", 42: "Ashoknagar"
    },
    27: {
        21: "Thane", 22: "Mumbai Suburban", 23: "Mumbai", 24: "Raigarh",
        32: "Ratnagiri", 33: "Sindhudurg", 25: "Pune", 26: "Ahmadnagar",
        30: "Solapur", 31: "Satara", 34: "Kolhapur", 35: "Sangli",
        1: "Nandurbar", 2: "Dhule", 3: "Jalgaon", 20: "Nashik",
        15: "Nanded", 16: "Hingoli", 17: "Parbhani", 18: "Jalna",
        19: "Aurangabad", 27: "Bid", 28: "Latur", 29: "Osmanabad",
        4: "Buldana", 5: "Akola", 6: "Washim", 7: "Amravati",
        8: "Wardha", 9: "Nagpur", 14: "Yavatmal", 10: "Bhandara",
        11: "Gondiya", 12: "Gadchiroli", 13: "Chandrapur"
    },
    14: {
        4: "Bishnupur", 5: "Thoubal", 6: "Imphal West", 7: "Imphal East",
        1: "Senapati", 2: "Tamenglong", 3: "Churachandpur", 8: "Ukhrul",
        9: "Chandel"
    },
    17: {
        1: "West Garo Hills", 2: "East Garo Hills", 3: "South Garo Hills",
        4: "West Khasi Hills", 5: "Ribhoi", 6: "East Khasi Hills.",
        7: "Jaintia Hills"
    },
    15: {
        1: "Mamit", 2: "Kolasib", 3: "Aizwal", 4: "Champhai",
        5: "Serchhip", 6: "Lunglei", 7: "Lawngtlai", 8: "Saiha"
    },
    13: {
        1: "Mon", 2: "Mokokchung", 3: "Zunheboto", 4: "Wokha",
        5: "Dimapur", 6: "Phek", 7: "Tuensang", 8: "Longleng",
        9: "Kiphire", 10: "Kohima", 11: "Peren"
    },
    21: {
        8: "Baleshwar", 9: "Bhadrak", 10: "Kendrapara", 11: "Jagatsinghapur",
        12: "Cuttack", 13: "Jajapur", 16: "Nayagarh", 17: "Khordha",
        18: "Puri", 19: "Ganjam", 20: "Gajapati", 21: "Kandhamal",
        22: "Baudh", 23: "Subarnapur", 24: "Balangir", 25: "Nuapada",
        26: "Kalahandi", 27: "Rayagada", 28: "Nabarangapur", 29: "Koraput",
        30: "Malkangiri", 1: "Bargarh", 2: "Jharsuguda", 3: "Sambalpur",
        4: "Debagarh", 5: "Sundargarh", 6: "Kendujhar", 7: "Mayurbhanj",
        14: "Dhenkanal", 15: "Anugul"
    },
    34: {
        1: "Yanam", 2: "Puducherry", 3: "Mahe", 4: "Karaikal"
    },
    3: {
        1: "Gurdaspur", 2: "Kapurthala", 3: "Jalandhar", 4: "Hoshiarpur",
        5: "Shahid Bhagat Singh Nagar", 15: "Amritsar", 16: "Tarn Taran",
        17: "Rupnagar", 18: "Sahibzada Ajit Singh Nagar", 21: "Pathankot",
        6: "Fatehgarh Sahib", 7: "Ludhiana", 8: "Moga", 9: "Firozpur",
        10: "Muktsar", 11: "Faridkot", 12: "Bhatinda", 13: "Mansa",
        14: "Patiala", 19: "Sangrur", 20: "Barnala", 22: "Fazilka"
    },
    8: {
        3: "Bikaner", 15: "Jodhpur", 16: "Jaisalmer", 17: "Barmer",
        18: "Jalor", 19: "Sirohi", 20: "Pali", 6: "Alwar",
        7: "Bharatpur", 8: "Dhaulpur", 9: "Karauli", 10: "Sawai Madhopur",
        11: "Dausa", 12: "Jaipur", 21: "Ajmer", 22: "Tonk",
        24: "Bhilwara", 25: "Rajsamand", 26: "Dungarpur", 27: "Banswara",
        32: "Udaipur", 23: "Bundi", 28: "Chittaurgarh", 29: "Kota",
        30: "Baran", 31: "Jhalawar", 33: "Pratapgarh", 1: "Sri Ganganagar",
        2: "Hanumangarh", 4: "Churu", 5: "Jhunjhunun", 13: "Sikar",
        14: "Nagaur"
    },
    11: {
        1: "North District", 2: "West District", 3: "South District", 4: "East District"
    },
    # Tamil Nadu (State Code 33)
    33: {
        1: "Thiruvallur", 2: "Chennai", 3: "Kancheepuram", 4: "Vellore",
        5: "Tiruvannamalai", 6: "Viluppuram", 16: "Cuddalore", 12: "Karur",
        13: "Tiruchirappalli", 14: "Perambalur", 15: "Ariyalur", 17: "Nagapattinam",
        18: "Thiruvarur", 19: "Thanjavur", 20: "Pudukkottai", 11: "Dindigul",
        21: "Sivaganga", 22: "Madurai", 23: "Theni", 24: "Virudhunagar",
        25: "Ramanathapuram", 26: "Thoothukkudi", 27: "Tirunelveli", 28: "Kanniyakumari",
        7: "Salem", 8: "Namakkal", 9: "Erode", 10: "The Nilgiris",
        29: "Dharmapuri", 30: "Krishnagiri", 31: "Coimbatore", 32: "Tiruppur"
    },
    # Telangana (State Code 36)
    36: {
        1: "Adilabad", 2: "Komaram Bheem", 3: "Mancherial", 4: "Nirmal",
        5: "Nizamabad", 15: "Kamareddy", 16: "Sangareddy", 17: "Medak",
        18: "Siddipet", 21: "Medchal-Malkajgiri", 22: "Hyderabad", 23: "Rangareddy",
        24: "Vikarabad", 25: "Mahbubnagar", 26: "Jogulamba", 27: "Wanaparthy",
        28: "Nagarkurnool", 6: "Jagtial", 7: "Peddapalli", 8: "Jayashankar",
        9: "Bhadradri", 10: "Mahabubabad", 11: "Warangal Rural", 12: "Warangal Urban",
        13: "Karimnagar", 14: "Rajanna", 19: "Jangaon", 20: "Yadadri",
        29: "Nalgonda", 30: "Suryapet", 31: "Khammam"
    },
    # Tripura (State Code 16)
    16: {
        1: "West Tripura", 2: "South Tripura", 3: "Dhalai", 4: "North Tripura"
    },
    # Uttarakhand (State Code 05)
    5: {
        1: "Uttarkashi", 2: "Chamoli", 3: "Rudraprayag", 4: "Tehri Garhwal",
        5: "Dehradun", 6: "Garhwal", 7: "Pithoragarh", 8: "Bageshwar",
        9: "Almora", 10: "Champawat", 11: "Nainital", 12: "Udham Singh Nagar",
        13: "Hardwar"
    },
    # Uttar Pradesh (State Code 09)
    9: {
        1: "Saharanpur", 2: "Muzaffarnagar", 3: "Bijnor", 4: "Moradabad",
        5: "Rampur", 6: "Jyotiba Phule Nagar", 7: "Meerut", 8: "Baghpat",
        9: "Ghaziabad", 10: "Gautam Buddha Nagar", 23: "Sitapur", 24: "Hardoi",
        25: "Unnao", 26: "Lucknow", 27: "Rae Bareli", 32: "Kanpur Dehat",
        33: "Kanpur Nagar", 41: "Fatehpur", 45: "Bara Banki", 42: "Pratapgarh",
        43: "Kaushambi", 44: "Allahabad", 46: "Faizabad", 47: "Ambedkar Nagar",
        48: "Sultanpur", 49: "Bahraich", 50: "Shrawasti", 51: "Balrampur",
        52: "Gonda", 53: "Siddharthnagar", 54: "Basti", 55: "Sant Kabir Nagar",
        56: "Maharajganj", 57: "Gorakhpur", 58: "Kushinagar", 59: "Deoria",
        60: "Azamgarh", 61: "Mau", 62: "Ballia", 63: "Jaunpur",
        64: "Ghazipur", 65: "Chandauli", 66: "Varanasi", 67: "Sant Ravidas Nagar(Bhadohi)",
        68: "Mirzapur", 69: "Sonbhadra", 34: "Jalaun", 35: "Jhansi",
        36: "Lalitpur", 37: "Hamirpur", 38: "Mahoba", 39: "Banda",
        40: "Chitrakoot", 11: "Bulandshahr", 12: "Aligarh", 13: "Mahamaya Nagar",
        14: "Mathura", 15: "Agra", 16: "Firozabad", 17: "Mainpuri",
        18: "Budaun", 19: "Bareilly", 20: "Pilibhit", 21: "Shahjahanpur",
        22: "Kheri", 28: "Farrukhabad", 29: "Kannauj", 30: "Etawah",
        31: "Auraiya", 70: "Etah", 71: "Kanshiram Nagar"
    },
    # West Bengal (State Code 19)
    19: {
        1: "Darjiling", 2: "Jalpaiguri", 3: "Koch Bihar", 20: "Alipurduar",
        21: "Kalimpong", 4: "Uttar Dinajpur", 5: "Dakshin Dinajpur", 6: "Maldah",
        7: "Murshidabad", 8: "Birbhum", 10: "Nadia", 11: "North Twenty Four Parganas",
        16: "Kolkata", 17: "South Twenty Four Parganas", 9: "Purba Barddhaman", 12: "Hugli",
        15: "Haora", 23: "Paschim Barddhaman", 13: "Bankura", 14: "Puruliya",
        18: "Paschim Medinipur", 19: "Purba Medinipur", 22: "Jhargram"
    }
}


def get_district_name(state_code: int, district_code: int, mapping_data: dict = district_encoding_map) -> str:

    try:
        if state_code not in mapping_data:
            return f"Error: State code '{state_code}' not found in list."
        
        state = mapping_data[state_code]
        
        if district_code not in state:
            return f"Error: District code '{district_code}' not found for State code '{state_code}'."
            
        return state[district_code]
        
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    

