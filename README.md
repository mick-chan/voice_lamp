# voice_lamp
Voice controlled dot-matrix lamp

Recompiling voicecommand:

$ g++ -march=armv6zk -mtune=arm1176jzf-s -mcpu=arm1176jzf-s -mfpu=vfp -mfloat-abi=hard -D'BUILDTS="160506 05:20:31 -0700"' -O3 -lcurl -lboost_regex -o voicecommand voicecommand.cpp
