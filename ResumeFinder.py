import nltk;
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def sentence_similarity(sentence1, sentence2):
    stopwords_list = set(stopwords.words("english"))
    
    sentence1_tokens = [token.lower() for token in word_tokenize(sentence1) if token.lower() not in stopwords_list]
    sentence2_tokens = [token.lower() for token in word_tokenize(sentence2) if token.lower() not in stopwords_list]
    
    sentence1_synsets = [wordnet.synsets(token)[0] for token in sentence1_tokens if len(wordnet.synsets(token)) > 0]
    sentence2_synsets = [wordnet.synsets(token)[0] for token in sentence2_tokens if len(wordnet.synsets(token)) > 0]
    
    score = 0.0
    
    for synset1 in sentence1_synsets:
        for synset2 in sentence2_synsets:
            if synset1.wup_similarity(synset2) is not None:
                score += synset1.wup_similarity(synset2)
    
    return score / (len(sentence1_synsets) + len(sentence2_synsets))



def find_best_candidate(job_requirements, candidates):
    best_candidate = None
    best_score = 0.0
    
    for candidate in candidates:
        resume = candidate['resume']
        score = sentence_similarity(job_requirements, resume)
        
        if score > best_score:
            best_score = score
            best_candidate = candidate
    
    return best_candidate



job_requirements = "We are looking for a candidate with strong programming skills, experience in machine learning, and good communication skills."

candidates = [
    {
        'name': 'Candidate 1',
        'resume': "I have a degree in computer science and 5 years of experience in Python programming. I have worked on various machine learning projects and have excellent communication skills."
    },
    {
        'name': 'Candidate 2',
        'resume': "I am a software engineer with expertise in programming languages like Java and C++. I have some exposure to machine learning techniques and can communicate effectively."
    },
    {
        'name': 'Candidate 3',
        'resume': "I have a background in data analysis and statistics. While I don't have much experience in programming, I am a quick learner and have good communication skills."
    }
]



best_candidate = find_best_candidate(job_requirements, candidates)
print("Best candidate:", best_candidate['name'])
