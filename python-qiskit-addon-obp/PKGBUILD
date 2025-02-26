# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_name=qiskit-addon-obp
pkgname=python-${_name}
pkgver=0.1.0
pkgrel=1
pkgdesc="An addon to reduce the depth of circuits with operator backpropagation"
arch=(any)
url=https://github.com/Qiskit/qiskit-addon-obp
license=(Apache-2.0)
depends=(
    python-numpy
    python-qiskit
    python-matplotlib
)
makedepends=(
    python-build
    python-installer
    python-hatchling
)
checkdepends=(
    python-pytest
    python-qiskit-addon-utils
)
source=($_name-$pkgver.tar.gz::https://github.com/Qiskit/$_name/archive/refs/tags/$pkgver.tar.gz)
b2sums=('bf9d3f3e7b9e467de3634c19e16990dda5c1b46b819b3f2f97ba1496084c978d3096c95776363fac941e835ba85181fb489095cfe19c142408064494f8643435')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_name-$pkgver
    local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    python -m installer --destdir=../test_dir dist/*.whl
    rm -rf ${_name//-/_}
    PYTHONPATH="$PWD/../test_dir/usr/lib/python$python_version/site-packages" pytest test
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
