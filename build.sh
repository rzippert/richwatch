#!/bin/bash
PKGNAME="richwatch"

while getopts ":v:f" opt; do
  case ${opt} in
    f )
      FORCE="-f "
      ;;
    v )
      VERSION=$OPTARG
      ;;
    \? )
      echo "Invalid option: $OPTARG" 1>&2
      ;;
    : )
      echo "Invalid option: $OPTARG requires an argument" 1>&2
      ;;
  esac
done

if [[ -z $VERSION ]]
then
	echo "Please, set a version with -v." 1>&2
	exit 127
fi

type -P "pyinstaller" 2>&1 > /dev/null || { echo "pyinstaller is required."; exit 1; }
type -P "fpm" 2>&1 > /dev/null || { echo "fpm is required."; exit 1; }

pyinstaller richwatch.spec -F
cd dist
echo fpm -s dir -t deb "$FORCE"-n $PKGNAME -v "$VERSION" --prefix /usr/bin/ $PKGNAME
fpm -s dir -t deb "$FORCE"-n $PKGNAME -v "$VERSION" --prefix /usr/bin/ $PKGNAME
