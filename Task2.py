import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize
import string

# Завантаження необхідних ресурсів NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Читання тексту з файлу
with open('textfrom100worlds.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Токенізація по словам
tokens = word_tokenize(text)

# Лемматизація
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(token) for token in tokens]

# Стеммінг
stemmer = PorterStemmer()
stemmed = [stemmer.stem(token) for token in lemmatized]

# Видалення стоп-слів
filtered_words = [word for word in stemmed if word.lower() not in stopwords.words('english')]

# Видалення пунктуації
final_text = ' '.join([word for word in filtered_words if word not in string.punctuation])

# Запис обробленого тексту у новий файл
with open('processed_text.txt', 'w', encoding='utf-8') as file:
    file.write(final_text)
