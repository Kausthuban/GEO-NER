# Commands required
# pip install spacy
# pip install spacy-transformers
# python -m spacy download en_core_web_trf

import spacy

# Load the en_core_web_trf model.
# nlp = spacy.load("en_core_web_trf")
# print("loaded")
# Create a spaCy document from the location words.
def extract(nlp,text):
    location_words = text
    doc = nlp(location_words)

    # Iterate over the tokens in the document and print their named entity type.
    test = []
    locations = []
    for token in doc:
        test.append(token.ent_type_)
        if token.ent_type_ == "GPE":
            locations.append(1)
        else:
            locations.append(0)

    print(test)

    result = []
    temp_start = -1
    for i in range(len(locations)):
        if locations[i] == 1:
            if temp_start == -1:
                temp_start = i
        elif temp_start != -1:
            result.append(doc[temp_start:i])
            temp_start = -1

    # Append the last sequence if it ends with 'GPE'
    if temp_start != -1:
        result.append(doc[temp_start:])

    return result

# batch_res = []
# sentences = ["New York City is a bustling metropolis located in the United States.",
# "London is the capital city of England and the United Kingdom.",
# "The Eiffel Tower is located in Paris, France.",
# "Sydney is the largest city in Australia, known for its iconic Opera House.",
# "Tokyo, Japan's capital, is a vibrant city known for its advanced technology and rich culture.",
# "The Great Wall of China is a historic landmark in Beijing, China.",
# "Rio de Janeiro, located in Brazil, is famous for its Carnival festival.",
# "The Taj Mahal, situated in Agra, India, is an architectural marvel.",
# "Rome, the capital of Italy, is renowned for its ancient ruins and art treasures.",
# "Cape Town, a city in South Africa, offers stunning views of Table Mountain"]
# for i in sentences:
#     batch_res.append(extract(i))

# for i in batch_res:
#     print(i)

# txt = "The climate in Arakkonam is Different from Madurai, which is a neighbouring area. This shows that areas in chennai have differences in weather, the same applies for Tamil Nadu and Kerala"
# print(extract(txt))