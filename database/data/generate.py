from faker import Faker

def generate_kits() -> list:
    pass

def main() -> None:
    locales = ['it_IT', 'fr_FR', 'de_DE', 'es_ES', 'nl_NL', 'pl_PL']
    europenan_fake_names = Faker(locales)
    
    european_names = [europenan_fake_names.name() for _ in range(50)]

    for name in european_names:
        print(name)



if __name__ == "__main__":
    main()