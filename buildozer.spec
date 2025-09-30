[app]
title = IKISKY VPN
package.name = ikiskyvpn
package.domain = com.ikisky
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4,json
version = 1.0
requirements = python3,kivy==2.3.0
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.archs = arm64-v8a,armeabi-v7a
orientation = portrait
fullscreen = 0
android.minapi = 21
android.api = 33
android.ndk = 25b
android.accept_sdk_license = True
android.release_artifact = apk
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
