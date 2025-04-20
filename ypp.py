 

---

### ✅ Project: Unit Converter (Beginner Level)

#### 📁 Folder Structure
```
unit_converter/
├── converter.py
└── main.py
```

---

### 📄 `converter.py`
This file contains the core conversion logic.

```python
# converter.py

def convert_length(value, from_unit, to_unit):
    # Conversion rates to meters
    conversion_to_meters = {
        "meters": 1,
        "kilometers": 1000,
        "feet": 0.3048,
        "inches": 0.0254,
        "miles": 1609.34,
        "centimeters": 0.01
    }

    if from_unit not in conversion_to_meters or to_unit not in conversion_to_meters:
        raise ValueError("Invalid unit.")

    # Convert from the source unit to meters
    value_in_meters = value * conversion_to_meters[from_unit]

    # Convert from meters to the target unit
    result = value_in_meters / conversion_to_meters[to_unit]

    return result
```

---

### 📄 `main.py`
This file handles user input and calls the conversion function.

```python
# main.py

from converter import convert_length

def main():
    print("Welcome to the Unit Converter!")

    print("\nAvailable units: meters, kilometers, feet, inches, miles, centimeters")

    try:
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from: ").lower()
        to_unit = input("Enter the unit to convert to: ").lower()

        result = convert_length(value, from_unit, to_unit)
        print(f"\n{value} {from_unit} = {result:.4f} {to_unit}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("Something went wrong. Please check your inputs.")

if __name__ == "__main__":
    main()
```

---

### ▶️ How to Run in VS Code

1. Open the `unit_converter` folder in VS Code.
2. Open a terminal (`Ctrl + ~`) and make sure you're in the correct folder.
3. Run the app:
   ```bash
   python main.py
   ```

---

