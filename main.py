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




