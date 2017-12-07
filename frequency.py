import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

stopwords = set(stopwords.words('english'))
# added stopwords to nltk list from tweet outputs
stopwords.update(("another","rt", "here", 'go', "i've", "it's", "we've", "we'll", "you're",
                    "were","your","their","they're","there","aren't","didn't","that's",
                    "however","although","except","great","s","t","yet","you","us","w","i",
                    "it","u","re","a","go","h","ed","n","f","let","gt","tha","al","ne","th"))

#stopwords from https://github.com/igorbrigadir/stopwords/blob/master/en/ranksnl_large.txt
stopwords.update(('able', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act',
                'actually', 'added', 'adj', 'affected', 'affecting', 'affects', 'afterwards',
                'ah', 'almost', 'alone', 'along', 'already', 'also', 'always', 'among', 'amongst',
                'announce', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway',
                'anyways', 'anywhere', 'apparently', 'approximately', 'arent', 'arise', 'around',
                'aside', 'ask', 'asking', 'auth', 'available', 'away', 'awfully', 'b', 'back',
                'became', 'become', 'becomes', 'becoming', 'beforehand', 'begin','begins', 'behind',
                'beside', 'besides', 'beyond', 'biol', 'brief', 'briefly', 'c', 'ca', 'came','cannot',
                'certain','certainly', 'co', 'com', 'come', 'comes', 'contain', 'containing', 'contains',
                'could', 'couldnt', 'done', 'downwards', 'due', 'e', 'edu','effect', 'eg', 'eight',
                'eighty', 'either', 'else', 'elsewhere', 'end', 'ending','enough', 'especially',
                'et', 'et', 'etc', 'even', 'ever', 'every', 'everybody','everyone', 'everything',
                'everywhere', 'ex', 'far', 'ff', 'fifth', 'first', 'five','fix', 'followed',
                'following', 'follows', 'former', 'formerly', 'forth', 'found','four', 'furthermore',
                'g', 'gave', 'get', 'gets', 'getting', 'give', 'given','gives', 'giving', 'goes',
                'gone', 'got', 'gotten', 'happens', 'hardly', 'hed', 'hence', 'hereafter', 'hereby',
                'herein', 'heres', 'hereupon', 'hes', 'hi', 'hid','hither', 'home', 'howbeit',
                'hundred', 'id', 'ie', 'im', 'immediately', 'inc', 'indeed', 'index', 'instead', 'inward',
                'itd', 'j', 'k', 'keep', 'keeps', 'kept', 'kg', 'km', 'know', 'known', 'knows', 'l',
                'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest',
                'lets', 'like', 'liked', 'likely', 'line', 'little', 'look', 'looking', 'looks',
                'ltd', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'mean', 'means',
                'meantime', 'meanwhile', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'moreover',
                'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'na', 'name', 'namely', 'nay', 'nd',
                'near', 'nearly', 'necessarily','neither', 'never','nevertheless', 'new', 'next',
                'nine', 'ninety', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'normally', 'nos',
                'noted', 'nothing', 'nowhere', 'obtain', 'obtained', 'obviously', 'often', 'oh', 'ok',
                'okay', 'old', 'omitted', 'one', 'ones', 'onto', 'ord', 'others', 'otherwise', 'ought',
                'outside', 'overall', 'owing', 'p', 'page', 'pages', 'part', 'particular', 'particularly',
                'per', 'perhaps', 'placed', 'please', 'plus', 'poorly', 'possible', 'possibly',
                'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'probably',
                'promptly', 'proud', 'provides', 'put', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran',
                'rather', 'rd', 'readily', 'really', 'recent', 'recently', 'ref', 'refs', 'regarding',
                'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted',
                'resulting', 'results', 'right', 'run', 'said', 'saw', 'say', 'saying', 'says', 'sec',
                'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves',
                'sent', 'seven', 'several', 'shall', 'shed', 'shes', 'show', 'showed', 'shown', 'showns',
                'significantly','similar', 'similarly', 'since', 'six', 'slightly', 'somebody', 'somehow',
                'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere',
                'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'still', 'stop',
                'strongly', 'sub', 'substantially', 'successfully', 'sufficiently', 'suggest', 'sup',
                'sure', 'take', 'taken', 'taking', 'tell', 'tends', 'thank', 'thanks', 'thanx', 'thats',
                'thence', 'thereafter', 'thereby', 'thered', 'therefore', 'therein', 'thereof', 'therere',
                'theres', 'thereto', 'thereupon', 'theyd', 'theyre', 'think', 'thou', 'though', 'thoughh',
                'thousand', 'throug', 'throughout', 'thru', 'thus', 'til', 'tip', 'together', 'took',
                'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'twice', 'two',
                'un', 'unfortunately', 'unless', 'unlike', 'unlikely', 'unto', 'upon', 'ups', 'use', 'used',
                'useful', 'usefully', 'usefulness', 'uses', 'using', 'usually', 'v', 'value', 'various', 'via',
                'viz', 'vol', 'vols', 'vs', 'want', 'wants', 'wasnt', 'way', 'wed', 'welcome', 'went', 'werent',
                'whatever', 'whats', 'whence', 'whenever', 'whereafter', 'whereas', 'whereby', 'wherein',
                'wheres', 'whereupon', 'wherever', 'whether', 'whim', 'whither', 'whod', 'whoever', 'whole',
                'whomever', 'whos', 'whose', 'widely', 'willing', 'within', 'without', 'wont', 'words',
                'would', 'wouldnt', 'www', 'x', 'yes', 'youd', 'youre', 'z', 'zero'))
 
# Following functions are used to extract frequency of words
def openFile(filename):
    fh = open(filename, "r+")
    str = fh.read()
    fh.close()
    return str
 
def removePunct(str):
    # Replace one or more non-word (non-alphanumeric) chars with a space
    exception = "#@"
    str = re.sub(r'[^\w'+exception+']', ' ', str)
    str = str.lower()
    return str
 
def wordBin(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt
 
def tf(filename, topwords):
    txt = openFile(filename)
    txt = removePunct(txt)
    words = txt.split(' ')

    # remove stopwords
    resultwords  = [word for word in words if word.lower() not in stopwords]

    bins = wordBin(resultwords)
    total = (len(resultwords))
    for key, value in bins.most_common(topwords):
        # get only the words who have appeared at least 10 times
        if value > 9:
            print key

# total words count
# biden = 13641
# clinton = 30443
# mccain = 34672
# obama = 29582
# pence = 34565
# romney = 15209
# ryan = 18100
# sanders = 34622
# trump = 34238
# warren = 31975


tf('politicians/files/clean/biden.txt', 1000)
tf('politicians/files/clean/clinton.txt', 1000)
tf('politicians/files/clean/mccain.txt', 1000)
tf('politicians/files/clean/obama.txt', 1000)
tf('politicians/files/clean/pence.txt', 1000)
tf('politicians/files/clean/romney.txt', 1000)
tf('politicians/files/clean/ryan.txt', 1000)
tf('politicians/files/clean/sanders.txt', 1000)
tf('politicians/files/clean/trump.txt', 1000)
tf('politicians/files/clean/warren.txt', 1000)
