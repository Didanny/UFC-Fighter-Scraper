from selenium  import webdriver

driver = webdriver.Firefox()

# List to store the weight classes 
weight_classes = [
    'Flyweight',
    'Bantamweight',
    'Featherweight',
    'Lightweight',
    'Welterweight',
    'Middleweight',
    'Light_Heavyweight',
    'Heavyweight',
    'Women_Strawweight',
    'Women_Flyweight',
    'Women_Bantamweight',
    'Women_Featherweight'
]

# List to store the fighter hrefs 
fighter_hrefs = []

# Iterate over every weight class
for weight_class in weight_classes:
    driver.get('http://www.ufc.com/fighter/Weight_Class/' + weight_class)
    fighter_names = driver.find_elements_by_class_name('fighter-name')
    
    for fighter_name in fighter_names:
        fighter_hrefs.append(fighter_name.get_attribute('href'))

    steps = driver.find_elements_by_class_name('step')
    step_hrefs = []

    for step in steps:
        step_hrefs.append(step.get_attribute('href'))
    
    for step_href in step_hrefs:
        driver.get(step_href)
        fighter_names = driver.find_elements_by_class_name('fighter-name')

        for fighter_name in fighter_names:
            fighter_hrefs.append(fighter_name.get_attribute('href'))

# List to store the fighters
fighters = []

# Iterate over each fighter and store data
for fighter_href in fighter_hrefs:
    driver.get(fighter_href)

    name = driver.find_element_by_xpath('//meta[@property=\'og:title\']').get_attribute('content')
    record = driver.find_element_by_id('fighter-skill-record').get_attribute('innerText').split('-')
    wins = record[0]
    losses = record[1]
    draws = record[2].split(',')[0]
    
    try:
        summary = driver.find_element_by_id('fighter-skill-summary').get_attribute('innerText')
    except:
        summary = None

    try:
        fighter_from = driver.find_element_by_id('fighter-from').get_attribute('innerText')
    except:
        fighter_from = None        
    
    try:
        fighter_lives_in = driver.find_element_by_id('fighter-lives-in').get_attribute('innerText')
    except:
        fighter_lives_in = None
    
    try:
        age = driver.find_element_by_id('fighter-age').get_attribute('innerText')
    except:
        age = None   

    fighter = {
        'name': name,
        'record': {
            'wins': wins,
            'losses': losses,
            'draw': draws
        },
        'summary': summary,
        'from': fighter_from,
        'fights out of': fighter_lives_in,
        'age': age
    }
        
    fighters.append(fighter)



driver.close()
print(fighter_hrefs)

