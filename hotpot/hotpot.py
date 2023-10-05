standard_prompt = '''
Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be: {input}
'''

reflection_prompt = '''You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an Docstore API environment and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>], or you used up your set number of reasoning steps. In a few sentences, Diagnose a possible reason for failure and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.  
Here are some examples:
Previous Trial:
Question: The Rome Protocols were signed by three Prime Ministers one of which was assassinated as part of what?
Thought 1: I need to search Rome Protocols, find the three Prime Ministers, then find what they were assassinated as part of.
Action 1: Search[Rome Protocols]
Observation 1: The Rome Protocols were a series of three international agreements concluded in Rome on 17 March 1934 between the governments of Austria, Hungary and Italy. They were signed by Italian Prime Minister Benito Mussolini, Austrian Chancellor Engelbert Dollfuss and Hungarian Prime Minister Gyula Gömbös. All of the protocols went into effect on 12 July 1934 and were registered in League of Nations Treaty Series on 12 December 1934.
Thought 2: The three Prime Ministers were Benito Mussolini, Engelbert Dollfuss, and Gyula Gömbös. I need to search Benito Mussolini and find what he was assassinated as part of.
Action 2: Search[Benito Mussolini]
Observation 2: Benito Amilcare Andrea Mussolini (UK:  MU(U)SS-ə-LEE-nee, US:  MOOSS-, Italian: [beˈniːto aˈmilkare anˈdrɛːa mussoˈliːni]; 29 July 1883 – 28 April 1945) was an Italian politician and journalist who founded and led the National Fascist Party (PNF). He was Prime Minister of Italy from the March on Rome in 1922 until his deposition in 1943, as well as "Duce" of Italian fascism from the establishment of the Italian Fasces of Combat in 1919 until his summary execution in 1945 by Italian partisans. As dictator of Italy and principal founder of fascism, Mussolini inspired and supported the international spread of fascist movements during the inter-war period.Mussolini was originally a socialist politician and a journalist at the Avanti! newspaper. In 1912, he became a member of the National Directorate of the Italian Socialist Party (PSI), but he was expelled from the PSI for advocating military intervention in World War I, in opposition to the party's stance on neutrality. In 1914, Mussolini founded a new journal, Il Popolo d'Italia, and served in the Royal Italian Army during the war until he was wounded and discharged in 1917. Mussolini denounced the PSI, his views now centering on Italian nationalism instead of socialism, and later founded the fascist movement which came to oppose egalitarianism and class conflict, instead advocating "revolutionary nationalism" transcending class lines. On 31 October 1922, following the March on Rome (28–30 October), Mussolini was appointed prime minister by King Victor Emmanuel III, becoming the youngest individual to hold the office up to that time. After removing all political opposition through his secret police and outlawing labor strikes, Mussolini and his followers consolidated power through a series of laws that transformed the nation into a one-party dictatorship. Within five years, Mussolini had established dictatorial authority by both legal and illegal means and aspired to create a totalitarian state. In 1929, Mussolini signed the Lateran Treaty with the Holy See to establish Vatican City.
Mussolini's foreign policy aimed to restore the ancient grandeur of the Roman Empire by expanding Italian colonial possessions and the fascist sphere of influence. In the 1920s, he ordered the Pacification of Libya, instructed the bombing of Corfu over an incident with Greece, established a protectorate over Albania, and incorporated the city of Fiume into the Italian state via agreements with Yugoslavia. In 1936, Ethiopia was conquered following the Second Italo-Ethiopian War and merged into Italian East Africa (AOI) with Eritrea and Somalia. In 1939, Italian forces annexed Albania. Between 1936 and 1939, Mussolini ordered the successful Italian military intervention in Spain in favor of Francisco Franco during the Spanish Civil War. Mussolini's Italy initially tried to avoid the outbreak of a second global war, sending troops at the Brenner Pass to delay Anschluss and taking part in the Stresa Front, the Lytton Report, the Treaty of Lausanne, the Four-Power Pact and the Munich Agreement. However, Italy then alienated itself from Britain and France by aligning with Germany and Japan. Germany invaded Poland on 1 September 1939, resulting in declarations of war by France and the UK and the start of World War II.
On 10 June 1940, Mussolini decided to enter the war on the Axis side. Despite initial success, the subsequent Axis collapse on multiple fronts and eventual Allied invasion of Sicily made Mussolini lose the support of the population and members of the Fascist Party. As a consequence, early on 25 July 1943, the Grand Council of Fascism passed a motion of no confidence in Mussolini; later that day King Victor Emmanuel III dismissed him as head of government and had him placed in custody, appointing Pietro Badoglio to succeed him as Prime Minister. After the king agreed to an armistice with the Allies, on 12 September 1943 Mussolini was rescued from captivity in the Gran Sasso raid by German paratroopers and Waffen-SS commandos led by Major Otto-Harald Mors. Adolf Hitler, after meeting with the rescued former dictator, then put Mussolini in charge of a puppet regime in northern Italy, the Italian Social Republic (Italian: Repubblica Sociale Italiana, RSI), informally known as the Salò Republic, causing a civil war. In late April 1945, in the wake of near total defeat, Mussolini and his mistress Clara Petacci attempted to flee to Switzerland, but both were captured by Italian communist partisans and summarily executed by firing squad on 28 April 1945 near Lake Como. The bodies of Mussolini and his mistress were then taken to Milan, where they were hung upside down at a service station to publicly confirm their demise.
Thought 3: Benito Mussolini was assassinated as part of the collapse of the Axis powers during World War II. So the Rome Protocols were signed by three Prime Ministers one of which was assassinated as part of World War II.
Action 3: Finish[World War II]

Reflection: I searched one of the prime ministers involved in the signing, then attemted to answer right away. I should have searched each of the prime ministers, then looked up 'death' on each of their pages in order to get more information before answering.

Previous Trial:
Question: Kam Heskin plays Paige Morgan in a 2004 film directed by who?
Thought 1: I need to search Kam Heskin and Paige Morgan, find the 2004 film they are in, then find the director of the film.
Action 1: Search[Kam Heskin]
Observation 1: Kam Erika Heskin (born May 8, 1973) is an American actress. She began her career playing Caitlin Deschanel on the NBC daytime soap opera Sunset Beach (1998–1999), before appearing in films Planet of the Apes (2001) and Catch Me If You Can (2002). Heskin went on in 2003 to play Elizabeth Bennet in an independent film Pride & Prejudice: A Latter-Day Comedy, Robin in Charmed (2004),  and Paige Morgan in The Prince and Me film franchise (2006–2010).
Thought 2: Kam Heskin plays Paige Morgan in The Prince and Me film franchise. I need to search The Prince and Me film franchise and find the director of the 2004 film.
Action 2: Search[The Prince and Me film franchise]
Observation 2: Could not find [The Prince and Me film franchise]. Similar: ['Kam Heskin', 'Prince of Persia', 'Harry Potter and the Half-Blood Prince (film)', 'Prince of Persia: The Sands of Time (film)', 'The Chronicles of Narnia (film series)', 'Majestic Prince (franchise)', 'Kingsman (franchise)', 'The Little Prince (2015 film)', 'Shrek (franchise)', 'Harry Potter (film series)']
Thought 3: I need to search The Prince and Me (2004 film) instead.
Action 3: Search[The Prince and Me (2004 film)]
Observation 3: Could not find [The Prince and Me (2004 film)]. Similar: ['The Prince & Me', 'The Prince & Me 2: The Royal Wedding', 'Kam Heskin', 'Prince of Darkness (film)', 'Prince of Persia: The Sands of Time (film)', 'Rob Knox', 'Alexander (2004 film)', 'Prince of Persia', 'Brooklynn Prince', 'Prince (musician)']
Thought 4: I need to search The Prince & Me (2004 film).
Action 4: Search[The Prince & Me (2004 film)]
Observation 4: Could not find [The Prince & Me (2004 film)]. Similar: ['The Prince & Me', 'The Prince & Me 2: The Royal Wedding', 'Prince of Darkness (film)', 'Prince of Persia: The Sands of Time (film)', 'Rob Knox', 'Alexander (2004 film)', 'Prince (musician)', 'Prince of Persia', 'Kam Heskin', 'Brooklynn Prince']
Thought 5: I need to search The Prince & Me (2004 film) instead.
Action 5: Search[The Prince & Me (2004 film)]
Observation 5: Could not find [The Prince & Me (2004 film)]. Similar: ['The Prince & Me', 'The Prince & Me 2: The Royal Wedding', 'Prince of Darkness (film)', 'Prince of Persia: The Sands of Time (film)', 'Rob Knox', 'Alexander (2004 film)', 'Prince (musician)', 'Prince of Persia', 'Kam Heskin', 'Brooklynn Prince']
Thought 6: I need to search The Prince & Me (2004 film).
Action 6: Search[The Prince & Me (2004 film)]
Observation 6: Could not find [The Prince & Me (2004 film)]. Similar: ['The Prince & Me', 'The Prince & Me 2: The Royal Wedding', 'Prince of Darkness (film)', 'Prince of Persia: The Sands of Time (film)', 'Rob Knox', 'Alexander (2004 film)', 'Prince (musician)', 'Prince of Persia', 'Kam Heskin', 'Brooklynn Prince']

Reflection: I got stuck in a loop where I kept trying to search 'The Prince & Me (2004 film)' but the page could not be found. Instead I should have tried to search the similar results that had a similar name to see and they were made in 2004.

Previous Trial:
Question: The Oberoi family is part of a hotel company that has a head office in what city?
Thought 1: I need to search the Oberoi family and find the city where the hotel company's head office is located.
Action 1: Search[Oberoi family]
Observation 1: The Oberoi Group is a luxury hotel group with its head office in New Delhi, India.[2] Founded in 1934, the company owns and operates 32 luxury hotels and two river cruise ships in 7 countries, primarily under its Oberoi Hotels & Resorts and Trident brands.[3] The group also operates The Oberoi Centre for Learning and Development, which is regarded as one of Asia's top institutions for hospitality education.[4]. The foundations of the Oberoi Group date back to 1934 when The Rai Bahadur Mohan Singh Oberoi, the founder of the group, bought two properties: the Maidens in Delhi and the Clarke's in Shimla.[5] In the following years Oberoi, assisted by his two sons, Tilak Raj Singh Oberoi and Prithvi Raj Singh Oberoi (P.R.S. Oberoi
Thought 2: The Oberoi Group has its head office in New Delhi, India. I just need to finish with New Delhi.
Action 2: Finish[New Delhi]
Observation 2: Episode finished, reward = 0

Reflection: I appeared to have retrieved the correct information about The Oberoi Family and the location of it's head office, and provided a corresponding answer. However this answer does not exactly match the ground truth answer so I should try a different wording, such as Delhi.

Previous trial:
{trajectory}Reflection:'''

cot_prompt = '''
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78\u20131.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Observation 1: Guitars for Wounded Warriors is the sixth solo studio album by guitarist Brian Tarquin, released in August 2014 by Cleopatra Records. In 2016, it received a Best Compilation Album nomination by the Independent Music Awards. All tracks were recorded at Tarquin's Jungle Room Studios in New Paltz (village), New York. Being moved by the lack of support for returning veterans through his life Tarquin decided to compose a heavy instrumental rock album as a way to show his appreciation to all veterans. So once again he enlisted top notch players to guest with him on the album, Billy Sheehan on Black Hawk, Ron \"Bumblefoot\" Thal and Reb Beach on Taliban Terror, Steve Morse on Freedom, Chris Poland on Charlie Surfs and Hunting, Chuck Loeb on Escape Kabul, Hal Lindes on Sand & Blood, Gary Hoey on 5 Klicks To Hell and Baghdad, Alex De Rosso Dokken on Broken Arrow, and The Flyin' Ryan Brothers on Surgical Strike.  The entire album was engineered, produced and composed by Tarquin especially for each one of the guest guitarists. Partial proceeds are donated to the Fisher House Foundation from sales.
Thought 2: Guitars for Wounded Warriors was recorded in New Paltz (village), New York. I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Observation 2: New Paltz is a village in Ulster County located in the U.S. state of New York. It is approximately 80 miles (130 km) north of New York City and 70 miles (110 km) south of Albany. The population was 7,324 at the 2020 census.[3]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

{input}
'''

cot_prompt_short = '''
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78\u20131.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

{input}
'''

cot_prompt_feedback_short = '''You are also an advanced reasoning agent that can improve based on self refection. Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78\u20131.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

You have attempted to answer the following question before and failed. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.

{trajectories}

{input}
'''

cot_prompt_feedback = '''You are also an advanced reasoning agent that can improve based on self refection. Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
After each observation, provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. This took place from 1780 to 1650 million years ago (Mya), during the Paleoproterozoic (Statherian Period). It is recorded in the Colorado orogen, a >500-km-wide belt of oceanic arc rock that extends southward into New Mexico. The Colorado orogeny was likely part of the larger Yavapai orogeny.
Thought 2: It does not mention the eastern sector of the Colorado orogeny. I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The Colorado orogen, formerly called the Colorado province, is a >500-km-wide belt of oceanic arc rock (1.78\u20131.65 Ga) that extends southward into New Mexico and composes a major part of the Proterozoic provinces of southwestern United States. This transcontinental collisional event occurred during the  Paleoproterozoic (Statherian Period).[1] The Wyoming sector of the Colorado orogeny was formerly called the Medicine Bow orogeny. The eastern sector extends into the High Plains and is called the Central Plains orogeny. The boundary between the Colorado orogeny and the Wyoming craton is the Cheyenne belt, a 5-km-wide mylonitic shear zone that verges northward. The Cheyenne belt transects and cuts off the south edge of the older Trans-Hudson orogeny.[2]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains, mainly in the Western United States, but also partly in the Midwest states of Nebraska, Kansas, and South Dakota, generally encompassing the western part of the Great Plains before the region reaches the Rocky Mountains. The High Plains are located in eastern Montana, southeastern Wyoming, southwestern South Dakota, western Nebraska, eastern Colorado, western Kansas, eastern New Mexico, western Oklahoma, and to just south of the Texas Panhandle.[4] The southern region of the Western High Plains ecology region contains the geological formation known as Llano Estacado which can be seen from a short distance or on satellite maps.[5] From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Observation 1: Guitars for Wounded Warriors is the sixth solo studio album by guitarist Brian Tarquin, released in August 2014 by Cleopatra Records. In 2016, it received a Best Compilation Album nomination by the Independent Music Awards. All tracks were recorded at Tarquin's Jungle Room Studios in New Paltz (village), New York. Being moved by the lack of support for returning veterans through his life Tarquin decided to compose a heavy instrumental rock album as a way to show his appreciation to all veterans. So once again he enlisted top notch players to guest with him on the album, Billy Sheehan on Black Hawk, Ron \"Bumblefoot\" Thal and Reb Beach on Taliban Terror, Steve Morse on Freedom, Chris Poland on Charlie Surfs and Hunting, Chuck Loeb on Escape Kabul, Hal Lindes on Sand & Blood, Gary Hoey on 5 Klicks To Hell and Baghdad, Alex De Rosso Dokken on Broken Arrow, and The Flyin' Ryan Brothers on Surgical Strike.  The entire album was engineered, produced and composed by Tarquin especially for each one of the guest guitarists. Partial proceeds are donated to the Fisher House Foundation from sales.
Thought 2: Guitars for Wounded Warriors was recorded in New Paltz (village), New York. I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Observation 2: New Paltz is a village in Ulster County located in the U.S. state of New York. It is approximately 80 miles (130 km) north of New York City and 70 miles (110 km) south of Albany. The population was 7,324 at the 2020 census.[3]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

You have attempted to answer the following question before and failed, either because your reasoning for the answer was incorrect or the phrasing of your response did not exactly match the answer. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.

{trajectories}
When providing the thought and action for the current trial, that into account these failed trajectories and make sure not to repeat the same mistakes and incorrect answers. 

{input}
'''

vote_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a list of trajectories, decide which trajectory is most promising. Analyze each trajectory in detail and consider possible errors, then conclude in the last line "The best trajectory is {s}", where s the integer id of the trajectory.
'''

compare_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Briefly analyze the correctness of the following two trajectories. Conclude in the last line "The more correct trajectory is 1", "The more correct trajectory is 2", or "The two trajectories are similarly correct".
'''

score_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by pairs of thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, analyze the following trajectory, then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.
'''

value_prompt = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, evaluate its correctness and provide your reasoning and analysis in detail. Focus on the latest thought, action, and observation. Incomplete trajectories can be correct if the thoughts and actions so far are correct, even if the answer is not found yet. Do not generate additional thoughts or actions. Then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Question: Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990?
Thought 1: I need to search for a list of Mexican Formula One race car drivers, then eliminate the one who drove for Force India and was born in 1990.
Action 1: Search[Formula One drivers from Mexico]
Observation 1: There have been six Formula One drivers from Mexico who have taken part in races since the championship began in 1950. Sergio P\u00e9rez is the most successful, having won six Grands Prix. Since 2021, P\u00e9rez drives for the Red Bull team.. P\u00e9rez is the only Mexican F1 driver to achieve a pole position. He took his first pole position at the 2022 Saudi Arabian Grand Prix, in his 219th Grand Prix meeting (a record for the most Grands Prix before a pole).
Thought 2: Sergio P\u00e9rez, born in 1990 and drove for Force India, is not the Mexican driver we are looking for. The passage does not give me enough information about other Mexican drivers who have achieved a podium finish. I need to look up more information.
Action 2: Lookup[Formula One drivers from Mexico]
Observation 2: No more results.
Thought 3: The available information doesn't allow me to determine which other Mexican Formula One race car driver, besides Sergio P\u00e9rez, has held the podium. With the search function failing to provide a full list of Mexican Formula One drivers, I need to return different search results. Let's try searching for Mexican Grand Prix winners, as they would have held the podium.
Action 3: Search[Mexican Grand Prix winners]
Observation 3: Could not find Mexican Grand Prix winners. Similar: ['Mexican Grand Prix', 'List of Formula One Grand Prix winners', '1990 Mexican Grand Prix', '2018 Mexican Grand Prix', '2019 Mexican Grand Prix'].
Thought 4: Given the difficulties in finding a direct list of Mexican Grand Prix winners, I should search for the Mexican Grand Prix to get a broader picture of the race's history. This might include winners.
Action 4: Search[Mexican Grand Prix]
Thus the correctness score is 3

Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?
Thought 1: I need to search for the football manager who recruited David Beckham, and then find out the timeframe in which he managed Manchester United.
Action 1: Search[David Beckham's football manager]
Observation 1: Could not find David Beckham's football manager. Similar: ['David Beckham', 'Inter Miami CF (redirect from Miami Beckham United)', 'Victoria Beckham', 'The Beckham Experiment', 'Miami Freedom Park'].
Thought 2: I couldn't find the information on David Beckham's football manager. I need to search Manchester United and find out the timeframe of the manager.
Action 2: Search[Manchester United]
Observation 2: Manchester United Football Club, commonly referred to as Man United (often stylised as Man Utd), or simply United, is a professional football club based in Old Trafford, Greater Manchester, England. The club competes in the Premier League, the top division in the English football league system. Nicknamed the Red Devils, they were founded as Newton Heath LYR Football Club in 1878, but changed their name to Manchester United in 1902. After a spell playing in Clayton, Manchester, the club moved to their current stadium, Old Trafford, in 1910.. Domestically, Manchester United have won a record 20 league titles, 12 FA Cups, six League Cups and a record 21 FA Community Shields.
Thought 3: The information about David Beckham's football manager is not available. I will search for Manchester United's managers to find the timeframe.
Action 3: Search[Manchester United managers]
Observation 3: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
Thought 4: The information about David Beckham's football manager is not available. The question asks for the timeframe when the manager managed Manchester United, so I need to find a list of Manchester United managers.
Action 4: Search[list of Manchester United managers]
Observation 4: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
Thus the correctness score is 4

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search Arthur's Magazine and First for Women, and find which was started first.
Action 1: Search[Arthur's Magazine]
Observation 1: Arthur's Magazine (1844\u00e2\u0080\u00931846) was an American literary periodical published in Philadelphia in the 19th century. Edited by Timothy Shay Arthur, it featured work by Edgar A. Poe, J.H. Ingraham, Sarah Josepha Hale, Thomas G. Spear, and others.[1][2] In May 1846 it was merged into Godey's Lady's Book.[3]
Thus the correctness score is 10

{input}
'''

value_prompt_feedback = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, evaluate its correctness and provide your reasoning and analysis in detail. Focus on the latest thought, action, and observation. Incomplete trajectories can be correct if the thoughts and actions so far are correct, even if the answer is not found yet. Do not generate additional thoughts or actions. Then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Question: Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990?
Thought 1: I need to search for a list of Mexican Formula One race car drivers, then eliminate the one who drove for Force India and was born in 1990.
Action 1: Search[Formula One drivers from Mexico]
Observation 1: There have been six Formula One drivers from Mexico who have taken part in races since the championship began in 1950. Sergio P\u00e9rez is the most successful, having won six Grands Prix. Since 2021, P\u00e9rez drives for the Red Bull team.. P\u00e9rez is the only Mexican F1 driver to achieve a pole position. He took his first pole position at the 2022 Saudi Arabian Grand Prix, in his 219th Grand Prix meeting (a record for the most Grands Prix before a pole).
Thought 2: Sergio P\u00e9rez, born in 1990 and drove for Force India, is not the Mexican driver we are looking for. The passage does not give me enough information about other Mexican drivers who have achieved a podium finish. I need to look up more information.
Action 2: Lookup[Formula One drivers from Mexico]
Observation 2: No more results.
Thought 3: The available information doesn't allow me to determine which other Mexican Formula One race car driver, besides Sergio P\u00e9rez, has held the podium. With the search function failing to provide a full list of Mexican Formula One drivers, I need to return different search results. Let's try searching for Mexican Grand Prix winners, as they would have held the podium.
Action 3: Search[Mexican Grand Prix winners]
Observation 3: Could not find Mexican Grand Prix winners. Similar: ['Mexican Grand Prix', 'List of Formula One Grand Prix winners', '1990 Mexican Grand Prix', '2018 Mexican Grand Prix', '2019 Mexican Grand Prix'].
Thought 4: Given the difficulties in finding a direct list of Mexican Grand Prix winners, I should search for the Mexican Grand Prix to get a broader picture of the race's history. This might include winners.
Action 4: Search[Mexican Grand Prix]
Thus the correctness score is 3

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search Arthur's Magazine and First for Women, and find which was started first.
Action 1: Search[Arthur's Magazine]
Observation 1: Arthur's Magazine (1844\u00e2\u0080\u00931846) was an American literary periodical published in Philadelphia in the 19th century. Edited by Timothy Shay Arthur, it featured work by Edgar A. Poe, J.H. Ingraham, Sarah Josepha Hale, Thomas G. Spear, and others.[1][2] In May 1846 it was merged into Godey's Lady's Book.[3]
Thus the correctness score is 10

{trajectories}
Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]
Thus the correctness score is 10

{input}
'''

value_prompt_reasoning = '''You are an advanced reasoning agent that can improve based on self refection. Analyze the trajectories of your previous solutions to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, evaluate its correctness and provide your reasoning and analysis in detail. Focus on the latest thought, action, and observation. Incomplete trajectories can be correct if the thoughts and actions so far are correct, even if the answer is not found yet. Do not generate additional thoughts or actions. Then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Question: Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990?
Thought 1: I need to search for a list of Mexican Formula One race car drivers, then eliminate the one who drove for Force India and was born in 1990.
Action 1: Search[Formula One drivers from Mexico]
Observation 1: There have been six Formula One drivers from Mexico who have taken part in races since the championship began in 1950. Sergio P\u00e9rez is the most successful, having won six Grands Prix. Since 2021, P\u00e9rez drives for the Red Bull team.. P\u00e9rez is the only Mexican F1 driver to achieve a pole position. He took his first pole position at the 2022 Saudi Arabian Grand Prix, in his 219th Grand Prix meeting (a record for the most Grands Prix before a pole).
Thought 2: Sergio P\u00e9rez, born in 1990 and drove for Force India, is not the Mexican driver we are looking for. The passage does not give me enough information about other Mexican drivers who have achieved a podium finish. I need to look up more information.
Action 2: Lookup[Formula One drivers from Mexico]
Observation 2: No more results.
Thought 3: The available information doesn't allow me to determine which other Mexican Formula One race car driver, besides Sergio P\u00e9rez, has held the podium. With the search function failing to provide a full list of Mexican Formula One drivers, I need to return different search results. Let's try searching for Mexican Grand Prix winners, as they would have held the podium.
Action 3: Search[Mexican Grand Prix winners]
Observation 3: Could not find Mexican Grand Prix winners. Similar: ['Mexican Grand Prix', 'List of Formula One Grand Prix winners', '1990 Mexican Grand Prix', '2018 Mexican Grand Prix', '2019 Mexican Grand Prix'].
Thought 4: Given the difficulties in finding a direct list of Mexican Grand Prix winners, I should search for the Mexican Grand Prix to get a broader picture of the race's history. This might include winners.
Action 4: Search[Mexican Grand Prix]
This trajectory is incorrect as my search should be related to Mexican Formula One race car drivers, not winners of the Mexican Grand Prix, a seperate event. A better search would have been for the List of Formula One Grand Prix winners, as suggested.
Thus the correctness score is 3

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search Arthur's Magazine and First for Women, and find which was started first.
Action 1: Search[Arthur's Magazine]
Observation 1: Arthur's Magazine (1844\u00e2\u0080\u00931846) was an American literary periodical published in Philadelphia in the 19th century. Edited by Timothy Shay Arthur, it featured work by Edgar A. Poe, J.H. Ingraham, Sarah Josepha Hale, Thomas G. Spear, and others.[1][2] In May 1846 it was merged into Godey's Lady's Book.[3]
This trajectory is correct as it is reasonable to search for the first magazine provided in the question. It is also better to have simple searches corresponding to a single entity, making this the best action.
Thus the correctness score is 10

Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?
Thought 1: I need to search for the football manager who recruited David Beckham, and then find out the timeframe in which he managed Manchester United.
Action 1: Search[David Beckham's football manager]
Observation 1: Could not find David Beckham's football manager. Similar: ['David Beckham', 'Inter Miami CF (redirect from Miami Beckham United)', 'Victoria Beckham', 'The Beckham Experiment', 'Miami Freedom Park'].
Thought 2: I couldn't find the information on David Beckham's football manager. I need to search Manchester United and find out the timeframe of the manager.
Action 2: Search[Manchester United]
Observation 2: Manchester United Football Club, commonly referred to as Man United (often stylised as Man Utd), or simply United, is a professional football club based in Old Trafford, Greater Manchester, England. The club competes in the Premier League, the top division in the English football league system. Nicknamed the Red Devils, they were founded as Newton Heath LYR Football Club in 1878, but changed their name to Manchester United in 1902. After a spell playing in Clayton, Manchester, the club moved to their current stadium, Old Trafford, in 1910.. Domestically, Manchester United have won a record 20 league titles, 12 FA Cups, six League Cups and a record 21 FA Community Shields.
Thought 3: The information about David Beckham's football manager is not available. I will search for Manchester United's managers to find the timeframe.
Action 3: Search[Manchester United managers]
Observation 3: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
Thought 4: The information about David Beckham's football manager is not available. The question asks for the timeframe when the manager managed Manchester United, so I need to find a list of Manchester United managers.
Action 4: Search[list of Manchester United managers]
Observation 4: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
This trajectory is mostly incorrect as I was not able to retrieve the relevant information to answer the question. The searches are too broad and not relevant to the specific player recruited, David Beckham. The last two actions are also too similar. It would be better to first search for David Beckham and lookup information related to his manager.
Thus the correctness score is 4

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]
This trajectory is correct as all of my thoughts and actions are correct. It makes sense to search for Milhouse first as it is the central subject of the question. It is also correct to directly look up the relevant information in the article, instead of trying another search. 
Thus the correctness score is 10

{input}
'''

value_prompt_reasoning_feedback = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, evaluate its correctness and provide your reasoning and analysis in detail. Focus on the latest thought, action, and observation. Incomplete trajectories can be correct if the thoughts and actions so far are correct, even if the answer is not found yet. Do not generate additional thoughts or actions. Then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Question: Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990?
Thought 1: I need to search for a list of Mexican Formula One race car drivers, then eliminate the one who drove for Force India and was born in 1990.
Action 1: Search[Formula One drivers from Mexico]
Observation 1: There have been six Formula One drivers from Mexico who have taken part in races since the championship began in 1950. Sergio P\u00e9rez is the most successful, having won six Grands Prix. Since 2021, P\u00e9rez drives for the Red Bull team.. P\u00e9rez is the only Mexican F1 driver to achieve a pole position. He took his first pole position at the 2022 Saudi Arabian Grand Prix, in his 219th Grand Prix meeting (a record for the most Grands Prix before a pole).
Thought 2: Sergio P\u00e9rez, born in 1990 and drove for Force India, is not the Mexican driver we are looking for. The passage does not give me enough information about other Mexican drivers who have achieved a podium finish. I need to look up more information.
Action 2: Lookup[Formula One drivers from Mexico]
Observation 2: No more results.
Thought 3: The available information doesn't allow me to determine which other Mexican Formula One race car driver, besides Sergio P\u00e9rez, has held the podium. With the search function failing to provide a full list of Mexican Formula One drivers, I need to return different search results. Let's try searching for Mexican Grand Prix winners, as they would have held the podium.
Action 3: Search[Mexican Grand Prix winners]
Observation 3: Could not find Mexican Grand Prix winners. Similar: ['Mexican Grand Prix', 'List of Formula One Grand Prix winners', '1990 Mexican Grand Prix', '2018 Mexican Grand Prix', '2019 Mexican Grand Prix'].
Thought 4: Given the difficulties in finding a direct list of Mexican Grand Prix winners, I should search for the Mexican Grand Prix to get a broader picture of the race's history. This might include winners.
Action 4: Search[Mexican Grand Prix]
This trajectory is incorrect as my search should be related to Mexican Formula One race car drivers, not winners of the Mexican Grand Prix, a seperate event. A better search would have been for the List of Formula One Grand Prix winners, as suggested.
Thus the correctness score is 3

Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search Arthur's Magazine and First for Women, and find which was started first.
Action 1: Search[Arthur's Magazine]
Observation 1: Arthur's Magazine (1844\u00e2\u0080\u00931846) was an American literary periodical published in Philadelphia in the 19th century. Edited by Timothy Shay Arthur, it featured work by Edgar A. Poe, J.H. Ingraham, Sarah Josepha Hale, Thomas G. Spear, and others.[1][2] In May 1846 it was merged into Godey's Lady's Book.[3]
This trajectory is correct as it is reasonable to search for the first magazine provided in the question. It is also better to have simple searches corresponding to a single entity, making this the best action.
Thus the correctness score is 10

Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?Question: The football manager who recruited David Beckham managed Manchester United during what timeframe?
Thought 1: I need to search for the football manager who recruited David Beckham, and then find out the timeframe in which he managed Manchester United.
Action 1: Search[David Beckham's football manager]
Observation 1: Could not find David Beckham's football manager. Similar: ['David Beckham', 'Inter Miami CF (redirect from Miami Beckham United)', 'Victoria Beckham', 'The Beckham Experiment', 'Miami Freedom Park'].
Thought 2: I couldn't find the information on David Beckham's football manager. I need to search Manchester United and find out the timeframe of the manager.
Action 2: Search[Manchester United]
Observation 2: Manchester United Football Club, commonly referred to as Man United (often stylised as Man Utd), or simply United, is a professional football club based in Old Trafford, Greater Manchester, England. The club competes in the Premier League, the top division in the English football league system. Nicknamed the Red Devils, they were founded as Newton Heath LYR Football Club in 1878, but changed their name to Manchester United in 1902. After a spell playing in Clayton, Manchester, the club moved to their current stadium, Old Trafford, in 1910.. Domestically, Manchester United have won a record 20 league titles, 12 FA Cups, six League Cups and a record 21 FA Community Shields.
Thought 3: The information about David Beckham's football manager is not available. I will search for Manchester United's managers to find the timeframe.
Action 3: Search[Manchester United managers]
Observation 3: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
Thought 4: The information about David Beckham's football manager is not available. The question asks for the timeframe when the manager managed Manchester United, so I need to find a list of Manchester United managers.
Action 4: Search[list of Manchester United managers]
Observation 4: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England. The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup. The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.. From the beginning of the club's official managerial records in 1892 to the start of the 2022–23 season, Manchester United have had 23 full-time managers.
This trajectory is mostly incorrect as I was not able to retrieve the relevant information to answer the question. The searches are too broad and not relevant to the specific player recruited, David Beckham. The last two actions are also too similar. It would be better to first search for David Beckham and lookup information related to his manager.
Thus the correctness score is 4

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]
This trajectory is correct as all of my thoughts and actions are correct. It makes sense to search for Milhouse first as it is the central subject of the question. It is also correct to directly look up the relevant information in the article, instead of trying another search. 
Thus the correctness score is 10

{trajectories}

{input}
'''

value_prompt_reasoning_feedback_short = '''Analyze the trajectories of a solution to a question answering task. The trajectories are labeled by environmental observations about the situation, thoughts that can reason about the current situation and actions that can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Given a question and a trajectory, evaluate its correctness and provide your reasoning and analysis in detail. Focus on the latest thought, action, and observation. Incomplete trajectories can be correct if the thoughts and actions so far are correct, even if the answer is not found yet. Do not generate additional thoughts or actions. Then at the last line conclude "Thus the correctness score is {s}", where s is an integer from 1 to 10.

Question: Which other Mexican Formula One race car driver has held the podium besides the Force India driver born in 1990?
Thought 1: I need to search for a list of Mexican Formula One race car drivers, then eliminate the one who drove for Force India and was born in 1990.
Action 1: Search[Formula One drivers from Mexico]
Observation 1: There have been six Formula One drivers from Mexico who have taken part in races since the championship began in 1950. Sergio P\u00e9rez is the most successful, having won six Grands Prix. Since 2021, P\u00e9rez drives for the Red Bull team.. P\u00e9rez is the only Mexican F1 driver to achieve a pole position. He took his first pole position at the 2022 Saudi Arabian Grand Prix, in his 219th Grand Prix meeting (a record for the most Grands Prix before a pole).
Thought 2: Sergio P\u00e9rez, born in 1990 and drove for Force India, is not the Mexican driver we are looking for. The passage does not give me enough information about other Mexican drivers who have achieved a podium finish. I need to look up more information.
Action 2: Lookup[Formula One drivers from Mexico]
Observation 2: No more results.
Thought 3: The available information doesn't allow me to determine which other Mexican Formula One race car driver, besides Sergio P\u00e9rez, has held the podium. With the search function failing to provide a full list of Mexican Formula One drivers, I need to return different search results. Let's try searching for Mexican Grand Prix winners, as they would have held the podium.
Action 3: Search[Mexican Grand Prix winners]
Observation 3: Could not find Mexican Grand Prix winners. Similar: ['Mexican Grand Prix', 'List of Formula One Grand Prix winners', '1990 Mexican Grand Prix', '2018 Mexican Grand Prix', '2019 Mexican Grand Prix'].
Thought 4: Given the difficulties in finding a direct list of Mexican Grand Prix winners, I should search for the Mexican Grand Prix to get a broader picture of the race's history. This might include winners.
Action 4: Search[Mexican Grand Prix]
This trajectory is incorrect as my search should be related to Mexican Formula One race car drivers, not winners of the Mexican Grand Prix, a seperate event. A better search would have been for the List of Formula One Grand Prix winners, as suggested.
Thus the correctness score is 3

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]
This trajectory is correct as all of my thoughts and actions are correct. It makes sense to search for Milhouse first as it is the central subject of the question. It is also correct to directly look up the relevant information in the article, instead of trying another search. 
Thus the correctness score is 10

{trajectories}

{input}
'''

rap_prompt = '''
Solve a question answering task with interleaving Thought and Action steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
Provide the next Thought and next Action. Here are some examples:

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Thought 2: Then I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains, so High Plains is the area. I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]
Thought 4: I need to search High Plains (United States).
Action 4: Search[High Plains (United States)]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Question: Guitars for Wounded Warriors is an album that was recorded in the village in which New York county?
Thought 1: I need to search Guitars for Wounded Warriors, then find in which New York county it was recorded.
Action 1: Search[Guitars for Wounded Warriors]
Thought 2: I need to search New Paltz (village), New York and find which county it is in
Action 2: Search[New Paltz (village), New York]
Thought 3: New Paltz (village), New York is in Ulster County, so the answer is Ulster County.
Action 3: Finish[Ulster County]

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Thought 2: I can look up "named after" for finding the specific individual Milhouse is named after.
Action 2: Lookup[named after]
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[President Richard Nixon]

{input}
'''