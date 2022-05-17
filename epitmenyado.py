#1. feladat
buildings = []
with open("utca.txt") as file:
    for x, building in enumerate(file):
        building = building.strip().split()
        if x != 0:
            building = {
                'tax_number': building[0],
                'street': building[1],
                'housenumber': building[2],
                'tax_zone': building[3],
                'area': int(building[4])
            }
            buildings.append(building)

print(f"2. feladat. A mintában {len(buildings)} telek szerepel.")
tax_number, volt = input("3. feladat. Egy tulajdonos adószáma: "), False
for building in buildings:
    if tax_number == building['tax_number']:
        print(f"{building['street']} street {building['housenumber']}")
        volt = True
if not volt:
    print("Nem szerepel az adatállományban.")

def tax(tax_zone, area):
    if tax_zone == 'A' and 800 * area >=10000:
        return 800 * area
    elif tax_zone == 'B' and 600 * area >=10000:
        return 600 * area
    elif tax_zone == 'C' and 100 * area >=10000:
        return 100 * area
    else:
        return 0

zone_a, zone_b, zone_c, = 0, 0, 0
sum_a, sum_b, sum_c = 0, 0, 0
for building in buildings:
    if building['tax_zone'] == 'A':
        zone_a += 1
        sum_a += tax(building['tax_zone'],building['area'])
    if building['tax_zone'] == 'B':
        zone_b += 1
        sum_b += tax(building['tax_zone'],building['area'])
    if building['tax_zone'] == 'C':
        zone_c += 1
        sum_c += tax(building['tax_zone'],building['area'])

print(f"""5. feladat
A sávba {zone_a} telek esik, az adó {sum_a} Ft.
B sávba {zone_b} telek esik, az adó {sum_b} Ft.
C sávba {zone_c} telek esik, az adó {sum_c} Ft.""")

print("6. feladat. A több sávba sorolt utcák:")
other_zone = set()
for x, building in enumerate(buildings):
    if building['tax_zone'] != buildings[x - 1]['tax_zone'] and building['street'] == buildings[x - 1]['street']:
        other_zone.add(building['street'])
for building in sorted(other_zone):
    print(building)

tax_numbers = {}
for building in buildings:
    if tax_numbers.get(building['tax_number'], 0):
        tax_numbers[building['tax_number']] += tax(building['tax_zone'], building['area'])
    else:
        tax_numbers[building['tax_number']] = tax(building['tax_zone'], building['area'])

with open("fizetendo.txt", "w", encoding="utf-8") as file:
    for key, value in tax_numbers.items():
        print(f"{key} {value}", file = file)