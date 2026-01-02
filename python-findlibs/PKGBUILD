# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_name=findlibs
pkgname=python-${_name}
pkgver=0.1.2
pkgrel=1
pkgdesc="A Python package that searches for shared libraries on various platforms"
arch=(any)
url=https://github.com/ecmwf/findlibs
license=(Apache-2.0)
depends=(python)
makedepends=(
    git
    python-build
    python-installer
    python-setuptools
)
checkdepends=(
    python-pyfakefs
    python-pytest
)
source=($_name::git+https://github.com/ecmwf/$_name.git#tag=$pkgver)
b2sums=('6f979588a896f256d2b51f147f90ed3ed7234b7a1484f4e1e0737569c52070b63b2eaadf342e239242bc1214113aefa95dfa721d8dc37dd4fc60f7bb1569c406')

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
