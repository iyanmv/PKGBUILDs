# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_name=json_repair
pkgname=python-$_name
pkgver=0.35.0
pkgrel=1
pkgdesc="A python module to repair invalid JSON, commonly used to parse the output of LLMs"
arch=(any)
url=https://github.com/mangiucugna/json_repair
license=(MIT)
depends=(python)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
checkdepends=(python-pytest)
source=($_name-$pkgver.tar.gz::https://github.com/mangiucugna/$_name/archive/refs/tags/v$pkgver.tar.gz)
b2sums=('95bc905122c8a1367b775627d06ce5c8386665697165f9c9d92793dc3ee87478dc28945f32a842c4dd5cd19c664959b2442ddd8fe07f3e1063f70a15c53d6489')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_name-$pkgver
    local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    python -m installer --destdir=../test_dir dist/*.whl
    PYTHONPATH="$PWD/../test_dir/usr/lib/python$python_version/site-packages" pytest tests/test_json_repair.py
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
