voters = {
    'Purok 1, Juan Dela Cruz, 26',
    'Purok 2, Shelby Terrell, 17',
    'Purok 2, Stacy Newton, 12',
    'Purok 1, Phillip Summers, 18',
    'Purok 2, Kristine Travis, 19',
    'Purok 3, Yesenia Martinez, 15',
    'Purok 1, Lori Todd, 46',
    'Purok 4, Erin Day, 50',
    'Purok 1, Katherine Buck, 20',
    'Purok 1, Sheila Ross, 14',
    'Kangkong, Dave Farrell, 89',
    'Nangka, Isaiah Downs, 13'
}

brgyvoters = set()
skvoters = set()
notqualifiedvoters = set()
notresidence = set()

# Iterate through the voters and categorize them accordingly
for voter in voters:
    # Split the voter information into purok, name, and age
    purok, name, age = voter.split(', ')
    age = int(age)
    
    #Barangay Voters starting age is 18 years old to Up
    if purok.startswith(('Purok 1', 'Purok 2', 'Purok 3', 'Purok 4')) and  age >= 18:
        brgyvoters.add(name)
    elif purok.startswith(('Purok 1', 'Purok 2', 'Purok 3', 'Purok 4')):
        notqualifiedvoters.add(name)
        
    #SK Voters starting age is 15 years old to 30 years Old
    if purok.startswith(('Purok 1', 'Purok 2', 'Purok 3', 'Purok 4')) and (age >= 15 and age <= 30):
            skvoters.add(name)
    if not purok.startswith(('Purok 1', 'Purok 2', 'Purok 3', 'Purok 4')):
        notresidence.add(name)

# Print the results
print ("Qualified voters:", brgyvoters)
print ("SK voters:",skvoters)
print ("Not qualified voters:",notqualifiedvoters)
print ("Not residence:" ,notresidence)
