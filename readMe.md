# PYTHON GET ANY CAR DATA (JSON)

this project i made for the purpose of easing the development or practice of back-end and front-end using the car data as a placeholder. using the web /auto-data.net to gather the data and selenium to traverse in the web.

## Cloning the repo

```console
git clone https://github.com/kiddogum/python-json-car-data.git
```

## JSON result

```json
{
  "general_information": {
    "brand": "Porsche",
    "model": "718",
    "generation": "718 Cayman (982)",
    "modification": "GT4 RS 4.0 (493 Hp) PDK",
    "start_of_production": "2022 year",
    "powertrain_architecture": "Internal Combustion engine",
    "body_type": "Coupe",
    "seats": "2",A
    "doors": "2"
  },
  "performance_specs": {
    "combined_fuel_consumption": "13.2 l/100 km",
    "co2_emissions": "281 g/km",
    "fuel_consumption_combined": "12.3 l/100 km",
    "fuel_type": "Petrol (Gasoline)",
    "acceleration_0_100_km/h": "3.4 sec",
    "acceleration_0_62_mph": "3.4 sec",
    "acceleration_0_60_mph": "3.2 sec",
    "maximum_speed": "315 km/h",
    "weighttopower_ratio": "3 kg/Hp, 336.7 Hp/tonne",
    "weighttotorque_ratio": "3.3 kg/Nm, 306.7 Nm/tonne"
  },
  "engine_specs": {
    "power": "493 Hp @ 8400 rpm.",
    "power_per_litre": "123.4 Hp/l",
    "torque": "449 Nm @ 6250 rpm.",
    "maximum_engine_speed": "9000 rpm.",
    "engine_layout": "Middle, Longitudinal",
    "engine_model/code": "MDG.GA",
    "engine_displacement": "3996 cm3",
    "number_of_cylinders": "6",
    "engine_configuration": "Boxer",
    "cylinder_bore": "102 mm",
    "piston_stroke": "81.5 mm",
    "number_of_valves_per_cylinder": "4",
    "fuel_injection_system": "Direct injection",
    "engine_aspiration": "Naturally aspirated engine",
    "valvetrain": "DOHC",
    "engine_oil_specification": "Log in to see.",
    "engine_systems": "Particulate filter"
  },
  "space_volume_and_weights": {
    "kerb_weight": "1464 kg",
    "max_weight": "1771 kg",
    "max_load": "307 kg",
    "trunk_space_maximum": "136 l",
    "fuel_tank_capacity": "64 l"
  },
  "dimensions": {
    "length": "4455 mm",
    "width": "1822 mm",
    "width_including_mirrors": "1994 mm",
    "height": "1267 mm",
    "wheelbase": "2484 mm",
    "ride_height": "102 mm",
    "drag_coefficient": "0.33",
    "approach_angle": "6.4-10.6�",
    "rampover_angle": "10.3�"
  },
  "images": {
    "image_1": "https://www.auto-data.net/images/f77/Porsche-718-Cayman-982.jpg",
    "image_2": "https://www.auto-data.net/images/f95/Porsche-718-Cayman-982.jpg",
    "image_3": "https://www.auto-data.net/images/f119/Porsche-718-Cayman-982.jpg",
    "image_4": "https://www.auto-data.net/images/f110/Porsche-718-Cayman-982.jpg",
    "image_5": "https://www.auto-data.net/images/f47/Porsche-718-Cayman-982_4.jpg",
    "image_6": "https://www.auto-data.net/images/f114/Porsche-718-Cayman-982.jpg",
    "image_7": "https://www.auto-data.net/images/f128/Porsche-718-Cayman-982_2.jpg",
    "image_8": "https://www.auto-data.net/images/f110/Porsche-718-Cayman-982_2.jpg",
    "image_9": "https://www.auto-data.net/images/f111/Porsche-718-Cayman-982.jpg",
    "image_10": "https://www.auto-data.net/images/f125/Porsche-718-Cayman-982_2.jpg",
    "image_11": "https://www.auto-data.net/images/f78/Porsche-718-Cayman-982.jpg",
    "image_12": "https://www.auto-data.net/images/f48/Porsche-718-Cayman-982.jpg",
    "image_13": "https://www.auto-data.net/images/f128/Porsche-718-Cayman-982_4.jpg",
    "image_14": "https://www.auto-data.net/images/f56/Porsche-718-Cayman-982.jpg",
    "image_15": "https://www.auto-data.net/images/f47/Porsche-718-Cayman-982_2.jpg",
    "image_16": "https://www.auto-data.net/images/f102/Porsche-718-Cayman-982.jpg",
    "image_17": "https://www.auto-data.net/images/f118/Porsche-718-Cayman-982.jpg"
  }
}

```

## Installing / Set-up and Using the repo

### making the venv folder

if you are using VSCode IDE, you can do <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> to open up VSCode Command Pallete and the search for Python: Create Environment... After that Click Venv and click on Python version 3.12, as that is the version I am using to make this project.

now VSCode will automatically make the venv folder for you

### activate the venv

to use python venv, you will have to activate the scripts inside .venv folder, usually it is behind the bin or the Scripts folder, so you can run in the terminal:

```console
path\to\your\activate\file
```

or (example)

```console
.venv\Scripts\activate
```

### Install the libraries

the needed libraries is all in the requirements.txt file, so to navigate and install the libraries you can run this in the terminal:

```console
pip install -r requirements.txt
```

### Change the car model

to change the car model you wanted to fetch, you will have to change the string inside app.py file, the variable you need to change is:

```python
search_model = '718 cayman 2024'
```

### Run the project

to run the project, run this in the terminal and wait until the project has finished gathering the data:

```console
python app.py
```

when finished the data result will be seen on the car_model.json as a JSON file.
