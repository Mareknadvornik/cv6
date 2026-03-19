import math
import matplotlib.pyplot as plt


# =========================
# Funkce pro výpočty kružnic
# =========================

def radius_sum(r1, r2):
    return r1 + r2


def euclid_distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


def has_intersection(circle_1, circle_2, tol=1e-9):
    d = euclid_distance(circle_1['x'], circle_1['y'], circle_2['x'], circle_2['y'])
    r_sum = radius_sum(circle_1['r'], circle_2['r'])
    r_diff = abs(circle_1['r'] - circle_2['r'])

    if math.isclose(d, 0, abs_tol=tol) and math.isclose(circle_1['r'], circle_2['r'], abs_tol=tol):
        # na sobě
        return {"intersects": True, "intersections_count": float('inf')}
    elif d > r_sum + tol:
        # daleko od sebe
        return {"intersects": False, "intersections_count": 0}
    elif d < r_diff - tol:
        # Jedna uvnitř druhé bez dotyku
        return {"intersects": False, "intersections_count": 0}
    elif math.isclose(d, r_sum, abs_tol=tol) or math.isclose(d, r_diff, abs_tol=tol):
        # jednom bodě
        return {"intersects": True, "intersections_count": 1}
    else:
        # Mají dva průniky
        return {"intersects": True, "intersections_count": 2}



def draw_data(circle_1, circle_2):
    """Vykreslí dvě kružnice do grafu."""
    fig, ax = plt.subplots()

    c1 = plt.Circle((circle_1['x'], circle_1['y']), circle_1['r'], fill=False, color="blue", label="Circle 1")
    c2 = plt.Circle((circle_2['x'], circle_2['y']), circle_2['r'], fill=False, color="red", label="Circle 2")

    ax.add_patch(c1)
    ax.add_patch(c2)

    # Nastavení rozsahu os podle polohy a velikosti kružnic
    all_x = [circle_1['x'], circle_2['x']]
    all_y = [circle_1['y'], circle_2['y']]
    all_r = [circle_1['r'], circle_2['r']]

    x_min = min(all_x[i] - all_r[i] for i in range(2)) - 1
    x_max = max(all_x[i] + all_r[i] for i in range(2)) + 1
    y_min = min(all_y[i] - all_r[i] for i in range(2)) - 1
    y_max = max(all_y[i] + all_r[i] for i in range(2)) + 1

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_aspect("equal")
    ax.set_title("Intersection of Two Circles")
    ax.legend()

    plt.show()


# =========================
# Hlavní skript
# =========================

if __name__ == "__main__":
    # Definice kružnic
    circle_1 = {"x": 0, "y": 8, "r": 2}
    circle_2 = {"x": 0, "y": 8, "r": 1}

    # Zjištění průniku
    result = has_intersection(circle_1, circle_2)

    # Výpis výsledku
    if result['intersections_count'] == float('inf'):
        print("Kružnice jsou totožné a mají nekonečně mnoho průniků.")
    elif result['intersects']:
        print(f"Kružnice se protínají a mají {result['intersections_count']} průnik(y).")
    else:
        print("Kružnice se neprotínají.")

    # Vykreslení kružnic
    draw_data(circle_1, circle_2)