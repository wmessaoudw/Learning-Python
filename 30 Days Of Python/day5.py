from logging import config
from os.path import join

list=[]
List_five=[1,2,3,4,5]
length=len(List_five)
print(len(List_five))
print(List_five[0])
print(List_five[int(length/2)])
print(List_five[-1])
mixed_list=["Messaoud",20,"Algeria",184,"Ante1"]
companies=["Facebook","Google","IBM","Microsoft"]
print(companies)
print(len(companies))
print(companies[0],companies[-1],companies[int(len(companies)/2)])
companies[2]="Apple"
print(companies)
companies.append("IT")
print(companies)
companies.insert(int(len(companies)/2),"IT2")
print(companies)
companies[0]=companies[0].upper()
print(companies)
companies=companies+["#:"]
print(companies)
print(companies.index("FACEBOOK"))
companies.sort()
print(companies)
companies.reverse()
print(companies)
first_three=companies[0:2]
last_three=companies[-1:-3]
middle_company=[int(len(companies)/2)]
del companies[0:2]
print(companies)
del companies[-1]
del companies[-1]
del companies[-1]
print(companies)
del companies[int(len(companies)/2)]
print(companies)
del companies[0:len(companies)]
print("this is",companies)
del companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
full_stack=front_end
full_stack.insert(full_stack.index("Redux")+1,"python")
full_stack.insert(full_stack.index("Redux")+1,"sql")
print(full_stack)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(min(ages),max(ages))
ages.append(min(ages))
ages.append(max(ages))
print(ages)
ages.sort()
print((ages[int(len(ages)/2)]+ages[(int(len(ages)/2) +1) ])/2)
avg=sum(ages)/len(ages)
print(sum(ages)/len(ages))
print(max(ages)-min(ages))
print(abs(min(ages)-avg),abs(max(ages)-avg))
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
middle=int(len(countries)/2)
print(countries[int(len(countries)/2)])
first_half=countries[0:middle]
second_half=countries[middle:]
print(first_half)
print(second_half)
last_list=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
one,two,three,*rst=last_list
print(one)
print(two)
print(three)
print(rst)