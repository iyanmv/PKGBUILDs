# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_name=pybufrkit
pkgname=python-${_name}
pkgver=0.2.25
pkgrel=1
pkgdesc="Pure Python toolkit to work with WMO BUFR messages"
arch=(any)
url=https://github.com/ywangd/pybufrkit
license=(MIT)
depends=(
    python-bitstring
    python-six
)
makedepends=(
    python-build
    python-installer
    python-setuptools
)
checkdepends=(python-pytest)
source=($_name-$pkgver.tar.gz::https://github.com/ywangd/$_name/archive/refs/tags/v$pkgver.tar.gz)
b2sums=('607b172a561ead28faf3270fe555261e80b814e02e76f1ef18586c98f2689ead7be05a6b289c3a2a0dfd71fa2ff7955436696872e4c892bd2425f5a912f9ddd9')

prepare() {
    sed -i 's/pytest-runner//' $_name-$pkgver/setup.py
}

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_name-$pkgver
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    rm -rf $_name
    test-env/bin/python -P -m pytest -o addopts="" -v
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
