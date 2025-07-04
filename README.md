# macroPAD
# Natasha’s Sensory Fidget v1

A 5-key macropad powered by the Seeed Studio XIAO RP2040, designed as a colorful, tactile fidget tool that also sends useful keyboard shortcuts — with reactive RGB lighting using SK6812Mini LEDs!

---

## 💡 Features

- 🎛️ 5 tactile pushbuttons
- 🌈 2 SK6812Mini RGB LEDs (addressable NeoPixels)
- ⌨️ Sends keyboard shortcuts (Copy, Paste, etc.)
- 🧠 Unique LED color feedback for each key
- 🔌 USB HID device — plug and use with any computer

---

## 🔧 Hardware

- **Microcontroller:** XIAO RP2040 (CircuitPython-compatible)
- **Switches:** 5x pushbuttons (direct GPIO)
- **LEDs:** 2x SK6812Mini (WS2812-compatible)
- **PCB Design:** Custom (KiCad) — see `/pcb/` folder

---

## 🗂️ Key Functions

| Key | Shortcut | LED Color     |
|-----|----------|---------------|
| 1   | Ctrl+C   | Hot Pink      |
| 2   | Ctrl+V   | Turquoise     |
| 3   | Ctrl+X   | Orange        |
| 4   | Ctrl+Z   | Purple        |
| 5   | Ctrl+Y   | Lime Green    |

---

## 🧪 Installation

### 1. Flash CircuitPython

Follow [Adafruit’s guide](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) to flash CircuitPython onto the XIAO RP2040.

### 2. Install Required Libraries

Use [Circup](https://learn.adafruit.com/using-circup) or copy these manually into `lib/` on the board:

- `kmk/`
- `adafruit_hid/`
- `neopixel.mpy`

### 3. Add Your Firmware

Save the `code.py` file (from this repo) onto the root of the CIRCUITPY drive.

---

## 🚀 Usage

- Plug into USB — it acts as a keyboard!
- Press any button to trigger a shortcut and light up the LEDs.
- You can edit the macros and colors inside `code.py`.

---

## 🖼️ Preview

![PCB Layout](./images/pcb_layout.png)

---

## 🛠️ Customize

Want to:

- Change shortcuts? → Edit the `keyboard.keymap` list
- Change colors? → Edit the `COLORS` list in `code.py`
- Add layers, encoders, OLEDs? → KMK can handle it!

Let me know if you’d like advanced config examples.

---

## 📄 License

MIT License — open source and remix-friendly!

---

## ✨ Credits

- Designed by Natasha Doan
- Powered by [KMK Firmware](https://github.com/KMKfw/kmk_firmware)
- Built with ❤️ and tactile joy

