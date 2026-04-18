#!/bin/bash


thisdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd "$thisdir" || exit 1

echo "================================================="
echo "Changelog:"

if [ -f "changelog" ]; then
    head -10 changelog
else
    echo "WARNING: Changelog file not found $thisdir!"
fi
echo "..."
echo "================================================="
echo


read -r -p "Is changelog up-to-date? (y/n) " ans
case "$ans" in
  y*|Y*) echo "Building deb..." ;;
  *)     echo "Bye."; echo; exit 1 ;;
esac


# -us Do not sign the source package
# -uc Do not sign the .changes file
(cd .. && debuild -us -uc -b)
status=$?

echo
case $status in
  0) 
     echo
     head -1 changelog 2>/dev/null
     echo "================================================="
     echo "SUCCESS! The package is built and located in the directory:"
     echo "$(cd ../.. && pwd)"

     ls -lh ../../*nativecam*.deb 2>/dev/null
     echo "================================================="
     ;;
  *) 
     echo "ERROR: Failed to build deb package. (Exit status: $status)"
     exit $status
     ;;
esac
