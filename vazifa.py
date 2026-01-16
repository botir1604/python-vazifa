import json

# 1. Ota sinfni yaratamiz (Asosiy qolip)
class Game:
    def start(self):
        # Bu metod barcha o'yinlar uchun umumiy nom
        return "O'yin boshlanmoqda..."

# 2. Chess (Shaxmat) sinfi - Game'dan hamma xususiyatni oladi
class Chess(Game):
    def start(self):
        # Polimorfizm: Ota sinfdagi start() metodini shaxmatga moslab o'zgartirdik
        return "Shaxmat o'yini boshlandi. Oqlar yurishni boshlaydi."

# 3. Football (Futbol) sinfi - Bu ham Game'dan meros oladi
class Football(Game):
    def start(self):
        # Polimorfizm: start() metodini futbolga moslab qayta yozdik
        return "Futbol o'yini boshlandi. Hakam hushtagi chalindi!"

# --- Polimorfizmni tekshirish ---

# O'yinlardan nusxa (obyekt) olamiz
shaxmat = Chess()
futbol = Football()

# Ularni bitta ro'yxatga solamiz
o_yinlar_ro_yxati = [shaxmat, futbol]

natija_json = []

for o_yin in o_yinlar_ro_yxati:
    # Mana shu yerda polimorfizm ishlaydi: 
    # bitta start() buyrug'i har xil sinfda har xil natija beradi
    malumot = {
        "o_yin_turi": o_yin.__class__.__name__,
        "xabar": o_yin.start()
    }
    natija_json.append(malumot)

# Natijani terminalga JSON formatida chiqaramiz
print(json.dumps(natija_json, indent=4))
