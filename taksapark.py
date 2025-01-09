
class Taksopark:
    def __init__(self, title):
        self.title = title
        self.balance = 0
        self.cars = []
        self.safarlar = []

    def add_car(self, car):
        self.cars.append(car)

    def add_safar(self, safar):
        self.safarlar.append(safar)
        self.balance += safar.narx * 0.1


class Car:
    def __init__(self, raqami, daraja, haydovchi_ismi):
        self.raqami = raqami
        self.balance = 0
        self.daraja = daraja
        self.haydovchi_ismi = haydovchi_ismi


class Client:
    def __init__(self, ism, tel_raqami, balans):
        self.ism = ism
        self.tel_raqami = tel_raqami
        self.card = Card(balans, self)


class Card:
    def __init__(self, balans, card_egasi):
        self.balans = balans
        self.card_egasi = card_egasi


class Safar:
    def __init__(self, client, car, qayerdan, qayerga, narx):
        self.client = client
        self.car = car
        self.qayerdan = qayerdan
        self.qayerga = qayerga
        self.narx = narx

def tariflarni_korsatish():
    print("--- Avtomobil darajalari va narxlari ---")
    narxlar = {"Ekonom": 3000, "Komfort": 4000, "Biznes": 5000}
    umumiy_narx = 100
    for daraja, km_narx in narxlar.items():
        print(f"{daraja}: {umumiy_narx * km_narx} so'm (1 km uchun {km_narx} so'm)")
    return narxlar


def main_menu():
    print("\n=== Xush kelibsiz! ===")
    print("1. Yangi safar boshlash")
    print("2. Taksopark haqida ma'lumot")
    print("3. Chiqish")
    return input("Tanlovingizni kiriting (1-3): ")


def telefon_tekshirish(clients):
    while True:
        tel_raqam = input("Telefon raqamingizni kiriting: ")
        for client in clients:
            if client.tel_raqami == tel_raqam:
                print(f"Xush kelibsiz, {client.ism}!")
                return client
        print("Bunday telefon raqami mavjud emas. Qaytadan kiriting.")


if __name__ == "__main__":
    taksopark = Taksopark("Yandex Taxi")

    avtomobillar = [
        # Bu yulduzchalar haydovchini darajasini bildiradi
        Car("R001AA", "Ekonom", "Muxammad  * "),
        Car("R002AA", "Komfort", "Humoyun **"),
        Car("R004AA", "Biznes", "Farrux *****"),
        Car("R005AA", "Komfort", "Shoxrux ****"),
    ]
    taksopark.cars = avtomobillar

    clients = [
        Client("Ali", "+998901234501", 100000),
        Client("Bobur", "+998901234502", 50000),
        Client("Dilshod", "+998901234503", 200000),
        Client("Elbek", "+998901234504", 15000),
        Client("Farrux", "+998901234505", 300000000),
    ]

    while True:
        tanlov = main_menu()
        if tanlov == "1":
            print("=== Yangi safar ===")

            client = telefon_tekshirish(clients)

            qayerdan = input("Qayerdan (manzil): ")
            qayerga = input("Qayerga (manzil): ")

            tariflar = tariflarni_korsatish()

            daraja = input("Avtomobil darajasini tanlang (Ekonom/Komfort/Biznes): ")
            if daraja not in tariflar:
                print("Noto'g'ri daraja tanlandi. Safar bekor qilindi.")
                continue

            narx = 100 * tariflar[daraja]

            if client.card.balans < narx:
                print(f"Mablag' yetarli emas! Kartadagi balans: {client.card.balans} so'm, safar narxi: {narx} so'm")
                continue

            mos_cars = [car for car in taksopark.cars if car.daraja == daraja]
            if not mos_cars:
                print(f"{daraja} darajasidagi avtomobil mavjud emas!")
                continue


            car = mos_cars[0]
            print(f"Biriktirilgan mashina: {car.raqami}, Daraja: {car.daraja}, Haydovchi: {car.haydovchi_ismi}")

            safar = Safar(client, car, qayerdan, qayerga, narx)
            taksopark.add_safar(safar)

            client.card.balans -= narx
            car.balance += narx * 0.8
            print(f"Safar yakunlandi. Narx: {narx} so'm")
            print(f"Taksopark balansi: {taksopark.balance} so'm")
            print(f"Haydovchi balansi: {car.balance} so'm")
            print(f"Qolgan balans: {client.card.balans} so'm")

        elif tanlov == "2":
            print("=== Taksopark haqida ma'lumot ===")
            print(f"Taksopark nomi: {taksopark.title}")
            print(f"Umumiy balans: {taksopark.balance} so'm")
            print(f"Avtomobillar soni: {len(taksopark.cars)}")
            print(f"Safarlar soni: {len(taksopark.safarlar)}")

        elif tanlov == "3":
            print("Dasturdan chiqilmoqda...")
            break

        else:
            print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")
