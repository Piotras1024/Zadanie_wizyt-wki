
from faker import Faker
from faker.providers import company, job, phone_number

fake = Faker()
fake.add_provider(company)
fake.add_provider(job)
fake.add_provider(phone_number)
class BaseContact:
    def __init__(self, imie, nazwisko, telefon_prywatny, adres_email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon_prywatny = telefon_prywatny
        self.adres_email = adres_email
        self.label_length = len(imie+nazwisko)

        self.telefon_korespondencyjny = self.telefon_prywatny
        self.telefon_label = "prywatny"


    def contact(self):
        print(f"Wybieram numer +48 {self.telefon_korespondencyjny} ({self.telefon_label}) i dzwonię do {self.imie} {self.nazwisko}")

class BusinessContact(BaseContact):
    def __init__(self, stanowisko, nazwa_firmy, telefon_sluzbowy, *args, **kwargs):   #po co args i kwargs ?
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.nazwa_firmy = nazwa_firmy
        self.telefon_sluzbowy = telefon_sluzbowy
        self.telefon_korespondencyjny = self.telefon_sluzbowy
        self.telefon_label = "służbowy"

    # def contact(self):
    #     print(f"Wybieram numer +48 {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}")

def create_base_contact():
    fake_name = fake.name()
    fake_imie = fake_name.split(" ")[0]
    fake_nazwisko = fake_name.split(" ")[1]
    fake_telefon_prywatny = fake.msisdn()
    return BaseContact(
        imie=fake_imie,
        nazwisko=fake_nazwisko,
        telefon_prywatny=fake_telefon_prywatny,
        adres_email=f'{fake_imie}.{fake_nazwisko}@fakemail.com'.lower()
    )
def create_busines_contact():
    fake_name = fake.name()
    fake_imie = fake_name.split(" ")[0]
    fake_nazwisko = fake_name.split(" ")[1]
    fake_telefon_prywatny = fake.msisdn()
    fake_stanowisko = fake.job()
    fake_nazwa_firmy = fake.company()
    fake_nazwa_firmy_replace = fake_nazwa_firmy.replace(" ", "")
    fake_telefon_sluzbowy = fake.msisdn()
    return BusinessContact(
        imie=fake_imie,
        nazwisko=fake_nazwisko,
        telefon_prywatny=fake_telefon_prywatny,
        adres_email=f'{fake_imie}.{fake_nazwisko}@{fake_nazwa_firmy_replace}.com'.lower(),
        stanowisko=fake_stanowisko,
        nazwa_firmy=fake_nazwa_firmy,
        telefon_sluzbowy=fake_telefon_sluzbowy
    )

def create_contacts(ilosc, rodzaj_wizytowki):
    tablica_wizytowek = []
    if rodzaj_wizytowki == "BusinessContact":
        for i in range (0,ilosc):
            tablica_wizytowek.append(create_busines_contact())
    if rodzaj_wizytowki == "BaseContact":
        for i in range (0,ilosc):
            tablica_wizytowek.append(create_base_contact())
    return tablica_wizytowek

def wypisz_wizytowki_bazowe(tablica_z_wizytowkami):
    for obiekt in tablica_z_wizytowkami:
        print(f"{obiekt.imie} {obiekt.nazwisko}, telefon prywatny : {obiekt.telefon_prywatny} , email : {obiekt.adres_email}")

def wypisz_wizytowki_biznesowe(tablica_z_wizytowkami):
    for obiekt in tablica_z_wizytowkami:
        print(f"{obiekt.imie} {obiekt.nazwisko}, telefon prywatny : {obiekt.telefon_prywatny} , email : {obiekt.adres_email} na stanowisku {obiekt.stanowisko} w firmie {obiekt.nazwa_firmy}, telefon służbowy : {obiekt.telefon_sluzbowy}")
#def contact_private(nazwisko, tabela_wizytowek):
#    for obiekt in tabela_wizytowek:
#        if obiekt.nazwisko == nazwisko:
#            print(f"Wybieram numer +48 {obiekt.telefon_prywatny} i dzwonię do {obiekt.imie} {obiekt.nazwisko}")


wizytowki = []

wizytowki.append(
    BaseContact(
        imie="Juliusz",
        nazwisko="Cezar",
        adres_email="juliusz.cezar@tesla.com",
        telefon_prywatny="999"
    )
)

wizytowki.append(
    BaseContact(
        imie="Juliusz",
        nazwisko="Anderson",
        adres_email="juliusz.anderson@tesla.com",
        telefon_prywatny="997"
    )
)


wizytowki.append(
    BusinessContact(
        imie="Piotr",
        nazwisko="Dab",
        adres_email="pio.dab@gmail.com",
        telefon_prywatny="787992898",
        stanowisko="Dyspozytor",
        nazwa_firmy="PSG",
        telefon_sluzbowy="332443554"
    )
)

a = wizytowki[0]
b = wizytowki[1]
c = wizytowki[2]
a.contact()
b.contact()
c.contact()
nowa=[]
nowa.append(create_busines_contact())
print(nowa[0].imie)
q = create_contacts(3,"BusinessContact")
print("Busines Contact")
wypisz_wizytowki_biznesowe(q)
print("----------------------------------"
      "Base Contact")
z = create_contacts(10, "BaseContact")

wypisz_wizytowki_bazowe(z)

print(z[9].label_length)
z[9].contact()
