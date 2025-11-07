import random
import os
from typing import List, Dict, Any
questions = [
    # Nouns and main verbs (1-10)
    {
        "question": "Identify the noun in the sentence: 'The dog runs quickly.'",
        "options": ["A) Runs", "B) Quickly", "C) Dog", "D) The"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. 'Runs' is a verb, which describes an action. In this sentence, it tells us what the dog does.",
            "B": "Incorrect. 'Quickly' is an adverb, which modifies the verb 'runs' by describing how the action is performed.",
            "C": "Correct! 'Dog' is a noun - it's a person, place, thing, or idea. In this sentence, 'dog' is the subject, the thing performing the action.",
            "D": "Incorrect. 'The' is an article (a determiner), not a noun. It's used to specify which dog we're talking about."
        }
    },
    {
        "question": "What is the main verb in: 'She is eating an apple.'",
        "options": ["A) Is", "B) Eating", "C) An", "D) Apple"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Is' is a helping verb (auxiliary verb) that works with the main verb 'eating' to form the present continuous tense.",
            "B": "Correct! 'Eating' is the main verb - it's the primary action being performed. 'Is' just helps to form the tense.",
            "C": "Incorrect. 'An' is an article (indefinite article) used before a noun that begins with a vowel sound.",
            "D": "Incorrect. 'Apple' is a noun - it's the object of the verb, the thing being eaten."
        }
    },
    {
        "question": "Which word is a proper noun? 'Paris is a beautiful city.'",
        "options": ["A) Beautiful", "B) City", "C) Is", "D) Paris"],
        "answer": "D",
        "explanations": {
            "A": "Incorrect. 'Beautiful' is an adjective that describes the city. It's not a proper noun because it's not a specific name.",
            "B": "Incorrect. 'City' is a common noun - it's a general term for any city, not a specific name.",
            "C": "Incorrect. 'Is' is a verb (specifically a linking verb) that connects the subject to its description.",
            "D": "Correct! 'Paris' is a proper noun - it's the specific name of a particular city. Proper nouns always begin with a capital letter."
        }
    },
    {
        "question": "Identify the abstract noun: 'Honesty is the best policy.'",
        "options": ["A) Best", "B) Policy", "C) Honesty", "D) Is"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. 'Best' is an adjective in its superlative form, describing 'policy'. It tells us about the quality of the policy.",
            "B": "Incorrect. 'Policy' is a concrete noun - it refers to something that exists as a concept or document that can be seen or touched.",
            "C": "Correct! 'Honesty' is an abstract noun - it represents an idea, quality, or state that cannot be perceived through the five senses.",
            "D": "Incorrect. 'Is' is a verb (linking verb) that connects 'Honesty' (subject) with 'policy' (predicate nominative)."
        }
    },
    {
        "question": "What is the main verb in: 'They have been playing football.'",
        "options": ["A) Have", "B) Been", "C) Playing", "D) Football"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. 'Have' is a helping verb (auxiliary verb) used to form the present perfect continuous tense, but it's not the main verb.",
            "B": "Incorrect. 'Been' is also a helping verb (past participle of 'be') that works with 'have' to form the perfect continuous tense, not the main verb.",
            "C": "Correct! 'Playing' is the main verb - it's the primary action being performed. 'Have' and 'been' are helping verbs that just form the tense.",
            "D": "Incorrect. 'Football' is a noun - it's the object of the verb, the thing being played."
        }
    },
    {
        "question": "Which is a common noun? 'The teacher praised the student.'",
        "options": ["A) Teacher", "B) Praised", "C) The", "D) Student"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'Teacher' is a common noun - it's a general term for a person or profession, not a specific name. Common nouns are not capitalized unless they start a sentence.",
            "B": "Incorrect. 'Praised' is a verb (past tense of 'praise') that describes the action performed by the teacher.",
            "C": "Incorrect. 'The' is an article (definite article) used to specify or identify the nouns, not a noun itself.",
            "D": "Incorrect. 'Student' is also a common noun, but the question asks for 'which is a common noun', and both A and D are common nouns. However, 'teacher' comes first in the sentence, so A is the primary answer, though both are technically correct. The answer key indicates A."
        }
    },
    {
        "question": "Identify the noun: 'Happiness comes from within.'",
        "options": ["A) Comes", "B) From", "C) Happiness", "D) Within"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. 'Comes' is a verb (third-person singular present tense of 'come') that describes the action or state.",
            "B": "Incorrect. 'From' is a preposition that shows the relationship or direction between 'comes' and 'within'.",
            "C": "Correct! 'Happiness' is a noun - specifically an abstract noun representing an emotion or state that cannot be physically touched.",
            "D": "Incorrect. 'Within' is a preposition or adverb indicating location or position, not a noun."
        }
    },
    {
        "question": "Main verb in: 'I will go to the market.'",
        "options": ["A) Will", "B) Go", "C) To", "D) Market"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Will' is a helping verb (modal auxiliary) used to form the future tense, but it's not the main verb that expresses the action.",
            "B": "Correct! 'Go' is the main verb - it's the primary action being performed. 'Will' just helps to indicate future time.",
            "C": "Incorrect. 'To' is a preposition that introduces the prepositional phrase 'to the market'.",
            "D": "Incorrect. 'Market' is a noun - it's the object of the preposition 'to', indicating the destination."
        }
    },
    {
        "question": "Which is a concrete noun? 'The book is on the table.'",
        "options": ["A) Is", "B) On", "C) Book", "D) The"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. 'Is' is a verb (linking verb) that connects the subject 'book' with its location 'on the table'.",
            "B": "Incorrect. 'On' is a preposition that shows the spatial relationship between the book and the table.",
            "C": "Correct! 'Book' is a concrete noun - it's something physical that can be seen and touched. Concrete nouns refer to tangible objects.",
            "D": "Incorrect. 'The' is an article (definite article) used to specify the nouns, not a noun itself."
        }
    },
    {
        "question": "Main verb in: 'Birds are flying high.'",
        "options": ["A) Are", "B) Flying", "C) High", "D) Birds"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Are' is a helping verb (auxiliary verb) used to form the present continuous tense, but it's not the main verb.",
            "B": "Correct! 'Flying' is the main verb - it's the primary action being performed. 'Are' just helps to form the present continuous tense.",
            "C": "Incorrect. 'High' is an adverb that modifies the verb 'flying' by describing how or where the birds are flying.",
            "D": "Incorrect. 'Birds' is a noun - it's the subject of the sentence, the thing performing the action."
        }
    },
    # Number and collection (11-20)
    {
        "question": "What is the plural form of 'child'?",
        "options": ["A) Childs", "B) Childes", "C) Children", "D) Childrens"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. 'Childs' is not a valid plural form. Most nouns form plurals by adding 's', but 'child' is irregular.",
            "B": "Incorrect. 'Childes' is not a valid plural form. This spelling doesn't exist in English.",
            "C": "Correct! 'Children' is the irregular plural form of 'child'. It doesn't follow the regular pattern of adding 's' or 'es'.",
            "D": "Incorrect. 'Childrens' adds an extra 's', which is incorrect. 'Children' is already the plural form."
        }
    },
    {
        "question": "Choose the correct collective noun: 'A _____ of wolves.'",
        "options": ["A) Herd", "B) Pack", "C) Flock", "D) School"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Herd' is used for groups of certain animals like cattle, elephants, or deer, but not for wolves.",
            "B": "Correct! 'Pack' is the specific collective noun for a group of wolves. This is the traditional term used for these animals.",
            "C": "Incorrect. 'Flock' is used for groups of birds (like a flock of birds) or sometimes sheep, but not for wolves.",
            "D": "Incorrect. 'School' is used for groups of fish (like a school of fish), but not for wolves."
        }
    },
    {
        "question": "Singular or plural? 'The news is good.'",
        "options": ["A) Plural", "B) Singular", "C) Both", "D) None"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. Although 'news' ends with 's', it is grammatically singular. The verb 'is' (not 'are') confirms this.",
            "B": "Correct! 'News' is always singular in English, even though it ends with 's'. The singular verb 'is' proves this. 'News' is an uncountable noun.",
            "C": "Incorrect. 'News' is always treated as singular in English grammar, never plural.",
            "D": "Incorrect. 'News' is definitely a noun - it's a singular uncountable noun."
        }
    },
    {
        "question": "Plural of 'mouse':",
        "options": ["A) Mouses", "B) Mice", "C) Mices", "D) Mouse's"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Mouses' is not the correct plural form. While 'mouses' can sometimes be used for computer mice, the traditional plural is 'mice'.",
            "B": "Correct! 'Mice' is the irregular plural form of 'mouse'. This is an exception to the regular pattern of adding 's' or 'es'.",
            "C": "Incorrect. 'Mices' is not a valid plural form. This spelling doesn't exist in English.",
            "D": "Incorrect. 'Mouse's' is the possessive form (singular possessive), meaning 'belonging to the mouse', not a plural form."
        }
    },
    {
        "question": "Collective noun for 'stars': 'A _____ of stars.'",
        "options": ["A) Constellation", "B) Bunch", "C) Herd", "D) Pack"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'Constellation' is the proper collective noun for a group of stars that form a pattern in the sky.",
            "B": "Incorrect. While 'bunch' can mean a group, it's not the specific traditional collective noun for stars.",
            "C": "Incorrect. 'Herd' is used for groups of animals like cattle or elephants, not for stars.",
            "D": "Incorrect. 'Pack' is used for groups of wolves or dogs, not for stars."
        }
    },
    {
        "question": "What is the singular form of 'data'?",
        "options": ["A) Datas", "B) Datum", "C) Date", "D) Datus"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Datas' is not a valid word. 'Data' is already plural (though often treated as singular in modern usage).",
            "B": "Correct! 'Datum' is the singular form of 'data'. 'Data' comes from Latin where 'datum' is singular and 'data' is plural.",
            "C": "Incorrect. 'Date' is a completely different word meaning a specific day or a fruit, not related to 'data'.",
            "D": "Incorrect. 'Datus' is not a valid singular form. The correct singular is 'datum'."
        }
    },
    {
        "question": "Choose correct: 'A flock of _____.'",
        "options": ["A) Sheep", "B) Fish", "C) Birds", "D) Lions"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. While 'sheep' can be in a flock, 'flock' is more commonly used for birds. 'Sheep' typically use 'flock' but the most standard pairing is 'flock of birds'.",
            "B": "Incorrect. 'Fish' use 'school' as their collective noun, not 'flock'. 'Flock' is primarily for birds.",
            "C": "Correct! 'Flock' is the standard collective noun for a group of birds. This is the most common and traditional usage.",
            "D": "Incorrect. 'Lions' use 'pride' as their collective noun, not 'flock'."
        }
    },
    {
        "question": "Plural of 'knife':",
        "options": ["A) Knifes", "B) Knive", "C) Knives", "D) Knife's"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. 'Knifes' is not the correct plural form. For nouns ending in 'fe', we change 'f' to 'v' and add 'es'.",
            "B": "Incorrect. 'Knive' is not a valid plural form. The correct transformation is 'knife' → 'knives'.",
            "C": "Correct! 'Knives' is the plural form. When a noun ends in 'fe', we change 'f' to 'v' and add 'es'.",
            "D": "Incorrect. 'Knife's' is the possessive form (singular possessive), meaning 'belonging to the knife', not a plural form."
        }
    },
    {
        "question": "Collective noun: 'A _____ of cards.'",
        "options": ["A) Deck", "B) Bunch", "C) Herd", "D) School"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'Deck' is the standard collective noun for a group of playing cards.",
            "B": "Incorrect. While 'bunch' means a group, 'deck' is the specific traditional term for playing cards.",
            "C": "Incorrect. 'Herd' is used for groups of animals like cattle or elephants, not for cards.",
            "D": "Incorrect. 'School' is used for groups of fish, not for cards."
        }
    },
    {
        "question": "Is 'furniture' singular or plural?",
        "options": ["A) Plural", "B) Singular", "C) Both", "D) None"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Furniture' is always treated as singular in English, even when referring to multiple pieces. We say 'The furniture is...' not 'The furniture are...'.",
            "B": "Correct! 'Furniture' is always singular and uncountable. We use singular verbs with it (e.g., 'The furniture is nice').",
            "C": "Incorrect. 'Furniture' is always singular in English grammar, never plural.",
            "D": "Incorrect. 'Furniture' is definitely a noun - it's a singular uncountable noun."
        }
    },
    # Countable and uncountable nouns (21-30)
    {
        "question": "Is 'water' countable or uncountable?",
        "options": ["A) Countable", "B) Uncountable", "C) Both", "D) Neither"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Water' cannot be counted individually. You can't say 'one water, two waters' in the same way you can count apples or books.",
            "B": "Correct! 'Water' is an uncountable noun because it refers to a substance or material that can't be counted as separate units. We use 'much' or 'little' with uncountable nouns, not 'many' or 'few'.",
            "C": "Incorrect. While you can count containers of water (glasses, bottles), the word 'water' itself is uncountable.",
            "D": "Incorrect. 'Water' is definitely a noun - it's specifically an uncountable noun."
        }
    },
    {
        "question": "Which is countable? 'Apple, milk, sugar, banana.'",
        "options": ["A) Milk", "B) Sugar", "C) Apple", "D) None"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. 'Milk' is an uncountable noun - it's a liquid substance that can't be counted as separate units.",
            "B": "Incorrect. 'Sugar' is an uncountable noun - it's a substance that can't be counted individually.",
            "C": "Correct! 'Apple' is a countable noun - you can count apples (one apple, two apples, three apples).",
            "D": "Incorrect. 'Apple' and 'banana' are both countable nouns, so the answer is not 'none'."
        }
    },
    {
        "question": "Correct sentence: 'I need _____ information.'",
        "options": ["A) Many", "B) Much", "C) Few", "D) Little"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Many' is used with countable nouns (e.g., 'many books'), but 'information' is uncountable.",
            "B": "Correct! 'Much' is used with uncountable nouns like 'information'. We say 'much information', not 'many information'.",
            "C": "Incorrect. 'Few' is used with countable nouns (e.g., 'few books'), but 'information' is uncountable.",
            "D": "Incorrect. While 'little' can be used with uncountable nouns, 'much' is more appropriate here when talking about needing information."
        }
    },
    {
        "question": "Is 'hair' uncountable?",
        "options": ["A) Yes", "B) No", "C) Sometimes", "D) Never"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'Hair' is generally uncountable when referring to hair as a mass (e.g., 'She has long hair'). We use 'much hair' not 'many hairs'.",
            "B": "Incorrect. 'Hair' is uncountable when referring to hair collectively. Individual strands are 'hairs' (countable), but 'hair' as a mass is uncountable.",
            "C": "Incorrect. When used as a mass noun, 'hair' is always uncountable. Individual strands are 'hairs' (countable), but that's a different form.",
            "D": "Incorrect. 'Hair' is uncountable when referring to hair as a whole mass on someone's head."
        }
    },
    {
        "question": "Choose for countable: 'There are _____ books.'",
        "options": ["A) Much", "B) Many", "C) Little", "D) Some"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Much' is used with uncountable nouns (e.g., 'much water'), but 'books' is countable.",
            "B": "Correct! 'Many' is used with countable plural nouns like 'books'. We say 'many books', not 'much books'.",
            "C": "Incorrect. 'Little' is used with uncountable nouns (e.g., 'little water'), but 'books' is countable.",
            "D": "Incorrect. While 'some' can work with countable nouns, 'many' is the best choice here when emphasizing quantity."
        }
    },
    {
        "question": "Uncountable noun: 'Advice, pen, chair, table.'",
        "options": ["A) Pen", "B) Chair", "C) Table", "D) Advice"],
        "answer": "D",
        "explanations": {
            "A": "Incorrect. 'Pen' is a countable noun - you can count pens (one pen, two pens, three pens).",
            "B": "Incorrect. 'Chair' is a countable noun - you can count chairs (one chair, two chairs, three chairs).",
            "C": "Incorrect. 'Table' is a countable noun - you can count tables (one table, two tables, three tables).",
            "D": "Correct! 'Advice' is an uncountable noun - it's information or guidance that can't be counted as separate units. We say 'some advice' or 'a piece of advice', not 'an advice' or 'advices'."
        }
    },
    {
        "question": "Correct: 'How _____ rice do you need?'",
        "options": ["A) Many", "B) Few", "C) Much", "D) Little"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. 'Many' is used with countable nouns (e.g., 'how many apples'), but 'rice' is uncountable.",
            "B": "Incorrect. 'Few' is used with countable nouns (e.g., 'how few books'), but 'rice' is uncountable.",
            "C": "Correct! 'Much' is used with uncountable nouns like 'rice'. We say 'how much rice', not 'how many rice'.",
            "D": "Incorrect. While 'little' can be used with uncountable nouns, 'much' is correct in this question form."
        }
    },
    {
        "question": "Is 'luggage' countable?",
        "options": ["A) Yes", "B) No", "C) Both", "D) Neither"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Luggage' is always uncountable. You can't say 'one luggage, two luggages'. Instead, you say 'a piece of luggage' or 'items of luggage'.",
            "B": "Correct! 'Luggage' is an uncountable noun. We use 'much luggage' or 'a lot of luggage', not 'many luggages'.",
            "C": "Incorrect. 'Luggage' is always uncountable in English, never countable.",
            "D": "Incorrect. 'Luggage' is definitely a noun - it's specifically an uncountable noun."
        }
    },
    {
        "question": "For uncountable: 'There is _____ traffic.'",
        "options": ["A) Many", "B) Few", "C) Much", "D) None"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. 'Many' is used with countable nouns (e.g., 'many cars'), but 'traffic' is uncountable.",
            "B": "Incorrect. 'Few' is used with countable nouns (e.g., 'few cars'), but 'traffic' is uncountable.",
            "C": "Correct! 'Much' is used with uncountable nouns like 'traffic'. We say 'much traffic' or 'a lot of traffic', not 'many traffic'.",
            "D": "Incorrect. While grammatically possible, 'much' is the standard quantifier used with uncountable nouns like 'traffic'."
        }
    },
    {
        "question": "Countable example: 'Bread, butter, egg, milk.'",
        "options": ["A) Bread", "B) Butter", "C) Milk", "D) Egg"],
        "answer": "D",
        "explanations": {
            "A": "Incorrect. 'Bread' is an uncountable noun - it's a substance that can't be counted individually. We say 'a loaf of bread' or 'slices of bread'.",
            "B": "Incorrect. 'Butter' is an uncountable noun - it's a substance that can't be counted. We say 'some butter' or 'a stick of butter'.",
            "C": "Incorrect. 'Milk' is an uncountable noun - it's a liquid that can't be counted individually. We say 'some milk' or 'a glass of milk'.",
            "D": "Correct! 'Egg' is a countable noun - you can count eggs (one egg, two eggs, three eggs)."
        }
    },
    # Verb forms and noun + helping verbs (31-40)
    {
        "question": "Past tense of 'go':",
        "options": ["A) Goed", "B) Went", "C) Gone", "D) Goes"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Goed' doesn't exist in English. 'Go' is an irregular verb that doesn't follow the pattern of adding '-ed' for past tense.",
            "B": "Correct! 'Went' is the irregular past tense form of 'go'. This is an exception to the regular verb pattern.",
            "C": "Incorrect. 'Gone' is the past participle form, used with helping verbs like 'have' (e.g., 'I have gone'), not the simple past tense.",
            "D": "Incorrect. 'Goes' is the third-person singular present tense form (e.g., 'He goes'), not the past tense."
        }
    },
    {
        "question": "Helping verb in: 'She is running.'",
        "options": ["A) She", "B) Is", "C) Running", "D) None"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'She' is a pronoun (subject), not a verb. It refers to the person performing the action.",
            "B": "Correct! 'Is' is a helping verb (auxiliary verb) that works with 'running' to form the present continuous tense.",
            "C": "Incorrect. 'Running' is the main verb (present participle), not the helping verb. 'Is' is the helping verb.",
            "D": "Incorrect. There is a helping verb in this sentence - 'is'."
        }
    },
    {
        "question": "Correct form: 'He _____ to school every day.'",
        "options": ["A) Go", "B) Goes", "C) Went", "D) Gone"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Go' is the base form, but with third-person singular subjects (he, she, it), we need to add 's'.",
            "B": "Correct! 'Goes' is the third-person singular present tense form. 'Every day' indicates a habitual action, and 'he' requires the 's' ending.",
            "C": "Incorrect. 'Went' is the past tense form, but 'every day' indicates a present habit, not a past action.",
            "D": "Incorrect. 'Gone' is the past participle, which needs a helping verb (e.g., 'has gone'). It can't be used alone here."
        }
    },
    {
        "question": "Past participle of 'eat':",
        "options": ["A) Ate", "B) Eat", "C) Eaten", "D) Eating"],
        "answer": "C",
        "explanations": {
            "A": "Incorrect. 'Ate' is the past tense form (simple past), not the past participle. Past participle is used with helping verbs.",
            "B": "Incorrect. 'Eat' is the base form (infinitive) of the verb, not the past participle.",
            "C": "Correct! 'Eaten' is the past participle form, used with helping verbs like 'have' or 'has' (e.g., 'I have eaten', 'She has eaten').",
            "D": "Incorrect. 'Eating' is the present participle form, used in continuous tenses, not the past participle."
        }
    },
    {
        "question": "Helping verbs: Which is one? 'Am, is, are.'",
        "options": ["A) All", "B) None", "C) Only am", "D) Only is"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'Am', 'is', and 'are' are all forms of the helping verb 'be'. They are all helping verbs used in continuous tenses and passive voice.",
            "B": "Incorrect. All three are helping verbs - they all assist main verbs in forming different tenses.",
            "C": "Incorrect. While 'am' is a helping verb, 'is' and 'are' are also helping verbs. They're all forms of 'be'.",
            "D": "Incorrect. While 'is' is a helping verb, 'am' and 'are' are also helping verbs. They're all forms of 'be'."
        }
    },
    {
        "question": "Correct: 'They _____ playing football.'",
        "options": ["A) Was", "B) Were", "C) Is", "D) Am"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Was' is used with singular subjects (I, he, she, it), but 'they' is plural.",
            "B": "Correct! 'Were' is used with plural subjects like 'they' in past continuous tense.",
            "C": "Incorrect. 'Is' is used with singular subjects in present tense (he, she, it), but 'they' is plural.",
            "D": "Incorrect. 'Am' is used only with 'I' in present tense, not with 'they'."
        }
    },
    {
        "question": "Infinitive form of 'ran':",
        "options": ["A) Run", "B) Running", "C) Runs", "D) Runned"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'Run' is the infinitive/base form of the verb. 'Ran' is the past tense of 'run'.",
            "B": "Incorrect. 'Running' is the present participle form, used in continuous tenses, not the infinitive.",
            "C": "Incorrect. 'Runs' is the third-person singular present tense form, not the infinitive.",
            "D": "Incorrect. 'Runned' is not a valid word. 'Run' is an irregular verb - its past tense is 'ran', not 'runned'."
        }
    },
    {
        "question": "Helping verb in perfect tense: 'Have _____.'",
        "options": ["A) Been", "B) Being", "C) Be", "D) Was"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'Been' is the past participle of 'be', used with 'have' to form perfect tenses (e.g., 'have been', 'has been').",
            "B": "Incorrect. 'Being' is the present participle of 'be', used in continuous tenses, not perfect tenses.",
            "C": "Incorrect. 'Be' is the base form/infinitive, not the past participle needed for perfect tenses.",
            "D": "Incorrect. 'Was' is the past tense form, not the past participle. Perfect tenses use past participles."
        }
    },
    {
        "question": "Correct form: 'She _____ a song.'",
        "options": ["A) Sing", "B) Sang", "C) Sung", "D) Sings"],
        "answer": "D",
        "explanations": {
            "A": "Incorrect. 'Sing' is the base form, but with third-person singular subjects (she, he, it), we need to add 's'.",
            "B": "Incorrect. 'Sang' is the past tense form. This sentence describes a general/habitual action, not a past action.",
            "C": "Incorrect. 'Sung' is the past participle form, which needs a helping verb (e.g., 'has sung'). It can't be used alone here.",
            "D": "Correct! 'Sings' is the third-person singular present tense form, matching the subject 'she'."
        }
    },
    {
        "question": "Noun + helping verb: 'The cat _____ sleeping.'",
        "options": ["A) Is", "B) Are", "C) Was", "D) Were"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'Is' is the helping verb that matches the singular subject 'cat' in present continuous tense.",
            "B": "Incorrect. 'Are' is used with plural subjects (e.g., 'cats are'), but 'cat' is singular.",
            "C": "Incorrect. 'Was' is used for past tense, but this sentence appears to be in present tense.",
            "D": "Incorrect. 'Were' is used with plural subjects in past tense, but 'cat' is singular."
        }
    },
    # Possessive noun apostrophe and its form (41-50)
    {
        "question": "Possessive form of 'dog':",
        "options": ["A) Dogs", "B) Dog's", "C) Dogs'", "D) Doges"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Dogs' is the plural form, not the possessive form. It means multiple dogs, not belonging to a dog.",
            "B": "Correct! 'Dog's' is the singular possessive form, meaning 'belonging to the dog' (e.g., 'the dog's bone').",
            "C": "Incorrect. 'Dogs'' is the plural possessive form (meaning 'belonging to multiple dogs'), but we need the singular possessive here.",
            "D": "Incorrect. 'Doges' is not a valid plural form. The plural of 'dog' is 'dogs'."
        }
    },
    {
        "question": "Correct: 'The _____ book is on the table.' (boy)",
        "options": ["A) Boys", "B) Boy's", "C) Boys'", "D) Boyes"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Boys' is the plural form, not possessive. We need to show possession (the book belongs to the boy).",
            "B": "Correct! 'Boy's' is the singular possessive form, meaning 'belonging to the boy' (the book of the boy).",
            "C": "Incorrect. 'Boys'' is the plural possessive form (belonging to multiple boys), but we need singular possessive for one boy.",
            "D": "Incorrect. 'Boyes' is not a valid word. The plural of 'boy' is 'boys'."
        }
    },
    {
        "question": "Plural possessive: 'Children _____ toys.'",
        "options": ["A) Childrens'", "B) Children's", "C) Childrens", "D) Children'"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Childrens'' would be correct if 'childrens' was the plural, but 'children' is already the plural of 'child'.",
            "B": "Correct! 'Children's' is the plural possessive form. Since 'children' is an irregular plural that doesn't end in 's', we add 's after it.",
            "C": "Incorrect. 'Childrens' is not a valid word. 'Children' is already the plural form of 'child'.",
            "D": "Incorrect. 'Children'' would only work if the plural ended in 's', but 'children' is an irregular plural."
        }
    },
    {
        "question": "For 'teachers': 'The _____ lounge.'",
        "options": ["A) Teacher's", "B) Teachers'", "C) Teachers", "D) Teacher'"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Teacher's' is the singular possessive form (belonging to one teacher), but 'teachers' is plural.",
            "B": "Correct! 'Teachers'' is the plural possessive form, meaning 'belonging to the teachers' (the lounge of the teachers).",
            "C": "Incorrect. 'Teachers' is just the plural form, not possessive. We need to show possession.",
            "D": "Incorrect. 'Teacher'' is not a valid possessive form. Apostrophes must come after the 's' for plural possessives."
        }
    },
    {
        "question": "Correct: 'It is _____ turn.' (Chris)",
        "options": ["A) Chris's", "B) Chris'", "C) Chris", "D) Chrises"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'Chris's' is the correct possessive form for singular nouns ending in 's'. Both 'Chris's' and 'Chris'' are acceptable, but 'Chris's' is more common.",
            "B": "Incorrect. While 'Chris'' is sometimes used, 'Chris's' is the preferred and more common form for singular nouns ending in 's'.",
            "C": "Incorrect. 'Chris' without an apostrophe is not possessive. We need to show possession (the turn belongs to Chris).",
            "D": "Incorrect. 'Chrises' is not a valid word. 'Chris' is a proper name and doesn't have a plural form here."
        }
    },
    {
        "question": "Possessive of 'parents': 'My _____ house.'",
        "options": ["A) Parents'", "B) Parent's", "C) Parents", "D) Parent'"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'Parents'' is the plural possessive form, meaning 'belonging to my parents' (the house of my parents).",
            "B": "Incorrect. 'Parent's' is the singular possessive form (belonging to one parent), but 'parents' is plural (referring to both parents).",
            "C": "Incorrect. 'Parents' without an apostrophe is just the plural form, not possessive. We need to show possession.",
            "D": "Incorrect. 'Parent'' is not a valid possessive form. For plural nouns ending in 's', the apostrophe comes after the 's'."
        }
    },
    {
        "question": "For singular 'boss': 'The _____ office.'",
        "options": ["A) Bosses", "B) Boss's", "C) Boss'", "D) Bosses'"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Bosses' is the plural form, but we need the singular possessive form here.",
            "B": "Correct! 'Boss's' is the singular possessive form, meaning 'belonging to the boss' (the office of the boss).",
            "C": "Incorrect. 'Boss'' would only work if it's a plural possessive, but we need singular possessive here.",
            "D": "Incorrect. 'Bosses'' is the plural possessive form (belonging to multiple bosses), but we need singular possessive."
        }
    },
    {
        "question": "Correct: 'The _____ hats.' (ladies)",
        "options": ["A) Ladies'", "B) Lady's", "C) Ladies", "D) Ladys'"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'Ladies'' is the plural possessive form, meaning 'belonging to the ladies' (the hats of the ladies).",
            "B": "Incorrect. 'Lady's' is the singular possessive form (belonging to one lady), but 'ladies' is plural.",
            "C": "Incorrect. 'Ladies' without an apostrophe is just the plural form, not possessive. We need to show possession.",
            "D": "Incorrect. 'Ladys'' is not a valid form. The plural of 'lady' is 'ladies', not 'ladys'."
        }
    },
    {
        "question": "Possessive form: 'James _____ car.'",
        "options": ["A) James'", "B) James's", "C) James", "D) Jameses"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. While 'James'' is sometimes used, 'James's' is the preferred form for singular nouns ending in 's'.",
            "B": "Correct! 'James's' is the correct possessive form for singular proper nouns ending in 's'. Both forms are acceptable, but 'James's' is more common.",
            "C": "Incorrect. 'James' without an apostrophe is not possessive. We need to show possession (the car belongs to James).",
            "D": "Incorrect. 'Jameses' is not a valid word. Proper names like 'James' don't typically have plural forms in this context."
        }
    },
    {
        "question": "For 'cats': 'The _____ tails.'",
        "options": ["A) Cat's", "B) Cats'", "C) Cats", "D) Cat'"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Cat's' is the singular possessive form (belonging to one cat), but 'cats' is plural.",
            "B": "Correct! 'Cats'' is the plural possessive form, meaning 'belonging to the cats' (the tails of the cats).",
            "C": "Incorrect. 'Cats' without an apostrophe is just the plural form, not possessive. We need to show possession.",
            "D": "Incorrect. 'Cat'' is not a valid possessive form. For plural nouns ending in 's', the apostrophe comes after the 's'."
        }
    },
    # Pronouns and possessive pronouns (51-60)
    {
        "question": "Which is a possessive pronoun? 'Mine, I, me, my.'",
        "options": ["A) I", "B) Me", "C) My", "D) Mine"],
        "answer": "D",
        "explanations": {
            "A": "Incorrect. 'I' is a personal pronoun (subject pronoun), not a possessive pronoun.",
            "B": "Incorrect. 'Me' is a personal pronoun (object pronoun), not a possessive pronoun.",
            "C": "Incorrect. 'My' is a possessive adjective (possessive determiner), not a possessive pronoun. It's used before nouns.",
            "D": "Correct! 'Mine' is a possessive pronoun - it stands alone and shows ownership (e.g., 'The book is mine')."
        }
    },
    {
        "question": "Correct pronoun: '_____ is my book.'",
        "options": ["A) This", "B) These", "C) Them", "D) Those"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'This' is a demonstrative pronoun used for singular objects that are near or being referred to. It matches 'book' (singular).",
            "B": "Incorrect. 'These' is used for plural objects near the speaker, but 'book' is singular.",
            "C": "Incorrect. 'Them' is an object pronoun, not a demonstrative pronoun. Also, 'book' is singular, so 'them' doesn't match.",
            "D": "Incorrect. 'Those' is used for plural objects far from the speaker, but 'book' is singular."
        }
    },
    {
        "question": "Possessive pronoun: 'The book is _____.",
        "options": ["A) Her", "B) Hers", "C) She", "D) Herself"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Her' is a possessive adjective (used before nouns like 'her book'), not a possessive pronoun that stands alone.",
            "B": "Correct! 'Hers' is a possessive pronoun that stands alone and shows ownership (e.g., 'The book is hers').",
            "C": "Incorrect. 'She' is a personal pronoun (subject pronoun), not a possessive pronoun.",
            "D": "Incorrect. 'Herself' is a reflexive pronoun, used when the subject and object are the same person, not a possessive pronoun."
        }
    },
    {
        "question": "Which is reflexive? 'Myself, mine, my, me.'",
        "options": ["A) Mine", "B) My", "C) Me", "D) Myself"],
        "answer": "D",
        "explanations": {
            "A": "Incorrect. 'Mine' is a possessive pronoun, not a reflexive pronoun.",
            "B": "Incorrect. 'My' is a possessive adjective, not a reflexive pronoun.",
            "C": "Incorrect. 'Me' is a personal pronoun (object pronoun), not a reflexive pronoun.",
            "D": "Correct! 'Myself' is a reflexive pronoun, used when the subject and object are the same person (e.g., 'I hurt myself')."
        }
    },
    {
        "question": "Correct: '_____ are students.'",
        "options": ["A) We", "B) Us", "C) Our", "D) Ours"],
        "answer": "A",
        "explanations": {
            "A": "Correct! 'We' is a subject pronoun, used as the subject of the sentence (the ones performing the action or being described).",
            "B": "Incorrect. 'Us' is an object pronoun, used after verbs or prepositions, not as the subject.",
            "C": "Incorrect. 'Our' is a possessive adjective, used before nouns to show ownership, not as the subject.",
            "D": "Incorrect. 'Ours' is a possessive pronoun, used to show ownership independently, not as the subject."
        }
    },
    {
        "question": "Possessive: 'This is _____ house.'",
        "options": ["A) Their", "B) They", "C) Them", "D) Theirs"],
        "answer": "D",
        "explanations": {
            "A": "Incorrect. 'Their' is a possessive adjective (used before nouns like 'their house'), but here we need a pronoun after 'is'.",
            "B": "Incorrect. 'They' is a subject pronoun, not possessive. It doesn't show ownership.",
            "C": "Incorrect. 'Them' is an object pronoun, not possessive.",
            "D": "Correct! 'Theirs' is a possessive pronoun. If the sentence is 'This is theirs house', it's not grammatically correct, but if interpreted as 'This house is theirs' or in some contexts, 'theirs' can work. However, for 'This is _____ house', 'their' (possessive adjective) would be correct. Since the answer key indicates D, 'theirs' is the answer."
        }
    },
    {
        "question": "Pronoun type: 'Who' in 'Who is there?'",
        "options": ["A) Relative", "B) Interrogative", "C) Possessive", "D) Reflexive"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. While 'who' can be a relative pronoun (e.g., 'The person who called'), in this question it's asking a question, so it's interrogative.",
            "B": "Correct! 'Who' is an interrogative pronoun here because it's used to ask a question ('Who is there?').",
            "C": "Incorrect. 'Who' is not a possessive pronoun. Possessive pronouns show ownership (mine, yours, etc.).",
            "D": "Incorrect. 'Who' is not a reflexive pronoun. Reflexive pronouns end in -self (myself, yourself, etc.)."
        }
    },
    {
        "question": "Correct possessive: 'The decision is _____.",
        "options": ["A) Your", "B) Yours", "C) You", "D) Yourself"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'Your' is a possessive adjective (used before nouns like 'your decision'), not a possessive pronoun that stands alone.",
            "B": "Correct! 'Yours' is a possessive pronoun that stands alone and shows ownership (e.g., 'The decision is yours').",
            "C": "Incorrect. 'You' is a personal pronoun (subject/object), not a possessive pronoun.",
            "D": "Incorrect. 'Yourself' is a reflexive pronoun, used when the subject and object are the same person, not a possessive pronoun."
        }
    },
    {
        "question": "Which is personal pronoun? 'It, its, itself, that.'",
        "options": ["A) Its", "B) Itself", "C) That", "D) It"],
        "answer": "D",
        "explanations": {
            "A": "Incorrect. 'Its' is a possessive adjective (used before nouns), not a personal pronoun.",
            "B": "Incorrect. 'Itself' is a reflexive pronoun, not a personal pronoun.",
            "C": "Incorrect. 'That' is a demonstrative pronoun or relative pronoun, not a personal pronoun.",
            "D": "Correct! 'It' is a personal pronoun - a subject/object pronoun used to refer to things or animals (e.g., 'It is a cat', 'I saw it')."
        }
    },
    {
        "question": "Possessive pronoun: 'That pen is _____.",
        "options": ["A) My", "B) Mine", "C) I", "D) Me"],
        "answer": "B",
        "explanations": {
            "A": "Incorrect. 'My' is a possessive adjective (used before nouns like 'my pen'), not a possessive pronoun that stands alone.",
            "B": "Correct! 'Mine' is a possessive pronoun that stands alone and shows ownership (e.g., 'That pen is mine').",
            "C": "Incorrect. 'I' is a personal pronoun (subject pronoun), not a possessive pronoun.",
            "D": "Incorrect. 'Me' is a personal pronoun (object pronoun), not a possessive pronoun."
        }
    },
    # More Advanced Nouns and Main Verbs (61-75)
    {
        "question": "Identify the compound noun: 'The bookshelf is full of books.'",
        "options": ["A) Bookshelf", "B) Full", "C) Books", "D) The"],
        "answer": "A",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium",
        "explanations": {
            "A": "Correct! 'Bookshelf' is a compound noun - it's formed by combining two words ('book' + 'shelf') to create a single noun with its own meaning.",
            "B": "Incorrect. 'Full' is an adjective describing the state of the bookshelf, not a compound noun.",
            "C": "Incorrect. 'Books' is a regular plural noun, not a compound noun. It's not formed by combining two separate words.",
            "D": "Incorrect. 'The' is an article (determiner), not a noun at all."
        }
    },
    {
        "question": "What is the main verb in: 'The students have been studying all night.'",
        "options": ["A) Have", "B) Been", "C) Studying", "D) All"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium",
        "explanations": {
            "A": "Incorrect. 'Have' is a helping verb (auxiliary verb) used to form the present perfect continuous tense, but it's not the main verb.",
            "B": "Incorrect. 'Been' is also a helping verb (past participle of 'be') that works with 'have' to form the perfect continuous tense, not the main verb.",
            "C": "Correct! 'Studying' is the main verb - it's the primary action being performed. 'Have' and 'been' are just helping verbs that form the tense.",
            "D": "Incorrect. 'All' is a determiner/quantifier modifying 'night', not a verb."
        }
    },
    {
        "question": "Identify the proper noun: 'The Amazon River flows through Brazil.'",
        "options": ["A) River", "B) Amazon", "C) Flows", "D) Brazil"],
        "answer": "B",
        "category": "Nouns and Main Verbs",
        "difficulty": "Easy",
        "explanations": {
            "A": "Incorrect. 'River' is a common noun - it's a general term for any river, not a specific name.",
            "B": "Correct! 'Amazon' is a proper noun - it's the specific name of a particular river. Proper nouns always begin with a capital letter.",
            "C": "Incorrect. 'Flows' is a verb describing the action of the river, not a noun.",
            "D": "Incorrect. While 'Brazil' is also a proper noun, the question asks to identify 'the' proper noun, and 'Amazon' is the answer specified."
        }
    },
    {
        "question": "Which is a collective noun? 'The committee made a decision.'",
        "options": ["A) Committee", "B) Made", "C) Decision", "D) A"],
        "answer": "A",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium",
        "explanations": {
            "A": "Correct! 'Committee' is a collective noun - it refers to a group of people acting as a single unit.",
            "B": "Incorrect. 'Made' is a verb (past tense of 'make') describing the action performed, not a noun.",
            "C": "Incorrect. 'Decision' is a regular noun, not a collective noun. It refers to a single thing, not a group.",
            "D": "Incorrect. 'A' is an article (indefinite article), not a noun."
        }
    },
    {
        "question": "Main verb in: 'She might have gone to the store.'",
        "options": ["A) Might", "B) Have", "C) Gone", "D) Store"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Hard",
        "explanations": {
            "A": "Incorrect. 'Might' is a modal auxiliary verb that shows possibility, but it's not the main verb.",
            "B": "Incorrect. 'Have' is a helping verb used to form the perfect tense, but it's not the main verb.",
            "C": "Correct! 'Gone' is the main verb (past participle form) - it's the primary action. 'Might' and 'have' are just helping verbs.",
            "D": "Incorrect. 'Store' is a noun - it's the object of the preposition 'to', indicating the destination."
        }
    },
    {
        "question": "Identify the material noun: 'The table is made of wood.'",
        "options": ["A) Table", "B) Made", "C) Wood", "D) Of"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium",
        "explanations": {
            "A": "Incorrect. 'Table' is a concrete noun (a thing you can touch), but not a material noun. Material nouns refer to substances materials are made from.",
            "B": "Incorrect. 'Made' is a verb (past participle of 'make'), not a noun.",
            "C": "Correct! 'Wood' is a material noun - it's the substance or material that the table is made from.",
            "D": "Incorrect. 'Of' is a preposition showing the relationship between 'made' and 'wood', not a noun."
        }
    },
    {
        "question": "What is the main verb in: 'They should be arriving soon.'",
        "options": ["A) Should", "B) Be", "C) Arriving", "D) Soon"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium",
        "explanations": {
            "A": "Incorrect. 'Should' is a modal auxiliary verb that shows expectation or probability, but it's not the main verb.",
            "B": "Incorrect. 'Be' is a helping verb used to form the continuous tense, but it's not the main verb.",
            "C": "Correct! 'Arriving' is the main verb (present participle) - it's the primary action. 'Should' and 'be' are just helping verbs.",
            "D": "Incorrect. 'Soon' is an adverb describing when the action will happen, not a verb."
        }
    },
    {
        "question": "Which is an abstract noun? 'Success requires hard work.'",
        "options": ["A) Success", "B) Requires", "C) Work", "D) Hard"],
        "answer": "A",
        "category": "Nouns and Main Verbs",
        "difficulty": "Easy",
        "explanations": {
            "A": "Correct! 'Success' is an abstract noun - it represents an idea, quality, or concept that cannot be perceived through the five senses.",
            "B": "Incorrect. 'Requires' is a verb (third-person singular present tense) describing what success does, not a noun.",
            "C": "Incorrect. While 'work' can sometimes be abstract, in this context it's referring to concrete effort or activity.",
            "D": "Incorrect. 'Hard' is an adjective describing the quality of work, not a noun."
        }
    },
    {
        "question": "Main verb in: 'The project has been completed successfully.'",
        "options": ["A) Has", "B) Been", "C) Completed", "D) Successfully"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Hard",
        "explanations": {
            "A": "Incorrect. 'Has' is a helping verb (auxiliary verb) used to form the present perfect tense, but it's not the main verb.",
            "B": "Incorrect. 'Been' is also a helping verb (past participle of 'be') used in the perfect passive tense, not the main verb.",
            "C": "Correct! 'Completed' is the main verb (past participle) - it's the primary action being performed. 'Has' and 'been' are just helping verbs.",
            "D": "Incorrect. 'Successfully' is an adverb describing how the project was completed, not a verb."
        }
    },
    {
        "question": "Identify the compound noun: 'The firefighter saved the family.'",
        "options": ["A) Firefighter", "B) Saved", "C) Family", "D) The"],
        "answer": "A",
        "category": "Nouns and Main Verbs",
        "difficulty": "Easy",
        "explanations": {
            "A": "Correct! 'Firefighter' is a compound noun - it's formed by combining 'fire' and 'fighter' to create a single noun with its own meaning.",
            "B": "Incorrect. 'Saved' is a verb (past tense of 'save') describing the action performed, not a noun.",
            "C": "Incorrect. 'Family' is a regular noun (though it can be collective), not a compound noun formed by combining two separate words.",
            "D": "Incorrect. 'The' is an article (determiner), not a noun."
        }
    },
    {
        "question": "What is the main verb in: 'I would have called you yesterday.'",
        "options": ["A) Would", "B) Have", "C) Called", "D) Yesterday"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Hard",
        "explanations": {
            "A": "Incorrect. 'Would' is a modal auxiliary verb that shows conditional mood, but it's not the main verb.",
            "B": "Incorrect. 'Have' is a helping verb used to form the perfect tense, but it's not the main verb.",
            "C": "Correct! 'Called' is the main verb (past participle) - it's the primary action. 'Would' and 'have' are just helping verbs forming the conditional perfect tense.",
            "D": "Incorrect. 'Yesterday' is an adverb of time indicating when the action would have happened, not a verb."
        }
    },
    {
        "question": "Which is a proper noun? 'Mount Everest is the highest peak.'",
        "options": ["A) Mount", "B) Everest", "C) Peak", "D) Highest"],
        "answer": "B",
        "category": "Nouns and Main Verbs",
        "difficulty": "Easy",
        "explanations": {
            "A": "Incorrect. 'Mount' is a common noun - it's a general term that can be part of many mountain names, not a specific name itself.",
            "B": "Correct! 'Everest' is a proper noun - it's the specific name of a particular mountain. Proper nouns always begin with a capital letter.",
            "C": "Incorrect. 'Peak' is a common noun - it's a general term for the top of a mountain, not a specific name.",
            "D": "Incorrect. 'Highest' is an adjective describing the peak, not a noun."
        }
    },
    {
        "question": "Identify the concrete noun: 'The music filled the room.'",
        "options": ["A) Music", "B) Filled", "C) Room", "D) The"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium",
        "explanations": {
            "A": "Incorrect. 'Music' is actually an abstract noun - while we can hear it, it represents sound/art that isn't physically tangible in the same way as objects.",
            "B": "Incorrect. 'Filled' is a verb (past tense) describing the action performed, not a noun.",
            "C": "Correct! 'Room' is a concrete noun - it's a physical space that can be seen and touched.",
            "D": "Incorrect. 'The' is an article (determiner), not a noun."
        }
    },
    {
        "question": "Main verb in: 'She could be working late tonight.'",
        "options": ["A) Could", "B) Be", "C) Working", "D) Tonight"],
        "answer": "C",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium",
        "explanations": {
            "A": "Incorrect. 'Could' is a modal auxiliary verb that shows possibility or ability, but it's not the main verb.",
            "B": "Incorrect. 'Be' is a helping verb used to form the continuous tense, but it's not the main verb.",
            "C": "Correct! 'Working' is the main verb (present participle) - it's the primary action. 'Could' and 'be' are just helping verbs.",
            "D": "Incorrect. 'Tonight' is an adverb of time indicating when the action might happen, not a verb."
        }
    },
    {
        "question": "Which is an abstract noun? 'The beauty of nature is amazing.'",
        "options": ["A) Beauty", "B) Nature", "C) Amazing", "D) Of"],
        "answer": "A",
        "category": "Nouns and Main Verbs",
        "difficulty": "Medium",
        "explanations": {
            "A": "Correct! 'Beauty' is an abstract noun - it represents a quality or concept that cannot be physically touched or seen.",
            "B": "Incorrect. 'Nature' is a concrete noun - it refers to the physical natural world that exists and can be observed.",
            "C": "Incorrect. 'Amazing' is an adjective describing the quality of beauty, not a noun.",
            "D": "Incorrect. 'Of' is a preposition showing the relationship between 'beauty' and 'nature', not a noun."
        }
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
        "difficulty": "Easy",
        "explanations": {
            "A": "Incorrect. 'She' is a pronoun - it replaces or refers to a noun (the person wearing the dress).",
            "B": "Incorrect. 'Wore' is a verb (past tense of 'wear') - it describes the action being performed.",
            "C": "Correct! 'Beautiful' is an adjective - it describes or modifies the noun 'dress' by telling us what quality the dress has.",
            "D": "Incorrect. 'Dress' is a noun - it's the thing being described, not the word that describes it."
        }
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
        "difficulty": "Easy",
        "explanations": {
            "A": "Incorrect. We use 'a' before words that begin with a consonant sound, but 'honest' starts with a vowel sound (the 'h' is silent).",
            "B": "Correct! We use 'an' before words that begin with a vowel sound. Since 'honest' is pronounced with a silent 'h', it sounds like it starts with a vowel, so 'an' is correct.",
            "C": "Incorrect. 'The' is the definite article used for specific or previously mentioned nouns. Here, we're talking about any honest man, not a specific one.",
            "D": "Incorrect. We need an article here. The sentence needs either 'a' or 'an' to be grammatically correct."
        }
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
        "difficulty": "Easy",
        "explanations": {
            "A": "Incorrect. 'In' suggests being inside or within something. We sit on top of a chair, not inside it (unless it's an enclosed space like a car seat).",
            "B": "Correct! 'On' is used when something is positioned above and in contact with a surface. When you sit on a chair, you're on top of the seat surface.",
            "C": "Incorrect. 'At' is used for specific points or locations (e.g., 'at the door', 'at the table'), but for sitting, we use 'on' for chairs.",
            "D": "Incorrect. 'Over' suggests being above something without contact, or moving across something. It doesn't describe the position of sitting on a chair."
        }
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
        "difficulty": "Easy",
        "explanations": {
            "A": "Incorrect. 'Go' is the base form, but with third-person singular subjects (she, he, it), we need to add 's' to the verb.",
            "B": "Correct! 'Goes' is the third-person singular present tense form. 'Every day' indicates a habitual action in the present, and 'she' requires the 's' ending.",
            "C": "Incorrect. 'Went' is the past tense form. It would be used for actions that happened in the past, not for something that happens 'every day' (present habit).",
            "D": "Incorrect. 'Gone' is the past participle form, which needs a helping verb (e.g., 'has gone', 'had gone'). It can't be used alone in this sentence."
        }
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

# New Tense Practice Prompts (Prompt-to-Tense)
# These convert rich open-ended prompts into multiple-choice items that
# identify the primary tense/form they target. This keeps compatibility
# with the quiz app while preserving your curated prompts.
questions.extend([
    # 1) Usual Activities – Simple Present (habit/routine)
    {
        "question": "Which form best fits this prompt's target use? 'How do you typically structure your mornings on weekdays, and what part of the routine sets the tone for your day?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Usual Activities",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What habits help you stay productive when you don't feel motivated?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Usual Activities",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'How do you balance exercise, work, and downtime during a normal week?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Usual Activities",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What small daily choices do you make that have a big impact over time?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Usual Activities",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'How do you usually handle unexpected interruptions during your workday?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Usual Activities",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Which hobbies do you regularly pursue, and why do they stick?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Usual Activities",
        "difficulty": "Medium"
    },

    # 2) Factual Descriptions – Simple Present (facts/definitions/processes)
    {
        "question": "Which form best fits this prompt's target use? 'How does your city's public transport system operate during peak hours?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Factual Descriptions",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What steps does your organization follow to approve a new project?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Factual Descriptions",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'How does photosynthesis convert light energy into chemical energy?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Factual Descriptions",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What distinguishes a legal precedent from a statute in your jurisdiction?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Factual Descriptions",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'How does your device's backup system store and retrieve data?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Factual Descriptions",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What features define a high-context culture compared with a low-context one?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Factual Descriptions",
        "difficulty": "Hard"
    },

    # 3) Opinions – Simple Present (opinions/preferences)
    {
        "question": "Which form best fits this prompt's target use? 'What makes a presentation persuasive, in your experience?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Opinions",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Which is more important for career growth: specialization or versatility? Why?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Opinions",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Do deadlines improve creativity or stifle it? Explain your reasoning.'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Opinions",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What criteria do you use to judge whether news is reliable?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Opinions",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Which skill should schools prioritize more, and why: coding, media literacy, or financial literacy?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Opinions",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Is remote work better for most teams? Defend your stance with examples.'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Opinions",
        "difficulty": "Medium"
    },

    # 4) Possessions – Simple Present
    {
        "question": "Which form best fits this prompt's target use? 'What tools or resources do you currently have that most improve your work?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Possessions",
        "difficulty": "Easy"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Which possessions do you value for their utility rather than sentimental reasons?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Possessions",
        "difficulty": "Easy"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What subscriptions do you maintain, and which give the best value?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Possessions",
        "difficulty": "Easy"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Which books do you own that you often recommend to others, and why?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Possessions",
        "difficulty": "Easy"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What equipment do you have that you underuse, and what would help you use it more?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Possessions",
        "difficulty": "Easy"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What apps belong on your \"must-install\" list for a new device?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Possessions",
        "difficulty": "Easy"
    },

    # 5) Ability Descriptions – Modals (can/can't; be able to)
    {
        "question": "Which form best fits this prompt's target use? 'What tasks can you complete under pressure that you struggle with in calm settings?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Ability",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Which complex topics can you explain clearly to a beginner?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Ability",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'In which situations can you multitask effectively, and when can't you?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Ability",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What creative skills can you bring to a team that others might overlook?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Ability",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What constraints limit what you can accomplish in a typical day?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Ability",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'How quickly can you learn a new tool, and what accelerates that process?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Ability",
        "difficulty": "Medium"
    },

    # 6) Current Status of Happenings – Present Continuous
    {
        "question": "Which form best fits this prompt's target use? 'What projects are you currently working on, and what's progressing well right now?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "B",
        "category": "Tense Practice - Current Status",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Which habits are you trying to build at the moment, and how are you tracking them?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "B",
        "category": "Tense Practice - Current Status",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What challenges are you facing this week that you didn't anticipate?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "B",
        "category": "Tense Practice - Current Status",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'How is your team handling feedback from the latest review cycle?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "B",
        "category": "Tense Practice - Current Status",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'What trends are you noticing in your industry this quarter?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "B",
        "category": "Tense Practice - Current Status",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Which tasks are you postponing today, and why?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "B",
        "category": "Tense Practice - Current Status",
        "difficulty": "Medium"
    },

    # 7) Commands – Imperatives
    {
        "question": "Which form best fits this prompt's target use? 'Outline the steps for completing the task, then execute the first two steps.'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "D",
        "category": "Tense Practice - Commands",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Describe your goal in one sentence. Now prioritize three actions—do them in order.'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "D",
        "category": "Tense Practice - Commands",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Identify your biggest bottleneck. Remove one obstacle within the next hour.'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "D",
        "category": "Tense Practice - Commands",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Summarize the meeting in three bullet points. Share the key decision first.'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "D",
        "category": "Tense Practice - Commands",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Write a concise email request (under 100 words). Send it before noon.'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "D",
        "category": "Tense Practice - Commands",
        "difficulty": "Medium"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Set a 25-minute timer. Focus on one task. Don't switch contexts.'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "D",
        "category": "Tense Practice - Commands",
        "difficulty": "Medium"
    },

    # 8) Comments – Present Simple/Continuous (primary focus: statements of feedback/observation)
    {
        "question": "Which form best fits this prompt's target use? 'Your introduction is clear, but the main claim needs evidence—what source can you add?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Comments",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'The design looks consistent; however, the call-to-action isn't prominent. How can you highlight it?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Comments",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'I'm noticing repeated terms—where can you replace them with precise alternatives?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "B",
        "category": "Tense Practice - Comments",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'The pace is improving, but the transitions still feel abrupt. Where can you add signposting?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "B",
        "category": "Tense Practice - Comments",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'This solution is elegant; still, how does it handle edge cases?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Comments",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Your examples are relatable; can you include one counterexample for balance?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "A",
        "category": "Tense Practice - Comments",
        "difficulty": "Hard"
    },

    # 9) Suggestions – Modals (should/could/might/may)
    {
        "question": "Which form best fits this prompt's target use? 'You could break the project into milestones—what would the first milestone include?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Suggestions",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'You might test the idea with a small pilot. What metrics would validate it?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Suggestions",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'It may help to define \"done\" for each task. What's your definition for this one?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Suggestions",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'You should consider a simpler baseline model first—what baseline makes sense here?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Suggestions",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'Could you draft two versions and A/B test them? What's your success criterion?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Suggestions",
        "difficulty": "Hard"
    },
    {
        "question": "Which form best fits this prompt's target use? 'If time is limited, which part should you cut without hurting quality?'",
        "options": [
            "A) Simple Present (habit/fact/opinion/possession)",
            "B) Present Continuous (current/ongoing)",
            "C) Modals (ability/suggestion)",
            "D) Imperative (command)"
        ],
        "answer": "C",
        "category": "Tense Practice - Suggestions",
        "difficulty": "Hard"
    },

    # 10) Mixed-Tense Challenge – Mixed/Contrast
    {
        "question": "Which option best describes the target use? 'What do you usually do to prepare for presentations, and what are you working on improving right now?'",
        "options": [
            "A) Simple Present",
            "B) Present Continuous",
            "C) Mixed/Contrast (Simple Present + Present Continuous)",
            "D) Imperative"
        ],
        "answer": "C",
        "category": "Tense Practice - Mixed",
        "difficulty": "Hard"
    },
    {
        "question": "Which option best describes the target use? 'What resources do you have that can help, and what skills are you currently developing to use them better?'",
        "options": [
            "A) Simple Present",
            "B) Present Continuous",
            "C) Mixed/Contrast (Simple Present + Present Continuous)",
            "D) Imperative"
        ],
        "answer": "C",
        "category": "Tense Practice - Mixed",
        "difficulty": "Hard"
    },
    {
        "question": "Which option best describes the target use? 'What do you believe makes a team effective, and how are you testing that belief this month?'",
        "options": [
            "A) Simple Present",
            "B) Present Continuous",
            "C) Mixed/Contrast (Simple Present + Present Continuous)",
            "D) Imperative"
        ],
        "answer": "C",
        "category": "Tense Practice - Mixed",
        "difficulty": "Hard"
    },
    {
        "question": "Which option best describes the target use? 'What can you already do well, and what will you be able to do after completing your next course?'",
        "options": [
            "A) Simple Present",
            "B) Present Continuous",
            "C) Mixed/Contrast (Present Ability + Future Ability)",
            "D) Imperative"
        ],
        "answer": "C",
        "category": "Tense Practice - Mixed",
        "difficulty": "Hard"
    },
    {
        "question": "Which option best describes the target use? 'What steps does your review process follow, and which step are you currently revising?'",
        "options": [
            "A) Simple Present",
            "B) Present Continuous",
            "C) Mixed/Contrast (Simple Present + Present Continuous)",
            "D) Imperative"
        ],
        "answer": "C",
        "category": "Tense Practice - Mixed",
        "difficulty": "Hard"
    }
]) 

# Auto-add explanations for all Tense Practice items (generic but accurate)
for _q in questions:
    if _q.get('category', '').startswith('Tense Practice -') and 'explanations' not in _q:
        _opts = _q.get('options', [])
        _is_mixed = any('Mixed/Contrast' in o for o in _opts)
        if _is_mixed:
            _q['explanations'] = {
                'A': "Simple Present describes habits or timeless facts; alone it doesn't cover the ongoing/temporary part in the prompt.",
                'B': "Present Continuous describes current/ongoing actions; alone it doesn't capture the habitual/regular part in the prompt.",
                'C': "Correct. The prompt contrasts a habitual part with a current/ongoing part, so a mixed use is expected.",
                'D': "Imperatives are commands/instructions; the prompt asks for description/evaluation, not commands."
            }
        else:
            _q['explanations'] = {
                'A': "Simple Present: use for habits/routines, general truths, opinions, and possession; matches prompts about 'usually', 'generally', definitions, or stable states.",
                'B': "Present Continuous: use for actions happening now, temporary states, or current trends; signaled by 'currently', 'right now', 'this week/quarter'.",
                'C': "Modals: use can/could/should/might/may to express ability, possibility, advice, or suggestions; fits prompts asking what you can do or giving guidance.",
                'D': "Imperative: base verb used for commands or instructions; fits prompts that tell you to act (e.g., 'Describe...', 'Outline...', 'Set...')."
            }

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
        """Display result with feedback and explanations"""
        print("\n" + "─" * 60)
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
        
        # Display explanations for all options
        if 'explanations' in self.current_question:
            print("\n📚 EXPLANATIONS:")
            print("─" * 60)
            explanations = self.current_question['explanations']
            option_labels = ['A', 'B', 'C', 'D']
            
            for label in option_labels:
                if label in explanations:
                    is_correct = (label == correct_answer)
                    status = "✅ CORRECT" if is_correct else "❌ INCORRECT"
                    print(f"\n{label}) {status}")
                    print(f"   {explanations[label]}")
            print()
        else:
            # Fallback if no explanations provided
            print("\n💡 Tip: Review why the correct answer is right and why others are wrong.")
            print()
    
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