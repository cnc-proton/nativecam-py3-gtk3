#!/bin/bash

# Безопасное определение директории, из которой запущен скрипт
thisdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd "$thisdir" || exit 1

echo "================================================="
echo "Changelog:"
# Проверяем, существует ли файл, чтобы не сыпать непонятными ошибками
if [ -f "changelog" ]; then
    head -10 changelog
else
    echo "ВНИМАНИЕ: Файл changelog не найден в $thisdir!"
fi
echo "..."
echo "================================================="
echo

# Более современный способ запроса ввода у пользователя
read -r -p "Is changelog up-to-date? (y/n) " ans
case "$ans" in
  y*|Y*) echo "Building deb..." ;;
  *)     echo "Bye."; echo; exit 1 ;;
esac

# Запуск сборщика deb-пакетов
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
     echo "УСПЕХ! Пакет собран и лежит в директории:"
     echo "$(cd ../.. && pwd)"
     # Красиво выводим информацию о созданном deb-файле
     ls -lh ../../*nativecam*.deb 2>/dev/null
     echo "================================================="
     ;;
  *) 
     echo "ОШИБКА: Failed to build deb package. (Exit status: $status)"
     exit $status
     ;;
esac
