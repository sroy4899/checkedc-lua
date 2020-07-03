CCONV=~/checkedc-clang/build/bin/cconv-standalone
INCUDES=~/checkedc/include/
BASEDIR=.

CPATH=$INCLUDES $CCONV \
-output-postfix=checked \
-extra-arg-before=-DLUA_COMPAT_5_2 \
-extra-arg-before=-DLUA_USE_LINUX \
-extra-arg-before=-w \
-base-dir="$BASEDIR" \
$BASEDIR/loslib.c \
$BASEDIR/lgc.c \
$BASEDIR/lmathlib.c \
$BASEDIR/lapi.c \
$BASEDIR/lauxlib.c \
$BASEDIR/lmem.c \
$BASEDIR/ldebug.c \
$BASEDIR/lparser.c \
$BASEDIR/luac.c \
$BASEDIR/ldo.c \
$BASEDIR/ltm.c \
$BASEDIR/lstrlib.c \
$BASEDIR/ltablib.c \
$BASEDIR/lctype.c \
$BASEDIR/lfunc.c \
$BASEDIR/lzio.c \
$BASEDIR/lstate.c \
$BASEDIR/lua.c \
$BASEDIR/llex.c \
$BASEDIR/lstring.c \
$BASEDIR/ltable.c \
$BASEDIR/linit.c \
$BASEDIR/ldblib.c \
$BASEDIR/lvm.c \
$BASEDIR/lundump.c \
$BASEDIR/lbaselib.c \
$BASEDIR/lcorolib.c \
$BASEDIR/lbitlib.c \
$BASEDIR/lcode.c \
$BASEDIR/ldump.c \
$BASEDIR/lobject.c \
$BASEDIR/lopcodes.c \
$BASEDIR/loadlib.c \
$BASEDIR/liolib.c \
$BASEDIR/lutf8lib.c
