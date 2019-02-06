states = {
    "CA": "California",
    "VA": "Virginia",
    "MD": "Maryland",
    "RI": "Rhode Island",
    "NV": "Nevada"
}

print(states["CA"])
print(states["NV"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39550000
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8500000
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034382
    }

}

print(nested_dictionary["NV"]["POPULATION"])
print(nested_dictionary["RI"]["NAME"])

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39550000,
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8500000,
        "CITIES": [
            "Richmond",
            "Norfolk",
            "Alexandria"

        ]
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718,
        "CITIES": [
            "Bethesda",
            "Baltimore",
            "Annapolis"
        ]
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315,
        "CITIES": [
            "Providence",
            "Newport",
            "Warwick"
        ]
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034382,
        "CITIES": [
            "Carson City",
            "Las Vegas",
            "Reno"
        ]
    }

}

print(complex_dictionary["RI"]["CITIES"][2])
print(complex_dictionary["VA"]["NAME"])
print(complex_dictionary["MD"]["CITIES"][0])

print(complex_dictionary.keys())
print(nested_dictionary.items())

print()
for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)

print()
for state, facts in complex_dictionary.items():
    for attr, value in facts.items():
        print(attr)
        print(value)
        print("-" * 20)
    print("=" * 20)


# adding to dictionary
states['AL'] = "Alaska?"

# changing a dictionary value

states['AL'] = "Alabama"

