# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=ibm-quantum-schemas
pkgname=python-${_pkgname}
pkgver=0.5.20260320
pkgrel=1
pkgdesc="IBM Quantum API Schemas"
arch=(any)
url=https://github.com/Qiskit/ibm-quantum-schemas
license=(Apache-2.0)
depends=(
    python-pydantic
    python-qiskit
    python-samplomatic
)
makedepends=(
    git
    python-build
    python-installer
    python-setuptools
    python-setuptools-scm
)
checkdepends=(python-pytest)
source=($_pkgname::git+https://github.com/Qiskit/$_pkgname.git#tag=$pkgver)
b2sums=('0d0aa11b1c51c5f175f02c5a5a5acc213256b588d396be3d07b8935d882549e271c9cbd93f35d3def08c9e936c5fea34f09b5022ceadeda603321cdcc3148ad8')

build() {
    cd $_pkgname
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    rm -rf ${_pkgname//-/_}
    test-env/bin/python -P -m pytest -o addopts=""
}

package() {
    cd $_pkgname
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
