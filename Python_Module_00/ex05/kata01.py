#!/usr/bin/env python3.7

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

for language, creator in languages.items():
    print(language, 'was created by', creator)
