# Commands required
# pip install spacy
# pip install spacy-transformers
# python -m spacy download en_core_web_trf

import spacy


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

