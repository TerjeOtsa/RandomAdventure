import pandas as pd
import os
# Given list of activities with realistic times and intensities
activities = [
    ("Visit the Viking Ship Museum", 60, 3),
    ("Explore Vigeland Park", 90, 4),
    ("Walk along Karl Johans gate", 60, 2),
    ("Tour the Royal Palace", 45, 3),
    ("Visit the National Gallery", 60, 2),
    ("Take a fjord cruise", 120, 5),
    ("Visit the Fram Museum", 60, 3),
    ("Explore the Akershus Fortress", 90, 4),
    ("Visit the Oslo Opera House", 45, 2),
    ("Go to the Munch Museum", 60, 3),
    ("Explore the Botanical Gardens", 90, 3),
    ("Visit the Kon-Tiki Museum", 60, 3),
    ("Hike in Nordmarka", 180, 8),
    ("Visit the Holmenkollen Ski Museum", 90, 4),
    ("Swim at Sørenga Seawater Pool", 60, 5),
    ("Visit the Astrup Fearnley Museum", 60, 2),
    ("Bike around Bygdøy Peninsula", 120, 6),
    ("Picnic in Frogner Park", 90, 2),
    ("Take a boat to the Oslo Fjord Islands", 180, 4),
    ("Visit the Nobel Peace Center", 60, 2),
    ("Visit the Norwegian Museum of Cultural History", 90, 3),
    ("Take a guided tour of Oslo City Hall", 45, 2),
    ("Explore Grünerløkka district", 120, 4),
    ("Attend a concert at Oslo Spektrum", 120, 3),
    ("Visit the Ekebergparken Sculpture Park", 90, 4),
    ("Enjoy a show at the Norwegian National Opera & Ballet", 180, 3),
    ("Go skiing in Oslo Winter Park", 180, 7),
    ("Explore the Aker Brygge and Tjuvholmen area", 90, 3),
    ("Visit the Historical Museum", 60, 2),
    ("Take a food tour", 120, 3),
    ("Watch a movie at the Odeon Cinema", 120, 1),
    ("Visit the Popsenteret", 60, 2),
    ("Play mini golf at Oslo Camping", 60, 4),
    ("Walk through the Barcode Project", 60, 3),
    ("Shop at the Oslo City Shopping Center", 90, 2),
    ("Relax at the Oslo Sauna", 60, 1),
    ("Go to a football match at Ullevaal Stadium", 120, 4),
    ("Visit the International Museum of Children's Art", 60, 2),
    ("Attend a festival at the Oslo Spectrum", 180, 3),
    ("Explore the Sørenga area", 90, 3),
    ("Go kayaking in the Oslo Fjord", 120, 6),
    ("Visit the Emanuel Vigeland Museum", 60, 2),
    ("Hike to Vettakollen", 120, 6),
    ("Take a tour of the Storting Building", 45, 2),
    ("Explore the Mathallen Food Hall", 90, 2),
    ("Attend an outdoor cinema event", 120, 1),
    ("Visit the Intercultural Museum", 60, 2),
    ("Walk around the St. Hanshaugen Park", 60, 3),
    ("Go to a performance at the Det Norske Teatret", 120, 3),
    ("Explore the Oslo Reptile Park", 60, 3),
    ("Visit the Armed Forces Museum", 60, 2),
    ("Take a street art tour", 90, 4),
    ("Go to a rooftop bar", 90, 2),
    ("Visit the Jewish Museum in Oslo", 60, 2),
    ("Attend a poetry reading", 60, 1),
    ("Explore the Vulkan area", 90, 3),
    ("Visit the DogA - Norwegian Centre for Design and Architecture", 60, 2),
    ("Hike to the Grefsenkollen viewpoint", 120, 6),
    ("Go on a ghost walk", 90, 4),
    ("Visit the Norwegian Maritime Museum", 60, 2),
    ("Explore the Stenersen Museum", 60, 2),
    ("Take a photography tour", 90, 4),
    ("Visit the Oslo Transport Museum", 60, 2),
    ("Take a yoga class", 60, 3),
    ("Visit the Oslo School Museum", 60, 2),
    ("Go on a fishing trip", 120, 4),
    ("Attend a classical music concert", 120, 1),
    ("Explore the Tøyen area", 90, 3),
    ("Visit the Norwegian Center for Studies of Holocaust and Religious Minorities", 60, 2),
    ("Walk along the Akerselva River", 120, 3),
    ("Take a pastry baking class", 90, 2),
    ("Go to a comedy club", 120, 2),
    ("Visit the Mini Bottle Gallery", 60, 2),
    ("Take a day trip to Drøbak", 240, 3),
    ("Visit the Nordiska Museet", 60, 2),
    ("Explore the Grønland area", 90, 3),
    ("Take a drawing class", 60, 2),
    ("Go to a board game café", 120, 2),
    ("Visit the NRK Television Tower", 60, 2),
    ("Visit the Natural History Museum", 60, 2),
    ("Go on a street food tour", 90, 3),
    ("Visit the Nobel Peace Prize Exhibition", 60, 2),
    ("Explore the Akershus Castle", 90, 3),
    ("Attend a dance class", 60, 4),
    ("Visit the Oslo Philharmonic", 120, 2),
    ("Walk around the Oslo University Botanical Garden", 90, 2),
    ("Take a beer tasting tour", 90, 4),
    ("Visit the National Museum of Art, Architecture and Design", 60, 2),
    ("Explore the Sørenga District", 90, 3),
    ("Go to a trampoline park", 60, 5),
    ("Visit the Ski Museum", 60, 3),
    ("Go bird watching at Østensjøvannet", 90, 3),
    ("Visit the Resistance Museum", 60, 2),
    ("Explore the Bygdøy area", 120, 3),
    ("Attend a language exchange event", 90, 2),
    ("Visit the Viking Planet", 60, 2),
    ("Take a boat tour of Oslo's harbor", 90, 3),
    ("Explore the Ekebergparken Sculpture Park", 90, 4),
      ("Cross-country skiing in Nordmarka", 180, 9),
    ("Mountain biking in Oslomarka", 120, 8),
    ("Trail running in Østmarka", 90, 9),
    ("Rock climbing at Kolsås", 90, 10),
    ("Kayaking in the Oslo Fjord", 120, 8),
    ("Snowshoe hiking in Nordmarka", 180, 9),
    ("Cycling from Oslo to Drøbak", 180, 8),
    ("Swimming in the Oslo Fjord", 90, 8),
    ("Long-distance running along Akerselva River", 120, 9),
    ("Intensive yoga session", 60, 8),
    ("High-intensity interval training (HIIT) at Frogner Park", 60, 10),
    ("Hiking to the top of Grefsenkollen", 120, 8),
    ("Paddleboarding in the Oslo Fjord", 90, 8),
    ("Ski touring in Oslo Winter Park", 180, 10),
    ("Mountain hike in the Oslo Fjord Islands", 180, 8),
    ("Rowing on the Oslo Fjord", 120, 9),
    ("Extreme sports at Oslo Sommerpark", 120, 10),
    ("Long-distance hiking from Sognsvann to Ullevålseter", 180, 8),
    ("Bootcamp session at Ekeberg Park", 60, 9),
    ("Power yoga class", 60, 8),
    ("Spinning class at the gym", 60, 8),
    ("Bootcamp workout session", 60, 9),
    ("CrossFit training", 60, 10),
    ("Interval running at the park", 45, 8),
    ("High-intensity aerobics class", 60, 9),
    ("Boxing workout", 45, 9),
    ("Circuit training session", 60, 8),
    ("Jump rope workout", 30, 9),
    ("Stair climbing exercise", 45, 8),
    ("Rowing machine workout", 60, 9),
     ("Walk in Frogner Park", 60, 2),
    ("Visit the Norwegian National Opera and Ballet", 120, 2),
    ("Take a guided bike tour of Oslo", 90, 3),
    ("Visit the Museum of Cultural History", 60, 2),
    ("Explore the Ekeberg Park", 120, 4),
    ("Go to a sauna boat", 90, 5),
    ("Take a cooking class", 90, 3),
    ("Visit the Oslo City Museum", 60, 2),
    ("Walk along the Oslo Fjord", 120, 3),
    ("Go to a music festival", 180, 4),
    ("Attend a fitness bootcamp", 60, 8),
    ("Join a dance workshop", 60, 4),
    ("Go ice skating at Frogner Stadium", 90, 5),
    ("Visit the Folk Museum", 60, 3),
    ("Take a guided kayak tour", 120, 6),
    ("Do a walking tour of Oslo", 90, 2),
    ("Attend a local theater performance", 120, 2),
    ("Go ziplining at Oslo Sommerpark", 60, 7),
    ("Take a guided historical tour", 90, 3),
    ("Do a photography walk", 60, 2),
    ("Attend a wine tasting event", 60, 3),
    ("Visit the Fram Museum", 60, 2),
    ("Go to a trampoline park", 60, 5),
    ("Visit the Oslo Science Center", 90, 3),
    ("Do a parkour class", 60, 7),
    ("Attend a jazz concert", 90, 2),
    ("Go to an escape room", 90, 4),
    ("Visit the Norwegian Museum of Technology", 90, 3),
    ("Take a guided city tour", 90, 2),
    ("Explore the Oslo Fjord Islands", 180, 3),
    ("Visit the Oslo Fire Museum", 60, 2),
    ("Take a yoga class", 60, 3),
    ("Go on a Nordic walking tour", 120, 4),
    ("Attend a cooking workshop", 90, 3),
    ("Visit the DogA Design Museum", 60, 2),
    ("Go to a roller skating rink", 60, 4),
    ("Do a guided forest hike", 120, 5),
    ("Visit the Vigeland Museum", 60, 2),
    ("Explore the Tjuvholmen Sculpture Park", 60, 2),
    ("Take a guided snowshoe hike", 120, 6),
    ("Go to a spa day", 120, 2),
    ("Take a guided art tour", 90, 2),
    ("Do a pilates class", 60, 3),
    ("Attend a chocolate making class", 60, 3),
    ("Go horseback riding", 90, 5),
    ("Take a guided boat tour", 90, 3),
    ("Attend a local fair", 120, 3),
    ("Go to a food market", 90, 2),
    ("Do a meditation session", 60, 1),
    ("Explore the Opera House", 60, 2),
    ("Go for a jog in St. Hanshaugen Park", 60, 4),
    ("Visit the Nobel Peace Center", 60, 2),
    ("Take a snowboarding class", 90, 8),
    ("Go to a poetry slam", 60, 2),
    ("Attend a cultural festival", 120, 3),
    ("Take a guided ice fishing trip", 120, 5),
    ("Do a graffiti tour", 90, 3),
    ("Go on a winter hike", 120, 4),
    ("Take a guided snorkeling tour", 90, 6),
    ("Visit the Historical Museum", 60, 2),
    ("Go to a local comedy show", 90, 2),
    ("Take a guided fjord safari", 120, 6),
    ("Do a high ropes course", 90, 7),
    ("Attend a beer festival", 120, 3),
    ("Explore the Sørenga Seawater Pool", 60, 4),
    ("Visit the National Theater", 60, 2),
    ("Go to a vintage market", 60, 2),
    ("Take a Nordic walking class", 90, 4),
    ("Visit the Museum of Magic", 60, 2),
    ("Go to a ballet performance", 120, 2),
    ("Take a nature photography class", 90, 3),
    ("Explore the Alna River Trail", 120, 3),
    ("Go to a cycling class", 60, 5),
    ("Do a fitness class in the park", 60, 5),
    ("Attend a storytelling event", 60, 2),
    ("Take a guided bird watching tour", 90, 3),
    ("Visit the Museum of Contemporary Art", 60, 2),
    ("Go to a science fair", 90, 2),
    ("Take a guided architecture tour", 90, 3),
    ("Do a strength training session", 60, 5),
    ("Go to a history lecture", 60, 2),
    ("Take a guided photography tour", 90, 3),
    ("Visit the Oslo Observatory", 60, 2),
    ("Attend a film screening", 90, 2),
    ("Do a city scavenger hunt", 90, 4),
    ("Go to a pottery class", 90, 2),
    ("Explore the Oslo Opera House", 60, 2),
    ("Do a city park run", 60, 4),
    ("Take a pastry class", 90, 3),
    ("Visit the National Gallery", 60, 2),
    ("Attend a local craft fair", 120, 2),
    ("Go to a beer tasting event", 60, 3),
    ("Take a high-intensity spin class", 60, 9),
    ("Attend a guided star gazing event", 60, 2),
    ("Go on a guided wildlife tour", 120, 4),
    ("Visit the Norwegian Museum of Magic", 60, 2),
    ("Explore the Akerselva River", 90, 3),
    ("Go to a local market", 60, 2),
    ("Do a circuit training workout", 60, 8),
    ("Attend a yoga workshop", 60, 3),
    ("Take a cooking class", 90, 3),
    ("Do a hiking and yoga retreat", 120, 4),
    ("Explore the Mathallen Food Hall", 90, 2),
]

# Create a DataFrame
activities_df = pd.DataFrame(activities, columns=["activity", "time", "intensity"])

# Save to a CSV file
os.makedirs('activities', exist_ok=True)
activities_df.to_csv('activities/oslo.csv', index=False)

activities_df.head()  # Display the first few rows for verification