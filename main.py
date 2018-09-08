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
    
    fighter = {}

    try:
        fighter['name'] = driver.find_element_by_xpath('//meta[@property=\'og:title\']').get_attribute('content')
    except:
        pass
    
    try:
        record = driver.find_element_by_id('fighter-skill-record').get_attribute('innerText').split('-')
        fighter['record'] = {}
        fighter['record']['wins'] = record[0]
        fighter['record']['losses'] = record[1]
        fighter['record']['draws'] = record[2].split(',')[0]
    except:
        pass
    
    try:
        fighter['summary'] = driver.find_element_by_id('fighter-skill-summary').get_attribute('innerText')
    except:
        pass

    try:
        fighter['from'] = driver.find_element_by_id('fighter-from').get_attribute('innerText')     
    except:
        pass
    
    try:
        fighter['fights_out_of'] = driver.find_element_by_id('fighter-lives-in').get_attribute('innerText')
    except:
        pass
    
    try:
        fighter['age'] = driver.find_element_by_id('fighter-age').get_attribute('innerText')
    except:
        pass
        
    try:
        fighter['nickname'] = driver.find_element_by_id('fighter-nickname').get_attribute('innerText')
    except:
        pass

    try:
        height = driver.find_element_by_id('fighter-height').get_attribute('innerText').split(' ')
        fighter['height_cm'] = height[3]
        fighter['height_ft'] = height[0] + height[1]
    except:
        pass

    try:
        weight = driver.find_element_by_id('fighter-weight').get_attribute('innerText').split(' ')
        fighter['weight_lb'] = weight[0]
        fighter['weight_kg'] = weight[3]     
    except:
        pass
        
    try:
        fighter['reach'] = driver.find_element_by_id('fighter-reach').get_attribute('innerText').split('"')[0]
    except:
        pass
        
    try:
        fighter['leg_reach'] = driver.find_element_by_id('fighter-leg-reach').get_attribute('innerText').split('"')[0]
    except:
        pass
        
    try:
        fighter['college'] = driver.find_element_by_id('fighter-college').get_attribute('innerText')
    except:
        pass
        
    try:
        fighter['degree'] = driver.find_element_by_id('fighter-degree').get_attribute('innerText')
    except:
        pass
    
    try:
        stats = driver.find_elements_by_class_name('bar-text')
        fighter['strikes'] = {}
        fighter['strikes']['total_successful'] = stats[1].get_attribute('innerText')
        fighter['striking_types'] = {}
        fighter['striking_types']['standing'] = stats[-11].get_attribute('innerText')
        fighter['striking_types']['clinch'] = stats[-10].get_attribute('innerText')
        fighter['striking_types']['ground'] = stats[-9].get_attribute('innerText')
        fighter['takedowns'] = {}
        fighter['takedowns']['total_successful'] = stats[-7].get_attribute('innerText')
        fighter['grappling'] = {}
        fighter['grappling']['submissions'] = stats[-3].get_attribute('innerText')
        fighter['grappling']['passes'] = stats[-2].get_attribute('innerText')
        fighter['grappling']['sweeps'] = stats[-1].get_attribute('innerText')
        
        stats = driver.find_elements_by_class_name('max-number')
        fighter['strikes']['total_attempted'] = stats[0].get_attribute('innerText')
        fighter['takedowns']['total_attempted'] = stats[2].get_attribute('innerText')
    except:
        pass
    
    try:
#        stats = driver.find_elements_by_css_selector('.cufon.cufon-canvas')
#        for i, stat in stats:
#            stat = stat.get_attribute('alt')
#            if stat == 'Striking':
#                fighter['striking_defense'] = stats[i + 1].get_attribute('alt')
#            if stats == 'Grappling':
#                fighter['takedown_defense'] = stats[i + 1].get_attribute('alt')
        
        stats = driver.find_elements_by_css_selector('.cufon.cufon-canvas')
        for i,stat in enumerate(stats):
            if stat.get_attribute('alt') == 'Striking':
#                print(stats[i + 1].get_attribute('alt'))
                fighter['striking_defense'] = stats[i + 1].get_attribute('alt')
            if stat.get_attribute('alt') == 'Grappling':
#                print(stats[i + 1].get_attribute('alt'))
                fighter['takedown_defense'] = stats[i + 1].get_attribute('alt')
    except:
        pass
            
        
    fighters.append(fighter)



#driver.close()
#print(fighter_hrefs)
#
#benavidez = []
#beltran = []
#
#driver.get('http://www.ufc.com/fighter/Joseph-Benavidez')
#
#stats = driver.find_elements_by_css_selector('.cufon.cufon-canvas')
#for i,stat in enumerate(stats):
#    benavidez.append(stat.get_attribute('alt'))
#    if stat.get_attribute('alt') == 'Striking':
#        print(stats[i + 1].get_attribute('alt'))
#    if stat.get_attribute('alt') == 'Grappling':
#        print(stats[i + 1].get_attribute('alt'))
#    
#driver.get('http://www.ufc.com/fighter/Marco-Beltran')
#
#stats = driver.find_elements_by_css_selector('.cufon.cufon-canvas')
#for i,stat in enumerate(stats):
#    beltran.append(stat.get_attribute('alt'))
#    if stat.get_attribute('alt') == 'Striking':
#        print(stats[i + 1].get_attribute('alt'))
#    if stat.get_attribute('alt') == 'Grappling':
#        print(stats[i + 1].get_attribute('alt'))
    

# Go to the first page of past events
driver.get('http://www.ufc.com/event/Past_Events')

# List to store the past event hrefs
past_event_hrefs = []

# Get the past event hrefs from the first page
past_events = driver.find_elements_by_css_selector('.event-title a')
for past_event in past_events:
    past_event_hrefs.append(past_event.get_attribute('href'))

def next_found():
    try:
        driver.find_element_by_class_name('nextLink')
        return True
    except:
        return False

# Visit all pages and collect the past event hrefs 
while next_found():
    nextLink =  driver.find_element_by_class_name('nextLink').get_attribute('href')
    driver.get(nextLink)
    
    past_events = driver.find_elements_by_css_selector('.event-title a')
    for past_event in past_events:
        past_event_hrefs.append(past_event.get_attribute('href'))
        
        
# Get all past event info
for past_event_href in past_event_hrefs:
    driver.get(past_event_href)
    
    
    
    
    
    