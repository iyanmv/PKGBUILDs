# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=marknote
pkgver=1.0.0
pkgrel=1
pkgdesc="KDE's WYSIWYG note-taking application"
arch=(x86_64)
url='https://apps.kde.org/marknote/'
license=('GPL-2.0-or-later')
depends=(
    'kconfig'
    'kcoreaddons'
    'ki18n'
    'kiconthemes'
    'kirigami'
    'qt6-declarative'
    'qt6-svg'
)
makedepends=(
    'extra-cmake-modules'
    'git'
)
source=(git+https://invent.kde.org/office/marknote#tag=v$pkgver)
sha256sums=('adfa923c50afd88b7eba1959be05a971fc29f22ea94e9be7d041e1fbee2c8330')
validpgpkeys=(39FFA93CAE9C6AFC212AD00202325448204E452A)  # Carl Schwan <carl@carlschwan.eu>

build() {
    cmake -B build -S $pkgname \
        -DBUILD_TESTING=OFF
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}


