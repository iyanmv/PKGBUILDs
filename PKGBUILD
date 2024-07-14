# Maintainer: Marco Rubin <marco.rubin@protonmail.com>

_name=quimb
pkgname=python-$_name
pkgver=1.8.3
pkgrel=1
pkgdesc='Quantum information and many-body library.'
arch=(any)
url='https://github.com/jcmgray/quimb'
license=(Apache)
depends=(python)
makedepends=(python-build python-installer python-setuptools python-setuptools-scm python-wheel)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
b2sums=('9b72aa3db541e6100a8f752fa14a8193c0a977e2bad88d5c37cf808da460e0027eb496db2fe04bf2f46450f8ae9bc04291e9cd09553bc89a6e5189a0fc61522b')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
