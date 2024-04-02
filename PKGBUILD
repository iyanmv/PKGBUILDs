# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=plasma6-applets-uptime-widget-git
_gitpkgname=plasma-applet-uptime-widget
pkgver=r15.be8cc87
pkgrel=1
pkgdesc='A simple uptime KDE plasmoid'
arch=(any)
url='https://github.com/KaOSx/plasma-applet-uptime-widget'
license=(GPL-2.0-only)
depends=(
    libplasma
    plasma5support
)
makedepends=(
    extra-cmake-modules
    git
)
conflicts=(plasma6-applets-uptime-widget-git)
source=($_gitpkgname::git+https://github.com/KaOSx/$_gitpkgname)
b2sums=(SKIP)

pkgver() {
    cd $_gitpkgname
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
}

build() {
    cmake -B build -S $_gitpkgname \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
