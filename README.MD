<div align="center">

📼 VCR Manager | Nightwave Edition
English | Español

</div>
📼 VCR Manager | Nightwave Edition (English) 🇺🇸

Bring the past to the present.
Convert your digital files into authentic 90s VHS tapes.

VCR Manager is a desktop application developed in Python that combines the power of the ntsc-rs engine (written in Rust) with FFmpeg to transform modern videos and images, giving them a truly analog aesthetic—both visually and sonically.

📺 Screenshot

The interface features random animated backgrounds inspired by City Pop / Vaporwave aesthetics.

✨ Main Features
🎨 Vaporwave / Win95 Aesthetics

Nostalgic graphical interface

Random animated backgrounds

Retro-futuristic design

🔊 Realistic Analog Audio

Automatic audio conversion to AAC for maximum compatibility

Low-Pass filters to simulate VHS warmth and sound opacity

Failsafe Mode: automatically detects videos without audio to prevent rendering errors

🌎 Universal Input

Supports drag-and-drop processing of almost any format:

.mp4, .mkv, .avi, .mov, .flv, .png, .jpg, .webp

⚡ Hybrid Engine

Visual: NTSC composite signal emulation via ntsc-rs

Core: Robust orchestration using Python + PyQt6

🛠️ System Requirements

To run the source code or compile the project:

Python 3.x

FFmpeg (available in PATH)

Linux (Mint / Ubuntu / Debian)

sudo apt install ffmpeg

Python Libraries
pip install PyQt6 pyinstaller

🚀 Installation & Usage (Source Code)

Clone the repository:

git clone https://github.com/mati-sly/VHS-CONVERTER.git
cd VHS-CONVERTER


Verify binary permissions:

chmod +x bin/ntsc-rs-cli


Run the application:

python main.py

🏗️ Compilation (Create Executable)

Run the following command from the project root:

pyinstaller --noconfirm --onefile --windowed --name "VCR_Manager" \
  --add-data "assets:assets" \
  --add-binary "bin/ntsc-rs-cli:bin" \
  --icon "assets/icon.png" \
  main.py

📂 Project Structure
├── assets/          # Animated GIFs, system icon, graphic resources
├── bin/             # Compiled ntsc-rs binary (video engine)
├── main.py          # Main source code (logic + GUI)
└── README.md        # Official documentation

👨‍💻 Credits

Developer: Matías

VHS Engine: Based on the ntsc-rs project

Media Processing: FFmpeg

<div align="center"> <sub>Developed with ❤️ and plenty of static on Linux Mint. © 2026</sub> </div>
📼 VCR Manager | Nightwave Edition (Español) 🇪🇸

Trae el pasado al presente.
Convierte tus archivos digitales en cintas VHS auténticas de los años 90.

VCR Manager es una aplicación de escritorio desarrollada en Python que combina la potencia del motor ntsc-rs (escrito en Rust) con FFmpeg para transformar videos e imágenes modernas, otorgándoles una estética analógica real, tanto visual como sonora.

📺 Captura de pantalla

La interfaz cuenta con fondos animados aleatorios inspirados en el estilo City Pop / Vaporwave.

✨ Características principales
🎨 Estética Vaporwave / Win95

Interfaz gráfica nostálgica

Fondos animados aleatorios

Diseño retro-futurista

🔊 Audio analógico realista

Conversión automática de audio a AAC

Filtros Low-Pass (paso bajo) para simular la calidez del VHS

Modo a prueba de fallos: detecta videos sin audio automáticamente

🌎 Entrada universal

Soporta arrastrar y procesar casi cualquier formato:

.mp4, .mkv, .avi, .mov, .flv, .png, .jpg, .webp

⚡ Motor híbrido

Visual: Emulación de señal compuesta NTSC mediante ntsc-rs

Core: Orquestación robusta con Python + PyQt6

🛠️ Requisitos del sistema

Para ejecutar el código fuente o compilar el proyecto:

Python 3.x

FFmpeg accesible desde la terminal

Linux (Mint / Ubuntu / Debian)

sudo apt install ffmpeg

Librerías de Python
pip install PyQt6 pyinstaller

🚀 Instalación y uso (código fuente)

Clonar el repositorio:

git clone https://github.com/mati-sly/VHS-CONVERTER.git
cd VHS-CONVERTER


Verificar permisos del binario:

chmod +x bin/ntsc-rs-cli


Ejecutar la aplicación:

python main.py

🏗️ Compilación (crear ejecutable)

Ejecuta el siguiente comando en la raíz del proyecto:

pyinstaller --noconfirm --onefile --windowed --name "VCR_Manager" \
  --add-data "assets:assets" \
  --add-binary "bin/ntsc-rs-cli:bin" \
  --icon "assets/icon.png" \
  main.py

📂 Estructura del proyecto
├── assets/          # GIFs animados, icono del sistema y recursos gráficos
├── bin/             # Binario compilado de ntsc-rs (motor de video)
├── main.py          # Código fuente principal (lógica + GUI)
└── README.md        # Documentación oficial

👨‍💻 Créditos

Desarrollador: Matías

Motor VHS: Basado en el proyecto open-source ntsc-rs

Procesamiento de medios: FFmpeg

<div align="center"> <sub>Desarrollado con ❤️ y mucha estática en Linux Mint. © 2026</sub> </div>
