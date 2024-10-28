from faker import Faker

def main():
    fake = Faker()
    for i in range(69):
        print(fake.name())

if __name__ == "__main__":
    main()