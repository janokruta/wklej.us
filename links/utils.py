from string import ascii_letters, digits
from random import randint, choice


def random_string_generator(size, chars=ascii_letters[:26] + digits):
    return ''.join(choice(chars) for _ in range(size))


def unique_slug_generator(instance):
    slug = random_string_generator(size=randint(3, 5))
    while instance.__class__.objects.filter(slug=slug).exists():
        slug = random_string_generator(size=randint(3, 5))
    return slug
