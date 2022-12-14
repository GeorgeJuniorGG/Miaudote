[app]

# (str) Title of your application
title = Miaudote

# (str) Package name
package.name = miaudote

# (str) Package domain (needed for android/ios packaging)
package.domain = org.miaudote

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec, lock, md, txt, toml, yaml, Dockerfile

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, __pycache__, .pytest_cache

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.5

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.0.0,Kivy-Garden, https://github.com/kivymd/KivyMD/archive/master.zip,certifi, cffi, charset-normalizer, cryptography, Deprecated, docutils, future, gax-google-logging-v2, gax-google-pubsub-v1, gcloud, google-gax, googleapis-common-protos, grpc-google-logging-v2, grpc-google-pubsub-v1, grpcio, httplib2, idna, jwcrypto, monotonic, oauth2client, Pillow, ply, protobuf, pyasn1, pyasn1-modules, pycparser, pycryptodome, Pygments, pyparsing, Pyrebase4, firebase-admin, pydantic, email-validator, python-jwt, requests, requests-toolbelt, rsa, six, urllib3, wrapt

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True


# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
# android.accept_sdk_license = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ../.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

