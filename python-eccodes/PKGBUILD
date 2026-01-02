# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_name=eccodes
pkgname=python-${_name}
pkgver=2.44.0
pkgrel=1
pkgdesc="Python interface to the ecCodes GRIB/BUFR decoder/encoder"
arch=(any)
url=https://github.com/ecmwf/eccodes-python
license=(Apache-2.0)
depends=(
    eccodes
    python-attrs
    python-cffi
    python-findlibs
    python-numpy
)
makedepends=(
    git
    python-build
    python-installer
    python-setuptools
)
checkdepends=(python-pytest)
source=($_name::git+https://github.com/ecmwf/$_name-python.git#tag=$pkgver)
b2sums=('37ceedb364fef5bcefd7a4a74fd20322921e7899bfaf00d380858f99c4a29da13f23c409eacc4ad0d819f68458fd9b77f45c675af3152c7968c2cc9349a6c111')

build() {
    cd $_name
    python -m build --wheel --no-isolation
}

check() {
    cd $_name
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    rm -rf $_name
    test-env/bin/python -P -m pytest -o addopts=""
}

package() {
    cd $_name
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
