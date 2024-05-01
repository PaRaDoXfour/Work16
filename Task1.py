import nltk
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import gutenberg

# Завантаження пакету Gutenberg для доступу до корпусу текстів
nltk.download('gutenberg')

# Отримання переліку текстів у пакеті Gutenberg
files = nltk.corpus.gutenberg.fileids()
print(files[8])  # Виведення восьмого файлу зі списку, щоб перевірити, що доступ є

# Спроба зчитування вибраного тексту; обробка помилки, якщо файл відсутній
try:
    text = gutenberg.raw(files[8])
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)


# Функція для підрахунку кількості слів у тексті
def count_words(text):
    sentences = nltk.sent_tokenize(text)  # Токенізація тексту на речення
    k_words = 0
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)  # Токенізація речення на слова
        k_words += len(words)  # Підрахунок слова в кожному реченні
    return k_words


# Функція для знаходження і візуалізації 10 найбільш вживаних слів у тексті
def most_used_words(text, num_words=10):
    words = nltk.word_tokenize(text.lower())  # Токенізація і переведення тексту у нижній регістр
    filtered_words = [word for word in words if word.isalpha()]  # Фільтрація, щоб виключити не-слова (розділові знаки)
    cnt = Counter(filtered_words)  # Підрахунок слова
    common_words = cnt.most_common(num_words)  # Отримання top N найчастіше вживаних слів

    x = [word for word, _ in common_words]  # Слова для візуалізації
    y = [count for _, count in common_words]  # Частота кожного слова

    plt.bar(x, y)  # Створення гістограми
    plt.title(f"{num_words} найбільш вживаних слів у тексті")
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()

    return set(x)  # Повертаємо набір слів для подальшого видалення


# Перший виклик функції для відображення 10 найпопулярніших слів
most_used = most_used_words(text)

# Видаляємо ці слова з тексту, формуючи новий текст з вилученими словами
words = nltk.word_tokenize(text.lower())
filtered_text = ' '.join([word for word in words if word not in most_used])

# Викликаємо функцію ще раз, щоб показати наступні 10 найпопулярніших слів у зміненому тексті
most_used_words(filtered_text)
