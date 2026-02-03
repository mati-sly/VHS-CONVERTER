import sys
import os
import subprocess
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                             QWidget, QFileDialog, QLabel, QCheckBox, QFrame)
from PyQt6.QtCore import QThread, pyqtSignal, Qt, QTimer
from PyQt6.QtGui import QMovie, QIcon

# --- FUNCIÓN NECESARIA PARA PYINSTALLER ---
# Permite que el programa encuentre sus archivos (binarios e imágenes) 
# tanto en modo desarrollo como dentro del ejecutable comprimido.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ==========================================
#   MOTOR LÓGICO: UNIVERSAL & ROBUSTO
# ==========================================
class EngineThread(QThread):
    finished = pyqtSignal(str)

    def __init__(self, input_path, output_path, apply_audio):
        super().__init__()
        self.input_path = input_path
        self.output_path = output_path
        self.apply_audio = apply_audio

    def run(self):
        # Detectar extensión para saber si es imagen o video
        ext = os.path.splitext(self.input_path)[1].lower()
        is_image = ext in ['.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tiff', '.gif']
        
        # --- MODIFICACIÓN CLAVE: Usamos resource_path para el binario ---
        binary_path = resource_path(os.path.join("bin", "ntsc-rs-cli"))

        # En Linux, al descomprimirse el ejecutable, el binario a veces pierde
        # el permiso de ejecución. Esto lo arregla automáticamente.
        if not os.access(binary_path, os.X_OK):
            os.chmod(binary_path, 0o755)

        if is_image:
            # --------------------------------------
            # MODO IMAGEN
            # --------------------------------------
            # Si el usuario eligió mp4 por error en imagen, forzamos png
            if self.output_path.endswith(".mp4"):
                self.output_path = self.output_path.replace(".mp4", ".png")

            temp_render = "temp_image_render.mp4"
            
            # 1. ntsc-rs genera un video corto de la imagen
            subprocess.run([binary_path, "-i", self.input_path, "-o", temp_render])
            
            # 2. Extraemos el primer frame como imagen final
            if os.path.exists(temp_render):
                subprocess.run(["ffmpeg", "-y", "-i", temp_render, "-vframes", "1", self.output_path])
                os.remove(temp_render)
                
        else:
            # --------------------------------------
            # MODO VIDEO
            # --------------------------------------
            temp_video = "temp_vhs_video.mp4"
            
            # 1. Procesamiento visual (ntsc-rs)
            subprocess.run([binary_path, "-i", self.input_path, "-o", temp_video])

            # 2. Procesamiento de Audio (Plan A / Plan B / Plan C)
            success = False
            
            if self.apply_audio:
                # PLAN A: Filtro Lo-Fi + Conversión AAC (Universal)
                # Usamos AAC para asegurar compatibilidad con MP4
                cmd_audio = [
                    "ffmpeg", "-y", "-i", temp_video, "-i", self.input_path,
                    "-filter_complex", "[1:a]lowpass=f=3000,volume=1.5[a]",
                    "-map", "0:v", "-map", "[a]", 
                    "-c:v", "copy",   # Video se copia tal cual
                    "-c:a", "aac",    # Audio se convierte a estándar
                    "-b:a", "192k", 
                    self.output_path
                ]
                result = subprocess.run(cmd_audio, capture_output=True)
                if result.returncode == 0: success = True
            else:
                # PLAN B: Audio Original + Conversión AAC
                cmd_audio = [
                    "ffmpeg", "-y", "-i", temp_video, "-i", self.input_path, 
                    "-map", "0:v", "-map", "1:a", 
                    "-c:v", "copy", 
                    "-c:a", "aac",
                    self.output_path
                ]
                result = subprocess.run(cmd_audio, capture_output=True)
                if result.returncode == 0: success = True

            # PLAN C: Fallback Mudo (Si el video original no tenía audio)
            if not success:
                print("Aviso: Fallo de audio o video mudo. Generando video sin sonido...")
                cmd_silent = ["ffmpeg", "-y", "-i", temp_video, "-c:v", "copy", "-an", self.output_path]
                subprocess.run(cmd_silent, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # Limpieza de temporales
            if os.path.exists(temp_video): os.remove(temp_video)
            
        self.finished.emit(self.output_path)

# ==========================================
#   INTERFAZ GRÁFICA: NIGHTWAVE EDITION
# ==========================================
class Win95Plaza(QMainWindow):
    def __init__(self, background_gif, icon_path):
        super().__init__()
        self.setWindowTitle("VCR Manager v1.0 | Universal Edition")
        self.setFixedSize(600, 500)
        
        # --- CONFIGURACIÓN DE ICONO (SISTEMA) ---
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # --- FONDO ANIMADO ---
        self.bg_label = QLabel(self)
        self.bg_label.setGeometry(0, 0, 600, 500)
        self.bg_label.setScaledContents(True)
        
        if background_gif and os.path.exists(background_gif):
            self.bg_movie = QMovie(background_gif)
            self.bg_label.setMovie(self.bg_movie)
            self.bg_movie.start()
        
        self.bg_label.lower() 

        # --- HOJA DE ESTILOS (VAPORWAVE / WIN95) ---
        self.setStyleSheet("""
            QFrame#MainPanel {
                background-color: #c0c0c0;
                border-top: 2px solid #fff;
                border-left: 2px solid #fff;
                border-right: 2px solid #000;
                border-bottom: 2px solid #000;
            }
            QLabel#Title { 
                color: #fff; 
                font-family: 'Courier New'; 
                font-weight: bold;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #000080, stop:1 #1084d0);
                padding: 4px;
            }
            QPushButton { 
                background-color: #c0c0c0; 
                color: #000; 
                border-top: 2px solid #fff;
                border-left: 2px solid #fff;
                border-right: 2px solid #808080;
                border-bottom: 2px solid #808080;
                padding: 10px;
                font-family: 'MS Sans Serif';
                font-weight: bold;
            }
            QPushButton:pressed { 
                border-top: 2px solid #808080;
                border-left: 2px solid #808080;
                border-right: 2px solid #fff;
                border-bottom: 2px solid #fff;
            }
            QCheckBox { color: #000; font-weight: bold; background: transparent; }
            
            QLabel#Status {
                background-color: #000; color: #05ffa1; border: 2px inset #808080; font-family: monospace;
            }
            
            /* Estilo para los créditos */
            QLabel#Credits {
                color: #555;
                font-family: 'MS Sans Serif';
                font-size: 10px;
                font-style: italic;
                background: transparent;
            }
        """)

        # --- LAYOUT PRINCIPAL ---
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 50, 50, 50) 
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # --- PANEL CENTRAL (COMPACTO) ---
        self.panel = QFrame()
        self.panel.setObjectName("MainPanel")
        # Altura reducida a 240px para que se vea compacto
        self.panel.setFixedSize(400, 240)
        
        panel_layout = QVBoxLayout()
        panel_layout.setSpacing(10)
        panel_layout.setContentsMargins(15, 15, 15, 15)

        # 1. Barra de Título Falsa
        self.title_bar = QLabel(" VHS_CONVERTER.EXE ")
        self.title_bar.setObjectName("Title")
        panel_layout.addWidget(self.title_bar)

        # 2. Botón de Carga
        self.btn_load = QPushButton("📂 CARGAR ARCHIVO")
        self.btn_load.clicked.connect(self.start)
        panel_layout.addWidget(self.btn_load)

        # 3. Checkbox de Audio
        self.audio_check = QCheckBox("AUDIO ANALÓGICO")
        self.audio_check.setChecked(True)
        panel_layout.addWidget(self.audio_check)

        # Espaciador (Stretch)
        panel_layout.addStretch()

        # 4. CRÉDITOS (A la derecha)
        self.credits = QLabel("dev by Matías © 2026")
        self.credits.setObjectName("Credits")
        self.credits.setAlignment(Qt.AlignmentFlag.AlignRight)
        panel_layout.addWidget(self.credits)

        # 5. Barra de Estado
        self.status = QLabel(" SISTEMA LISTO ")
        self.status.setObjectName("Status")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        panel_layout.addWidget(self.status)

        self.panel.setLayout(panel_layout)
        main_layout.addWidget(self.panel)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def start(self):
        # Filtros Universales (Video + Imagen)
        filtros = "Media (*.mp4 *.avi *.mkv *.mov *.flv *.jpg *.png *.jpeg *.webp);;Todos (*.*)"
        file, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo", "", filtros)
        
        if file:
            ext_origen = os.path.splitext(file)[1].lower()
            
            # Sugerir nombre de salida según tipo
            if ext_origen in ['.jpg', '.jpeg', '.png', '.webp', '.bmp']:
                nombre_defecto = "imagen_vhs.png"
                filtro_guardar = "Imagen PNG (*.png)"
            else:
                nombre_defecto = "video_vhs.mp4"
                filtro_guardar = "Video MP4 (*.mp4)"

            out, _ = QFileDialog.getSaveFileName(self, "Guardar", nombre_defecto, filtro_guardar)
            
            if out:
                self.btn_load.setEnabled(False)
                self.status.setText(" PROCESANDO... ")
                self.worker = EngineThread(file, out, self.audio_check.isChecked())
                self.worker.finished.connect(self.done)
                self.worker.start()

    def done(self, path):
        self.btn_load.setEnabled(True)
        self.status.setText(" FINALIZADO ")
        # Abrir carpeta contenedora
        subprocess.run(["xdg-open", os.path.dirname(path)])

# ==========================================
#   LÓGICA DE INICIO Y ASSETS
# ==========================================
def get_random_gifs():
    # --- MODIFICACIÓN CLAVE: resource_path para assets ---
    assets_dir = resource_path("assets")
    try:
        # Filtramos para no usar el icono como fondo por error
        gifs = [f for f in os.listdir(assets_dir) if f.endswith(".gif")]
        if not gifs: return None, None
        splash = os.path.join(assets_dir, random.choice(gifs))
        background = os.path.join(assets_dir, random.choice(gifs))
        return splash, background
    except FileNotFoundError: return None, None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # --- MODIFICACIÓN CLAVE: resource_path para icono ---
    icon_path = resource_path(os.path.join("assets", "icon.png"))
    
    # Obtener GIFs
    splash_gif, bg_gif = get_random_gifs()
    
    # Instanciar Ventana Principal
    window = Win95Plaza(bg_gif, icon_path)

    # Centrar en Pantalla
    screen = window.screen().availableGeometry()
    win_geo = window.frameGeometry()
    win_geo.moveCenter(screen.center())
    window.move(win_geo.topLeft())

    # Lógica de Splash Screen
    if splash_gif:
        splash = QLabel()
        
        # Aplicar icono al Splash también (barra de tareas)
        if os.path.exists(icon_path):
            splash.setWindowIcon(QIcon(icon_path))
            
        splash.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        splash.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        movie = QMovie(splash_gif)
        splash.setMovie(movie)
        splash.resize(500, 400)
        
        # Centrar Splash
        splash_geo = splash.frameGeometry()
        splash_geo.moveCenter(screen.center())
        splash.move(splash_geo.topLeft())
        
        movie.start()
        splash.show()

        def start_app():
            movie.stop()
            splash.close()
            window.show()

        # 3.5 segundos de carga
        QTimer.singleShot(3500, start_app)
    else:
        window.show()
    
    sys.exit(app.exec())