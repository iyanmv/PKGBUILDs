# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-qasm3-import
pkgname=python-${_pkgname}
pkgver=0.5.0
pkgrel=1
pkgdesc="Importer from OpenQASM 3 to Qiskit's QuantumCircuit"
arch=(any)
url=https://github.com/Qiskit/qiskit-qasm3-import
license=(Apache-2.0)
depends=(
    python-openqasm3
    python-qiskit
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
checkdepends=(python-pytest)
source=($_pkgname-$pkgver.tar.gz::https://github.com/Qiskit/$_pkgname/archive/refs/tags/v$pkgver.tar.gz)
b2sums=('44eb08e435329ff67c4e241973a61590cf31d87c21bdc470654f4e3f2a4c819cdc875e6b186024818ad2e1c8ffaa3f0f168ff78b6b9ea9c949ca154ba27c7ee7')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

check() {
   cd $_pkgname-$pkgver
   local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
   python -m installer --destdir=../test_dir dist/*.whl
   PYTHONPATH=../test_dir/$_site_packages pytest tests
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
