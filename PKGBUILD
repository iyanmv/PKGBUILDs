# Maintainer: Jameson Pugh <imntreal@gmail.com>
# Contributor: Rene Schoebel (wesley) <schoebel.r at gmail dot com>

pkgname=openjk-git
pkgver=2983.1b6e1ec
pkgrel=1
pkgdesc="Open Source Jedi Knight II + III Engine"
arch=('i686' 'x86_64')
url="https://github.com/Razish/OpenJK"
license=('GPL')
depends=('libgl' 'openal' 'zlib' 'sdl2' 'libjpeg' 'glu')
optdepends=('libpng')
makedepends=('cmake' 'yasm')
provides=(openjk)
conflicts=(openjk)
source=("openjk::git://github.com/Razish/OpenJK.git"
				'openjk.install'
				'openjkmp.png'
				'openjksp.png'
				'openjkmp.desktop'
				'openjksp.desktop')
install=openjk.install
sha256sums=('SKIP'
            '8873237a7c6f12a0347b3e44cb237110ba526603e2b64aa4914bf4845be477c2'
            '0e82e720777eeb2043c2c25cdbce702c6d4ca077543aedfe51e5c4e96cf03969'
            'afb2c1a757720c70798e7f7218f823297a43bc61e0cb192e9443df67c2963903'
            'd3ad7dd270e57d36a22caef21bff17f2eb4acb0ad9087f6a17ca4a0bf9c566fc'
            'd03554bd926954218c243a1a97d39ea9700d064a2374f671249a533ebd970375')
_jkarch=i386
[ "$CARCH" == "x86_64" ] && {
        _jkarch=x86_64
}

pkgver() {
  cd openjk
	echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build() {
  cd "${srcdir}/openjk"

  mkdir -p build
  cd build
  cmake ../ \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_PREFIX=/opt/${pkgname} \
		-DCMAKE_SIZEOF_VOID_P=4
  make
}

package() {
  cd "${srcdir}/openjk/build"

	make DESTDIR="${pkgdir}" install

	mkdir -p "${pkgdir}/usr/bin"
	ln -s "/opt/${pkgname}/JediAcademy/openjk.${_jkarch}" "${pkgdir}/usr/bin/openjk"
	ln -s "/opt/${pkgname}JediAcademy/openjk_sp.${_jkarch}" "${pkgdir}/usr/bin/openjk_sp"
	ln -s "/opt/${pkgname}JediAcademy/openjkded.${_jkarch}" "${pkgdir}/usr/bin/openjkded"

	install -Dm755 "${srcdir}/openjkmp.png" "${pkgdir}/usr/share/pixmaps/openjkmp.png"
	install -Dm755 "${srcdir}/openjksp.png" "${pkgdir}/usr/share/pixmaps/openjksp.png"
	install -Dm755 "${srcdir}/openjkmp.desktop" "${pkgdir}/usr/share/applications/openjkmp.desktop"
	install -Dm755 "${srcdir}/openjksp.desktop" "${pkgdir}/usr/share/applications/openjksp.desktop"
}

# vim: set ts=2 sw=2 ft=sh noet:
