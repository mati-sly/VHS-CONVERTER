# 📼 VCR Manager | Nightwave Edition

**Trae el pasado al presente.** Convierte tus archivos digitales en cintas VHS de los 90.

**VCR Manager** es una aplicación de escritorio desarrollada en **Python** que combina la potencia del motor **ntsc-rs** (escrito en Rust) con **FFmpeg** para transformar videos e imágenes modernas, otorgándoles una auténtica estética analógica, tanto visual como sonora.

---

## 📺 Captura de pantalla

La interfaz cuenta con **fondos animados aleatorios** inspirados en el estilo *City Pop / Vaporwave*.

---

## ✨ Características principales

### 🎨 Estética Vaporwave / Win95

Interfaz gráfica nostálgica con fondos animados aleatorios y un diseño retro‑futurista.

### 🔊 Audio analógico realista

* Conversión automática de audio a **AAC** para máxima compatibilidad.
* Aplicación de filtros **Low‑Pass (paso bajo)** para simular la calidez y opacidad del sonido de una cinta VHS.
* **Modo a prueba de fallos**: detecta videos sin audio automáticamente para evitar errores de renderizado.

### 🌎 Entrada universal

Soporta arrastrar y procesar casi cualquier formato de entrada:
`.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`, `.png`, `.jpg`, `.webp`.

### ⚡ Motor híbrido

* **Visual**: Emulación de señal compuesta NTSC mediante *ntsc-rs*.
* **Core**: Orquestación robusta con **Python + PyQt6**.

---

## 🛠️ Requisitos del sistema

Para ejecutar el código fuente o compilar el proyecto, necesitas:

* **Python 3.x** instalado.
* **FFmpeg** instalado y accesible desde la terminal.

### Linux (Mint / Ubuntu / Debian)

```bash
sudo apt install ffmpeg
```

### Librerías de Python

```bash
pip install PyQt6 pyinstaller
```

---

## 🚀 Instalación y uso (código fuente)

1. **Clonar el repositorio**

```bash
git clone https://github.com/mati-sly/VHS-CONVERTER.git
cd VHS-CONVERTER
```

2. **Verificar permisos del binario**
   Asegúrate de que el motor en Rust tenga permisos de ejecución:

```bash
chmod +x bin/ntsc-rs-cli
```

3. **Ejecutar la aplicación**

```bash
python main.py
```

---

## 🏗️ Compilación (crear ejecutable)

El proyecto está preparado para ser compilado con **PyInstaller**. El código incluye una función `resource_path` para gestionar correctamente los archivos internos (GIFs, iconos y binarios) dentro del ejecutable portátil.

Ejecuta el siguiente comando en la raíz del proyecto:

```bash
pyinstaller --noconfirm --onefile --windowed --name "VCR_Manager" \
  --add-data "assets:assets" \
  --add-binary "bin/ntsc-rs-cli:bin" \
  --icon "assets/icon.png" \
  main.py
```

El ejecutable final se generará en la carpeta **`dist/`**.

---

## 📂 Estructura del proyecto

```
├── assets/          # GIFs animados, icono del sistema y recursos gráficos
├── bin/             # Binario compilado de ntsc-rs (motor de video)
├── main.py          # Código fuente principal (lógica + GUI)
└── README.md        # Documentación oficial
```

---

## 👨‍💻 Créditos

* **Desarrollador**: Matías
* **Motor VHS**: Basado en el proyecto open‑source *ntsc-rs*
* **Procesamiento de medios**: FFmpeg

<div align="center"><sub>Desarrollado con ❤️ y mucha estática en Linux Mint. © 2026</sub></div>
