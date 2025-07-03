[app]

title = Calculator
package.name = calculator
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,ttf
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

# L'icône peut être ajoutée plus tard
icon.filename = 

# L’APK sera généré dans le dossier bin/
output.filename = calculator.apk

# (Optionnel) autorisations Android
android.permissions = INTERNET

# Support Python 3 uniquement
android.api = 31
android.ndk = 23b
android.gradle_dependencies = 
android.gradle_version = 7.0.0

[buildozer]

log_level = 2
warn_on_root = 1

# activer pour utiliser le mode débug verbose
debug = 1
