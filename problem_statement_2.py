from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

stopwords = ['i','me','my','myself','we','our','ours','you',"you're","you've","you'll","you'd",'your','yours','yourself',
'yourselves','he','him','his','himself','she',"she's",'her','hers','herself','it',"it's",'its','itself','they','them','their',
'theirs','themselves','what','which','who','whom','this','that',"that'll",'these','those','am','is','are','was','were','be',
'been','being','have','has','had','having','do','does','did','a','an','the','and','but','if','or','because','as','until',
'while','of','at','by','for','with','about','between','into','through','after','above','below','to','from','up','down','in','out','on',
'off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more',
'most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don',"don't",'should'
,"should've",'now','d','ll','m','o','re','ve','y','ain','aren',"aren't",'couldn',"couldn't",'didn',"didn't",'doesn',"doesn't",'hadn',"hadn't",
'hasn',"hasn't",'haven',"haven't",'isn',"isn't",'ma','mightn',"mightn't",'mustn',"mustn't",'needn',"needn't",'shan',"shan't",'shouldn',"shouldn't",
'wasn',"wasn't",'weren',"weren't",'won',"won't",'wouldn',"wouldn't"]

# corpus = ["good morning","how are you doing ?","the weather is awesome today","samsung","good afternoon","baseball is played in the USA","there is a thunderstorm","are you doing good ?","The polar regions are melting","apple","nokia","cricket is a fun game","the climate change is a problem"]
# corpus = ["Football is played in Brazil" ,"Traveling is good for health","Cricket is played in India","People love traveling in winter"]

symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    
def to_lower(data):
    return [i.lower() for i in data]

def remove_stopword(corpus):
    new_corpus = []
    for i in corpus:
        new_text = ""
        for w in i.split(" "):
            if w not in stopwords:
                new_text = new_text+' '+w
        new_corpus.append(new_text)
    return new_corpus

def remove_symbols(corpus):
    new_corpus = []
    for i in corpus:
        new_text = ""
        for w in i.split(" "):
            if w not in symbols:
                new_text = new_text+" "+w
        new_corpus.append(new_text)
    return new_corpus

def get_similar_sents(corpus,result,similar_matrix):
    set_of_index = []
    for i in result: 
        temp = set() 
        for j in i: 
            temp = temp|set(similar_matrix[j]) 
        set_of_index.append(list(temp))
    return [[corpus[i] for i in m] for m in set_of_index] 


def main(corpus):
    main_corpus = corpus
    corpus = to_lower(corpus)
    corpus = remove_stopword(corpus)
    corpus = remove_symbols(corpus)
    vectorizer=TfidfVectorizer()
    features=vectorizer.fit_transform(corpus)
    similarity = cosine_similarity(features,features)
    similar_matrix = [[j for j in range(len(i)) if i[j]>0]for i in similarity]

    list_2 = [i for i in range(len(similar_matrix))]
    result = []
    while len(list_2)>0:
        list_ = list_2
        temp = similar_matrix[list_[0]]
        temp_id = [list_[0]]
        list_2 = []
        for i in list_[1:]:
            temp2 = [x in temp for x in similar_matrix[i]]
            if any(temp2):
                if len(temp) > len(similar_matrix[i]):
                    continue
                else:
                    temp = similar_matrix[i]
                    temp_id.append(i)
            else:
                list_2.append(i)
        result.append(temp_id)
    out = get_similar_sents(main_corpus,result, similar_matrix)
    del vectorizer,similarity,similar_matrix
    return out