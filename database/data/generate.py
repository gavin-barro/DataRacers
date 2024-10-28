from faker import Faker

def main():
    locales = ['it_IT', 'fr_FR', 'de_DE', 'es_ES', 'nl_NL', 'pl_PL']
    fake = Faker(locales)
    
    european_names = [fake.name() for _ in range(50)]

    for name in european_names:
        print(name)

if __name__ == "__main__":
    main()