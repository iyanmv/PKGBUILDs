# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_name=samplomatic
pkgname=python-${_name}
pkgver=0.17.0
pkgrel=1
pkgdesc="A library that helps you sample randomizations of your quantum circuits"
arch=(any)
url=https://github.com/Qiskit/samplomatic
license=(Apache-2.0)
depends=(
    blas-openblas
    python-numpy
    python-orjson
    python-pybase64
    python-qiskit
    python-rustworkx
)
makedepends=(
    git
    python-build
    python-installer
    python-setuptools
    python-setuptools-scm
)
checkdepends=(
    jupyter-nbformat
    python-matplotlib
    python-plotly
    python-pylatexenc
    python-pytest
    python-qiskit-aer
    python-scipy-doctest
)
optdepends=(
    "jupyter-nbformat: visualization"
    "python-plotly: visualization"
    "python-matplotlib: visualization"
    "python-pylatexenc: LaTeX"
)
source=($_name::git+https://github.com/Qiskit/$_name.git#tag=$pkgver)
b2sums=('14485ba66578e74f20ffaa73c3bab14a93f99ad7212c2d89ce30df05258d08c7449b515b529c8aeafe332ab2a8ab4486b03ded48c962579f3a0a85d74572be65')

build() {
    cd $_name
    python -m build --wheel --no-isolation
}

check() {
    cd $_name
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    rm -rf $_name
    test-env/bin/python -P -m pytest -o addopts="" test/unit
}

package() {
    cd $_name
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
