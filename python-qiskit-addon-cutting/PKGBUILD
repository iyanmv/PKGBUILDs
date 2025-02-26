# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_name=qiskit-addon-cutting
pkgname=python-${_name}
pkgver=0.9.0
pkgrel=1
pkgdesc="Reduce width and depth of quantum circuits by cutting gates and wires"
arch=(any)
url=https://github.com/Qiskit/qiskit-addon-cutting
license=(Apache-2.0)
depends=(
    python-numpy
    python-qiskit
    python-rustworkx
)
makedepends=(
    python-build
    python-installer
    python-hatchling
)
checkdepends=(
    python-ddt
    python-pytest
    python-qiskit-aer
    python-qiskit-ibm-runtime
)
source=($_name-$pkgver.tar.gz::https://github.com/Qiskit/$_name/archive/refs/tags/$pkgver.tar.gz)
b2sums=('362d427cfca8febc64337a458e8cae68e30cdf437ed03dacb56790bebe1d72b3a5effb466feead72ecbfc8bb7557664d77dfa42df573a68a90432a7afc1c86ec')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_name-$pkgver
    local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    python -m installer --destdir=../test_dir dist/*.whl
    rm -rf qiskit_addon_cutting
    PYTHONPATH="$PWD/../test_dir/usr/lib/python$python_version/site-packages" pytest test
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
