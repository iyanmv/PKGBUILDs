# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-gym
pkgname=python-${_pkgname}
pkgver=0.3.0
pkgrel=1
pkgdesc="A collection of quantum information science problems formulated as reinforcement learning environments"
arch=(x86_64)
url=https://github.com/AI4quantum/qiskit-gym
license=(Apache-2.0)
depends=(
    python-gymnasium
    python-qiskit
    python-twisterl
)
makedepends=(
    git
    python-build
    python-installer
    python-maturin
)
source=($_pkgname::git+https://github.com/AI4quantum/$_pkgname#tag=$pkgver)
b2sums=('a7631209753791dfadb549c6f6b13423b89c74ad2abb1e8eae8ba61960d87a066c1bed2b52bbfecdce45b77d04cd27ded0f4e23df58f9625fafe3755bca23870')

build() {
    cd $_pkgname
    python -m build --wheel --no-isolation
}

package() {
    cd $_pkgname
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
