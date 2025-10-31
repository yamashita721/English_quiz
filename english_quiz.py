import random
import os
from typing import List, Dict, Any
questions = [
    # Nouns and main verbs (1-10)
    {
        "question": "Identify the noun in the sentence: 'The dog runs quickly.'",
        "options": ["A) Runs", "B) Quickly", "C) Dog", "D) The"],
        "answer": "C"
    },
    {
        "question": "What is the main verb in: 'She is eating an apple.'",
        "options": ["A) Is", "B) Eating", "C) An", "D) Apple"],
        "answer": "B"
    },
    {
        "question": "Which word is a proper noun? 'Paris is a beautiful city.'",
        "options": ["A) Beautiful", "B) City", "C) Is", "D) Paris"],
        "answer": "D"
    },
    {
        "question": "Identify the abstract noun: 'Honesty is the best policy.'",
        "options": ["A) Best", "B) Policy", "C) Honesty", "D) Is"],
        "answer": "C"
    },
    {
        "question": "What is the main verb in: 'They have been playing football.'",
        "options": ["A) Have", "B) Been", "C) Playing", "D) Football"],
        "answer": "C"
    },
    {
        "question": "Which is a common noun? 'The teacher praised the student.'",
        "options": ["A) Teacher", "B) Praised", "C) The", "D) Student"],
        "answer": "A"
    },
    {
        "question": "Identify the noun: 'Happiness comes from within.'",
        "options": ["A) Comes", "B) From", "C) Happiness", "D) Within"],
        "answer": "C"
    },
    {
        "question": "Main verb in: 'I will go to the market.'",
        "options": ["A) Will", "B) Go", "C) To", "D) Market"],
        "answer": "B"
    },
    {
        "question": "Which is a concrete noun? 'The book is on the table.'",
        "options": ["A) Is", "B) On", "C) Book", "D) The"],
        "answer": "C"
    },
    {
        "question": "Main verb in: 'Birds are flying high.'",
        "options": ["A) Are", "B) Flying", "C) High", "D) Birds"],
        "answer": "B"
    },
    # Number and collection (11-20)
    {
        "question": "What is the plural form of 'child'?",
        "options": ["A) Childs", "B) Childes", "C) Children", "D) Childrens"],
        "answer": "C"
    },
    {
        "question": "Choose the correct collective noun: 'A _____ of wolves.'",
        "options": ["A) Herd", "B) Pack", "C) Flock", "D) School"],
        "answer": "B"
    },
    {
        "question": "Singular or plural? 'The news is good.'",
        "options": ["A) Plural", "B) Singular", "C) Both", "D) None"],
        "answer": "B"
    },
    {
        "question": "Plural of 'mouse':",
        "options": ["A) Mouses", "B) Mice", "C) Mices", "D) Mouse's"],
        "answer": "B"
    },
    {
        "question": "Collective noun for 'stars': 'A _____ of stars.'",
        "options": ["A) Constellation", "B) Bunch", "C) Herd", "D) Pack"],
        "answer": "A"
    },
    {
        "question": "What is the singular form of 'data'?",
        "options": ["A) Datas", "B) Datum", "C) Date", "D) Datus"],
        "answer": "B"
    },
    {
        "question": "Choose correct: 'A flock of _____.'",
        "options": ["A) Sheep", "B) Fish", "C) Birds", "D) Lions"],
        "answer": "C"
    },
    {
        "question": "Plural of 'knife':",
        "options": ["A) Knifes", "B) Knive", "C) Knives", "D) Knife's"],
        "answer": "C"
    },
    {
        "question": "Collective noun: 'A _____ of cards.'",
        "options": ["A) Deck", "B) Bunch", "C) Herd", "D) School"],
        "answer": "A"
    },
    {
        "question": "Is 'furniture' singular or plural?",
        "options": ["A) Plural", "B) Singular", "C) Both", "D) None"],
        "answer": "B"
    },
    # Countable and uncountable nouns (21-30)
    {
        "question": "Is 'water' countable or uncountable?",
        "options": ["A) Countable", "B) Uncountable", "C) Both", "D) Neither"],
        "answer": "B"
    },
    {
        "question": "Which is countable? 'Apple, milk, sugar, banana.'",
        "options": ["A) Milk", "B) Sugar", "C) Apple", "D) None"],
        "answer": "C"
    },
    {
        "question": "Correct sentence: 'I need _____ information.'",
        "options": ["A) Many", "B) Much", "C) Few", "D) Little"],
        "answer": "B"
    },
    {
        "question": "Is 'hair' uncountable?",
        "options": ["A) Yes", "B) No", "C) Sometimes", "D) Never"],
        "answer": "A"
    },
    {
        "question": "Choose for countable: 'There are _____ books.'",
        "options": ["A) Much", "B) Many", "C) Little", "D) Some"],
        "answer": "B"
    },
    {
        "question": "Uncountable noun: 'Advice, pen, chair, table.'",
        "options": ["A) Pen", "B) Chair", "C) Table", "D) Advice"],
        "answer": "D"
    },
    {
        "question": "Correct: 'How _____ rice do you need?'",
        "options": ["A) Many", "B) Few", "C) Much", "D) Little"],
        "answer": "C"
    },
    {
        "question": "Is 'luggage' countable?",
        "options": ["A) Yes", "B) No", "C) Both", "D) Neither"],
        "answer": "B"
    },
    {
        "question": "For uncountable: 'There is _____ traffic.'",
        "options": ["A) Many", "B) Few", "C) Much", "D) None"],
        "answer": "C"
    },
    {
        "question": "Countable example: 'Bread, butter, egg, milk.'",
        "options": ["A) Bread", "B) Butter", "C) Milk", "D) Egg"],
        "answer": "D"
    },
    # Verb forms and noun + helping verbs (31-40)
    {
        "question": "Past tense of 'go':",
        "options": ["A) Goed", "B) Went", "C) Gone", "D) Goes"],
        "answer": "B"
    },
    {
        "question": "Helping verb in: 'She is running.'",
        "options": ["A) She", "B) Is", "C) Running", "D) None"],
        "answer": "B"
    },
    {
        "question": "Correct form: 'He _____ to school every day.'",
        "options": ["A) Go", "B) Goes", "C) Went", "D) Gone"],
        "answer": "B"
    },
    {
        "question": "Past participle of 'eat':",
        "options": ["A) Ate", "B) Eat", "C) Eaten", "D) Eating"],
        "answer": "C"
    },
    {
        "question": "Helping verbs: Which is one? 'Am, is, are.'",
        "options": ["A) All", "B) None", "C) Only am", "D) Only is"],
        "answer": "A"
    },
    {
        "question": "Correct: 'They _____ playing football.'",
        "options": ["A) Was", "B) Were", "C) Is", "D) Am"],
        "answer": "B"
    },
    {
        "question": "Infinitive form of 'ran':",
        "options": ["A) Run", "B) Running", "C) Runs", "D) Runned"],
        "answer": "A"
    },
    {
        "question": "Helping verb in perfect tense: 'Have _____.'",
        "options": ["A) Been", "B) Being", "C) Be", "D) Was"],
        "answer": "A"
    },
    {
        "question": "Correct form: 'She _____ a song.'",
        "options": ["A) Sing", "B) Sang", "C) Sung", "D) Sings"],
        "answer": "D"
    },
    {
        "question": "Noun + helping verb: 'The cat _____ sleeping.'",
        "options": ["A) Is", "B) Are", "C) Was", "D) Were"],
        "answer": "A"
    },
    # Possessive noun apostrophe and its form (41-50)
    {
        "question": "Possessive form of 'dog':",
        "options": ["A) Dogs", "B) Dog's", "C) Dogs'", "D) Doges"],
        "answer": "B"
    },
    {
        "question": "Correct: 'The _____ book is on the table.' (boy)",
        "options": ["A) Boys", "B) Boy's", "C) Boys'", "D) Boyes"],
        "answer": "B"
    },
    {
        "question": "Plural possessive: 'Children _____ toys.'",
        "options": ["A) Childrens'", "B) Children's", "C) Childrens", "D) Children'"],
        "answer": "B"
    },
    {
        "question": "For 'teachers': 'The _____ lounge.'",
        "options": ["A) Teacher's", "B) Teachers'", "C) Teachers", "D) Teacher'"],
        "answer": "B"
    },
    {
        "question": "Correct: 'It is _____ turn.' (Chris)",
        "options": ["A) Chris's", "B) Chris'", "C) Chris", "D) Chrises"],
        "answer": "A"
    },
    {
        "question": "Possessive of 'parents': 'My _____ house.'",
        "options": ["A) Parents'", "B) Parent's", "C) Parents", "D) Parent'"],
        "answer": "A"
    },
    {
        "question": "For singular 'boss': 'The _____ office.'",
        "options": ["A) Bosses", "B) Boss's", "C) Boss'", "D) Bosses'"],
        "answer": "B"
    },
    {
        "question": "Correct: 'The _____ hats.' (ladies)",
        "options": ["A) Ladies'", "B) Lady's", "C) Ladies", "D) Ladys'"],
        "answer": "A"
    },
    {
        "question": "Possessive form: 'James _____ car.'",
        "options": ["A) James'", "B) James's", "C) James", "D) Jameses"],
        "answer": "B"
    },
    {
        "question": "For 'cats': 'The _____ tails.'",
        "options": ["A) Cat's", "B) Cats'", "C) Cats", "D) Cat'"],
        "answer": "B"
    },
    # Pronouns and possessive pronouns (51-60)
    {
        "question": "Which is a possessive pronoun? 'Mine, I, me, my.'",
        "options": ["A) I", "B) Me", "C) My", "D) Mine"],
        "answer": "D"
    },
    {
        "question": "Correct pronoun: '_____ is my book.'",
        "options": ["A) This", "B) These", "C) Them", "D) Those"],
        "answer": "A"
    },
    {
        "question": "Possessive pronoun: 'The book is _____.",
        "options": ["A) Her", "B) Hers", "C) She", "D) Herself"],
        "answer": "B"
    },
    {
        "question": "Which is reflexive? 'Myself, mine, my, me.'",
        "options": ["A) Mine", "B) My", "C) Me", "D) Myself"],
        "answer": "D"
    },
    {
        "question": "Correct: '_____ are students.'",
        "options": ["A) We", "B) Us", "C) Our", "D) Ours"],
        "answer": "A"
    },
    {
        "question": "Possessive: 'This is _____ house.'",
        "options": ["A) Their", "B) They", "C) Them", "D) Theirs"],
        "answer": "D"
    },
    {
        "question": "Pronoun type: 'Who' in 'Who is there?'",
        "options": ["A) Relative", "B) Interrogative", "C) Possessive", "D) Reflexive"],
        "answer": "B"
    },
    {
        "question": "Correct possessive: 'The decision is _____.",
        "options": ["A) Your", "B) Yours", "C) You", "D) Yourself"],
        "answer": "B"
    },
    {
        "question": "Which is personal pronoun? 'It, its, itself, that.'",
        "options": ["A) Its", "B) Itself", "C) That", "D) It"],
        "answer": "D"
    },
    {
        "question": "Possessive pronoun: 'That pen is _____.",
        "options": ["A) My", "B) Mine", "C) I", "D) Me"],
        "answer": "B"
    },
    # More Advanced Nouns and Main Verbs (61-75)
    {
        "question": "Identify the compound noun: 'The bookshelf is full of books.'",
        "options": ["A) Bookshelf", "B) Full", "C) Books", "D) The"],
        "answer": "A",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "What is the main verb in: 'The students have been studying all night.'",
        "options": ["A) Have", "B) Been", "C) Studying", "D) All"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Identify the proper noun: 'The Amazon River flows through Brazil.'",
        "options": ["A) River", "B) Amazon", "C) Flows", "D) Brazil"],
        "answer": "B",
        "category": "Nouns and Main Verbs",
        "difficulty": "Easy"
    },
    {
        "question": "Which is a collective noun? 'The committee made a decision.'",
        "options": ["A) Committee", "B) Made", "C) Decision", "D) A"],
        "answer": "A",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Main verb in: 'She might have gone to the store.'",
        "options": ["A) Might", "B) Have", "C) Gone", "D) Store"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Hard"
    },
    {
        "question": "Identify the material noun: 'The table is made of wood.'",
        "options": ["A) Table", "B) Made", "C) Wood", "D) Of"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "What is the main verb in: 'They should be arriving soon.'",
        "options": ["A) Should", "B) Be", "C) Arriving", "D) Soon"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Which is an abstract noun? 'Success requires hard work.'",
        "options": ["A) Success", "B) Requires", "C) Work", "D) Hard"],
        "answer": "A",
        "category": "Nouns and Main Verbs",
        "difficulty": "Easy"
    },
    {
        "question": "Main verb in: 'The project has been completed successfully.'",
        "options": ["A) Has", "B) Been", "C) Completed", "D) Successfully"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Hard"
    },
    {
        "question": "Identify the compound noun: 'The firefighter saved the family.'",
        "options": ["A) Firefighter", "B) Saved", "C) Family", "D) The"],
        "answer": "A",
        "category": "Nouns and Main Verbs",
        "difficulty": "Easy"
    },
    {
        "question": "What is the main verb in: 'I would have called you yesterday.'",
        "options": ["A) Would", "B) Have", "C) Called", "D) Yesterday"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Hard"
    },
    {
        "question": "Which is a proper noun? 'Mount Everest is the highest peak.'",
        "options": ["A) Mount", "B) Everest", "C) Peak", "D) Highest"],
        "answer": "B",
        "category": "Nouns and Main Verbs",
        "difficulty": "Easy"
    },
    {
        "question": "Identify the concrete noun: 'The music filled the room.'",
        "options": ["A) Music", "B) Filled", "C) Room", "D) The"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Main verb in: 'She could be working late tonight.'",
        "options": ["A) Could", "B) Be", "C) Working", "D) Tonight"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Which is an abstract noun? 'The beauty of nature is amazing.'",
        "options": ["A) Beauty", "B) Nature", "C) Amazing", "D) Of"],
        "answer": "A",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium"
    },
    # More Advanced Number and Collection (76-90)
    {
        "question": "Plural form of 'ox':",
        "options": ["A) Oxes", "B) Oxen", "C) Oxs", "D) Oxies"],
        "answer": "B",
        "category": "Number and Collection",
        "difficulty": "Hard"
    },
    {
        "question": "Collective noun for 'elephants': 'A _____ of elephants.'",
        "options": ["A) Herd", "B) Pack", "C) Flock", "D) School"],
        "answer": "A",
        "category": "Number and Collection",
        "difficulty": "Medium"
    },
    {
        "question": "Plural of 'cactus':",
        "options": ["A) Cactuses", "B) Cacti", "C) Both A and B", "D) Cactuss"],
        "answer": "C",
        "category": "Number and Collection",
        "difficulty": "Hard"
    },
    {
        "question": "Collective noun for 'ants': 'A _____ of ants.'",
        "options": ["A) Colony", "B) Swarm", "C) Both A and B", "D) Army"],
        "answer": "C",
        "category": "Number and Collection",
        "difficulty": "Medium"
    },
    {
        "question": "Plural form of 'basis':",
        "options": ["A) Basises", "B) Bases", "C) Basiss", "D) Basis"],
        "answer": "B",
        "category": "Number and Collection",
        "difficulty": "Hard"
    },
    {
        "question": "Collective noun for 'bees': 'A _____ of bees.'",
        "options": ["A) Swarm", "B) Colony", "C) Hive", "D) All are correct"],
        "answer": "D",
        "category": "Number and Collection",
        "difficulty": "Medium"
    },
    {
        "question": "Plural of 'crisis':",
        "options": ["A) Crisises", "B) Crises", "C) Crisis", "D) Crisess"],
        "answer": "B",
        "category": "Number and Collection",
        "difficulty": "Hard"
    },
    {
        "question": "Collective noun for 'lions': 'A _____ of lions.'",
        "options": ["A) Pride", "B) Pack", "C) Herd", "D) Group"],
        "answer": "A",
        "category": "Number and Collection",
        "difficulty": "Medium"
    },
    {
        "question": "Plural form of 'thesis':",
        "options": ["A) Thesises", "B) Theses", "C) Thesiss", "D) Thesis"],
        "answer": "B",
        "category": "Number and Collection",
        "difficulty": "Hard"
    },
    {
        "question": "Collective noun for 'penguins': 'A _____ of penguins.'",
        "options": ["A) Colony", "B) Huddle", "C) Rookery", "D) All are correct"],
        "answer": "D",
        "category": "Number and Collection",
        "difficulty": "Hard"
    },
    {
        "question": "Plural of 'analysis':",
        "options": ["A) Analysises", "B) Analyses", "C) Analysis", "D) Analysiss"],
        "answer": "B",
        "category": "Number and Collection",
        "difficulty": "Hard"
    },
    {
        "question": "Collective noun for 'owls': 'A _____ of owls.'",
        "options": ["A) Parliament", "B) Flock", "C) Wisdom", "D) All are correct"],
        "answer": "D",
        "category": "Number and Collection",
        "difficulty": "Hard"
    },
    {
        "question": "Plural form of 'phenomenon':",
        "options": ["A) Phenomenons", "B) Phenomena", "C) Phenomenas", "D) Phenomenon"],
        "answer": "B",
        "category": "Number and Collection",
        "difficulty": "Hard"
    },
    {
        "question": "Collective noun for 'giraffes': 'A _____ of giraffes.'",
        "options": ["A) Tower", "B) Herd", "C) Both A and B", "D) Group"],
        "answer": "C",
        "category": "Number and Collection",
        "difficulty": "Hard"
    },
    {
        "question": "Plural of 'criterion':",
        "options": ["A) Criterions", "B) Criteria", "C) Criterias", "D) Criterion"],
        "answer": "B",
        "category": "Number and Collection",
        "difficulty": "Hard"
    },
    # More Advanced Countable and Uncountable Nouns (91-105)
    {
        "question": "Is 'furniture' countable or uncountable?",
        "options": ["A) Countable", "B) Uncountable", "C) Both", "D) Neither"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Medium"
    },
    {
        "question": "Which is uncountable? 'Equipment, chair, table, computer.'",
        "options": ["A) Equipment", "B) Chair", "C) Table", "D) Computer"],
        "answer": "A",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Medium"
    },
    {
        "question": "Correct quantifier: 'There is _____ bread in the kitchen.'",
        "options": ["A) Much", "B) Many", "C) Few", "D) Little"],
        "answer": "A",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Easy"
    },
    {
        "question": "Is 'information' countable?",
        "options": ["A) Yes", "B) No", "C) Sometimes", "D) Never"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Easy"
    },
    {
        "question": "Choose for countable: 'How _____ students are in the class?'",
        "options": ["A) Much", "B) Many", "C) Little", "D) Some"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Easy"
    },
    {
        "question": "Which is countable? 'Music, song, sound, noise.'",
        "options": ["A) Music", "B) Song", "C) Sound", "D) Noise"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Medium"
    },
    {
        "question": "Correct: 'There isn't _____ time left.'",
        "options": ["A) Many", "B) Much", "C) Few", "D) Little"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Medium"
    },
    {
        "question": "Is 'homework' countable?",
        "options": ["A) Yes", "B) No", "C) Both", "D) Neither"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Easy"
    },
    {
        "question": "For countable: 'I have _____ books to read.'",
        "options": ["A) Much", "B) Many", "C) Little", "D) None"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Easy"
    },
    {
        "question": "Which is uncountable? 'Knowledge, fact, idea, thought.'",
        "options": ["A) Knowledge", "B) Fact", "C) Idea", "D) Thought"],
        "answer": "A",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Medium"
    },
    {
        "question": "Correct: 'How _____ money do you have?'",
        "options": ["A) Many", "B) Much", "C) Few", "D) Little"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Easy"
    },
    {
        "question": "Is 'weather' countable?",
        "options": ["A) Yes", "B) No", "C) Sometimes", "D) Never"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Medium"
    },
    {
        "question": "For uncountable: 'There is _____ pollution in the city.'",
        "options": ["A) Many", "B) Much", "C) Few", "D) None"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Medium"
    },
    {
        "question": "Which is countable? 'News, story, report, article.'",
        "options": ["A) News", "B) Story", "C) Report", "D) Article"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Medium"
    },
    {
        "question": "Correct: 'There are _____ people waiting.'",
        "options": ["A) Much", "B) Many", "C) Little", "D) Some"],
        "answer": "B",
        "category": "Countable and Uncountable Nouns",
        "difficulty": "Easy"
    },
    # More Advanced Verb Forms and Helping Verbs (106-120)
    {
        "question": "Past tense of 'swim':",
        "options": ["A) Swimmed", "B) Swam", "C) Swum", "D) Swimming"],
        "answer": "B",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Past participle of 'choose':",
        "options": ["A) Chose", "B) Chosen", "C) Choose", "D) Choosing"],
        "answer": "B",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Helping verb in: 'I have been waiting for hours.'",
        "options": ["A) Have", "B) Been", "C) Waiting", "D) For"],
        "answer": "A",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Past tense of 'throw':",
        "options": ["A) Throwed", "B) Threw", "C) Thrown", "D) Throwing"],
        "answer": "B",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Correct form: 'She _____ her homework yesterday.'",
        "options": ["A) Do", "B) Does", "C) Did", "D) Done"],
        "answer": "C",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Easy"
    },
    {
        "question": "Past participle of 'break':",
        "options": ["A) Broke", "B) Broken", "C) Break", "D) Breaking"],
        "answer": "B",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Helping verbs: Which are helping verbs? 'Am, is, are, was, were.'",
        "options": ["A) All", "B) None", "C) Only am, is, are", "D) Only was, were"],
        "answer": "A",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Easy"
    },
    {
        "question": "Past tense of 'bring':",
        "options": ["A) Bringed", "B) Brought", "C) Brung", "D) Bringing"],
        "answer": "B",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Correct: 'They _____ playing tennis now.'",
        "options": ["A) Is", "B) Are", "C) Was", "D) Were"],
        "answer": "B",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Easy"
    },
    {
        "question": "Past participle of 'drive':",
        "options": ["A) Drove", "B) Driven", "C) Drive", "D) Driving"],
        "answer": "B",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Helping verb in perfect tense: 'I _____ finished my work.'",
        "options": ["A) Have", "B) Has", "C) Had", "D) Will have"],
        "answer": "A",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Past tense of 'teach':",
        "options": ["A) Teachted", "B) Taught", "C) Teached", "D) Teaching"],
        "answer": "B",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Correct form: 'He _____ to school every day.'",
        "options": ["A) Walk", "B) Walks", "C) Walked", "D) Walking"],
        "answer": "B",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Easy"
    },
    {
        "question": "Past participle of 'write':",
        "options": ["A) Wrote", "B) Written", "C) Writed", "D) Writing"],
        "answer": "B",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Medium"
    },
    {
        "question": "Helping verb in continuous tense: 'She _____ reading a book.'",
        "options": ["A) Is", "B) Was", "C) Will be", "D) All are correct"],
        "answer": "D",
        "category": "Verb Forms and Helping Verbs",
        "difficulty": "Medium"
    },
    # More Advanced Possessive Nouns and Apostrophes (121-135)
    {
        "question": "Possessive form of 'James':",
        "options": ["A) James'", "B) James's", "C) Both A and B", "D) James"],
        "answer": "C",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Hard"
    },
    {
        "question": "Correct: 'The _____ car is red.' (women)",
        "options": ["A) Woman's", "B) Womens'", "C) Women's", "D) Woman"],
        "answer": "C",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Medium"
    },
    {
        "question": "Plural possessive: 'The _____ meeting is tomorrow.' (teachers)",
        "options": ["A) Teacher's", "B) Teachers'", "C) Teachers", "D) Teacher"],
        "answer": "B",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Medium"
    },
    {
        "question": "Possessive form of 'Thomas':",
        "options": ["A) Thomas'", "B) Thomas's", "C) Both A and B", "D) Thomas"],
        "answer": "C",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Hard"
    },
    {
        "question": "Correct: 'The _____ house is big.' (family)",
        "options": ["A) Family's", "B) Families'", "C) Family", "D) Familys'"],
        "answer": "A",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Easy"
    },
    {
        "question": "Plural possessive: 'The _____ books are on the shelf.' (students)",
        "options": ["A) Student's", "B) Students'", "C) Students", "D) Student"],
        "answer": "B",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Medium"
    },
    {
        "question": "Possessive form of 'Charles':",
        "options": ["A) Charles'", "B) Charles's", "C) Both A and B", "D) Charles"],
        "answer": "C",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Hard"
    },
    {
        "question": "Correct: 'The _____ office is closed.' (boss)",
        "options": ["A) Boss's", "B) Bosses'", "C) Boss", "D) Boss'"],
        "answer": "A",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Easy"
    },
    {
        "question": "Plural possessive: 'The _____ meeting room is booked.' (managers)",
        "options": ["A) Manager's", "B) Managers'", "C) Managers", "D) Manager"],
        "answer": "B",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Medium"
    },
    {
        "question": "Possessive form of 'Alex':",
        "options": ["A) Alex'", "B) Alex's", "C) Both A and B", "D) Alex"],
        "answer": "C",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Hard"
    },
    {
        "question": "Correct: 'The _____ room is upstairs.' (child)",
        "options": ["A) Child's", "B) Children's", "C) Child", "D) Childrens'"],
        "answer": "A",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Easy"
    },
    {
        "question": "Plural possessive: 'The _____ uniforms are blue.' (players)",
        "options": ["A) Player's", "B) Players'", "C) Players", "D) Player"],
        "answer": "B",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Medium"
    },
    {
        "question": "Possessive form of 'Ross':",
        "options": ["A) Ross'", "B) Ross's", "C) Both A and B", "D) Ross"],
        "answer": "C",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Hard"
    },
    {
        "question": "Correct: 'The _____ voice is beautiful.' (singer)",
        "options": ["A) Singer's", "B) Singers'", "C) Singer", "D) Singers"],
        "answer": "A",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Easy"
    },
    {
        "question": "Plural possessive: 'The _____ opinions matter.' (experts)",
        "options": ["A) Expert's", "B) Experts'", "C) Experts", "D) Expert"],
        "answer": "B",
        "category": "Possessive Nouns and Apostrophes",
        "difficulty": "Medium"
    },
    # More Advanced Pronouns and Possessive Pronouns (136-150)
    {
        "question": "Which is a demonstrative pronoun? 'This, that, these, those.'",
        "options": ["A) All", "B) None", "C) Only this, that", "D) Only these, those"],
        "answer": "A",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Medium"
    },
    {
        "question": "Correct pronoun: '_____ is my favorite book.'",
        "options": ["A) That", "B) Those", "C) Them", "D) These"],
        "answer": "A",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Easy"
    },
    {
        "question": "Possessive pronoun: 'The car is _____.",
        "options": ["A) Their", "B) Theirs", "C) They", "D) Them"],
        "answer": "B",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Medium"
    },
    {
        "question": "Which is an indefinite pronoun? 'Somebody, anyone, everyone, nobody.'",
        "options": ["A) All", "B) None", "C) Only somebody, anyone", "D) Only everyone, nobody"],
        "answer": "A",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Medium"
    },
    {
        "question": "Correct: '_____ should study hard.'",
        "options": ["A) You", "B) Your", "C) Yours", "D) Yourself"],
        "answer": "A",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Easy"
    },
    {
        "question": "Possessive pronoun: 'This laptop is _____.",
        "options": ["A) Her", "B) Hers", "C) She", "D) Herself"],
        "answer": "B",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Medium"
    },
    {
        "question": "Which is a relative pronoun? 'Who, which, that, whose.'",
        "options": ["A) All", "B) None", "C) Only who, which", "D) Only that, whose"],
        "answer": "A",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Medium"
    },
    {
        "question": "Correct pronoun: '_____ are the best students.'",
        "options": ["A) Them", "B) They", "C) Their", "D) Theirs"],
        "answer": "B",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Easy"
    },
    {
        "question": "Possessive pronoun: 'The decision is _____.",
        "options": ["A) Our", "B) Ours", "C) Us", "D) Ourselves"],
        "answer": "B",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Medium"
    },
    {
        "question": "Which is an interrogative pronoun? 'What, which, who, whom.'",
        "options": ["A) All", "B) None", "C) Only what, which", "D) Only who, whom"],
        "answer": "A",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Medium"
    },
    {
        "question": "Correct: '_____ is the winner?'",
        "options": ["A) Who", "B) Whom", "C) Which", "D) What"],
        "answer": "A",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Easy"
    },
    {
        "question": "Possessive pronoun: 'That house is _____.",
        "options": ["A) His", "B) Him", "C) Himself", "D) He"],
        "answer": "A",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Medium"
    },
    {
        "question": "Which is a reflexive pronoun? 'Myself, yourself, himself, herself.'",
        "options": ["A) All", "B) None", "C) Only myself, yourself", "D) Only himself, herself"],
        "answer": "A",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Medium"
    },
    {
        "question": "Correct pronoun: '_____ did you see?'",
        "options": ["A) Who", "B) Whom", "C) Which", "D) What"],
        "answer": "A",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Easy"
    },
    {
        "question": "Possessive pronoun: 'The success is _____.",
        "options": ["A) Your", "B) Yours", "C) You", "D) Yourself"],
        "answer": "B",
        "category": "Pronouns and Possessive Pronouns",
        "difficulty": "Medium"
    }
]

# Added categories: Adjectives (Identification, Application, Degree); Articles; Prepositions; Question Words; Contractions and Interjections; Tenses; Possession
questions.extend([
    # Adjectives - Identification
    {
        "question": "Identify the adjective: 'She wore a beautiful dress.'",
        "options": ["A) She", "B) Wore", "C) Beautiful", "D) Dress"],
        "answer": "C",
        "category": "Adjectives - Identification",
        "difficulty": "Easy"
    },
    {
        "question": "Which word is an adjective? 'The tall building touched the sky.'",
        "options": ["A) Building", "B) Tall", "C) Touched", "D) Sky"],
        "answer": "B",
        "category": "Adjectives - Identification",
        "difficulty": "Easy"
    },
    {
        "question": "Choose the adjective: 'Fresh bread smells amazing.'",
        "options": ["A) Fresh", "B) Bread", "C) Smells", "D) Amazing"],
        "answer": "A",
        "category": "Adjectives - Identification",
        "difficulty": "Medium"
    },

    # Adjectives - Application
    {
        "question": "Select the sentence that correctly uses an adjective:",
        "options": [
            "A) He runs quick.",
            "B) He is quick.",
            "C) He quick runs.",
            "D) He run quick."
        ],
        "answer": "B",
        "category": "Adjectives - Application",
        "difficulty": "Medium"
    },
    {
        "question": "Choose the correct option: 'This is a _____ story.'",
        "options": ["A) Interest", "B) Interested", "C) Interesting", "D) Interests"],
        "answer": "C",
        "category": "Adjectives - Application",
        "difficulty": "Medium"
    },
    {
        "question": "Pick the best adjective: 'He gave a _____ answer.'",
        "options": ["A) Honesty", "B) Honest", "C) Honestly", "D) Honestness"],
        "answer": "B",
        "category": "Adjectives - Application",
        "difficulty": "Easy"
    },

    # Adjectives - Degree
    {
        "question": "Choose the correct degree: 'This is the _____ mountain in the range.'",
        "options": ["A) High", "B) Higher", "C) Highest", "D) Most high"],
        "answer": "C",
        "category": "Adjectives - Degree",
        "difficulty": "Easy"
    },
    {
        "question": "Select the correct comparative: 'She is _____ than her sister.'",
        "options": ["A) More tall", "B) Tallest", "C) Taller", "D) Most taller"],
        "answer": "C",
        "category": "Adjectives - Degree",
        "difficulty": "Easy"
    },
    {
        "question": "Correct superlative form: 'Of the three, Tom is the _____ student.'",
        "options": ["A) More smart", "B) Most smart", "C) Smarter", "D) Smartest"],
        "answer": "D",
        "category": "Adjectives - Degree",
        "difficulty": "Medium"
    },

    # Articles (A, An, The)
    {
        "question": "Choose the correct article: 'He is _____ honest man.'",
        "options": ["A) a", "B) an", "C) the", "D) no article"],
        "answer": "B",
        "category": "Articles (A/An/The)",
        "difficulty": "Easy"
    },
    {
        "question": "Select the correct article: 'I saw _____ eagle flying.'",
        "options": ["A) a", "B) an", "C) the", "D) no article"],
        "answer": "B",
        "category": "Articles (A/An/The)",
        "difficulty": "Easy"
    },
    {
        "question": "Best choice: 'Please close _____ door.'",
        "options": ["A) a", "B) an", "C) the", "D) no article"],
        "answer": "C",
        "category": "Articles (A/An/The)",
        "difficulty": "Easy"
    },
    {
        "question": "Pick the correct option: '_____ Nile is a long river.'",
        "options": ["A) A", "B) An", "C) The", "D) No article"],
        "answer": "C",
        "category": "Articles (A/An/The)",
        "difficulty": "Medium"
    },

    # Prepositions
    {
        "question": "Choose the correct preposition: 'She sat _____ the chair.'",
        "options": ["A) In", "B) On", "C) At", "D) Over"],
        "answer": "B",
        "category": "Prepositions",
        "difficulty": "Easy"
    },
    {
        "question": "Select the best preposition: 'We arrived _____ the airport early.'",
        "options": ["A) In", "B) On", "C) At", "D) Into"],
        "answer": "C",
        "category": "Prepositions",
        "difficulty": "Easy"
    },
    {
        "question": "Pick the correct preposition: 'The picture is _____ the wall.'",
        "options": ["A) In", "B) On", "C) At", "D) By"],
        "answer": "B",
        "category": "Prepositions",
        "difficulty": "Easy"
    },
    {
        "question": "Fill in: 'He walked _____ the bridge.'",
        "options": ["A) Across", "B) Over", "C) Through", "D) Among"],
        "answer": "A",
        "category": "Prepositions",
        "difficulty": "Medium"
    },

    # Question Words
    {
        "question": "Choose the correct question word: '_____ are you late?'",
        "options": ["A) When", "B) Why", "C) What", "D) Who"],
        "answer": "B",
        "category": "Question Words",
        "difficulty": "Easy"
    },
    {
        "question": "Select the best option: '_____ did you call?'",
        "options": ["A) Who", "B) Whom", "C) Which", "D) What"],
        "answer": "A",
        "category": "Question Words",
        "difficulty": "Medium"
    },
    {
        "question": "Pick the correct word: '_____ book is yours?'",
        "options": ["A) Who", "B) Which", "C) Whose", "D) What"],
        "answer": "B",
        "category": "Question Words",
        "difficulty": "Medium"
    },

    # Contractions and Interjections
    {
        "question": "Choose the correct contraction for 'do not':",
        "options": ["A) don't", "B) do'nt", "C) dont'", "D) do nt"],
        "answer": "A",
        "category": "Contractions and Interjections",
        "difficulty": "Easy"
    },
    {
        "question": "Identify the interjection: 'Wow, that was amazing!'",
        "options": ["A) Wow", "B) That", "C) Was", "D) Amazing"],
        "answer": "A",
        "category": "Contractions and Interjections",
        "difficulty": "Easy"
    },
    {
        "question": "Best contraction: 'He _____ going to come.'",
        "options": ["A) is'nt", "B) isn't", "C) isnt'", "D) is nt"],
        "answer": "B",
        "category": "Contractions and Interjections",
        "difficulty": "Easy"
    },

    # Tenses
    {
        "question": "Choose the correct tense: 'She _____ to school every day.'",
        "options": ["A) go", "B) goes", "C) went", "D) gone"],
        "answer": "B",
        "category": "Tenses",
        "difficulty": "Easy"
    },
    {
        "question": "Select the correct past perfect form: 'They _____ before we arrived.'",
        "options": ["A) leave", "B) left", "C) had left", "D) have left"],
        "answer": "C",
        "category": "Tenses",
        "difficulty": "Medium"
    },
    {
        "question": "Pick the correct future continuous: 'I _____ at 8 pm.'",
        "options": ["A) will work", "B) will be working", "C) am working", "D) worked"],
        "answer": "B",
        "category": "Tenses",
        "difficulty": "Medium"
    },

    # Possession (general)
    {
        "question": "Choose the correct possessive: 'This is _____ book.'",
        "options": ["A) John book", "B) Johns book", "C) John's", "D) John"],
        "answer": "C",
        "category": "Possession",
        "difficulty": "Easy"
    },
    {
        "question": "Select the correct form: 'Is this pen _____?'",
        "options": ["A) your", "B) yours", "C) you", "D) you're"],
        "answer": "B",
        "category": "Possession",
        "difficulty": "Easy"
    },
    {
        "question": "Pick the correct option: 'The _____ tails are fluffy.'",
        "options": ["A) cats", "B) cat's", "C) cats'", "D) cats's"],
        "answer": "C",
        "category": "Possession",
        "difficulty": "Medium"
    }
])

class EnglishQuiz:
    def __init__(self):
        self.questions = questions
        self.score = 0
        self.total_questions = 0
        self.incorrect_answers = []
        
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display quiz header with formatting"""
        print("=" * 60)
        print("🎓 ADVANCED ENGLISH GRAMMAR QUIZ 🎓".center(60))
        print("=" * 60)
        print()
    
    def get_difficulty_color(self, difficulty: str) -> str:
        """Return color code based on difficulty"""
        colors = {
            "Easy": "🟢",
            "Medium": "🟡", 
            "Hard": "🔴"
        }
        return colors.get(difficulty, "⚪")
    
    def display_question(self, question_num: int, question: Dict[str, Any]):
        """Display a single question with enhanced formatting"""
        category = question.get('category', 'General')
        difficulty = question.get('difficulty', 'Medium')
        difficulty_icon = self.get_difficulty_color(difficulty)
        
        print(f"\n{'─' * 60}")
        print(f"Question {question_num}/{len(self.questions)} | {category} | {difficulty_icon} {difficulty}")
        print(f"{'─' * 60}")
        print(f"📝 {question['question']}")
        print()
        
        for option in question['options']:
            print(f"   {option}")
        print()
    
    def get_user_answer(self) -> str:
        """Get and validate user answer"""
        while True:
            user_input = input("Your answer (A/B/C/D) or 'Q' to quit: ").upper().strip()
            if user_input in ['A', 'B', 'C', 'D']:
                return user_input
            elif user_input == 'Q':
                return 'QUIT'
            else:
                print("❌ Invalid input! Please enter A, B, C, or D.")
    
    def display_result(self, correct: bool, user_answer: str, correct_answer: str):
        """Display result with feedback"""
        if correct:
            print("✅ Correct! Well done!")
        else:
            print(f"❌ Incorrect! The correct answer is {correct_answer}.")
            # Store incorrect answer for review
            self.incorrect_answers.append({
                'question': self.current_question['question'],
                'user_answer': user_answer,
                'correct_answer': correct_answer,
                'options': self.current_question['options']
            })
    
    def display_progress(self, current: int, total: int):
        """Display progress bar"""
        percentage = (current / total) * 100
        filled = int(percentage // 5)
        bar = "█" * filled + "░" * (20 - filled)
        print(f"\nProgress: [{bar}] {percentage:.1f}% ({current}/{total})")
    
    def shuffle_questions(self):
        """Shuffle the questions randomly"""
        random.shuffle(self.questions)
    
    def filter_by_difficulty(self, difficulty: str):
        """Filter questions by difficulty level"""
        if difficulty.upper() == 'ALL':
            return
        self.questions = [q for q in self.questions if q.get('difficulty', 'Medium').lower() == difficulty.lower()]
    
    def run_quiz(self, shuffle: bool = False, difficulty: str = 'ALL'):
        """Main quiz function with enhanced features"""
        self.clear_screen()
        self.display_header()
        
        # Filter and shuffle questions if requested
        if difficulty.upper() != 'ALL':
            self.filter_by_difficulty(difficulty)
        
        if shuffle:
            self.shuffle_questions()
            print("🔀 Questions have been shuffled!")
        
        print(f"📊 Total questions: {len(self.questions)}")
        print("🎯 Answer each question by typing A, B, C, or D")
        print("💡 Type 'Q' at any time to quit and see results")
        print("\nPress Enter to start...")
        input()
        
        self.clear_screen()
        self.display_header()
        
        for i, question in enumerate(self.questions, 1):
            self.current_question = question
            self.display_question(i, question)
            self.display_progress(i, len(self.questions))
            
            user_answer = self.get_user_answer()
            
            if user_answer == 'QUIT':
                print("\n🛑 Quiz stopped by user.")
                break
            
            correct = user_answer == question['answer']
            self.display_result(correct, user_answer, question['answer'])
            
            if correct:
                self.score += 1
            
            self.total_questions = i
            
            if i < len(self.questions):
                input("\nPress Enter for next question...")
                self.clear_screen()
                self.display_header()
        
        self.display_final_results()
    
    def display_final_results(self):
        """Display comprehensive final results"""
        self.clear_screen()
        print("=" * 60)
        print("🏆 QUIZ RESULTS 🏆".center(60))
        print("=" * 60)
        
        percentage = (self.score / self.total_questions) * 100 if self.total_questions > 0 else 0
        
        print(f"\n📊 Final Score: {self.score}/{self.total_questions}")
        print(f"📈 Percentage: {percentage:.1f}%")
        
        # Performance feedback
        if percentage >= 90:
            print("🌟 Excellent! Outstanding performance!")
        elif percentage >= 80:
            print("🎉 Great job! Very good performance!")
        elif percentage >= 70:
            print("👍 Good work! Keep practicing!")
        elif percentage >= 60:
            print("📚 Not bad! Review the topics you missed.")
        else:
            print("💪 Keep studying! Practice makes perfect!")
        
        # Show incorrect answers for review
        if self.incorrect_answers:
            print(f"\n📝 Review {len(self.incorrect_answers)} incorrect answers:")
            print("─" * 60)
            
            for i, item in enumerate(self.incorrect_answers, 1):
                print(f"\n{i}. {item['question']}")
                for option in item['options']:
                    marker = "✅" if option.startswith(item['correct_answer']) else "❌" if option.startswith(item['user_answer']) else "  "
                    print(f"   {marker} {option}")
                print()
        
        # Category breakdown
        self.show_category_breakdown()
        
        print("\n" + "=" * 60)
        print("Thank you for taking the quiz! Keep learning! 🎓")
    
    def show_category_breakdown(self):
        """Show performance by category"""
        categories = {}
        for q in self.questions[:self.total_questions]:
            cat = q.get('category', 'General')
            if cat not in categories:
                categories[cat] = {'total': 0, 'correct': 0}
            categories[cat]['total'] += 1
        
        # Count correct answers by category
        correct_by_category = {}
        for item in self.incorrect_answers:
            # This is simplified - in a real implementation, you'd track correct answers by category
            pass
        
        if len(categories) > 1:
            print(f"\n📊 Performance by Category:")
            print("─" * 40)
            for cat, stats in categories.items():
                print(f"{cat}: {stats['total']} questions")

    def show_question_categories(self):
        """Display available question categories and counts"""
        categories = {}
        for q in self.questions:
            cat = q.get('category', 'General')
            diff = q.get('difficulty', 'Medium')
            if cat not in categories:
                categories[cat] = {'Easy': 0, 'Medium': 0, 'Hard': 0}
            categories[cat][diff] += 1
        
        print("\n📚 Available Question Categories:")
        print("─" * 50)
        total = 0
        for cat, diffs in categories.items():
            cat_total = sum(diffs.values())
            total += cat_total
            print(f"\n{cat}: {cat_total} questions")
            print(f"  🟢 Easy: {diffs['Easy']}")
            print(f"  🟡 Medium: {diffs['Medium']}")
            print(f"  🔴 Hard: {diffs['Hard']}")
        
        print(f"\n📊 Total Questions Available: {total}")
        input("\nPress Enter to return to menu...")

def main():
    """Main function with menu options"""
    quiz = EnglishQuiz()
    
    while True:
        quiz.clear_screen()
        print("=" * 60)
        print("🎓 ENGLISH GRAMMAR QUIZ MENU 🎓".center(60))
        print("=" * 60)
        print("\nChoose your quiz options:")
        print("1. 🎯 Take Full Quiz (All Questions)")
        print("2. 🔀 Take Shuffled Quiz")
        print("3. 🟢 Easy Questions Only")
        print("4. 🟡 Medium Questions Only") 
        print("5. 🔴 Hard Questions Only")
        print("6. 📊 View Question Categories")
        print("7. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            quiz.run_quiz()
        elif choice == '2':
            quiz.run_quiz(shuffle=True)
        elif choice == '3':
            quiz.run_quiz(difficulty='Easy')
        elif choice == '4':
            quiz.run_quiz(difficulty='Medium')
        elif choice == '5':
            quiz.run_quiz(difficulty='Hard')
        elif choice == '6':
            quiz.show_question_categories()
        elif choice == '7':
            print("\n👋 Thank you for using the English Grammar Quiz!")
            break
        else:
            print("\n❌ Invalid choice! Please enter 1-7.")
            input("Press Enter to continue...")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()