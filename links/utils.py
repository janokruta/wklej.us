from string import ascii_letters, digits
from random import randint, choice


def random_string_generator(size=8, chars=ascii_letters + digits):
    return ''.join(choice(chars) for _ in range(size))


def unique_slug_generator(instance):
    slug = random_string_generator(size=randint(3, 6)).lower()
    while instance.__class__.objects.filter(slug=slug).exists():
        slug = random_string_generator(size=randint(3, 6)).lower()
    return slug
