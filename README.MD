<div align="center">

📼 VCR Manager | Nightwave Edition
A VHS-era video converter with authentic analog aesthetics

🇺🇸 English
 · 🇪🇸 Español

</div>
📼 VCR Manager | Nightwave Edition (English) 🇺🇸

Bring the past to the present.
Convert modern digital files into authentic 90s-style VHS tapes.

VCR Manager is a desktop application developed in Python, combining the ntsc-rs engine (Rust) with FFmpeg to recreate the visual and sonic imperfections of analog VHS media.

📺 Screenshot

Random animated backgrounds inspired by City Pop / Vaporwave aesthetics.

✨ Features
🎨 Visual Aesthetics

Vaporwave / Win95-inspired interface

Random animated backgrounds

Retro-futuristic UI design

🔊 Analog Audio Simulation

Automatic conversion to AAC

Low-Pass filters to emulate VHS warmth and muffling

Failsafe mode for videos without audio tracks

🌎 Universal Input

Drag & drop support for most common formats:

.mp4 · .mkv · .avi · .mov · .flv · .png · .jpg · .webp

⚡ Hybrid Processing Engine

Video: NTSC composite signal emulation via ntsc-rs

Core: Python + PyQt6 orchestration

🛠️ System Requirements

Python 3.x

FFmpeg (available in PATH)

Linux (Mint / Ubuntu / Debian)

sudo apt install ffmpeg

Python Dependencies
pip install PyQt6 pyinstaller

🚀 Installation (Source Code)
git clone https://github.com/mati-sly/VHS-CONVERTER.git
cd VHS-CONVERTER
chmod +x bin/ntsc-rs-cli
python main.py

🏗️ Build (Create Executable)
pyinstaller --noconfirm --onefile --windowed --name "VCR_Manager" \
  --add-data "assets:assets" \
  --add-binary "bin/ntsc-rs-cli:bin" \
  --icon "assets/icon.png" \
  main.py

📂 Project Structure
├── assets/          # Animated GIFs, icons, visual resources
├── bin/             # ntsc-rs compiled binary
├── main.py          # Core logic + GUI
└── README.md        # Documentation

👨‍💻 Credits

Developer: Matías

VHS Engine: Based on ntsc-rs

Media Processing: FFmpeg

<div align="center"> <sub>Developed with ❤️ and plenty of static on Linux Mint. © 2026</sub> </div>
📼 VCR Manager | Nightwave Edition (Español) 🇪🇸

Trae el pasado al presente.
Convierte archivos digitales modernos en cintas VHS con estética auténtica de los años 90.

VCR Manager es una aplicación de escritorio desarrollada en Python que combina el motor ntsc-rs (Rust) con FFmpeg para recrear las imperfecciones visuales y sonoras del formato VHS.

📺 Captura de pantalla

Fondos animados aleatorios inspirados en el estilo City Pop / Vaporwave.

✨ Características
🎨 Estética visual

Interfaz inspirada en Vaporwave / Win95

Fondos animados aleatorios

Diseño retro-futurista

🔊 Simulación de audio analógico

Conversión automática a AAC

Filtros Low-Pass para simular la calidez del VHS

Modo a prueba de fallos para videos sin audio

🌎 Entrada universal

Soporta arrastrar y soltar la mayoría de formatos:

.mp4 · .mkv · .avi · .mov · .flv · .png · .jpg · .webp

⚡ Motor híbrido

Video: Emulación de señal NTSC mediante ntsc-rs

Core: Python + PyQt6

🛠️ Requisitos del sistema

Python 3.x

FFmpeg accesible desde la terminal

Linux (Mint / Ubuntu / Debian)

sudo apt install ffmpeg

Dependencias de Python
pip install PyQt6 pyinstaller

🚀 Instalación (código fuente)
git clone https://github.com/mati-sly/VHS-CONVERTER.git
cd VHS-CONVERTER
chmod +x bin/ntsc-rs-cli
python main.py

🏗️ Compilación (crear ejecutable)
pyinstaller --noconfirm --onefile --windowed --name "VCR_Manager" \
  --add-data "assets:assets" \
  --add-binary "bin/ntsc-rs-cli:bin" \
  --icon "assets/icon.png" \
  main.py

📂 Estructura del proyecto
├── assets/          # GIFs animados, iconos y recursos visuales
├── bin/             # Binario compilado de ntsc-rs
├── main.py          # Lógica principal + GUI
└── README.md        # Documentación

👨‍💻 Créditos

Desarrollador: Matías

Motor VHS: Basado en el proyecto open-source ntsc-rs

Procesamiento de medios: FFmpeg

<div align="center"> <sub>Desarrollado con ❤️ y mucha estática en Linux Mint. © 2026</sub> </div>
