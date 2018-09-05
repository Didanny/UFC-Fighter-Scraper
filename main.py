from selenium  import webdriver

driver = webdriver.Firefox()

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

for weight_class in weight_classes:
    driver.get('http://www.ufc.com/fighter/Weight_Class/' + weight_class)
    fighter_names = driver.find_elements_by_class_name('fighter-name').clear()
    print(fighter_names[0].href)


