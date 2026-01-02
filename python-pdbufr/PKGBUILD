# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_name=pdbufr
pkgname=python-${_name}
pkgver=0.14.1
pkgrel=1
pkgdesc="High-level BUFR interface for ecCodes"
arch=(any)
url=https://github.com/earthobservations/wetterdienst
license=(Apache-2.0)
depends=(
    python-attrs
    python-eccodes
    python-pandas
    python-pint
)
makedepends=(
    git
    python-build
    python-installer
    python-setuptools
    python-setuptools-scm
)
checkdepends=(
    python-pytest
    python-requests
)
source=($_name::git+https://github.com/ecmwf/$_name.git#tag=$pkgver)
b2sums=('91b286d05a084baf92de5ff475b68fced442acc90ab30d041c7118b8af28408c0283a35989a5c2623fb5a52e2d7da62f15fdb69281dc1f9eebddd5e97867c0aa')

build() {
    cd $_name
    export SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_name
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    rm -rf src
    test-env/bin/python -P -m pytest -o addopts=""
}

package() {
    cd $_name
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
