from flask import Flask, jsonify

# 1. CLASS QISMI
class Animal:
    def __init__(self, species, name, speed=0.0):
        self.species = species
        self.name = name
        self.speed = speed
        self.activities = []

    def run(self, distance):
        time = distance / (self.speed if self.speed > 0 else 1)
        self.activities.append(f"Run: {distance} km")
        return f"{self.name} runs {distance} km"

    def jump(self, height):
        self.activities.append(f"Jump: {height} m")
        return f"{self.name} jumped"

    def to_dict(self):
        return {
            "species": self.species,
            "name": self.name,
            "current_speed": self.speed,
            "activity_log": self.activities
        }

# 2. FLASK QISMI
app = Flask(__name__)

@app.route('/animal-test') # Manzil shu yerda belgilangan
def animal_test():
    try:
        my_animal = Animal("Dog", "Oktosh", 20.5)
        my_animal.run(5.0)
        my_animal.jump(1.2)
        return jsonify(my_animal.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
