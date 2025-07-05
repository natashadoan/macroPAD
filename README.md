# Natasha’s Sensory Fidget Macropad!

A 5-key tactile RGB macropad built with the Seeed Studio XIAO RP2040. This project is designed for sensory feedback, creative expression, and workflow speed, featuring bright colored LEDs that change with each keypress. It can be used as a stress/anxiety/boredom reliever or for functional keyboard shortcuts.

This was my very first time using Kicad and designing a PCB, which was actually very fun! My friends and I go to artisan pop up markets in my hometown often, and I always see keypad fidget toys, so when I saw the beginner friendly project was a hackpad, I knew I had to attempt it!

---
## an overview

![Hackpad Overview](images/hackpad_overview.png)

_My overview shows the entire macropad, including where the 5 keys are located, the PCB, and the top and bottom covers_

---

## schematic

![Schematic](images/schematic.png)

_My schematic uses 5 pushbuttons to GPIO pins and two SK6812MINI RGB LEDs connected with one line_

---

## PCB layout:

![PCB Layout](images/pcb_layout.png)

_My PCB was designed in KiCad (first time!). Buttons are routed directly to the GPIOs, and my SK6812MINI LEDs flank either side of the of controller._

---

## case design & assembly

![Case Rendering](images/bottomCase_CAD.png)
![Case Rendering](images/topCase_CAD.png)

_My top and bottom cases can be attached with 4 screws on each corner of the case, and adequately hold the PCB and 5 buttons._

- **Top Plate:** Holds all 5 switches in place
- **Bottom Plate:** Secures the PCB from underneath
- **Standoffs/Screws:** Holds together the entire case

---

## Bill of Materials (BOM)

| Qty | Component              | Description                             | Part/Link                        |
|-----|------------------------|-----------------------------------------|----------------------------------|
| 1   | XIAO RP2040            | Microcontroller (tiny + USB-C)          | [Seeed XIAO RP2040](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html) |
| 5   | Tactile Switches       | Mechanical push buttons (through-hole)  | [e.g., MX-compatible or 6mm tact] |
| 2   | SK6812MINI LEDs        | Addressable RGB LED (WS2812-compatible) | [SK6812MINI](https://www.adafruit.com/product/3484) |
| 1   | PCB                    | Custom PCB for layout                   | _Generated via KiCad_           |
| 1   | Case (3D-printed)      | Top and bottom shell                    | _Printed or laser-cut acrylic_  |
| 5   | Resistors (optional)   | Pull-up resistors (not needed with KMK) | _Usually 10kΩ, optional_        |
| -   | Screws/Standoffs       | M2 or M3 depending on hole size         | _To secure case_                |

---

## features of this pad:
- reactive RGB LEDs (each key sets a unique color) - pink, orange, turquoise, green, or purple!
- 5 dedicated macro keys (copy, paste, cut, undo, redo)
- open-source firmware using KMK (it was CircuitPython)

---

## credits + license:

Designed with fun & exhaustion! This took me multiple days to get working as it was my first time working with hardware~ Glad I tried and learned!

